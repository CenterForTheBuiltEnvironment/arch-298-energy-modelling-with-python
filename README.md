# Energy Modelling with Python

## Python Course Preparation Guide

Hi 👋
and welcome to the course! 🎉  

Before we start, please make sure your computer is ready. This guide explains everything you need to install and configure so you can follow along with the course smoothly.
While you will be able to follow the course without setting up your personal environment on your own computer (e.g. by using [Google Colab](https://colab.research.google.com)), we encourage you to take the steps below. This will benefit all your potential future workflows and set you up to use Python and version control in a professional way.

---

## 1. Install Python
We’ll use **Python 3.10 or later**.

- **Windows & macOS**: Download from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

### ✅ Verify Installation

```bash
python --version
```
Expected output: `Python 3.10.x` or higher.



## 2. Install Visual Studio Code (VS Code)

We’ll use VS Code as our code editor and Jupyter Notebook environment.
- Download here: https://code.visualstudio.com/
- Recommended extensions (can be installed separately within VS Code):
    - Python (Microsoft)
    - Jupyter (Microsoft)

Once installed, you’ll be able to open and run Jupyter Notebooks directly inside VS Code (no need to open a browser separately). You might also use other IDEs like PyCharm. Most of the steps outlined in this guide should similarly apply there, too.



## 3. Set Up a Virtual Environment

It’s best practice to use a virtual environment for Python projects. PLACEHOLDER REASONS FOR VENV.

In a new terminal window ...

```bash
# Navigate to your course folder
cd path/to/your/course/folder

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

✅ You should see (venv) in your terminal prompt after activation.



## 4. Install Required Packages
```bash
pip install jupyter numpy pandas matplotlib
```


## 5. Run Jupyter Notebooks in VS Code

1. Open VS Code.
2. Use File > Open Folder and select your course folder.
3. Create or open a .ipynb file.
4. In the top-right corner of the notebook, select the correct Python interpreter (your virtual environment).
5. Run cells using the ▶️ button that appears next to them.


## 6. Verify Everything Works

Open a new Jupyter Notebook in VS Code and paste the following code into a cell:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("NumPy version:", np.__version__)
print("pandas version:", pd.__version__)

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

✅ If you see the versions printed and a simple line plot, you’re all set!


## 7. Install and Configure Git & GitHub (Optional)

If you want to clone the course repository and track your own progress with Git and GitHub:

### Install Git
- Download from: https://git-scm.com/downloads
- Verify installation (using a new terminal window):

```bash
git --version
```

### Create a GitHub account

Sign up at https://github.com/.


### Configure Git (one-time setup)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Connect Git with GitHub

You can connect in two ways:

- **HTTPS** (simpler for beginners)
    - Clone repos with: git clone https://github.com/username/repo.git
    - Enter your GitHub username & password (or personal access token).

- **SSH** (recommended if you use GitHub often)
    - Generate an SSH key:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
    ```

    - Copy the key
    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

    - Add it to your GitHub account: [GitHub SSH Keys Settings](https://github.com/settings/keys)
    - Test connection:
    ```bash
    ssh -T git@github.com
    ```
