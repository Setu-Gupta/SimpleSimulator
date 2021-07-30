# Simulates an execution engine
from utils.binAndDec import *
from ProgramCounter import ProgramCounter

class ExecutionEngine:

	memory = None
	registerFile = None

	def __init__(self, mem, rf):
		self.memory = mem
		self.registerFile = rf

	def handleAdd(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val + reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()
		if(reg1Val > 255):
			self.registerFile.setFlag("V")

	def handleSub(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = max(0, reg2Val - reg3Val)

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()
		if(reg3Val > reg2Val):
			self.registerFile.setFlag("V")

	def handleMovImm(self, inst):
		reg1 = binToDec(inst[5:8])
		imm = binToDec(inst[8:])

		self.registerFile.update(reg1, imm)
		self.registerFile.resetAllFlags()

	def handleMovReg(self, inst):
		reg1 = binToDec(inst[10:13])
		reg2 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)

		self.registerFile.update(reg1, reg2Val)
		self.registerFile.resetAllFlags()
	
	def handleLd(self, inst, cycle):
		reg1 = binToDec(inst[5:8])
		addr = binToDec(inst[8:])

		reg1Val = self.memory.fetch(addr, cycle)

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()

	def handleSt(self, inst, cycle):
		reg1 = binToDec(inst[5:8])
		addr = binToDec(inst[8:])

		reg1Val = self.registerFile.fetch(reg1)
		reg1ValBin = decToBin(reg1Val, 16)

		self.memory.store(addr, reg1ValBin, cycle)
		self.registerFile.resetAllFlags()

	def handleMul(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val * reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()
		if(reg1Val > 255):
			self.registerFile.setFlag("V")

	def handleDiv(self, inst):
		reg1 = binToDec(inst[10:13])
		reg2 = binToDec(inst[13:])

		reg1Val = self.registerFile.fetch(reg1)
		reg2Val = self.registerFile.fetch(reg2)

		quotient = reg1Val // reg2Val
		remainder = reg1Val % reg2Val

		self.registerFile.update(0, quotient)
		self.registerFile.update(1, remainder)
		self.registerFile.resetAllFlags()

	def handleRs(self, inst):
		reg1 = binToDec(inst[5:8])
		imm = binToDec(inst[8:])

		reg1Val = self.registerFile.fetch(reg1)
		reg1Val >>= imm
		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()

	def handleLs(self, inst):
		reg1 = binToDec(inst[5:8])
		imm = binToDec(inst[8:])

		reg1Val = self.registerFile.fetch(reg1)
		reg1Val <<= imm
		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()


	def handleXor(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val ^ reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()

	def handleOr(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val | reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()


	def handleAnd(self, inst):
		reg1 = binToDec(inst[7:10])
		reg2 = binToDec(inst[10:13])
		reg3 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val & reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()

	def handleNot(self, inst):
		reg1 = binToDec(inst[10:13])
		reg2 = binToDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg2ValBin = decToBin(reg2Val, 16)
		reg1ValBin = "".join(["0" if c == "1" else "1" for c in reg2ValBin])
		reg1Val  = binToDec(reg1ValBin)

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFlags()

	def handleCmp(self, inst):
		reg1 = binToDec(inst[10:13])
		reg2 = binToDec(inst[13:])

		reg1Val = self.registerFile.fetch(reg1)
		reg2Val = self.registerFile.fetch(reg2)

		self.registerFile.resetAllFlags()
		if(reg1Val == reg2Val):
			self.registerFile.setFlag("E")
		elif(reg1Val > reg2Val):
			self.registerFile.setFlag("G")
		else:
			self.registerFile.setFlag("L")

	def handleJmp(self, inst):
		addr = binToDec(inst[8:])

		self.registerFile.resetAllFlags()
		return ProgramCounter(addr)

	def handleJlt(self, inst):
		addr = binToDec(inst[8:])

		newPC = None
		if(self.registerFile.isFlagSet("L")):
			newPC = ProgramCounter(addr)

		self.registerFile.resetAllFlags()
		return newPC

	def handleJgt(self, inst):
		addr = binToDec(inst[8:])

		newPC = None
		if(self.registerFile.isFlagSet("G")):
			newPC = ProgramCounter(addr)

		self.registerFile.resetAllFlags()
		return newPC


	def handleJe(self, inst):
		addr = binToDec(inst[8:])

		newPC = None
		if(self.registerFile.isFlagSet("E")):
			newPC = ProgramCounter(addr)

		self.registerFile.resetAllFlags()
		return newPC

	def execute(self, inst, cycle):
		opcode = inst[:5]
		halted = False
		newPC = None
		
		if opcode == "00000": # add reg reg reg
			self.handleAdd(inst)
		elif opcode == "00001": # sub reg reg reg
			self.handleSub(inst)
		elif opcode == "00010": # mov reg $Imm
			self.handleMovImm(inst)
		elif opcode == "00011": # mov reg reg
			self.handleMovReg(inst)
		elif opcode == "00100": # ld reg mem_addr
			self.handleLd(inst, cycle)
		elif opcode == "00101": # st reg mem_addr
			self.handleSt(inst, cycle)
		elif opcode == "00110": # mul reg reg reg
			self.handleMul(inst)
		elif opcode == "00111": # div reg reg
			self.handleDiv(inst)
		elif opcode == "01000": # rs reg $Imm
			self.handleRs(inst)
		elif opcode == "01001": # ls reg $Imm
			self.handleLs(inst)
		elif opcode == "01010": # xor reg reg reg
			self.handleXor(inst)
		elif opcode == "01011": # or reg reg reg
			self.handleOr(inst)
		elif opcode == "01100": # and reg reg reg
			self.handleAnd(inst)
		elif opcode == "01101": # not reg reg
			self.handleNot(inst)
		elif opcode == "01110": # cmp reg reg
			self.handleCmp(inst)
		elif opcode == "01111": # jmp mem_addr
			newPC = self.handleJmp(inst)
		elif opcode == "10000": # jlt mem_addr
			newPC = self.handleJlt(inst)
		elif opcode == "10001": # jgt mem_addr
			newPC = self.handleJgt(inst)
		elif opcode == "10010": # je mem_addr
			newPC = self.handleJe(inst)
		elif opcode == "10011": # hlt
			halted = True

		return halted, newPC