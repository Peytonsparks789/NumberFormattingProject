#Number format code: Code will take a number a user enters, store it as a string, and then take said value and add commas where necessary.
#This program was inspired by a challenge located here https://pythonprinciples.com/challenges/Thousands-separator/ with a few steps added to make it more complex

#Known bugs:
    #1) If negative and decimal present on a large number, cutting decimal off of end of Number removes last few digits before decimal sometimes. 
                            #(-1654541189135489156.015649865184 reads -1,654,541,189,135,489,.015649865184 which cuts off last 3 numbers before decimal.)

def Restart(): #Restarts program after error occurs in user entry such as illegal characters, too many -'s, or too many .'s.
    import sys
    import os

    os.execv(sys.executable, ['python'] + sys.argv)

class Number:
        UserNumber = '0' #Objects of class Number
        IsFloat = False
        Neg = False
        Decimal = ''
        NumberofNeg = 0

        def NumberValidation(UserNumber, Decimal):
            if '-' in UserNumber: #Removes - from UserNumber and sets neg to true so it can be added to end of program later
                NegPos = UserNumber.find("-")
                NumberofNeg = UserNumber.count("-")
                if NegPos != 0:
                    print("Error, hyphen located, but not at beginning of number. Please re-enter value.\n")
                    Restart()
                if NumberofNeg > 1:
                    print("Error, more than one hyphen located. Please re-enter value.\n")
                    Restart()
                else:
                    UserNumber = UserNumber.replace('-', '') 
                    Neg = True
                return UserNumber, Neg

            Number.ErrorCheck(UserNumber)

            if '.' in UserNumber: #Allows for decimal numbers to be used by removing them from string
                NumberofDec = UserNumber.count(".")
                if NumberofDec > 1:
                    print("Error, more than one decimal present. Please re-enter value.\n")
                    Restart()
                else:
                    i = len(UserNumber) #gets length of string before split
                    Position = UserNumber.find('.')
                    if Position == 0: #Makes sure UserNumber isnt string for ValueCheck() as NumberValidation removes everything after decimal which 
                                            #would leave whitespace and wouldn't pass check to see if num or not
                        UserNumber = '0' + UserNumber
                        Position = 1
                    Decimal = UserNumber.split('.') #Splits string using decimal as delimiter
                    Decimal[1] = '.' + Decimal[1] #Adds decimal to split where needed
                    UserNumber = UserNumber[:Position] + UserNumber[i+1:] #Removes numbers past decimal
                    UserNumber = UserNumber.replace('.', '') #Removes decimal from value to be concatenated
                    IsFloat = True #Sets to true, so Decimal can be concatenated at end of UserNumber later
                    return UserNumber, IsFloat, Decimal[1], Position

        def ErrorCheck(UserNumber):
            try: #Validate no char but . and - are entered
                Num2 = int(UserNumber.replace('.', ''))
            except ValueError: #Throws error and reruns main
                print('Error, number entered contains illegal characters. Please try again \n')
                Restart()

        def NumFormat(UserNumber, i, Val):
            count = 1
            if (i % 3) == 0: #run this if modulo is 0
                if i<7 and i>3:
                    x = 3
                    UserNumber = UserNumber[:x] + ',' + UserNumber[x:]
                    Val = 0
                elif i<4:
                    Val = 0
                while Val > 0: #Concatenates commas to string
                    if count == 1:
                        x = 3
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends 
                        count = 0
                    else:
                        x = x + 4
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1
                    Val = Val - 1

            elif (i % 3) == 2: #run this if modulo is 2
                while Val > 0: #Concatenates commas to string      
                    if count == 1:
                        x = 2
                        count = count + 1
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1 
                    elif count == 2:
                        x = 6
                        count = 0
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1
                    else:
                        x = x + 4
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1

            else: #run this if modulo is 1
                count = 1
                while Val > 0: #Concatenates commas to string      
                    if count == 1:
                        x = 1
                        count = count + 1
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1 
                    elif count == 2:
                        x = 5
                        count = 0
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1
                    else:
                        x = x + 4
                        UserNumber = UserNumber[:x] + ',' + UserNumber[x:] #Slices string and appends
                        Val = Val - 1

            return UserNumber

        def DecimalAddBack(UserNumber, Position, i, Decimal):
            if i % 3 == 0: #Ensures position Decimal is added to string is correct using modulo
                print(Position)
                UserNumber = UserNumber[:Position + 2] + Decimal #Adding to position ensures Decimal is appended without overwriting existing numbers
            elif i % 3 == 1:
                UserNumber = UserNumber[:Position + 3] + Decimal #Adding to position ensures Decimal is appended without overwriting existing numbers
            else:
                UserNumber = UserNumber[:Position + 4] + Decimal #Adding to position ensures Decimal is appended without overwriting existing numbers
            return UserNumber

def main():
    Num = Number() #Creates member of class Number
    Num.UserNumber = input("Please enter a number: \n") #Appends User Input to UserNumber

    try: #Validation to see if non Number char entered
        Num2 = int(Num.UserNumber)
    except ValueError: #Check if non number char is illegal
        if '-' in Num.UserNumber and '.' in Num.UserNumber:
            Num.UserNumber, Num.Neg = Number.NumberValidation(Num.UserNumber, Num.Decimal)
            Num.UserNumber, Num.IsFloat, Num.Decimal, Position = Number.NumberValidation(Num.UserNumber, Num.Decimal)
        elif '.' in Num.UserNumber:
            Num.UserNumber, Num.IsFloat, Num.Decimal, Position = Number.NumberValidation(Num.UserNumber, Num.Decimal)
        elif '-' in Num.UserNumber:
            Num.UserNumber, Num.Neg = Number.NumberValidation(Num.UserNumber, Num.Decimal)

    Number.ErrorCheck(Num.UserNumber) #Validate no other non number characters get through if no - or . are present

    Num.UserNumber = Num.UserNumber.lstrip("0") #Removes leading zeroes from UserNumber
    i = len(Num.UserNumber) #Gets length of string after negatives ,zeroes, and decimals all gone
    Val = (i//3) #Gets value for determining end of while loop

    Num.UserNumber = Number.NumFormat(Num.UserNumber, i, Val)
    
    if Num.IsFloat == True: #Adds back values after decimal if needed
        Num.UserNumber = Number.DecimalAddBack(Num.UserNumber, Position, i, Num.Decimal)
        if Num.UserNumber.find('.') == 0:
            Num.UserNumber = '0' + Num.UserNumber #Adds zero if decimal first char

    if Num.Neg == True: #Adds - to start of value if needed
        Num.UserNumber = Num.UserNumber[:0] + '-' + Num.UserNumber[0:]

    print(Num.UserNumber)

if __name__ == '__main__':
    main()