#Program to get user input and try for loop

def main():
	number = int(input("Enter number: "))
	for i in range (1, 11,1 ): #syntax for range is - range(begin, end, step)
		print (number, "\tx\t", i, "\t=\t", number *i)

main()