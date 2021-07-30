# Provides utilities for binary to decimal, and vice-versa, conversions

def binToDec(bin):
	pass

def decToBin(dec, length):
	binVal = bin(dec)[2:]
	return "0" * (length - len(binVal)) + binVal