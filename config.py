import os

# Define constants
BASE_DIR = os.path.dirname(__file__)
PRICE_DB_PATH = os.path.join(BASE_DIR, 'data', 'price_db.csv')
FON_BALANCES_PATH = os.path.join(BASE_DIR, 'data', 'fon_balances.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'db.csv')
CAT_PATH = os.path.join(BASE_DIR, 'data', 'kategori.csv')
EXTERNAL_DATA_PATH = os.path.join(BASE_DIR, 'data', 'external_data.csv')
JSON_PATH = os.path.join(BASE_DIR, 'data', 'json_raw')
REPORT_OUTPUT = os.path.join(BASE_DIR, 'templates', 'rapor.html')
REPORT_TEMPLATE = os.path.join(BASE_DIR, 'templates', 'rapor_template.txt')
TEFAS_URL = 'https://www.tefas.gov.tr/api/DB/BindHistoryInfo'
REPORT_CSS_FILE = os.path.join(BASE_DIR, 'static', 'css', 'report.css')
REPORT_JS_FILE = os.path.join(BASE_DIR, 'static', 'js', 'report.js')
RISK_FREE = 'PPZ'
REPORT_DATES = ['2021', '2022', '2023', '2024', '2023-12', '2024-01', '2024-02', '2024-03', '2024-04', '2024-05', 'ALL']
NUM_DAYS = 10 #tail of report