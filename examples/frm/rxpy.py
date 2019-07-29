#%%


def userx() :
    """

    document https://rxpy.readthedocs.io/en/latest/

    reactive programming in python: https://auth0.com/blog/reactive-programming-in-python/

    ReactiveX : http://reactivex.io/

    observable, observer/subscribe, subject

    data stream

    toolbox = filter, create, transform, unify

    event-driven programming: handling any event to trigger the corresponding action

    reactive: wrap data into the reactive system as events

    """

    def simple() : 
        from rx import Observable, Observer 
        source = Observable.from_list([1,2,3,4,5,6])
        source.subscribe(lambda v : print("receive {}".format(v)))

    simple()

