[app]
title = 问心无愧
package.name = wenxinwukui
package.domain = com.wenxin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_exts = spec
main.filename = main.py
version = 1.0
requirements = python3,kivy==2.2.1,cython==0.29.37,pyjnius,openssl,urllib3,pycryptodome,requests
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.ndk = 25c
android.strings = 问心无愧=问心无愧
android.entry_class = org.kivy.android.PythonActivity
android.debug = True
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
build_dir = .buildozer
warn_on_root = True
