import os
import logging
from pathlib import Path


logging.basicConfig( level=logging.INFO, 
                     format='[%(asctime)s] %(message)s' )

# logging.info("Test Log")

list_of_files = [
                "src/__init__.py",
                "src/prompt.py",
                "src/helper.py",
                "research/trials.py", # before modularising
                "requirements.txt",
                "setup.py",
                "app.py",
                ".env"
                ]


for file in list_of_files:
    filedir, filename = os.path.split(file)

    logging.info(f"{filedir}, {filename}")

    if filedir != "":
        # create this dir
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"New Directory : {filedir} created")
    
    if (not os.path.exists(filename) or (os.path.getsize(filename) == 0) ):
        # file DNE or file exists but (if content present dont overwrite)
        with open(file, "w") as f:
            pass
            logging.info(f"New file created {filename}")
    else:
        logging.info(f"File already present")


