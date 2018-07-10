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
word_list = [elt.strip() for elt in open("words.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in word_list)

```

