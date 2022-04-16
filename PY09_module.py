import os
from os import getlogin
import psutil
from psutil import virtual_memory
sysdata = {
            'user_name': getlogin(),
            'memory_total': virtual_memory()[0],
            'memory_used':virtual_memory()[3],
            'memory_percent': virtual_memory()[2]
           }