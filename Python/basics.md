### Variables
- Underscore `_` in interactive interpreter
```
>>> 5 * 5
25
>>> _
25
```

- `sys` argv

### Reverse a word

```
word = "apple"
word[:]
word[::-1]
```

### Lists and Dictionaries
> Looking up an item in a list is *O*(n). Sorting / caring about order

> Looking up an item in a dict is *O*(1). Repeated lookups

```
# to list
word_list = [elt.strip() for elt in open("words.txt", "r").readlines()]

# to dictionary
word_dict = dict((elt, 1) for elt in word_list)

# to set
word_set = set(word_list)

# filter
[elt for elt in word_list if "UU" in elt]
```

### Matplotlib library
https://matplotlib.org/tutorials/index.html
> apt-get install python3-matplotlib

### Python Debugging
- python -i <python_script.py>
- import pdb
- pdb.pm()

### Sorting and Grouping
```
# portfolio is a list of dictionary objects
portfolio.sort()
>>> unorderable types

def holding_name(holding):
    return holding['name']    
portfolio.sort(key=holding_name)

portfolio.sort(key=lambda holding: hodling['name'])

# lambda function
a = lambda x, y: x + y
a(2, 3)
>>> 5

min(portfolio, key=lambda holding: holding['price'])
max(portfolio, key=lambda holding: holding['price'])

import itertools
for name, items in itertools.groupby(portfolio, key=lambda hodling: holding['name']):
   print('NAME: ', name)
   for item in items:
       print('      ', it)

```

### Module Basics
```
# only run can be seen here,but the simple module is fully loaded
from simple import run

# equivalent statements are
improt simpe
run = simple.run()

# Imported Modules are cached..the second import does not load the module again
import simple
import sys
sys.modules['simple']
sys.path   # python path

del sys.modules['simple']

# gloabl variable `__name__`
if __name__ = '__name__':
    # do something
```

