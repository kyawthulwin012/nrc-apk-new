[app]
title = NRC APK NEW
package.name = nrcapknew
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx,txt

version = 1.0

requirements = python3,kivy,pandas,openpyxl

orientation = portrait

# Android permissions (လိုအပ်ရင်တိုးနိုင်)
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# APK settings
fullscreen = 0

# Python version (important)
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
