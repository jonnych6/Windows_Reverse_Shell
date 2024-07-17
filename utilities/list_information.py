import platform
from datetime import datetime

def list_information():
    uname = platform.uname()
    info = {
        'system': uname.system,
        'node': uname.node
    }
    return info
