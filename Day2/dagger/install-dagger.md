# Dagger AI Agent Pipeline -- Ubuntu Installation & Run Guide

## 🎯 Objective

This guide walks you through:

1.  Installing all prerequisites on Ubuntu (WSL recommended)
2.  Setting up Docker and Dagger
3.  Creating a Python virtual environment
4.  Running the Dagger AI Agent pipeline

------------------------------------------------------------------------

# ✅ 1. Update Ubuntu

``` bash
sudo apt update
sudo apt upgrade -y
```

------------------------------------------------------------------------

# ✅ 2. Install Python 3.11

Check existing version:

``` bash
python3 --version
```

If Python 3.11 is not installed:

``` bash
sudo apt install python3.11 python3.11-venv python3.11-distutils -y
```

Verify:

``` bash
python3.11 --version
```

------------------------------------------------------------------------

# ✅ 3. Install Docker (Using Docker Desktop + WSL Integration Recommended)

### On Windows:

1.  Install Docker Desktop
2.  Open Docker Desktop → Settings → Resources → WSL Integration
3.  Enable Ubuntu integration
4.  Apply & Restart

### In Ubuntu:

``` bash
docker version
```

You should see both Client and Server sections.

------------------------------------------------------------------------

# ✅ 4. Install Dagger CLI

``` bash
curl -L https://dl.dagger.io/dagger/install.sh | sh
sudo mv ./bin/dagger /usr/local/bin/dagger
```

Verify:

``` bash
dagger version
```

------------------------------------------------------------------------

# ✅ 5. Create Project Folder

``` bash
mkdir dagger-ai-agent
cd dagger-ai-agent
```

------------------------------------------------------------------------

# ✅ 6. Create Python Virtual Environment

``` bash
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install dagger-io
```

------------------------------------------------------------------------

# ✅ 7. Verify Environment

``` bash
docker version
dagger version
python --version
```

All should work without errors.

------------------------------------------------------------------------
