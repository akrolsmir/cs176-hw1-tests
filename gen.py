# Usage: python gen.py alphabet size
# >>> python gen.py ACTG 20000 > actg_20k.txt
# >>> python gen.py AZ09 40000 > az09_40k.txt

import sys, random, string

alphabet = sys.argv[1]
if alphabet == 'AZ09':
	alphabet = string.ascii_uppercase + string.digits

size = sys.argv[2]
print ''.join(random.choice(alphabet) for _ in range(int(size)))
