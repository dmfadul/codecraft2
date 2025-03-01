from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "1d43505933ccba3e9522067997391569fd20aa2851e2d22d880e17632dde357c"
DEBUG = True
IS_DEVELOPMENT = True

STATICFILES_DIRS = [BASE_DIR / 'static']
