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


