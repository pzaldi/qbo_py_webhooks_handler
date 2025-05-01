import datetime

def get_date_time_hours_minutes():
    """
    Returns the current date and time formatted as YYYY-MM-DD HH:MM.
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
