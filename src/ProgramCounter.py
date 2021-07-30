# Simulates a 16 bit program counter
from utils.binAndDec import decToBin

class ProgramCounter:

	count = 0

	def __init__(self, init):
		self.count = 0

	def getVal(self):
		return self.count

	def update(self, nextPC):
		if nextPC:
			self.count = nextPC.count
		else:
			self.count += 1

	def dump(self):
		print(decToBin(self.count, 8) + " ", end="")