import shutil
du = shutil.disk_usage("/")
print("Total: %d GiB" % (du.total / 2**30))
print("Used: %d GiB" % (du.used / 2**30))
print("Free: %d GiB" % (du.free / 2**30))

import psutil
print(psutil.cpu_count(0.1))

