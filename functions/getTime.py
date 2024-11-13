from datetime import datetime

def get_time_response():
    now = datetime.now()
    return now.strftime("%H:%M:%S")