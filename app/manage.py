#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path
# from dotenv import load_dotenv

# Step 0: Set up the project root
# Assuming this file is at app/manage.py, the project root will be app
# This allows us to set the PYTHONPATH correctly
# and load environment variables from the correct .env file.
APP_ROOT = Path(__file__).resolve().parent 
sys.path.append(str(APP_ROOT))
# print(f"APPLICATION ROOT: {APP_ROOT}")

from core.settings import DJANGO_ENV

def main():
    """Run administrative tasks."""
    # Ensure manage.py is the script name
    sys.argv[0] = str(APP_ROOT / 'manage.py')
    
    # Ensure the working directory is set to the app directory
    os.chdir(APP_ROOT)

    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        print(f"Running server in {DJANGO_ENV} mode...")
    else:
        print(f"Running management command in {DJANGO_ENV} mode...")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
