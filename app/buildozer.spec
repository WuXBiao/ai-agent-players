[app]

# APP 基本信息
title = AI角色扮演
package.name = airoleplay
package.domain = com.aiplayer

# 源码目录
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 版本信息
version = 1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# 应用需求
requirements = python3,kivy,langchain-openai,langchain-core,python-dotenv,requests,certifi

# 图标和启动画面（可选，稍后添加）
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# 支持的方向
orientation = portrait

# 服务配置
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# Android 配置
[buildozer]

# Android SDK/NDK 版本
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# Android 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# Android 特性
android.archs = arm64-v8a,armeabi-v7a

# 日志级别
log_level = 2

# 警告作为错误
warn_on_root = 1


[buildozer:ios]

# iOS 配置（如需支持 iOS）
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
