import sys
from src.logger import logging


# This function i will call when any error is raised
def error_message_detail(error, error_detail:sys): # I will get error and the error details present in sys library
    """
     _,_,exc_tb = error_detail.exc_info()
    This will three(3) the first two information i am not at all interseted but the 3rd one gives on which file and on which line exeception
    has been occure
    """
    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_lineno = exc_tb.tb_lineno
    error = str(error)

    error_message = f"Error occured in python script {file_name} line number {error_lineno} error message {error}"
    return error_message




class CustomException(Exception):
    """
    This class will takes two parameters i.e error_message and error_details and will
    return an error message along with the file name, error line number
    """
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error=error_message, error_detail= error_detail)

    
    def __str__(self):
        return self.error_message
    

# Thw below code is just for checking the above code that it is working or not.
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divided by zero")
#         raise CustomException(e, sys)
        