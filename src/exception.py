import sys











def error_message_details(error,error_det:sys):
    _,_,exc_tb=error_det.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_mes="Error occured pyhton script name {0} line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )

    return error_mes




class CustomException(Exception):
    def __init__(self, error_mes,error_det:sys):
        super().__init__(error_mes)
        self.error_mes=error_message_details(
            error_mes,error_det=error_det
        )
    
    def __str__(self):
        return self.error_mes