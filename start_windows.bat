@echo off
chcp 65001 > nul
echo ======================================================
echo  📖 Oli 英语学习助手 Windows 一键启动脚本
echo ======================================================
echo.

:: 1. 检查 Python 是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未检测到 Python，请先去 https://www.python.org/ 下载并安装 Python 3！
    echo ⚠️ 安装时请务必勾选 "Add Python to PATH" (添加到系统环境变量)
    pause
    exit /b
)

:: 2. 创建或检测虚拟环境
if not exist ".venv" (
    echo 📦 正在创建 Python 虚拟环境，请稍候...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo ❌ 创建虚拟环境失败，请确保已安装 Python 并有完整权限。
        pause
        exit /b
    )
)

:: 3. 激活虚拟环境并安装依赖
echo ⚡ 正在激活虚拟环境并安装依赖库...
call .venv\Scripts\activate.bat
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Flask cryptography pyOpenSSL

:: 4. 启动应用
echo 🚀 正在启动 English Study Plan 服务...
cd English_Study_Plan
python app.py

pause
