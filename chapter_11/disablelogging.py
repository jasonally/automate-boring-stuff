#! /usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s - %(message)s')

logging.critical('Critical error! Critical error!')

logging.disable(logging.CRITICAL)

# These messages won't appear after logging.disable(logging.CRITICAL) call.
logging.critical('Critical error! Critical error!')

logging.error('Error! Error!')