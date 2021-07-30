# Simulates 512 bytes of double byte addressable memory

import sys
import re
from utils.colors import bcolors

class Memory:

	mem = []

	def __init__(self):
		for line in sys.stdin:
			line = line.strip()
			if(len(line) != 16 or not re.match('^[01]*$', line)):
				print(bcolors.FAIL + "ERROR: Unknown line format detected. Aborting! " + bcolors.OKCYAN + "Each line must for 16 characters long, composed of 0s and 1s." + bcolors.ENDC)
				exit(-1)
			self.mem.append(line.strip())

		if len(self.mem) > 256:
			print(bcolors.FAIL + "ERROR: More than 256 lines of memory provided. Aborting!" + bcolors.ENDC)
			exit(-1)

		if len(self.mem) < 256:
			defaultValue = "0"*16
			self.mem = self.mem + [defaultValue]*(256 - len(self.mem))

	def fetch(self, addr):
		return self.mem[addr]

	def dump(self):
		for m in self.mem:
			print(m)