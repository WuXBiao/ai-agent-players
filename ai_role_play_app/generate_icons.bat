@echo off
REM Flutter 应用图标生成脚本（Windows）
REM 用途：自动生成 iOS 和 Android 的应用图标

echo 🎨 开始生成应用图标...
echo.

REM 检查图标文件是否存在
if not exist "assets\icon\app_icon.png" (
    echo ❌ 错误：未找到 assets\icon\app_icon.png
    echo 📝 请先将你的图标（1024×1024）放在 assets\icon\app_icon.png
    pause
    exit /b 1
)

echo ✅ 图标文件已找到
echo.

REM 获取依赖
echo 📥 获取依赖...
call flutter pub get
echo.

REM 生成图标
echo 🔨 生成图标...
call flutter pub run flutter_launcher_icons
echo.

REM 检查生成结果
if exist "android\app\src\main\res\mipmap-mdpi\ic_launcher.png" (
    echo ✅ Android 图标生成成功
) else (
    echo ❌ Android 图标生成失败
    pause
    exit /b 1
)

if exist "ios\Runner\Assets.xcassets\AppIcon.appiconset" (
    echo ✅ iOS 图标生成成功
) else (
    echo ❌ iOS 图标生成失败
    pause
    exit /b 1
)

echo.
echo 🎉 图标生成完成！
echo.
echo 📝 后续步骤：
echo 1. 运行: flutter clean
echo 2. 运行: flutter pub get
echo 3. 运行: flutter run
echo.
echo ✨ 应用图标已更新！
echo.
pause
