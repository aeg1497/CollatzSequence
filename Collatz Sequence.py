#takes in parameter number
def collatz(number):
    #check to see if the number is even
    if number % 2 == 0:
        print(str(number) + '/ 2')
        even = number // 2
        print(str(even))
        return even
    else:
        print('3 * ' + str(number) + ' + 1')
        odd = 3 * number + 1
        print(str(odd))
        return odd

#Loop to keep asking for input until 1 is returned from the function
while True:
    
    #try and except
    try:
        num = int(input(('Enter number: ')))
    except:
        print('Error - Did not enter int')
        continue #Jump back to start of loop to ask for another int
    result = collatz(num) #calling function and getting return value
    #Ending when you get 1 from calculations.
    if result == 1:
        break
