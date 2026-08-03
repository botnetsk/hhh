[app]

# 应用标题
title = WenXinWuKui
package.name = wenxinwukui
package.domain = org.botnetsk

# 源代码目录 & 主文件
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,ttf,json,txt,csv,xml,kv,wav,mp3,ogg
source.exclude_exts = spec,pyc,pyo,bak,db,log
source.exclude_dirs = tests,bin,.buildozer,__pycache__
source.main = main.py

# 版本
version = 0.1

# 依赖库（python钉到3.11，不锁cython，不写pyjnius）
requirements = python3==3.11.4,kivy==2.2.1,openssl,urllib3,pycryptodome,requests

# 屏幕方向
orientation = portrait

# 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# API 配置
android.api = 33
android.minapi = 24
android.ndk = 25c
android.sdk = 33

# 架构
android.archs = arm64-v8a,armeabi-v7a

# 入口 Activity
android.entry_class = org.kivy.android.PythonActivity

# 调试模式
android.debug = True

# 全屏
fullscreen = 0

# 日志等级
log_level = 2

[buildozer]

# 日志等级
log_level = 2

# 构建目录
build_dir = .buildozer

# 输出目录
bin_dir = bin

# 构建后清理
clean_after_build = False

# 接受 SDK 许可
accept_sdk_license = True




