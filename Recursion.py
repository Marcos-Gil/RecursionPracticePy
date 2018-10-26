# By: Marcos Gil

def recursiveLongDivision(dividend, divisor): # My recursive division function which takes both a dividend and divisor from the user then calculates the answer using recursion
	
	if divisor == 0:
		return ("Sorry, you are not allowed to divide by zero. ")
    
	elif dividend < divisor:
		return (0, dividend)
	
	else:
		(x, y) = recursiveLongDivision(dividend - divisor, divisor)
		return (x + 1, y)
		
def recursiveMultiplication(factor1, factor2): # My recursive multiplication function which takes both the factors the user wants to use then calculates the answer using recursion
	
	if (factor1 == 0) or (factor2 == 0):
		return 0
	
	if factor1 == 1:
		return factor2
		
	if factor2 == 1:
		return factor1
	
	else:
		addition = factor2
		return addition + recursiveMultiplication(factor1 - 1, factor2)

def main():# Main function which will initialize my program, asks the user if they want to multiply or divide, then gets both the integers they'd like to enter

	userInput = input('Do you want to multiply or divide?(type "multiply" or "divide") ').lower()

	while (userInput != 'multiply') and (userInput != 'divide'):
		print('Sorry, you can only enter multiply or divide, please try again. ')
		userInput = input('Do you want to multiply or divide? ').lower()
	
	while True:
		try:
			if userInput == 'multiply':
				userIntOne = int(input('What is the first number being multiplied? '))
				userIntTwo = int(input('What is the second number being multiplied? '))
				print(recursiveMultiplication(userIntOne, userIntTwo))
				break

			if userInput == 'divide':	
				userIntOne = int(input('What is the dividend? '))
				userIntTwo = int(input('What is the divisor? '))
				print(recursiveLongDivision(userIntOne, userIntTwo))
				break
		
		except:
			print('Sorry only integers are accepted as input, please try again. ')
			continue
			
main() # Calling my main function to start the program