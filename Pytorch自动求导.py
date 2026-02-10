import torch

# 创建两个张量，并启用梯度计算
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# 定义一个简单的计算
z = x**2 + y**3

# 计算梯度
z.backward()

# 打印梯度
print("dz/dx =", x.grad)
print("dz/dy =", y.grad)