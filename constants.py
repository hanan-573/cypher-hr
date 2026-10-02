# constants.py

FIREWALL_CMD = "netsh advfirewall firewall show rule name=all"

# Color codes
HEADER = "\033[95m"   # Purple
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# PDF file path (Desktop)
import os
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
PDF_FILE = os.path.join(DESKTOP, "firewall_record.pdf")