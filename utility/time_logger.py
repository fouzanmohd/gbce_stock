import datetime
class TimeLogger:
    
    """This class helps in logging and manipulating time formats
    
    Methods
    -------
    get_current_time:
        returns current time in string format
    
    get_time_window:
        returns a time before selected minutes 
        
    convert_date_to_timestamp:
        convert date in string format to date in timestamp
    
    """
    def get_current_time(self) -> str:
        
        """This method returns current time in dd-mm-yyy hh:mm:ss formatS

        Returns:
            str: returns date and time in string format
        """
        
        return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S.%f')
        
    def get_time_window(self, minutes: int | float):
        
        """This method can be used to get a time window by taking minutes as argument. for example, to take the window of last 
           10 minutes, use this method with argument as 10

        Args:
            minutes (int | float): time in minutes

        Returns:
            datetime: returns the time before 'X' minutes. where X is the minute argument
        """
        return (datetime.datetime.now() - datetime.timedelta(minutes=minutes))
    
    def convert_date_to_timestamp(self, date:str)->float:
        
        """this method convert any date in string format to timestamp

        Args:
            date (str): date and time in string format

        Returns:
            float: returns timestamp in float type
        """
        
        date_time = datetime.datetime.strptime(date, '%d-%m-%Y %H:%M:%S.%f')
        return date_time.timestamp()
