import os
from typing import Final

ROOT: Final = os.path.abspath(os.getcwd())
DATABASE: Final = os.path.join(ROOT, 'database.db')
