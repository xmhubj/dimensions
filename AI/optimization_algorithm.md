# Mini-batch gradient descent

For large training data set:
- baby training sets -> mini-batch, say 1000 examples for each
- epoch is a word that means a single pass through the training set
- mini-batch gradient descent runs much faster than batch gradient descent(entire training set)

Understanding mini-batch gradient descent:
- mini-batch size in-between `1`(too small) to `m`(too large)
- if `m`, batch gradient descent, too long per iteration
- if `1`, stochastic gradient descent, noisiness, you lose all your speed up from vectorization

Rule of thumb:
- if training set < 2000, use batch gradient descent
- Typical mini batch size: 64, 128,256, 512, is a power of 2
- All of X{t}, Y{t} that fits in CPU/GPU memory
- 
