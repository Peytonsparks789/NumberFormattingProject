#Known errors:
    #1) If negative and decimal present on a large number, cutting decimal off of end of Num removes last few digits before decimal
    #2) Large numbers show inconsistency when entered into program in terms of accurately portaying number
    #3) Error checking for char that aren't . or - is implemented (line 27), but characters still append when printing results for some reason
    #4) Number removes leading decimal when zero is only value there. Would like to keep 0 if no other number present before decimal
    #5) Error checking for multiple decimals not functioning (line 35)

#Changelog
    #1) Moved some major functions out of main to their own respective functions
    #2) Added error validation for all characters. Not yet functioning fully
    #3) Added if __name__ = '__main__' at bottom to indicate runnable script

def DecimalAddBack(Num, Position, i, Decimal):
    if i % 3 == 0: #Ensures position Decimal is added to string is correct using modulo
        Num = Num[:Position + 1] + Decimal[1]
    elif i % 3 == 1:
        Num = Num[:Position + 2] + Decimal[1]
    else:
        Num = Num[:Position + 3] + Decimal[1]
    return Num

def NumberValidation(Num, Decimal):
    if '-' in Num: #Removes - from number and sets neg to true so it can be added to end of program later
        NegPos = Num.find("-")
        NumberofNeg = str.count("-", Num)
        if NegPos != 0:
            print("Error, hyphen located, but not at beginning of number. Please re-enter value.\n")
            main()
        if NumberofNeg > 1:
            print("Error, more than one hyphen located. Please re-enter value.\n")
            main()
        else:
            Num = Num.replace('-', '') 
            Neg = True
        return Num, NumberofNeg

    try: #Validate no char but . and - are entered
        Num2 = int(Num.replace('.', ''))
    except ValueError: #Throws error and reruns main
        print('Error, number entered contains illegal characters. Please try again \n')
        main()

    if '.' in Num: #Allows for decimal numbers to be used by removing them from string
        NumberofDec = str.count(".", Num)
        if NumberofDec > 1:
            print("Error, more than one decimal present. Please re-enter value.\n")
            main()
        else:
            i = len(Num) #gets length of string before split
            Position = Num.find('.')
            Decimal = Num.split('.') #Splits string using decimal as delimiter
            Decimal[1] = '.' + Decimal[1] #Adds decimal to split where needed
            Num = Num[:Position] + Num[i:] #Removes numbers past decimal
            Num = Num.replace('.', '') #Removes decimal from value to be concatenated
            IsFloat = True #Sets to true, so Decimal[1] can be concatenated at end of Num later
            print(Decimal) #Debugging purposes
        return Num, IsFloat, Decimal

    

def main():
    Num = input("Please enter a number: \n")
    IsFloat = False
    Neg = False
    count = 1
    Decimal = [2]
    NumberofNeg = 0

    try: #Validate no char but . and - are entered
        Num2 = int(Num)
    except ValueError: #Throws error and reruns main
        Num, Decimal, NumberofNeg, IsFloat = NumberValidation(Num, Decimal)

    Num = Num.lstrip("0") #Removes leading zeroes from Num
    i = len(Num) #Gets length of string after negatives ,zeroes, and decimals all gone
    Val = (i//3) #Gets value for determining end of while loop

    if (i % 3) == 0: #run this if modulo is 0
        if i<7 and i>3:
            x = 3
            Num = Num[:x] + ',' + Num[x:]
            Val = 0
        elif i<4:
            Val = 0
        while Val > 0: #Concatenates commas to string
            if count == 1:
                x = 3
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends 
                count = 0
            else:
                x = x + 4
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1
            Val = Val - 1

    elif (i % 3) == 2: #run this if modulo is 2
        while Val > 0: #Concatenates commas to string      
            if count == 1:
                x = 2
                count = count + 1
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1 
            elif count == 2:
                x = 6
                count = 0
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1
            else:
                x = x + 4
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1

    else: #run this if modulo is 1
        count = 1
        while Val > 0: #Concatenates commas to string      
            if count == 1:
                x = 1
                count = count + 1
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1 
            elif count == 2:
                x = 5
                count = 0
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1
            else:
                x = x + 4
                Num = Num[:x] + ',' + Num[x:] #Slices string and appends
                Val = Val - 1

    if IsFloat == True: #Adds back values after decimal if needed
        Num = DecimalAddBack(Num, Position, i, Decimal)

    if Neg == True: #Adds - to start of value if needed
        Num = Num[:0] + '-' + Num[0:]
    print(Num)


if __name__ == '__main__':
    main()