import random
import time
import os
import sys

rand1 = random.randint(1,10)
rand2 = random.randint(1,10)

print ("THE FIRST NUMBER IS %s." % rand1)
time.sleep(3)

print ("THE SECOND NUMBER IS %s" % rand2)
time.sleep(3)

sol1 = (rand1 * rand2)

print "%d X %d = %d "  % (rand1, rand2, sol1)
time.sleep(3)

os.system("clear")
sys.exit()