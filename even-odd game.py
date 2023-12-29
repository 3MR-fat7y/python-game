def game ():
    print("welcom to the Even-Odd game")
    print("---[ press 'x' to exit ]---")
    while True:
        user_input = input ("plese enter a number: ")
        try:     
            if user_input.lower() == 'x':
                print("_______________________________\n\nExiting the program. Thank you!\n_______________________________")
                break
            else: 
                user_input = int (user_input)
                if user_input % 2 == 0:
                    print (f"your number [{user_input}] is even")
                else:
                    print (f"your number [{user_input}] is odd")
        except ValueError :
            print ("Invalid input. Please enter a valid number or x to exit.")
game()