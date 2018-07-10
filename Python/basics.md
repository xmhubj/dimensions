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


### urllib -- URL handling

### Python Debugging
- python -i <python_script.py>
- import pdb
- pdb.pm()
