[app]

# 应用基本信息
title = WenXinWuKui
package.name = wenxinwukui
package.domain = org.botnetsk
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,ttf,json,txt,csv,xml,kv,wav,mp3,ogg
source.exclude_exts = spec,pyc,pyo,bak,db,log
source.exclude_dirs = tests,bin,.buildozer,__pycache__

# 入口文件，按你实际改，一般是 main.py
main = main.py

# 版本
version = 0.1

# 要求/依赖
# 关键：python3 钉到 3.11.x，去掉 cython 严格版本，先去掉 pyjnius
requirements = python3==3.11.4,kivy==2.2.1,openssl,urllib3,pycryptodome,requests

# 方向
orientation = portrait

[buildozer]

# 详细日志，方便抓真实错误
log_level = 2
log_color = True

build_dir = .buildozer
bin_dir = bin

# Android 配置
android.api = 33
android.minapi = 24
android.ndk = 25c
android.sdk = 33

# 架构
android.archs = arm64-v8a,armeabi-v7a

# 调试包
android.debug = True

# 全屏，按需要改
fullscreen = 0

# 清理旧缓存后再构建更稳
clean_after_build = False

accept_sdk_license = True



