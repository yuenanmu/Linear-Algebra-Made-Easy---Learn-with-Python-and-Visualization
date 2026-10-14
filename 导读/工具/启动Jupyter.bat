@echo off
chcp 65001 >nul
title 线性代数不难 - 启动 Jupyter Lab
cd /d "%~dp0..\.."

echo ============================================================
echo  《线性代数不难》一键启动
echo ============================================================
echo.

where conda >nul 2>nul
if %errorlevel%==0 (
    echo [1/3] 检测到 conda，尝试激活环境 ladm ...
    call conda activate ladm
) else (
    echo [1/3] 未检测到 conda。如果你用的是 venv，请先手动激活。
)

echo [2/3] 环境自检 ...
python "导读\工具\test_env.py"
if errorlevel 1 (
    echo.
    echo 自检未通过，请先按 导读\03-环境配置保姆级教程.md 修复环境。
    pause
    exit /b 1
)

echo.
echo [3/3] 启动 Jupyter Lab（关闭本窗口即停止服务）...
python -m jupyterlab
pause
