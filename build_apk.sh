#!/usr/bin/env bash
set -e

# Script to run on a Linux environment (WSL2/Ubuntu) to build the APK
# Usage: chmod +x build_apk.sh && ./build_apk.sh

echo "Installing system deps (Ubuntu)..."
sudo apt update
sudo apt install -y python3-pip build-essential git zlib1g-dev libncurses5 libffi-dev libssl-dev openjdk-11-jdk

echo "Installing Buildozer..."
python3 -m pip install --user --upgrade pip
python3 -m pip install --user buildozer

export PATH="$HOME/.local/bin:$PATH"

echo "Running Buildozer to build debug APK (this may download Android SDK/NDK)..."
buildozer -v android debug

echo "Build finished. APK will be in the bin/ directory."
