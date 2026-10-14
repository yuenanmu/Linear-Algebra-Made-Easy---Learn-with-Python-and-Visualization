#!/usr/bin/env bash
# 《线性代数不难》一键启动（macOS / Linux）
# 用法：bash 导读/工具/启动Jupyter.sh
set -e
cd "$(dirname "$0")/../.."

echo "============================================================"
echo " 《线性代数不难》一键启动"
echo "============================================================"

if command -v conda >/dev/null 2>&1; then
  echo "[1/3] 检测到 conda，尝试激活 ladm ..."
  # shellcheck disable=SC1091
  source "$(conda info --base)/etc/profile.d/conda.sh"
  conda activate ladm || echo "  (未找到 ladm 环境，将使用当前 Python)"
else
  echo "[1/3] 未检测到 conda（若用 venv 请先手动 activate）"
fi

echo "[2/3] 环境自检 ..."
python 导读/工具/test_env.py || {
  echo "自检未通过，请先看 导读/03-环境配置保姆级教程.md"; exit 1; }

echo "[3/3] 启动 Jupyter Lab ..."
python -m jupyterlab
