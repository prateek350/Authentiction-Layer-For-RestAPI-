import logging

def setup_logger(name):
    """Create a custon logger
    Inputs:
    name:str (location of the file for saving the logs)
    Output
    Returns a console and file logger for saving the logs"""
    logger =logging.getLogger(name)
    logger.setLevel(logging.DEBUG) #Set the base logging level
    # Create handlers
    console_handler=  logging.StreamHandler()
    file_handler =logging.FileHandler('app.log')

    #Set log levels for handlers    
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    
    #Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - X(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    #Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger