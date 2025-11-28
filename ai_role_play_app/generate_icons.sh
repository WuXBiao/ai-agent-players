#!/bin/bash

# Flutter 应用图标生成脚本
# 用途：自动生成 iOS 和 Android 的应用图标

echo "🎨 开始生成应用图标..."

# 检查是否安装了 flutter_launcher_icons
if ! grep -q "flutter_launcher_icons" pubspec.yaml; then
    echo "📦 添加 flutter_launcher_icons 依赖..."
    flutter pub add flutter_launcher_icons
fi

# 检查图标文件是否存在
if [ ! -f "assets/icon/app_icon.png" ]; then
    echo "❌ 错误：未找到 assets/icon/app_icon.png"
    echo "📝 请先将你的图标（1024×1024）放在 assets/icon/app_icon.png"
    exit 1
fi

echo "✅ 图标文件已找到"

# 获取依赖
echo "📥 获取依赖..."
flutter pub get

# 生成图标
echo "🔨 生成图标..."
flutter pub run flutter_launcher_icons

# 检查生成结果
if [ -f "android/app/src/main/res/mipmap-mdpi/ic_launcher.png" ]; then
    echo "✅ Android 图标生成成功"
else
    echo "❌ Android 图标生成失败"
    exit 1
fi

if [ -d "ios/Runner/Assets.xcassets/AppIcon.appiconset" ]; then
    echo "✅ iOS 图标生成成功"
else
    echo "❌ iOS 图标生成失败"
    exit 1
fi

echo ""
echo "🎉 图标生成完成！"
echo ""
echo "📝 后续步骤："
echo "1. 运行: flutter clean"
echo "2. 运行: flutter pub get"
echo "3. 运行: flutter run"
echo ""
echo "✨ 应用图标已更新！"
