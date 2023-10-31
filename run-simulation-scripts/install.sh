#!/bin/bash

# Install Python build dependencies
sudo yum -y groupinstall "Development Tools"
sudo yum -y install openssl-devel bzip2-devel libffi-devel
# Verify gcc and make tools installation
gcc --version
make --version
# Download Python3.9
wget https://www.python.org/ftp/python/3.9.17/Python-3.9.17.tgz
# Extract downloaded file
tar xvf Python-3.9.17.tgz
# Build and install Python3.9
cd Python-*/
./configure --enable-optimizations
sudo make altinstall
# Check Python version
python3.9 --version
# Check pip version
pip3.9 --version
# Upgrade pip
/usr/local/bin/python3.9 -m pip install --upgrade pip
# Install andes
pip3.9 install andes --user
# Run selftest
python3.9 -m andes selftest

