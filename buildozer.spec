[app]

title = NRC Search App
package.name = nrcsearch
package.domain = org.example

source.dir = .
source.include_exts = py,xlsx

version = 1.0

requirements = python3,kivy,pandas,openpyxl

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = True

[buildozer]

log_level = 2
warn_on_root = 1
