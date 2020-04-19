# by using if else perform arithmetic operation
print("\t\t==============================================================================================================================\t")
print("\t\tDesign a simple calcultor to perform a basic operation\t")
print("\t\t==============================================================================================================================\t")
#take input of two numbers in float
operand1 =float(input("\t\tenter first number:"))
operand2 =float(input("\t\tenter second number:"))
# take operator as string
operator=input("\t\tenter a operator to perform calculation:")
#add two numbers, 
if operator=='+':
    result= operand1 + operand2
    print("\t\t==============================================================================================================================\t")
# here str() operation use in print to concatenate(join) string and int. two different types of data ca print with each other until the type will not be changed
    print("\t\t The sum of two number is:"+str(result))
    print("\t\t==============================================================================================================================\t")
#subtract two number
elif operator=='-':
    result= operand1 - operand2
    print("\t\t==============================================================================================================================\t")
    print("\t\t The subtraction of two number is:"+str(result))
    print("\t\t==============================================================================================================================\t")
#multiply two numbers
elif operator=='*':
    result= operand1 * operand2
    print("\t\t==============================================================================================================================\t")
    print("\t\t The multiplication of two number is:"+str(result))
    print("\t\t==============================================================================================================================\t")
#divide two numbers
elif operator=='/':
    result= operand1 / operand2
    print("\t\t==============================================================================================================================\t")
    print("\t\t The division of two number is:"+str(result))
    print("\t\t==============================================================================================================================\t")
# when input wrong operator gives output as invalid operation
else:
    print("\t\t==============================================================================================================================\t")
    print("\t\t input invalid operation")
    print("\t\t==============================================================================================================================\t")

