# Logger.py
import logging

logger = logging.getLogger('log')

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logs.log')
logger.setLevel(logging.INFO)
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)


# logger.info('test')
