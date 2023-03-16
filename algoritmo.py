def productouct(op1, op2):
	i = 0
	acarreo = 0
	sum = []
	producto = 0

	# if firstBinary number or second Binary number is not
	# zero then calculate the product of two Binary numbers
	while op1 != 0 or op2 != 0:
		sum.insert(i, (((op1 % 10) + (op2 % 10) + acarreo) % 2))
		acarreo = int(((op1 % 10) + (op2 % 10) + acarreo) / 2)
		op1 = int(op1/10)
		op2 = int(op2/10)
		i = i+1

	# if acarreo value is not equal to
	# zero then insert the digit to sum array
	if acarreo != 0:
		sum.insert(i, acarreo)
		i = i+1
	i = i-1
	while i >= 0:
		producto = (producto * 10) + sum[i]
		i = i-1
	return producto


# Now check if secondbinary number have any
# digit or not and continue multiplying
# each digit of the second binary number with
# first binary number till the last digit of
# second binary number

def operar (firstBinary, secondBinary):
	binaryMultiply = 0 
	factor = 1
	while secondBinary != 0:
		digit = secondBinary % 10
		if digit == 1:
			firstBinary = firstBinary * factor
			binaryMultiply = productouct(firstBinary, binaryMultiply)
		else:
			firstBinary = firstBinary * factor
		secondBinary = int(secondBinary/10)
		factor = 10
	
	print("\nMultiplication Result = " + str(binaryMultiply))
	return binaryMultiply

 
 