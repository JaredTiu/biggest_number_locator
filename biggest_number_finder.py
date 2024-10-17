def highest_number (number_1, number_2, number_3, number_4, number_5):
# compare the 5 inputs given by the user 
    #compare number 1 to number 2, 3, 4 and 5
    if number_1 > number_2: 
        if number_1 > number_3: 
            if number_1 > number_4: 
                if number_1 > number_5: 
                    print("The highest number is:", number_1) 
#if it is not the highest then move on to number 2 
    #compare number 2 to number 3, 4, and 5 
    elif number_2 > number_3: 
        if number_2 > number_4: 
            if number_2 > number_5: 
                print("The highest number is:", number_2)
#if it is still not the highest move on to number 3
    #compare number 3 to number 4, and 5
    elif number_3 > number_4: 
        if number_3 > number_5:
            print("The highest number is:", number_3)
#if it not the highest move on to number 4
    #compare number 4 to number 5
    elif number_4 > number_5: 
            print("The highest number is:", number_4)
#if it still not the highest then number 5 is the highest.
    else:
        print ("The highest number is:", number_5)
#asking for user inputs
number_1 = int(input("input first number: "))
number_2 = int(input("input second number: "))
number_3 = int(input("input third number: "))
number_4 = int(input("input fourth number: "))
number_5 = int(input("input fifth number: ")) 
highest_number(number_1, number_2, number_3, number_4, number_5)