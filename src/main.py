# Main file which runs the simulator

from Memory import Memory
from RegisterFile import RegisterFile
from ExecutionEngine import ExecutionEngine
from ProgramCounter import ProgramCounter

def main():
	memory = Memory()
	registerFile = RegisterFile()
	executionEngine = ExecutionEngine(memory, registerFile)
	PC = ProgramCounter(0)
	halted = False

	while not halted:
		inst = memory.fetch(PC.getVal())
		halted, nextPC = executionEngine.execute(inst)
		PC.dump()
		registerFile.dump()
		PC.update(nextPC)

	memory.dump()

if __name__ == '__main__':
	main()