[app]

# (str) 应用标题
title = WenXin

# (str) 包名
package.name = wenxin
package.domain = org.wenxin

# (str) 源代码目录 & 主文件
# 确保仓库根目录有 main.py
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json
source.main = main.py

# (str) 应用版本
version = 1.0

# (list) 依赖库
# 重点：锁死 cython==0.29.37，防止云编译环境用 Cython 3.x 导致编译失败
requirements = python3,kivy==2.2.1,cython==0.29.37,pyjnius,openssl,urllib3,pycryptodome,requests

# (str) 屏幕方向
orientation = portrait

# (list) 权限
# INTERNET 必须，否则无法访问接口
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) 目标 API
android.api = 33

# (int) 最低 API
android.minapi = 21

# (str) 入口 Activity（修正了你原文件里的 =p 笔误）
android.entry_class = org.kivy.android.PythonActivity

# (bool) 是否全屏
fullscreen = 0

# (int) 日志等级 (2=DEBUG, 1=INFO)
log_level = 2

# (list) Android 架构 (64位优先，兼容32位)
android.archs = arm64-v8a, armeabi-v7a

#
# 以下为默认配置，通常无需修改
#

[buildozer]

# (int) Log level (1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = .buildozer

# (str) Path to build output (e.g. .apk, .aab, .ipa)
bin_dir = bin

# (bool) Clean build files after build (default: False)
clean_after_build = False

# (bool) Clean python build files after build (default: False)
clean_python_build = False

# (bool) Clean distribution files after build (default: False)
clean_dist = False

# (bool) Clean cache files after build (default: False)
clean_cache = False

# (bool) Clean temp files after build (default: False)
clean_temp = False

# (bool) Clean all files after build (default: False)
clean_all = False

# (bool) Force rebuild of distribution (default: False)
force_build = False

# (bool) Force download of dependencies (default: False)
force_download = False

# (bool) Skip updating build dependencies (default: False)
skip_update = False

# (bool) Accept SDK license automatically (default: False)
accept_sdk_license = True

# (str) Android NDK version
android.ndk = 23b

# (str) Android SDK directory
# android.sdk_path =

# (str) Android NDK directory
# android.ndk_path =

# (str) Python-for-Android directory
# p4a.directory =

# (str) Python-for-Android git repository
# p4a.url = https://github.com/kivy/python-for-android.git

# (str) Python-for-Android branch
# p4a.branch = master

# (bool) Enable p4a debug mode
# p4a.debug = False

# (bool) Enable p4a verbose mode
# p4a.verbose = False

# (bool) Use prebuilt p4a dist (default: False)
# p4a.use_prebuilt_dist = False

# (bool) Keep p4a build directory (default: False)
# p4a.keep_build = False

# (bool) Disable p4a byte compile (default: False)
# p4a.no_byte_compile = False

# (bool) Use setup.py for p4a (default: False)
# p4a.use_setup_py = False

# (bool) Optimize python code (default: True)
# p4a.optimize_python = True

# (bool) Compile python code (default: True)
# p4a.compile_python = True

# (bool) Use Cython for p4a (default: True)
# p4a.use_cython = True

# (bool) Use ctypes for p4a (default: True)
# p4a.use_ctypes = True

# (bool) Use CFFI for p4a (default: False)
# p4a.use_cffi = False

# (bool) Use PyJNIus for p4a (default: True)
# p4a.use_pyjnius = True

# (bool) Use Android for p4a (default: True)
# p4a.use_android = True

# (bool) Use Kivy for p4a (default: True)
# p4a.use_kivy = True

# (bool) Use SDL2 for p4a (default: True)
# p4a.use_sdl2 = True

# (bool) Use FFmpeg for p4a (default: False)
# p4a.use_ffmpeg = False

# (bool) Use OpenSSL for p4a (default: True)
# p4a.use_openssl = True

# (bool) Use SQLite3 for p4a (default: True)
# p4a.use_sqlite3 = True

# (bool) Use libffi for p4a (default: True)
# p4a.use_libffi = True

# (bool) Use zlib for p4a (default: True)
# p4a.use_zlib = True

# (bool) Use bzip2 for p4a (default: True)
# p4a.use_bzip2 = True

