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
> apt-get install python3-matplotlib

```
from matplotlib import pyplot
import random

x_values = [0, 4, 7, 20, 22, 25]
y_values = [random.randint(0, 30) for elt in x_values]

pyplot.plot(x_values, y_values, "o-")

pyplot.xlabel("Time")
pyplot.ylabel("Values")
pyplot.title("Test plot")

pyplot.show()
```
