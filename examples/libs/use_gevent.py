
#%%
import random
import gevent 

def joinall():

    """
    gevent.joinall
    """

    def foo() :
        print("foo")
        gevent.sleep(0)
        print("foo again")

    def bar():
        print("bar")
        gevent.sleep(0)
        print("bar again")

    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar)
    ])

#%%
def asyncfun():
    """
    start a group async task
    """
    import gevent
    import random
    def task(id: int):
        gevent.sleep(random.randint(0, 2)*0.001)
        print("task {} finished".format(id))

    threads = [ gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)
#%%
def use_Greenlet() : 
    """
    Greenlet : thread
    """
    import gevent 
    from gevent import Greenlet 

    class MyGL(Greenlet) :
        
        def __init__(self, msg, n):
            Greenlet.__init__(self)
            self.message = msg 
            self.n = n
        
        def _run(self):
            print("{}-{}".format(self.message, self.n))
            gevent.sleep(self.n)
            print("{}-{}, finished".format(self.message, self.n))

    g = MyGL("hello", 3)
    g.start()
    g.join()

#%%
def use_Actor():
    """
    Actor: a higher level concurrency model popularized by the language Erlang
    """

    import gevent 
    from gevent.queue import Queue 

    class Actor(gevent.Greenlet):
        
        def __init__(self):
            self.inbox = Queue()
            gevent.Greenlet.__init__(self)

        def receive(self, message):
            """
            Define in your subclass.
            """

            print("receive message={}".format(message))

        def _run(self):
            self.running = True 
            while self.running:
                message = self.inbox.get()
                self.receive(message)

    class Ping(Actor):
        def receive(self, msg):
             print("Ping receive {}".format(msg))
             pong.inbox.put("ping")
             gevent.sleep(1)

    class Pong(Actor):
        def receive(self, msg) :
            print("pong receive {}".format(msg))
            ping.inbox.put("pong")
            gevent.sleep(1)

    ping = Ping()
    pong = Pong()

    ping.start()
    pong.start()

    ping.inbox.put("start")
    gevent.joinall([ping, pong])
    

         

#%%
def use_zmq():
    """
    gevent-zmq
    """
    import gevent 
    import zmq.green as zmq

    context = zmq.Context 
    
    def server():
        server_socket = context.socket(zmq.REQ)
        server_socket.bind("inproc///")