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

# 🚀 8. Run the Pipeline

Make sure the following files exist in your project folder:

    agent.py
    requirements.txt
    dagger_pipeline.py

Run:

``` bash
python dagger_pipeline.py
```

------------------------------------------------------------------------

# 🔎 Expected Output

    Step 1: Load Source Code
    Step 2: Build AI Agent Container
    Step 3: Run AI Agent
    AI DOCUMENT SUMMARY ...
    Step 4: Publish Container Image
    Container image published

------------------------------------------------------------------------

# 🧠 What Happens Internally

1.  Dagger loads your project directory
2.  Builds a Python container dynamically
3.  Installs dependencies
4.  Executes AI agent inside container
5.  Publishes container image to registry

------------------------------------------------------------------------

# 🔥 Troubleshooting

## Docker Not Found

``` bash
docker version
```

If not found: - Ensure Docker Desktop is running - Restart WSL:
`wsl --shutdown`

## Dagger Session Error

-   Ensure `dagger version` works
-   Ensure Docker daemon is running

------------------------------------------------------------------------

# 🌍 Production Next Steps

You can extend this pipeline to:

-   Integrate OpenAI or Azure OpenAI
-   Add security scanning (Trivy)
-   Add test stage before deployment
-   Push image to Docker Hub or ACR
-   Deploy to Kubernetes

------------------------------------------------------------------------

You now have a complete Ubuntu-based setup for building and running AI
agents using Dagger 🚀
