import sqlite3

from config import CREDENTIALS_FILE, spreadsheet_id
from db.parse import parse

data = parse(CREDENTIALS_FILE, spreadsheet_id)
