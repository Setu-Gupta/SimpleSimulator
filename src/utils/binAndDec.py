# Provides utilities for binary to decimal, and vice-versa, conversions

def binToDec(binVal):
	return int(binVal, 2)

def decToBin(dec, length):
	binVal = bin(dec)[2:]
	if(len(binVal) > length):
		return binVal[-length:]
	return "0" * (length - len(binVal)) + binVal