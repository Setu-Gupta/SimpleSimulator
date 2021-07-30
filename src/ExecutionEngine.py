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
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val + reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()
		if(reg1Val > 255):
			self.registerFile.setFlag("V")

	def handleSub(self, inst):
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = max(0, reg2Val - reg3Val)

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()
		if(reg3Val > reg2Val):
			self.registerFile.setFlag("V")

	def handleMovImm(self, inst):
		pass

	def handleMovReg(self, inst):
		pass
	
	def handleLd(self, inst):
		pass

	def handleSt(self, inst):
		pass

	def handleMul(self, inst):
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val * reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()
		if(reg1Val > 255):
			self.registerFile.setFlag("V")

	def handleDiv(self, inst):
		pass

	def handleRs(self, inst):
		pass

	def handleLs(self, inst):
		pass

	def handleXor(self, inst):
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val ^ reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()

	def handleOr(self, inst):
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val | reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()


	def handleAnd(self, inst):
		reg1 = binAndDec(inst[7:10])
		reg2 = binAndDec(inst[10:13])
		reg3 = binAndDec(inst[13:])

		reg2Val = self.registerFile.fetch(reg2)
		reg3Val = self.registerFile.fetch(reg3)
		reg1Val = reg2Val & reg3Val

		self.registerFile.update(reg1, reg1Val)
		self.registerFile.resetAllFLags()

	def handleNot(self, inst):
		pass

	def handleCmp(self, inst):
		pass

	def handleJmp(self, inst):
		pass

	def handleJlt(self, inst):
		pass

	def handleJgt(self, inst):
		pass

	def handleJe(self, inst):
		pass


	def execute(self, inst, cycle):
		opcode = inst[:5]
		halted = True
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
			self.handleLd(inst)
		elif opcode == "00101": # st reg mem_addr
			self.handleSt(inst)
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