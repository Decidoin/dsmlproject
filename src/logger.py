import logging 
import os 
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
log_file = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_path = os.path.join(LOG_DIR)
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, log_file)

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO)

