
#%% 
import asyncio
import time
from select import epoll
from functools import partial
import socket
ls = [1,2,3,4,5]

it = iter(ls)

# generator is a subclass of iterator
gen = (i for i in ls)

#%%
scheduled_list = []

class Handle(object):
    def __init__(self, gen):
        self.gen = gen

    def call(self):
        next(self.gen)
        scheduled_list.append(self)

def loop(*coroutines) :
    scheduled_list.extend(Handle(c) for c in coroutines)
    while True:
        while scheduled_list:
            h = scheduled_list.pop(0)
            h.call()

def fun():
    return (i for i in ls)

loop(fun(), fun(), fun())

#%%
# Future
# Handler: call generator once, 
# generator
# scheduled_list: call handle one by one
# timeout
# 我们可以大致观察出一个规律，创建Future对象，切出协程，在合适的时机（如socket ready或到达deadline/timeout）让他完成，切入协程，这才是协程切换的关键所在，由此，我们可以使用Future来管理各种异步调用。

#%%


def fun():
    print("step1")
    sock = socket.socket()
    future = Future()

    def handler():
        future.set_done()

    add_handler(sock.fileno(), handler, READ)
    yield future
    print("step2")
    yield sleep(3)
    print("step3")
    future = Future()
    from multiprocessing import Process
    Process(target=long_time_call, args=(future, )).start()
    yield future


def long_time_call(future):
    #...
    future.set_done()


poll = epoll()
handlers = dict()

scheduled_list = []
# 创建一个timeout_list
timeout_list = []


def fun():
    print("step1")
    sock = socket.socket()
    future = Future()

    def handler():
        future.set_done()

    add_handler(sock.fileno(), handler, READ)
    yield future
    print("step2")
    yield sleep(3)
    print("step3")
    yield


def add_handler(fd, handler, events):
    handlers[fd] = handler
    poll.register(fd, events)


def sleep(sec):
    future = Future()
    timeout = Timeout(sec, future.set_done)
    timeout_list.append(timeout)
    return future


class Timeout(object):

    def __init__(self, timeout, callback):
        self.deadline = time.time() + timeout
        self.callback = callback

    def call(self):
        self.callback(None)


class Future(object):

    def __init__(self):
        self.callbacks = []
        self.value = None

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def set_done(self, value):
        self.value = value
        for callback in self.callbacks:
            callback()

    def get_result(self):
        return self.value


class Handle(object):
    def __init__(self, gen):
        self.gen = gen

    def call(self):
        yielded = next(self.gen)
        if isinstance(yielded, Future):
            yielded.add_callback(partial(scheduled_list.append, self))
        else:
            scheduled_list.append(self)


def loop(*coroutines):
    scheduled_list.extend(Handle(c) for c in coroutines)
    while True:

        default_timeout = 10000
        deadline = time.time()

        for timeout in timeout_list[:]:
            if timeout.deadline <= deadline:
                timeout.call()
                timeout_list.remove(timeout)

        while scheduled_list:
            handle = scheduled_list.pop(0)
            handle.call()

        for timeout in timeout_list:
            wait_time = timeout.deadline - deadline
            if wait_time <= 0:
                wait_time = 0
            default_timeout = min(default_timeout, wait_time)

        if not scheduled_list and not timeout_list and not handlers:
            break

        # 等待描述符可操作
        events = poll.poll(default_timeout)
        while events:
            fd, event = events.popitem()
            handlers[fd]()
            poll.unregister(fd)
            del handlers[fd]


if __name__ == "__main__":
    loop(fun(), fun(), fun())
'''
当协程执行到第三步时，遇到了长时间运行的函数调用，我们创建了一个Future，关联到一个子进程中，并在子进程完成时设置future完成，在子进程完成之前，父进程已完成协程的切出，将执行权交给其它协程执行。

这个地方遗漏了一个细节，当没有其它协程可以执行时，epoll会被设置成超时时间=10000，因而陷入到长时间的睡眠中，而子进程完成后需要切入协程，但父进程已经被epoll阻塞掉，如何唤醒主进程继续执行该协程呢？业界通用的做法是，创建一个管道，在切出协程时让epoll监听读fd，子进程完成后，往管道中写入一个字符，epoll监听的读fd 马上变成ready，因此epoll解除阻塞，事件循环得以继续执行。
'''

#%%
# yield from

def fun() :
    yield from (i for i in ls)
    yield from (i for i in ls)


#%% example
def read(sock):
    future = Future()

    def handler():
        buf = sock.recv(1024)
        future.set_done(buf)

    add_handler(sock.fileno(), handler, 0x001)
    yield future
    return future.get_result()


def sleep(sec):
    future = Future()
    timeout = Timeout(sec, future.set_done)
    timeout_list.append(timeout)
    yield future


def coroutine(num):
    client = socket.socket()
    client.connect(("", 1234))
    print(f"coroutine_{num} start")
    buffer = yield from read(client)
    print(f"coroutine_{num} recv: ", buffer)
    yield from sleep(3)
    print(f"coroutine_{num} wake up ")
    client.close()


if __name__ == "__main__":
    loop(coroutine(1), coroutine(2))


#%%
# await === yield from

import socket 
import asyncio

async def read(sock):
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    def handler():
        buf = sock.recv(1024)
        future.set_result(buf)
        loop.remove_reader(sock.fileno())

    loop.add_reader(sock.fileno(), handler)
    await future
    return future.result()


async def coroutine(num):
    client = socket.socket()
    client.connect(("", 1234))
    print(f"coroutine_{num} start")
    buffer = await read(client)
    print(f"coroutine_{num} recv: ", buffer)
    await asyncio.sleep(3)
    print(f"coroutine_{num} wake up ")
    client.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(coroutine(1), coroutine(2)))


#%%
def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
acc = gather_tallies(tallies)
next(acc)  # Ensure the accumulator is ready to accept values

for i in range(4):
    acc.send(i)
acc.send(None)  # Finish the first tally

for i in range(5):
    acc.send(i)
acc.send(None)  # Finish the second tally
print(tallies)


#%%
