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
	cycle = 0

	while not halted:
		inst = memory.fetch(PC.getVal(), cycle)
		halted, nextPC = executionEngine.execute(inst, cycle)
		PC.dump()
		registerFile.dump()
		PC.update(nextPC)
		cycle += 1

	memory.dump()
	memory.showTraces()

if __name__ == '__main__':
	main()