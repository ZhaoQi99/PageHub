from datetime import datetime


def get_now_str():
    return datetime.now().astimezone().strftime("%Y%m%d%H%M%S")
