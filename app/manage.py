#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Step 1: Get DJANGO_ENV early
DJANGO_ENV = os.getenv('DJANGO_ENV')
print(f"DJANGO_ENV: {DJANGO_ENV}")

# Step 2: Sanity check
if DJANGO_ENV not in ['development', 'production']:
    raise ValueError(f"Invalid DJANGO_ENV: {DJANGO_ENV}. Must be 'development' or 'production'.")

# Step 3: Load corresponding .env file
PROJECT_ROOT = Path(__file__).resolve().parent # Assuming manage.py is in the app directory
# Ensure the PYTHONPATH includes the project root
sys.path.append(str(PROJECT_ROOT))
# print(f"Project root: {PROJECT_ROOT}")
env_file = PROJECT_ROOT.parent / ('.env.development' if DJANGO_ENV == 'development' else '.env.production')
# print(f"Loading environment variables from: {env_file}")
load_dotenv(dotenv_path=env_file)

# Step 4: Set Django settings module
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"core.settings.{DJANGO_ENV}"
)

def main():
    """Run administrative tasks."""
    if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        # Ensure the working directory is set to the app directory
        os.chdir(PROJECT_ROOT / 'core')
        print(f"Running server in {DJANGO_ENV} mode...")
    else:
        print(f"Running management command in {DJANGO_ENV} mode...")

    # Step 5: Execute command line arguments
    sys.argv[0] = str(PROJECT_ROOT / 'manage.py')  # Ensure manage.py is correctly referenced
    if DJANGO_ENV == 'development':
        sys.argv.append('--settings=core.settings.development')
    else:
        sys.argv.append('--settings=core.settings.production')
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
