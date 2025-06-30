import logging


# logging.basicConfig(filename='log.txt', level=logging.info)

class Greet:
    """This class is for Greet
    """
    logging.info("This is a greet class")
    def greet(self,name):
        return f"Hello {name}"
    
    