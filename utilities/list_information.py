import platform
import psutil
from datetime import datetime

def basic_info():
    uname = platform.uname()
    info = {
        'System': uname.system,
        'Node': uname.node,
        'Release': uname.release,
        'Version': uname.version,  
        'Machine': uname.machine,
        'Processor': uname.processor,
    }
    return info


# this uses psutil, which means that you must activate virtual env in powershell, to use this function (or you will run into a psutil import problem and wont be able to start client.py)
def boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    info = {
        'year': bt.year,
        'month': bt.month,
        'day': bt.day,
        'hour': bt.hour,
        'minute': bt.minute,
        'second': bt.second,
    }
    return info

def cpu_info():
    
