# Simulates a register file of 8 16bit registers
from utils.binAndDec import decToBin

class RegisterFile:

	data = []

	def __init__(self):
		for i in range(8):
			self.data.append(0)

	def fetch(self, regNo):
		return self.data[regNo]

	def update(self, regNo, newVal):
		self.data[regNo] = newVal

	def getFlagIdx(self):
		idx = 100

		if flag == "V":
			idx = 3
		elif flag == "L":
			idx = 2
		elif flag == "G":
			idx = 1
		elif flag == "E":
			idx = 0

		return idx

	def setFlag(self, flag):
		idx = self.getFlagIdx(flag)
		self.data[-1] |= (2**idx) 

	def isFlagSet(self, flag):
		idx = self.getFlagIdx(flag)
		return self.data[-1] & (2**idx)
		
	def resetAllFlags(self):
		self.data[-1] = 0

	def dump(self):
		for i in range(8):
			print(decToBin(self.data[i], 16) + " ", end="")
		print("")