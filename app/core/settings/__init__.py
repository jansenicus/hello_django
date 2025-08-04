import os
from pathlib import Path
from dotenv import load_dotenv

APP_ROOT = Path(__file__).resolve().parent.parent.parent.parent
# Assuming this file is at app/core/settings/__init__.py, the BASE_DIR will be app/
# print(f"Base directory: {APP_ROOT}")

# Step 1: Check if the environment variable is set
if 'DJANGO_ENV' not in os.environ:
    raise EnvironmentError("\n\nDJANGO_ENV environment variable is not set." \
    "\nPlease set it to 'development', 'staging' or 'production'." \
    "\nExample:\nexport DJANGO_ENV=development\n")   

# Step 2: Get DJANGO_ENV early
DJANGO_ENV = os.getenv('DJANGO_ENV')

# Step 3: Sanity check
if DJANGO_ENV not in ['development', 'staging', 'production']:
    raise ValueError(f"\n\nInvalid DJANGO_ENV='{DJANGO_ENV}'. Only 'development', 'staging' or 'production' are allowed.\n")

# Step 4: Load corresponding .env file
env_file = APP_ROOT / ('.env.development' if DJANGO_ENV == 'development' else '.env.production')
print(f"Loading environment variables from: {env_file}")
load_dotenv(dotenv_path=env_file)

# Step 5: Set the default settings module based on DJANGO_ENV
os.environ.setdefault("DJANGO_SETTINGS_MODULE",f"core.settings.{DJANGO_ENV}")