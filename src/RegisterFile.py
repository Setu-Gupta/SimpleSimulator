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

	def dump(self):
		for i in range(8):
			print(decToBin(self.data[i], 16) + " ", end="")
		print("")