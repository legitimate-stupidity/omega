#!/usr/bin/env python3
"""
OMEGA Main Entry Point
Project OMEGA v4.0 - Advanced Persistent Attack Framework

Usage:
    python -m omega [options]
    python omega.py [options]

Options:
    --db <path>      Use persistent database at <path>
    --help           Show this help message
"""

import sys
import argparse
from src.agent import OmegaAgent
from src.utils import Color, print_header, print_error, print_info


def main():
    """Main entry point for OMEGA."""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Project OMEGA v4.0 - Advanced Persistent Attack Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python omega.py                  # Use in-memory database
  python omega.py --db omega.db    # Use persistent database
        '''
    )
    
    parser.add_argument(
        '--db',
        default=':memory:',
        help='Database path (default: in-memory)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='OMEGA v4.0'
    )
    
    args = parser.parse_args()
    
    # Version check
    if sys.version_info < (3, 8):
        print_error("ERROR: Python 3.8+ required")
        sys.exit(1)
    
    try:
        # Initialize and run OMEGA Agent
        agent = OmegaAgent(db_path=args.db)
        agent.cmdloop()
    
    except KeyboardInterrupt:
        print(f"\n{Color.OKBLUE}[!] Agent interrupted by user{Color.ENDC}")
        sys.exit(0)
    except Exception as e:
        print_error(f"Critical error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
