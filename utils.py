from datetime import datetime

def is_valid_datetime(date_string, date_format="%Y/%m/%d"):
    try:
        # Try to parse the date string with the provided format
        datetime.strptime(date_string, date_format)
        
        return True  # If parsing is successful, return True
    except:
        return False  # If an error occurs, it's not a valid datetime string
