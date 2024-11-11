from datetime import datetime

def get_time_of_day():
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 17:
        return "day"
    elif 17 <= current_hour < 21:
        return "evening"
    else:
        return "night"
