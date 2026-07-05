# AI/ML 实验集合

我的 AI 和机器学习实验记录，包含联邦学习、对抗样本、PyTorch 入门等探索。

## 目录结构

```
AI-Experiments/
├── notebooks/          # Jupyter Notebook 实验文件
│   ├── 联邦学习/
│   │   ├── fedavg_minimal.ipynb              # FedAvg 基础实现
│   │   └── fedavg_adversarial_experiment.ipynb # FedAvg 对抗样本实验
│   ├── 计算机视觉/
│   │   ├── fractal_visualization.ipynb       # 分形可视化（Julia集）
│   │   ├── mnist_handwriting_recognition.ipynb # MNIST 手写数字识别
│   │   └── adversarial_plotting.ipynb        # 对抗样本画图
│   ├── PyTorch 入门/
│   │   └── first_pytorch.ipynb               # 第一次使用 PyTorch
│   ├── Python 课程实验/
│   │   ├── python_experiment_01.ipynb        # 实验一：Python 基础
│   │   ├── python_experiment_02_numpy.ipynb  # 实验二：NumPy
│   │   ├── python_experiment_03_sympy.ipynb  # 实验三：SymPy 符号计算
│   │   └── python_experiment_04_matplotlib.ipynb # 实验四：Matplotlib 绘图
│   ├── 其他/
│   │   ├── number_guessing_game.ipynb        # 猜数游戏（class 练习）
│   │   ├── final_exam_review.ipynb           # Python 期末复习
│   │   └── hello_vsjupyter.ipynb             # VS Jupyter 测试
├── scripts/            # Python 脚本
│   ├── snake_game.py                         # 贪吃蛇游戏
│   └── consecutive_duplicates.py             # 连续重复数字处理
├── data/               # 数据集（仅小样本）
└── README.md           # 本文件
```

## 实验内容

### 联邦学习 (Federated Learning)
- **FedAvg 基础实现** — 使用 PyTorch 实现 FedAvg 算法，在 MNIST 数据集上进行分布式训练模拟
- **FedAvg 对抗样本实验** — 在联邦学习框架下研究对抗样本的影响

### 计算机视觉
- **分形可视化** — 使用 NumPy 和 Matplotlib 生成 Julia 集分形图像
- **MNIST 手写数字识别** — 使用 PyTorch 构建 CNN 识别手写数字

### PyTorch 入门
- **第一次 PyTorch** — PyTorch 框架的初次探索和版本验证

### Python 课程实验
- 涵盖 Python 基础语法、NumPy 数值计算、SymPy 符号计算、Matplotlib 数据可视化

## 环境要求

- Python 3.8+
- PyTorch
- NumPy, Matplotlib, SymPy
- Jupyter Notebook / VS Code

```bash
pip install torch numpy matplotlib sympy jupyter
```

## 许可证

MIT
