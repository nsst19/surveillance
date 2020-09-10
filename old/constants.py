BG_BLACK = '#0D0208'
FG_GREEN = '#008F11'

WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 600
FONT = ("Courier", 12)

CONSOLE_VERSION = '0.01'

PRINTSLOW_DEFAULT_SPEED = 50

DATABASE_NAME = 'Citizen Database'
DATABASE_FILE = f'{DATABASE_NAME}.db'
DATABASE_PATH = f'database/{DATABASE_FILE}'

NUM_RANDOM_CITIZENS = 200_000
MIN_PERSON_ID = 10_000_000
MAX_PERSON_ID = 99_999_999

VILLAIN_FIRST_NAME = 'Max'
VILLAIN_LAST_NAME = 'Rodney'
VILLAIN_PERSON_ID = 29582203

NAMED_CITIZENS_IDS = {VILLAIN_PERSON_ID}
NUM_NAMED_CITIZENS = len(NAMED_CITIZENS_IDS)
CHUNK_SIZE = 10000