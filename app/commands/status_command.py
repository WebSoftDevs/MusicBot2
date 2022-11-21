import time
import requests
import psutil
from app.utility import second_parser

# Latency measurement
url = "https://discord.com"
get_uptime = requests.get(url).elapsed.total_seconds()

# Uptime since running pc
def uptime():
    return time.time() - psutil.boot_time()


print("Uptime:", second_parser.parse_duration(uptime()))
print("Latency is:", int(get_uptime * 1000), "ms")
print("Available Memory:", psutil.virtual_memory()[1] // 1000000, "MB")
