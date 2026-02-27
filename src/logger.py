import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Log File Name

# Make a Path by take current directory(mlproject) and create logs directory and inside it create log file with a named by LOG_FILE.
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) 
os.makedirs(logs_path, exist_ok=True)         # Create directory with logs_path if exist ok otherwise create it.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # Create full path i.e logs path and inside it log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

# if __name__=="__main__":
#     logging.info("Logging has started")