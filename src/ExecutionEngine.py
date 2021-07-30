# Simulates an execution engine
from utils.binAndDec import *
from ProgramCounter import ProgramCounter

class ExecutionEngine:

	memory = None
	registerFile = None

	def __init__(self, mem, rf):
		self.memory = mem
		self.registerFile = rf

	def execute(self, inst, cycle):
		opcode = inst[:5]
		halted = True
		newPC = None
		
		if opcode == "00000": # add reg reg reg
			pass
		elif opcode == "00001": # sub reg reg reg
			pass
		elif opcode == "00010": # mov reg $Imm
			pass
		elif opcode == "00011": # mov reg reg
			pass
		elif opcode == "00100": # ld reg mem_addr
			pass
		elif opcode == "00101": # st reg mem_addr
			pass
		elif opcode == "00110": # mul reg reg reg
			pass
		elif opcode == "00111": # div reg reg
			pass
		elif opcode == "01000": # rs reg $Imm
			pass
		elif opcode == "01001": # ls reg $Imm
			pass
		elif opcode == "01010": # xor reg reg reg
			pass
		elif opcode == "01011": # or reg reg reg
			pass
		elif opcode == "01100": # and reg reg reg
			pass
		elif opcode == "01101": # not reg reg
			pass
		elif opcode == "01110": # cmp reg reg
			pass
		elif opcode == "01111": # jmp mem_addr
			pass
		elif opcode == "10000": # jlt mem_addr
			pass
		elif opcode == "10001": # jgt mem_addr
			pass
		elif opcode == "10010": # je mem_addr
			pass
		elif opcode == "10011": # hlt
			pass

		return halted, newPC