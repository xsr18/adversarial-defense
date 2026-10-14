# 对抗样本攻防研究项目

复现 FGSM / PGD 对抗攻击与防御蒸馏，验证防御蒸馏的局限，并用对抗训练与特征层蒸馏做改进。

## 项目目标

本项目在 MNIST 与 CIFAR-10 上完成一条完整的对抗攻防实验链：

1. **复现攻击**：手写 FGSM 与 PGD，验证实现正确性
2. **复现防御**：复现经典防御蒸馏（Papernot et al., 2016）
3. **验证局限**：用强攻击（C&W、多步 PGD）证明防御蒸馏会被攻破
4. **提出改进**：对抗训练 + 特征层蒸馏，做消融对比
5. **形成产出**：技术报告、论文投稿、软件著作权

> 说明：本项目是大创项目「基于多模态特征融合与知识蒸馏的鲁棒实时对抗样本防御方法研究」的**实际可执行范围**。
> 受算力与时间限制，技术路线做了收缩：以 MNIST / CIFAR-10 为主，不使用大规模多模态模型。

## 环境

| 项目 | 版本 / 位置 |
|---|---|
| 操作系统 | Windows 11 |
| Python | 3.12.15 |
| 包管理 | Miniconda（`C:\miniconda3`） |
| 环境路径 | `C:\conda-envs\dl` |
| 主要依赖 | numpy, matplotlib, pandas, scikit-learn, jupyter |

### 激活环境

```powershell
conda activate C:\conda-envs\dl
```

### 安装依赖

```powershell
pip install -r requirements.txt
```

### 验证环境

```powershell
python check_env.py
```

预期输出 5 项检查全部 `[OK]`，并生成 `demo_plot.png`。

## 目录结构

```
.
├── check_env.py          # 环境自检脚本
├── requirements.txt      # Python 依赖清单
├── 周报.md               # 项目周报（同时是技术报告素材）
├── data/                 # 数据集（不提交到仓库）
├── models/               # 模型定义
├── attacks/              # 攻击实现（FGSM、PGD、C&W）
├── defenses/             # 防御实现（防御蒸馏、对抗训练、特征层蒸馏）
├── experiments/          # 实验脚本
└── configs/              # 超参数配置
```

## 当前进度

- [x] 阶段 0：环境搭建（Miniconda + `dl` 环境 + Git）
- [ ] 阶段 1：深度学习与 PyTorch 入门
- [ ] 阶段 2：对抗样本攻击复现（FGSM / PGD）
- [ ] 阶段 3：防御蒸馏复现与改进
- [ ] 阶段 4：工程化与拓展实验
- [ ] 阶段 5：技术报告与成果产出

## 参考文献

- Goodfellow et al. *Explaining and Harnessing Adversarial Examples*, 2014. [arXiv:1412.6572](https://arxiv.org/abs/1412.6572)
- Madry et al. *Towards Deep Learning Models Resistant to Adversarial Attacks*, 2017. [arXiv:1706.06083](https://arxiv.org/abs/1706.06083)
- Papernot et al. *Distillation as a Defense to Adversarial Perturbations against Deep Neural Networks*, IEEE S&P 2016.
- Hinton et al. *Distilling the Knowledge in a Neural Network*, 2015. [arXiv:1503.02531](https://arxiv.org/abs/1503.02531)
- Carlini & Wagner. *Towards Evaluating the Robustness of Neural Networks*, IEEE S&P 2017. [arXiv:1608.04644](https://arxiv.org/abs/1608.04644)
