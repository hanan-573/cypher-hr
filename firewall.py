# main.py

import os
import sys
import ctypes
import colorama
from constants import GREEN, RED, YELLOW, BLUE, BOLD, RESET, HEADER, CYAN
from firewall_handler import get_all_rules, parse_rules, separate_rules, export_to_pdf

# Initialize colorama for Windows
colorama.init(autoreset=True)

def is_admin():
    """Check if script is running with admin privileges on Windows."""
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def run_as_admin():
    """Re-run the script with admin privileges (Windows) — shows UAC prompt."""
    script = os.path.abspath(sys.argv[0])
    args = ' '.join(f'"{arg}"' for arg in sys.argv[1:])
    cmd = f'"{script}" {args}' if args else f'"{script}"'
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, cmd, None, 1
        )
    except Exception as e:
        print(f"❌ Failed to elevate privileges: {e}")
        print("Please run as Administrator manually (Right-click -> Run as Administrator).")

def print_all_rules(all_rules):
    """Print all rules in a formatted table with Action column."""
    if not all_rules:
        print(f"{YELLOW}No rules found.{RESET}")
        return

    # Count blocking and allowed
    block_count = sum(1 for r in all_rules if r.get('Action') == 'Block')
    allow_count = len(all_rules) - block_count

    print(f"\n{CYAN}{BOLD}ALL FIREWALL RULES (Enabled){RESET}")
    print(f"{BLUE}Total: {len(all_rules)}  |  Blocking: {RED}{block_count}{RESET}  |  Allowed: {GREEN}{allow_count}{RESET}")
    print(f"{'='*100}")

    # Table header
    print(f"{BOLD}{'#':<4} {'Rule Name':<30} {'Direction':<10} {'Action':<8} {'Protocol':<10} {'Local Port':<12} {'Remote Port':<12}{RESET}")
    print("-"*100)

    for idx, r in enumerate(all_rules, 1):
        action = r.get('Action', 'N/A')
        color = RED if action == 'Block' else GREEN
        print(f"{color}{idx:<4} {r.get('Name', 'N/A')[:28]:<30} {r.get('Direction', 'N/A'):<10} {action:<8} {r.get('Protocol', 'N/A'):<10} {r.get('LocalPort', 'N/A'):<12} {r.get('RemotePort', 'N/A'):<12}{RESET}")
    print("-"*100)

def main():
    print(HEADER + "="*50)
    print("  FIREWALL RULE VIEWER - firewallpy")
    print("  (ALL RULES - Blocking & Allowed)")
    print("="*50 + RESET)

    # Check admin
    if not is_admin():
        print(f"{YELLOW}This script requires administrator privileges to fetch firewall rules.{RESET}")
        print(f"{BLUE}Attempting to run with admin... (UAC prompt will appear){RESET}")
        run_as_admin()
        sys.exit(0)

    # Now running as admin
    raw = get_all_rules()
    if raw is None:
        print(f"{RED}Failed to fetch firewall rules. Please check your system.{RESET}")
        return

    all_rules = parse_rules(raw)
    block_rules, allow_rules = separate_rules(all_rules)

    # Display all rules in table
    print_all_rules(all_rules)

    # Export to PDF
    print(f"\n{BLUE}Generating PDF report...{RESET}")
    pdf_path = export_to_pdf(all_rules, block_rules, allow_rules)
    print(f"{GREEN}✅ PDF saved at: {pdf_path}{RESET}")

    input(f"\n{YELLOW}Press Enter to exit...{RESET}")

if __name__ == "__main__":
    main()