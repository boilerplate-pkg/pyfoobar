
# functional programming

## generator

inspect.isgeneratrofunction()
inspect.getgeneratorstate()

genexpr
```python
l = [1,2,3,4]
g = (i for i in l)
```

## list comprehension, listcomp

```python
[ str(i) for i in [1,2,4]]
{ x:x.upper() for x in ["hello", "world"]}
{ x.upper() for x in ["hello", "world"]}
```

## built-in 

```python
map(func, iterable)
filter(func or None, iterable)
enumerate(iterable[,start])
sorted(iterable, key=None, reverse=False)
any(iterable)
all(iterable)
zip(iter1[,iter2])
```

## libs

### first

```python
from first import first
first([-1,0,1,2], key=lambda x: x>0)

def greater_than_zero(n):
    return n > 0

first(iterable, key = greater_than_zero)
```

### functools
['RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'cmp_to_key', 'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch', 'total_ordering', 'update_wrapper', 'wraps']

``` python
import functools
from first import first

def greater_than(number, min=0):
    return number > min

first(iterable, key = functools.partial(greater_than, min = 42))
```

### operator
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']

``` python
import operator
import functools import partial
import first
frist(iterable, key = partial(operator.le, 0))
```

### itertools
['accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
