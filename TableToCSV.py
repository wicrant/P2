# Program to try File IO
# Enter a number to calculate the table and then copy the table to a number.csv file
#import file
def someFunction (): 
	""" this is documentatio comment"""
	pass 				#Use pass if there is nothing defined in the fuction
def main(): 
	file = open ("table.csv", "r+")
	print (someFunction.__doc__)
	#file.write ( "Python writing to file" )
	#number = int(input("Enter number: "))
	#for i in range (1, 11,1 ): #syntax for range is - range(begin, end, step)
		#print (number, "\tx\t", i, "\t=\t", number * i)
	#	str = (number, 'x', i, '=', number * i)
		#str = (%d + "\tx\t" + %d + "\t=\t" + %d % (number, i, number*i))
		#print (%d  %d  %d %(number, i, number*i))
#		print (str)
#		file.write ( str )
#	file.close()
		
main() 
someFunction()
print ("name %s and age %d" % ('Vikrant', 39))
input("Press any key to exit")



