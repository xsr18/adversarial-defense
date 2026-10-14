# -*- coding: utf-8 -*-
"""
阶段0 环境自检脚本  check_env.py

作用：一条命令验证 dl 环境是否装好、能否正常画图。
用法：在 VS Code 里打开本文件，点右上角 ▷ 运行；或在终端执行  python check_env.py

预期：终端打印 8 项检查全部 [OK]，并在同目录生成一张 demo_plot.png。
"""

import sys          # sys 里存着解释器信息，用来确认"是不是 dl 环境的 Python"
import platform     # 用来读操作系统信息

print("=" * 60)
print("步骤 1：确认 Python 解释器身份")
print("=" * 60)
# 为什么先查这个：你机器上有两个 Python（系统的 3.14 和 dl 环境的 3.12）。
# 如果这里显示的路径不是 dl 环境，说明后面所有包都装错地方了，必须先纠正。
print("Python 版本 :", sys.version.split()[0])
print("解释器路径 :", sys.executable)
print("系统平台   :", platform.system(), platform.release())

# 检查版本对不对。这里用 assert 是"断言"：条件不成立就报错，
# 让你立刻发现问题，而不是继续跑下去得到一堆莫名其妙的结果。
major, minor = sys.version_info[:2]
assert (major, minor) == (3, 12), (
    f"当前 Python 是 {major}.{minor}，不是预期的 3.12！\n"
    f"说明你没有激活 dl 环境，或环境版本建错了。"
)
print("[OK] 版本正确，是 3.12")

print()
print("=" * 60)
print("步骤 2：逐个确认依赖库能正常导入")
print("=" * 60)

import numpy as np           # 数值计算，深度学习的"数据底座"
print("[OK] numpy      ", np.__version__)

import matplotlib            # 画图库
import matplotlib.pyplot as plt
print("[OK] matplotlib ", matplotlib.__version__)

import pandas as pd          # 表格数据处理，后面实验结果的 CSV 靠它
print("[OK] pandas     ", pd.__version__)

# 说明：这个脚本故意不导入 torch。
# 原因是 PyTorch 属于阶段1 的内容，阶段0 先不碰深度学习。
# 等阶段1 开始时，我们再单独验证 torch。

print()
print("=" * 60)
print("步骤 3：解决 matplotlib 显示中文的问题")
print("=" * 60)
# 为什么需要这一步：matplotlib 默认字体不含中文字形，
# 画出来的中文会变成一排方框（豆腐块）。这是新手最常见的坑之一。
# 微软雅黑来自 Windows 的字体目录，必须在 matplotlib 的字体列表里真实存在才生效。
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示成方块的问题

from matplotlib import font_manager
available = {f.name for f in font_manager.fontManager.ttflist}
if "Microsoft YaHei" in available:
    print("[OK] 微软雅黑可用，图中中文能正常显示")
else:
    print("[警告] 没找到微软雅黑，中文可能显示为方框。")
    print("       可换用其他中文字体，例如 SimHei（黑体）。")

print()
print("=" * 60)
print("步骤 4：造数据并算统计量")
print("=" * 60)
# 固定随机种子。为什么重要：不加种子，每次运行结果都不同，
# 实验就没法复现。这个习惯从第一天就要养成，后面跑对抗攻击实验时是硬要求。
np.random.seed(0)

# 造 100 个服从正态分布的随机数，模拟一次"测量结果"
data = np.random.randn(100)

mean_value = np.mean(data)   # 平均值
std_value = np.std(data)     # 标准差：衡量数据有多分散

print(f"样本数量 : {len(data)}")
print(f"平均值   : {mean_value:.4f}")
print(f"标准差   : {std_value:.4f}")
print("（理论值：标准正态分布均值应接近 0，标准差应接近 1）")

print()
print("=" * 60)
print("步骤 5：画图并保存")
print("=" * 60)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))   # 一行两列两张子图

# 左图：折线图，看数据的走势
axes[0].plot(data, color="tab:blue", linewidth=1)
axes[0].axhline(mean_value, color="tab:red", linestyle="--", label=f"均值 = {mean_value:.2f}")
axes[0].set_title("随机数据折线图")
axes[0].set_xlabel("样本序号")
axes[0].set_ylabel("数值")
axes[0].legend()

# 右图：直方图，看数据分布形状
axes[1].hist(data, bins=15, color="tab:orange", edgecolor="black")
axes[1].set_title("随机数据分布直方图")
axes[1].set_xlabel("数值")
axes[1].set_ylabel("出现次数")

plt.tight_layout()                      # 自动调整间距，防止标题被裁掉
plt.savefig("demo_plot.png", dpi=150)   # 保存成图片文件
print("[OK] 已生成图片: demo_plot.png")

print()
print("=" * 60)
print("全部检查通过！你的 dl 环境已经可以正常工作了。")
print("=" * 60)
