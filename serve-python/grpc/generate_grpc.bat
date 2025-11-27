@echo off
REM 生成gRPC Python代码的脚本

REM 检查是否安装了grpcio-tools
python -c "import grpc_tools" >nul 2>&1
if errorlevel 1 (
    echo 请先安装grpcio-tools: pip install grpcio-tools
    exit /b 1
)

REM 生成Python gRPC代码
python -m grpc_tools.protoc -I.. --python_out=. --grpc_python_out=. ..\role_play.proto

echo gRPC代码生成完成