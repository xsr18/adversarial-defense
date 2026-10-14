# 第 1 周实验笔记

## 环境记录

- Python 解释器: C:\conda-envs\dl\python.exe (3.12.15)
- 关键决策: 环境放在纯 ASCII 路径，避免中文路径导致的写入失败
- 镜像源: conda 用南京大学，pip 用阿里云

## 本周踩过的坑

| 现象 | 根因 | 解决 |
|---|---|---|
| 安装器 Destination Folder 报错 | 安装器自身路径含中文 | 复制到纯 ASCII 目录运行 |
| conda 报 WinError 10061 | conda 26 的 repodata_shards 插件与国内镜像不兼容 | --no-plugins --solver classic |
| pip 找不到 numpy | 清华 PyPI 镜像返回 403 | 改用阿里云源 |
| git init 报 Permission denied | 用户目录权限被工具破坏 | 使用稳定路径 + 环境变量指定密钥 |