from pathlib import Path

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / 'logs'

MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_DOC_URL = 'https://peps.python.org/'

EXPECTED_STATUS = {
    'A': ['Active', 'Accepted'],
    'D': ['Deferred'],
    'F': ['Final'],
    'P': ['Provisional'],
    'R': ['Rejected'],
    'S': ['Superseded'],
    'W': ['Withdrawn'],
    '': ['Draft', 'Active'],
}
