import logging
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
# imported logging to create logs of test cases

class LogGen:
    #created a static method to initialize log setup here
    @staticmethod
    def loggen():
        # For formate of the logs in file:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        # Handler where our file will store:
        BASE_DIR = Path(__file__).resolve().parent.parent
        config_dir = BASE_DIR / "Logs"
        handler = logging.FileHandler(filename=f'{config_dir}/automation.log')
        # Here setting format to file
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
