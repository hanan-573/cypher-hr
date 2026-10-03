# 🛡️ FirewallPy — Windows Firewall Rule Viewer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**FirewallPy** is a lightweight Python-based tool that fetches, displays, and exports **Windows Firewall rules** directly from the system using `netsh`.

It provides a clean, color-coded console view of **Blocking** and **Allowed** firewall rules and generates a professional **PDF report** on the Windows Desktop.

---

## 📋 Table of Contents

* [Overview](#-overview)
* [Features](#-features)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Requirements](#-requirements)
* [Installation](#-installation)
* [Usage](#-usage)
* [Output](#-output)
* [Manual Firewall Access](#-manual-firewall-access)
* [Troubleshooting](#-troubleshooting)
* [License](#-license)
* [Author](#-author)

---

## 📖 Overview

**FirewallPy** is a simple and useful utility for Windows users who want a quick overview of the currently enabled Windows Firewall rules.

Instead of manually navigating through the Windows Firewall interface using `wf.msc`, FirewallPy provides a command-line based solution that:

* Automatically fetches enabled firewall rules.
* Uses `netsh advfirewall` to access Windows Firewall information.
* Categorizes rules into **Blocking** and **Allowed**.
* Displays rules in a color-coded console table.
* Shows rule statistics.
* Generates a formatted PDF report on the Desktop.
* Automatically requests Administrator privileges when required.

---

## ✨ Features

* ✅ **Automatic Admin Elevation**
  Automatically triggers the Windows UAC prompt when Administrator privileges are required.

* ✅ **Fetches Enabled Firewall Rules**
  Retrieves inbound and outbound firewall rules using Windows `netsh advfirewall`.

* ✅ **Blocking & Allowed Classification**
  Separates firewall rules based on their configured action.

* ✅ **Color-Coded Console Output**
  Uses different colors to make blocked and allowed rules easier to identify.

* ✅ **Live Rule Counter**
  Displays the total number of rules along with blocking and allowed rule counts.

* ✅ **PDF Report Generation**
  Generates a professional `firewall_record.pdf` report on the Windows Desktop.

* ✅ **Windows Native**
  Uses the built-in Windows `netsh advfirewall` utility.

* ✅ **Lightweight**
  Built with Python and only a few external dependencies.

* ✅ **CMD / PowerShell Compatible**
  Uses `colorama` for cross-console color support.

---

## 🏗️ How It Works

The application follows this workflow:

```text
User
  │
  ▼
Run FirewallPy
  │
  ▼
Check Administrator Privileges
  │
  ├── Not Administrator
  │        │
  │        ▼
  │      Windows UAC Prompt
  │        │
  │        ▼
  │      Relaunch as Administrator
  │
  ▼
Run netsh advfirewall
  │
  ▼
Fetch Firewall Rules
  │
  ▼
Parse Rule Information
  │
  ▼
Filter Enabled Rules
  │
  ├───────────────┐
  ▼               ▼
Blocking        Allowed
Rules           Rules
  │               │
  └───────┬───────┘
          ▼
   Console Display
          │
          ▼
    PDF Generation
          │
          ▼
     Desktop Report
```

### Step-by-Step

1. The user runs `firewall.py`.
2. The application checks for Administrator privileges.
3. If Administrator privileges are missing, Windows displays a UAC prompt.
4. The application runs:

```powershell
netsh advfirewall firewall show rule name=all
```

5. The raw firewall information is parsed into structured data.
6. Only enabled firewall rules are processed.
7. Rules are categorized as **Blocking** or **Allowed**.
8. The rules are displayed in the terminal.
9. A PDF report is generated on the Desktop.

---

## 📁 Project Structure

```text
FirewallPy/
│
├── firewall.py
├── requirements.txt
└── README.md
```

> **Note:** The main application file is referred to as `firewall.py` in the project documentation. Make sure the filename in your actual project matches this name before running the commands below.

---

## ⚙️ Requirements

### Operating System

* Windows 10
* Windows 11

The application uses Windows' built-in:

```text
netsh advfirewall
```

### Python

Python **3.8 or higher** is required.

Check your Python version:

```bash
python --version
```

### Administrator Privileges

Administrator access is required to retrieve the necessary Windows Firewall information.

FirewallPy can automatically request Administrator privileges through Windows UAC.

---

## 📦 Python Dependencies

The required Python packages are listed in `requirements.txt`.

| Package     | Version | Purpose                       |
| ----------- | ------: | ----------------------------- |
| `reportlab` |   4.0.4 | PDF report generation         |
| `colorama`  |   0.4.6 | Colored console output        |
| `pick`      |   1.0.0 | Interactive selection utility |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/firewall-project.git
```

Move into the project directory:

```bash
cd firewall-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application using:

```bash
python firewall.py
```

If Administrator privileges are required, Windows will display a UAC prompt.

After successful execution, FirewallPy will retrieve the enabled Windows Firewall rules and display them in the terminal.

---

## 📊 Output

The application displays information similar to:

```text
==================================================
        FIREWALL RULE VIEWER - FIREWALLPY
        (ALL RULES - Blocking & Allowed)
==================================================

ALL FIREWALL RULES (Enabled)

Total: 245 | Blocking: 32 | Allowed: 213

====================================================================================================
#    Rule Name                       Direction    Action    Protocol    Local Port    Remote Port
----------------------------------------------------------------------------------------------------
1    @FirewallAPI.dll,-28752        In           Block     Any         Any           Any
2    Google Chrome (mDNS-In)        In           Allow     UDP         5353          Any
3    Remote Assistance (DCOM-In)    In           Block     TCP         135           Any
----------------------------------------------------------------------------------------------------
```

---

## 📄 PDF Report

After processing the firewall rules, FirewallPy generates:

```text
firewall_record.pdf
```

The PDF report is saved directly on the Windows Desktop.

The report provides a more readable and professional representation of the firewall rules collected by the application.

---

## 🧱 Manual Firewall Access

Windows provides a graphical interface for managing firewall rules.

You can open the Windows Firewall Advanced Security console by running:

```text
wf.msc
```

You can also view firewall rules from Command Prompt or PowerShell using:

```powershell
netsh advfirewall firewall show rule name=all
```

FirewallPy automates the collection and presentation of this information.

---

## 🛠️ Troubleshooting

### `python` command is not recognized

Make sure Python is installed and added to the Windows PATH.

Check the installation with:

```bash
python --version
```

---

### Permission / Administrator Error

Run the application with Administrator privileges.

You can also right-click Command Prompt or PowerShell and select:

```text
Run as administrator
```

Then run:

```bash
python firewall.py
```

---

### Dependencies are missing

Run:

```bash
pip install -r requirements.txt
```

---

### PDF is not generated

Make sure the required `reportlab` package is installed:

```bash
pip install reportlab
```

---

## 🔒 Security Note

FirewallPy is intended for **firewall monitoring and information purposes**.

The application reads Windows Firewall configuration using the native Windows firewall command-line interface.

Always review firewall rules carefully before making changes to your system's firewall configuration.

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute the project according to the terms of the MIT License.

---

## 👨‍💻 Author

**Hanan Naeem**

GitHub:
`https://github.com/yourusername`

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
