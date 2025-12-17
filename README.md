# Build an APK

This workspace contains `main_kivy.py` (the Kivy app) and media assets (images and `song.mp3`).

What I changed:
- Updated `main_kivy.py` to use relative paths and the system temp dir so it works when packaged.
- Added `buildozer.spec`, `build_apk.sh`, and `requirements.txt` to prepare and build an APK.

How to build an APK (recommended: use Linux or WSL2 with GUI support):

1. Open a Linux shell (Ubuntu/WSL2 recommended).
2. From the project root run:

```bash
chmod +x build_apk.sh
./build_apk.sh
```

3. Buildozer will download needed Android SDK/NDK and build the APK. The generated APK will be in `bin/`.

Notes and limitations:
- Building an APK requires a Linux environment (or Linux VM). Buildozer and Python-for-Android do not fully support native Windows build.
- The build process may take a long time on first run since SDK/NDK and other tools are downloaded.
- If you prefer CI-based builds, consider using a GitHub Actions workflow with a Ubuntu runner and the same `buildozer` commands.

If you'd like, I can create a GitHub Actions workflow file to build the APK automatically on push.
