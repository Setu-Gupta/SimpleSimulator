# Simulates an execution engine
from utils.binAndDec import *
from ProgramCounter import ProgramCounter

class ExecutionEngine:

	memory = None
	registerFile = None

	def __init__(self, mem, rf):
		self.memory = mem
		self.registerFile = rf

	def execute(self, inst):
		return True, ProgramCounter(0)