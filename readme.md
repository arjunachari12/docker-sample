# Dagger Agentic Workflow Exercises

## Prerequisites

1. Ubuntu (WSL recommended)
2. Docker Desktop with WSL integration enabled
3. Python 3.11
4. Dagger CLI installed
5. Python virtual environment activated

---

## Setup

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install dagger-io
```

Verify:

```bash
docker version
dagger version
```

---

# Exercise 1 – Simple Container Execution

Run:

```bash
python exercise1.py
```

Expected Output:
Hello from Dagger Exercise 1

---

# Exercise 2 – Mount Local Directory

Demonstrates mounting host directory into container.

Run:

```bash
python exercise2.py
```

---

# Exercise 3 – Multi-Step Workflow (DAG Concept)

Demonstrates container chaining and workflow composition.

Run:

```bash
python exercise3.py
```

---

# Exercise 4 – Simulated Agentic Workflow

Simulates AI generating code and Dagger executing it safely.

Run:

```bash
python exercise4.py
```

---

## Learning Objectives

- Understand Workflows as Code
- Run ephemeral containers
- Mount host directories
- Compose multi-step pipelines
- Execute AI-generated code safely

---

You're now ready to integrate Dagger with real Agentic AI systems like LangGraph or CrewAI.
