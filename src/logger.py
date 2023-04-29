import logging
import os,sys
from datetime import datetime

#log file name
logfile_name = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#log directory
logfile_dir = os.path.join(os.getcwd(),"logs")

#create folder if not available
os.makedirs(logfile_dir,exist_ok=True)

#log file path
logfile_path = os.path.join(logfile_dir,logfile_name)

logging.basicConfig(
    filename=logfile_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
