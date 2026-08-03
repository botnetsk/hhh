[app]

# 应用标题（桌面图标下的名字）
title = 问心无愧

# 包名
package.name = wenxinwukui
package.domain = com.wenxin

# 源代码目录 & 主文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_exts = spec
source.main = main.py

# 应用版本
version = 1.0

# 依赖库（去掉了 pyjnius，它是常见编译失败元凶）
requirements = python3,kivy==2.2.1,cython==0.29.37,openssl,urllib3,pycryptodome,requests

# 屏幕方向
orientation = portrait

# 权限
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# API 配置
android.api = 33
android.minapi = 24

# NDK 锁定 25c（避免 r28c 的兼容性问题）
android.ndk = 25c

# 入口 Activity（已修正之前的笔误）
android.entry_class = org.kivy.android.PythonActivity

# 调试模式
android.debug = True

# 是否全屏
fullscreen = 0

# 日志等级
log_level = 2

# 架构（64位优先，兼容32位）
android.archs = arm64-v8a, armeabi-v7a

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


