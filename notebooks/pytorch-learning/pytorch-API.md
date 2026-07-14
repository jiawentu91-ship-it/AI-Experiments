# PyTorch API 目录

| 类别 | API | 说明 |
|------|-----|------|
| **Tensor** | `tensor` | 从数据创建张量 |
| | `randn` | 从标准正态分布创建随机张量 |
| | `zeros` | 创建全零张量 |
| | `ones` | 创建全一张量 |
| **Shape** | `shape` | 获取张量的形状 |
| | `view` | 重塑张量（不改变内存布局） |
| | `reshape` | 重塑张量（可能改变内存布局） |
| | `permute` | 交换维度顺序 |
| | `transpose` | 交换两个维度 |
| | `unsqueeze` | 在指定位置插入维度 |
| | `squeeze` | 移除大小为 1 的维度 |
| **Module** | `Module` | 所有神经网络模块的基类 |
| | `forward` | 定义前向传播方法 |
| | `Parameter` | 将张量注册为可训练参数 |
| **Layers** | `Linear` | 全连接层 |
| | `Embedding` | 嵌入层（词嵌入等） |
| | `LayerNorm` | 层归一化 |
| | `Dropout` | 随机失活层（防止过拟合） |
| **Containers** | `Sequential` | 按顺序执行模块的容器 |
| | `ModuleList` | 以列表形式存储多个模块 |
| | `ModuleDict` | 以字典形式存储多个模块 |
| **Functional** | `softmax` | Softmax 激活函数 |
| | `cross_entropy` | 交叉熵损失函数 |
| | `gelu` | GELU 激活函数 |
| | `relu` | ReLU 激活函数 |
| **Training** | `backward` | 反向传播计算梯度 |
| | `zero_grad` | 清零梯度 |
| | `step` | 更新模型参数 |
| **Save** | `state_dict` | 获取模型参数（保存用） |
| | `load_state_dict` | 加载模型参数 |
| **Data** | `Dataset` | 自定义数据集的基类 |
| | `DataLoader` | 数据加载器（批量、打乱等） |
