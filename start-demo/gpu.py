from tinygrad.tensor import Tensor
a = (Tensor.ones(4,4).gpu() + Tensor.ones(4,4).gpu()).cpu()
print(a)
