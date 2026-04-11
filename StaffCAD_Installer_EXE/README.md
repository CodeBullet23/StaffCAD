# StaffCAD

StaffCAD is a local desktop application created by **BarSmithLabs** and published under the GitHub account **CodeBullet23**.  
It provides a simple Windows installer that sets up a Flask-based local web interface on your computer.

This project is **not malicious**, does not collect personal data, and does not send information anywhere.  
Everything runs **locally on your machine only**.

---

## 🚀 Features

- One‑click Windows installer  
- Self‑healing launcher (`run_app.bat`)  
- Automatically creates `.venv` if missing  
- Automatically installs Flask dependencies  
- Automatically upgrades pip when needed  
- Runs the app using the venv’s Python (no activation required)  
- Opens the StaffCAD interface at:  
  **http://127.0.0.1:5000/login**

---

## 📦 Installation

1. Download the latest installer from the Releases page.  
2. Run the installer.  
3. (Optional) Check the box to launch StaffCAD immediately.  
4. A desktop shortcut will be created for easy access.

---

## ▶️ Running StaffCAD

After installation, launch StaffCAD by:

- Double‑clicking the **StaffCAD** desktop shortcut  
- Or running `run_app.bat` inside the installation folder

The launcher will:

1. Check if Python is installed  
2. Create `.venv` if missing  
3. Install Flask dependencies if missing  
4. Start the Flask server  
5. Keep the window open so you can see errors if something goes wrong

---

## ❌ Uninstalling

To uninstall StaffCAD:

1. Open **Control Panel → Programs and Features**  
2. Find **StaffCAD**  
3. Click **Uninstall**

This removes:

- The installation folder  
- The `.venv`  
- The launcher  
- The shortcuts  

No leftover files remain.

---

## 🛡️ Disclaimer

StaffCAD is provided **as‑is**, without any warranty.  
It is not malicious, does not contain harmful code, and does not transmit data.  
It is intended for **local use only**.

You are responsible for how you use this software.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 🧠 How It Works (Technical Overview)

### Installer
The NSIS installer:

- Downloads the GitHub repository  
- Extracts the files  
- Places them in `C:\Program Files\StaffCAD`  
- Creates shortcuts  
- Adds an uninstaller  
- Does **not** install Python packages (the launcher handles that)

### Launcher (`run_app.bat`)
The launcher:

- Uses Python directly from `.venv\Scripts\python.exe`  
- Creates `.venv` if missing  
- Installs Flask packages if missing  
- Starts `app.py`  
- Keeps the window open  
- Never uses `activate.bat`  
- Works even after Python updates  

This makes the system extremely stable.

---

## 🧩 Requirements

- Windows 10 or later  
- Python 3.10+ installed  
- Internet connection (first run only)

---

## ❤️ Credits

Created by **BarSmithLabs**  
Published under **CodeBullet23**
