import os

if os.environ.get("STAFF_DB_PATH"):
    DB_PATH = os.environ.get("STAFF_DB_PATH")
else:
    DB_PATH = os.path.join(os.path.dirname(__file__), "staff.db")
