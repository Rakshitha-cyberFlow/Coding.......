##COLLATZ PROGRAM

def collatz(number):
    if number%2==0:
        number=number/2
    else:
        number=number*3+1
    print(number)
    return (number)
while True:
    try:
        user_input=int(input("Enter the NUMBER: "))
        break
    except:
        print("INVALID INPUT!!!....Enter a VALID NUMBER")
while user_input!=1:
    user_input=collatz(user_input)

