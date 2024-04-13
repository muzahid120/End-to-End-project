import logging
import os 
from datetime import datetime


log_file=f"{datetime.now().strftime('%m_%d_%Y_%M_%H_%S')}.log"
file_path=os.path.join(os.getcwd(),'Logs',log_file)

os.makedirs(file_path,exist_ok=True)

log_file_path=os.path.join(file_path,log_file)

logging.basicConfig(
filename=log_file_path,
format='%(asctime)***%(name)s***%(lineno)d***%(message)s',
level=logging.INFO,

)