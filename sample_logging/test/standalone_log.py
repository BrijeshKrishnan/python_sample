import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.logging import my_logger
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename=(str(__file__)).strip(".py")+".log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
@my_logger
def test_func():
    logger.info('Start reading database')
    # read database here
    records = {'john': 55, 'tom': 66}
    logger.debug('Records: %s', records)
    logger.info('Updating records ...')
    # update records here
    logger.info('Finish updating records')
test_func()