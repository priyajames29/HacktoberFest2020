import sub

num1 = ans = input("Enter the first number to be computed:")
flag = "Y"
while(flag == "Y" or flag == "y"):
	op = input("Enter the operator(+,-,*,/)")
	num2 = input("Enter the second number to be computed:")
	new = sub.Calculator(float(ans), float(num2))
	if op=='+':
		ans = new.addition()
		print(ans)	
	if op=='-':
		ans = new.substraction()
		print(ans)
	if op=='*':
		ans = new.mul()
		print(ans)
	if op=='/':
		ans = new.division()
		print(ans)
	flag = input("Do you want to do more operations on this problem(Y/N):")


