[app]
# (str) Title of your application
title = New Year 2026

# (str) Package name
package.name = newyear2026

# (str) Package domain (needed for android/ios packaging)
package.domain = org.jerry

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,gif,mp3

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (list) List of architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Bootstrap to use for android builds
# p4a.branch = master