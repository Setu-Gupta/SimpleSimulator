# Simulates 512 bytes of double byte addressable memory

import sys
import re
from utils.colors import bcolors
import matplotlib.pyplot as plt

class Memory:

	mem = []
	trace = []

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

	def fetch(self, addr, cycle):
		self.trace.append([cycle, addr])
		return self.mem[addr]

	def store(self, addr, data, cycle):
		self.trace.append([cycle, addr])
		self.mem[addr] = data

	def dump(self):
		for m in self.mem:
			print(m)

	def showTraces(self):
		x = [t[0] for t in self.trace]
		y = [t[1] for t in self.trace]
		plt.title("Memory Accesses v/s Cycles")
		plt.xlabel("Cycle")
		plt.ylabel("Address")

		plt.scatter(x, y)
		plt.autoscale(enable=True, axis='both', tight=True)
		
		plt.ylim([0, 255])
		plt.yticks([10*i for i in range(26)])
		plt.xlim(0)
		plt.savefig("pattern.png")