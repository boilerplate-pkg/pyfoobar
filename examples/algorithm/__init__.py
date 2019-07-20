
def use_collection() :
    """
    set
        add,clear,copy,difference,difference_update,discard,intersection,
        intersection_update,isdisjoint,issubset,issuperset,pop,remove,
        symmetric_difference,symmetric_difference_update,union,update
    dict
        clear,copy,fromkeys,get,items,keys,pop,popitem,setdefault,update,values
    list
        append,clear,copy,count,extend,index,insert,pop,remove,reverse,sort
    tuple
        count,index
    """

    c = [dict, list, tuple, set]
    
    def fns(cls) :
        o = cls()
        return ",".join([f for f in dir(o) if not f.startswith("__")])

    for cls in c :
        print(fns(cls))

if __name__ == "__main__" :
    use_collection()