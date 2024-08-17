import sys
import logging
def error_msg_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="error ocured in python script [{0}] line no [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    return error_msg


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message,error_detail=error_detail)
        
        def __str__(self):
            return self.error_message
        
if __name__=="__main__":
    
    try:
        a=1/0
    except Exception as e:
        
        logging.info('Divide by Zero')
        raise CustomException(e,sys)