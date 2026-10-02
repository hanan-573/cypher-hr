# 🛡️ FirewallPy — Windows Firewall Rule Viewer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A lightweight Python-based tool that fetches, displays, and exports **Windows Firewall rules** (both Blocking and Allowed) directly from the system using `netsh`, presenting them in a clean colored console table and generating a professional **PDF report** on the Desktop.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Output](#-output)
- [Manual Firewall Access](#-manual-firewall-access)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Author](#-author)

---

## 📖 Overview

**FirewallPy** is a simple yet powerful utility for Windows users who want a quick, readable overview of all currently enabled firewall rules on their machine. Instead of navigating through the tedious `wf.msc` GUI, this tool:

- Automatically fetches **all enabled firewall rules** via `netsh advfirewall`
- Categorizes them into **Blocking** and **Allowed** rules
- Displays them in a **color-coded console table**
- Exports a well-formatted **PDF report** to your Desktop

It auto-elevates itself to **Administrator** privileges using the Windows UAC prompt, so no manual setup is required.

---

## ✨ Features

- ✅ **Automatic Admin Elevation** — Triggers UAC prompt if not running as Administrator
- ✅ **Fetches All Enabled Rules** — Inbound & Outbound, Blocking & Allowed
- ✅ **Color-Coded Console Output** — Red for blocked, Green for allowed
- ✅ **Live Rule Counter** — Shows total, blocking, and allowed rule counts
- ✅ **PDF Report Generation** — Saves `firewall_record.pdf` directly to Desktop
- ✅ **Windows Native** — Uses built-in `netsh advfirewall` (no third-party firewall tools needed)
- ✅ **Lightweight & Fast** — Pure Python with minimal dependencies
- ✅ **Cross-Console Compatible** — Uses `colorama` for proper color support on Windows CMD/PowerShell

---

## 🏗️ How It Works

**Step-by-step flow:**

1. User runs `firewall.py`
2. Script checks for Administrator privileges
3. If not admin → UAC prompt appears → script re-launches elevated
4. Runs `netsh advfirewall firewall show rule name=all`
5. Parses raw text output into structured rule dictionaries
6. Filters only **Enabled** rules
7. Separates rules into **Blocking** and **Allowed**
8. Prints a color-coded table in the terminal
9. Generates a PDF report on the Desktop

---

## 📁 Project Structure

> 📝 **Note:** Although the main file is named `firewall.py`, its header comment says `main.py` — this is just a legacy comment and does not affect execution.

---

## ⚙️ Requirements

### System Requirements
- **OS:** Windows 10 / Windows 11 (uses `netsh advfirewall`)
- **Python:** 3.8 or higher
- **Privileges:** Administrator access (auto-elevated via UAC)

### Python Dependencies

Listed in `requirements.txt`:

| Package | Version | Purpose |
|---------|---------|---------|
| `reportlab` | 4.0.4 | PDF report generation |
| `colorama` | 0.4.6 | Cross-platform colored terminal output |
| `pick` | 1.0.0 | Interactive selection utility |

---

## 🚀 Installation

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/firewall-project.git
cd firewall-project

python -m venv venv
venv\Scripts\activate

Install dependencies: 
pip install -r requirements.txt


Usage:
python firewall.py



Example Console Output: 
==================================================
  FIREWALL RULE VIEWER - firewallpy
  (ALL RULES - Blocking & Allowed)
==================================================

ALL FIREWALL RULES (Enabled)
Total: 245  |  Blocking: 32  |  Allowed: 213
====================================================================================================
#    Rule Name                      Direction  Action   Protocol   Local Port   Remote Port
----------------------------------------------------------------------------------------------------
1    @FirewallAPI.dll,-28752         In         Block    Any        Any          Any
2    Google Chrome (mDNS-In)         In         Allow    UDP        5353         Any
3    Remote Assistance (DCOM-In)     In         Block    TCP        135          Any
...
----------------------------------------------------------------------------------------------------
