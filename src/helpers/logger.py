import logging
from src.config import settings

class Logger:
    def __init__(self):
        self.__init_python_logger()
        
    def __init_python_logger(self):
        #self.log using name instead of root
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)

        #create a handler for logs
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)

        '''
        the format that the logs will be:
        %(asctime)s     the time the self.log record was created
        %(name)s        name of the logger used
        %(levelname)s   the level of the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
        %(module)s      the module that issued the self.log call
        %(funcName)s    name of the function with the self.log call
        %(lineno)d      line number that issued self.log call
        %(message)s     the logged message
        '''
        format = logging.Formatter("(%(levelname)s) - %(filename)s:%(lineno)s :: %(message)s - DateTime(%(asctime)s)")
        
        #set the format for the each handler
        stream_handler.setFormatter(format)

        #add handler to the logging
        self.log.addHandler(stream_handler)
        return self.log

    def info(self, message):
        info_message = f"message({message})"
        self.log.info(info_message)
    
    def debug(self, message):
        debug_message = f"message({message})"
        self.log.debug(debug_message)
    
    def error(self, message):
        info_message = f"message({message}\n"
        self.log.error(info_message)
    

'''
debug("<debug-message>") #logs a debug level message at the line where the self.log request was made
info("<info_message>") #logs an info level message at the line where the self.log request was made
warning("<warning-message>") #logs a warning level message at the line where the self.log request was made
error("<error_message>") #logs an error level message at the line where the self.log request was made
critical("<critical-message>") #logs a critical level message at the line where the self.log request was made
'''

'''
try:
    # something that throws an exception
except Exception as e:
    exception("<exception-message>".format(type(e)))
#logs an error level message followed by the traceback of the error at the line where the self.log request was made
'''

logger = Logger()
logger = logger.log