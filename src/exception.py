import sys
import logging
from src.loggers import logging

def error_message_details(error,error_detais:sys):
    """
    Function to print error message
    :param error: Error message
    :param error_detais: Error details
    :return: None
    """
    _,_, exc_tb = sys.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    # Formatting the error message
    error_message = f"Error occurred in script: {0} at line {1} error: {2}".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details)
    def __str__(self):
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Division by zero error")
#         raise CustomException(e,sys)
    