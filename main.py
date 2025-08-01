#!/usr/bin/env python3

import sys
import traceback

def main():
    try:
        from ponder.ponder import activate_ponder
        print("Starting philosophical tweet generation...")
        activate_ponder()
        print("Tweet generation completed successfully!")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure all required files are present and ponder/__init__.py exists")
        sys.exit(1)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Full traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()