#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	from calculator_1 import add, sub, mul, div

	if len(argv) != 4:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)	
	opp = {"+": add, "-": sub, "*": mul, "/": div}
	a = argv[1]
	b = argv[3]
	u = argv[2]

	if u not in opp:
		print("Unknown operator. Available operators: +, -, * and /")
		exit(1)
	print("{} {} {} = {}".format(a, u, b, opp[u](a, b)))	
