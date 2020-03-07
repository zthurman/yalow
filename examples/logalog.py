from pathlib import Path
from yalow import Yalow
from examples.example_package import super_mega_ukulele

I_AM_GROOT = Path(__file__).parent.parent

logger = Yalow(root_path=I_AM_GROOT, project='logalog').logger

logger.info(f'IT\'S ALIVE!!!!!')
super_mega_ukulele()