# (bool) Use liblzma for p4a (default: True)
# p4a.use_liblzma = True

# (bool) Use libjpeg for p4a (default: True)
# p4a.use_libjpeg = True

# (bool) Use libpng for p4a (default: True)
# p4a.use_libpng = True

# (bool) Use freetype for p4a (default: True)
# p4a.use_freetype = True

# (bool) Use harfbuzz for p4a (default: False)
# p4a.use_harfbuzz = False

# (bool) Use pango for p4a (default: False)
# p4a.use_pango = False

# (bool) Use SDL2_image for p4a (default: True)
# p4a.use_sdl2_image = True

# (bool) Use SDL2_mixer for p4a (default: True)
# p4a.use_sdl2_mixer = True

# (bool) Use SDL2_ttf for p4a (default: True)
# p4a.use_sdl2_ttf = True

# (bool) Use SDL2_gfx for p4a (default: False)
# p4a.use_sdl2_gfx = False

# (bool) Use SDL2_net for p4a (default: False)
# p4a.use_sdl2_net = False

# (bool) Use SDL2_sound for p4a (default: False)
# p4a.use_sdl2_sound = False

# (bool) Use SDL2_rtf for p4a (default: False)
# p4a.use_sdl2_rtf = False

# (bool) Use SDL2_blend for p4a (default: False)
# p4a.use_sdl2_blend = False

# (bool) Use SDL2_particles for p4a (default: False)
# p4a.use_sdl2_particles = False

# (bool) Use SDL2_gesture for p4a (default: False)
# p4a.use_sdl2_gesture = False

# (bool) Use SDL2_haptic for p4a (default: False)
# p4a.use_sdl2_haptic = False

# (bool) Use SDL2_touch for p4a (default: False)
# p4a.use_sdl2_touch = False

# (bool) Use SDL2_joystick for p4a (default: False)
# p4a.use_sdl2_joystick = False

# (bool) Use SDL2_hidapi for p4a (default: False)
# p4a.use_sdl2_hidapi = False

# (bool) Use SDL2_wheel for p4a (default: False)
# p4a.use_sdl2_wheel = False

# (bool) Use SDL2_camera for p4a (default: False)
# p4a.use_sdl2_camera = False

# (bool) Use SDL2_power for p4a (default: False)
# p4a.use_sdl2_power = False

# (bool) Use SDL2_render for p4a (default: True)
# p4a.use_sdl2_render = True

# (bool) Use SDL2_dynapi for p4a (default: False)
# p4a.use_sdl2_dynapi = False

# (bool) Use SDL2_filesystem for p4a (default: True)
# p4a.use_sdl2_filesystem = True

# (bool) Use SDL2_cpuinfo for p4a (default: True)
# p4a.use_sdl2_cpuinfo = True

# (bool) Use SDL2_atomic for p4a (default: True)
# p4a.use_sdl2_atomic = True

# (bool) Use SDL2_barrier for p4a (default: True)
# p4a.use_sdl2_barrier = True

# (bool) Use SDL2_thread for p4a (default: True)
# p4a.use_sdl2_thread = True

# (bool) Use SDL2_timer for p4a (default: True)
# p4a.use_sdl2_timer = True

# (bool) Use SDL2_version for p4a (default: True)
# p4a.use_sdl2_version = True

# (bool) Use SDL2_video for p4a (default: True)
# p4a.use_sdl2_video = True

# (bool) Use SDL2_events for p4a (default: True)
# p4a.use_sdl2_events = True

# (bool) Use SDL2_audio for p4a (default: True)
# p4a.use_sdl2_audio = True

# (bool) Use SDL2_loadso for p4a (default: True)
# p4a.use_sdl2_loadso = True

# (bool) Use SDL2_assembly for p4a (default: False)
# p4a.use_sdl2_assembly = False

# (bool) Use SDL2_simd for p4a (default: False)
# p4a.use_sdl2_simd = False

# (bool) Use SDL2_misc for p4a (default: True)
# p4a.use_sdl2_misc = True

# (bool) Use SDL2_test for p4a (default: False)
# p4a.use_sdl2_test = False

# (bool) Use SDL2_docs for p4a (default: False)
# p4a.use_sdl2_docs = False

# (bool) Use SDL2_main for p4a (default: True)
# p4