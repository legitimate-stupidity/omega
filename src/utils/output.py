"""
OMEGA Output Formatting Module
Handles all terminal output, colors, and formatting.
"""

import sys


class Color:
    """ANSI color code manager for terminal output."""
    
    try:
        is_tty = sys.stdout.isatty()
    except:
        is_tty = False
    
    if is_tty:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
    else:
        HEADER = OKBLUE = OKCYAN = OKGREEN = WARNING = FAIL = ENDC = BOLD = ''


def print_header(title):
    """Print formatted header."""
    print(f"\n{Color.OKCYAN}{Color.BOLD}[*] {title} [*]{Color.ENDC}")


def print_sub_header(title):
    """Print formatted sub-header."""
    print(f"\n{Color.BOLD}--- {title} ---{Color.ENDC}")


def print_result(data):
    """Print formatted result."""
    print(f"\n{Color.OKGREEN}[+] Result:\n{data}{Color.ENDC}")


def print_error(message):
    """Print formatted error message."""
    print(f"{Color.FAIL}[!] {message}{Color.ENDC}")


def print_info(message):
    """Print formatted info message."""
    print(f"{Color.OKBLUE}[i] {message}{Color.ENDC}")


def print_debug(message):
    """Print formatted debug message."""
    print(f"{Color.HEADER}[DEBUG] {message}{Color.ENDC}")


def print_warning(message):
    """Print formatted warning message."""
    print(f"{Color.WARNING}[⚠] {message}{Color.ENDC}")


def print_success(message):
    """Print formatted success message."""
    print(f"{Color.OKGREEN}[✓] {message}{Color.ENDC}")
