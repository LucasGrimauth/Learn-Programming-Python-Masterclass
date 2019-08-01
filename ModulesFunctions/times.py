# import time

# print(time.gmtime(0))

# mytime = time.localtime()

# print(mytime)
# print("Year:", mytime[0], mytime.tm_year)
# print("Month", mytime[1], mytime.tm_mon)
# print("Day:", mytime[2], mytime.tm_mday)

import time
from time import time as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input('Press enter to stop')  

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))