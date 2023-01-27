from datetime import datetime, timedelta
from time import time

def formatTimestamp(timestamp: float, format: str = "%d.%m.%Y - %H:%M:%S"):
    """
        * Format date timestamp to date string
    """
    return datetime.fromtimestamp(timestamp).strftime(format)

def lastDaysTimestamp(days: int = 10):
    """
        * Get the last n days timestamp
    """
    day = timedelta(days=days).total_seconds()
    ctime = time()
    days_before_time_stamp = ctime - day
    return days_before_time_stamp

def nowTimestamp(): 
    """
        * Returns current timestamp
    """
    return time()