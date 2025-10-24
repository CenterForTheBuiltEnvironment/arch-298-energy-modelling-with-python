# 🧩 Virtual Environment Management in VS Code

When working with Python in VS Code, it’s recommended to use a virtual environment (venv) to keep dependencies isolated.

### ▶️ To Activate a venv
1. Open VS Code’s **Terminal** (Ctrl+` or View → Terminal).
2. Navigate to your project folder if not already there. You can do this in several ways depending on how you’re working:

   - **Option 1 – Use the VS Code menu:** From the top menu bar, select **File → Open Folder…**, then choose the folder containing your Python files (e.g., `C:\Users\YourName\Documents\EnergyPlus_Projects`). Once opened, VS Code automatically treats this as your working directory.
   
   - **Option 2 – Use the terminal command:** In the VS Code integrated terminal, type a `cd` (change directory) command. For example:
     ```bash
     cd Desktop/building_simulations
     ```
     or, on Windows with spaces in the path:
     ```powershell
     cd "C:\Users\YourName\Desktop\EnergyPlus Simulations"
     ```
     You can check where you are by typing `pwd` (macOS/Linux) or `cd` (Windows) — it will display your current folder path.
   
   - **Option 3 – Open from Explorer/Finder:** You can right-click your project folder in your system file browser and choose **Open with VS Code**. The terminal will automatically start in that folder.

3. Run the activation command:
   - **Windows (PowerShell):** `venv\Scripts\Activate`
   - **macOS/Linux:** `source venv/bin/activate`
4. You’ll see `(venv)` appear before the prompt — this means your virtual environment is active.

### ⏹️ To Deactivate a venv
When finished, simply type:
```
deactivate
```
This returns you to the global Python environment.

---

### 📦 Installing Packages in Your venv
Once the virtual environment is activated, you can install Python packages locally without affecting the global system installation. Use the `pip install` command:

- **Example:**
  ```bash
  pip install pandas eppy esoreader tqdm
  ```
  This installs the required libraries for your EnergyPlus automation workflow.

- To verify installations, run:
  ```bash
  pip list
  ```

- To save your environment configuration for later use (recommended):
  ```bash
  pip freeze > requirements.txt
  ```
  You can later reinstall the same setup in a new environment with:
  ```bash
  pip install -r requirements.txt
  ```

---

### 🧰 Other Common Tasks in VS Code Terminals

- **Check your Python version:**
  ```bash
  python --version
  ```
  or, if multiple versions are installed:
  ```bash
  python3 --version
  ```

- **Confirm the interpreter VS Code is using:**  
  Look at the bottom-right corner of VS Code — the Python version shown there should match your venv path. You can also open the Command Palette (`Ctrl+Shift+P`) → type and select **Python: Select Interpreter**, then choose your venv.

- **Check if a module is installed:**
  ```bash
  pip show eppy
  ```
  or try importing it directly in Python:
  ```python
  import eppy
  ```
  If it’s not installed, Python will raise a `ModuleNotFoundError`.

