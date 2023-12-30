def Multiplication_game():
    print("\nwelcom to the Multiplication game")
    print("-------[ press 'x' to exit ]-------\n")
    while True:
        try:
            print("____________________________")
            user_input1 = input('plese enter ur first numbers: ')
            if user_input1.lower() == 'x':
                print("_______________________________\n\nExiting the program. Thank you!\n_______________________________")
                break

            user_input2 = input('plese enter ur second numbers: ')
            if user_input2.lower() == 'x':
                print("_______________________________\n\nExiting the program. Thank you!\n_______________________________")
                break
            
            else:
                a = int (user_input1)
                b = int (user_input2)
                def game(a,b):
                    for num in range (a,b+1):
                        print ("---------------------------------- ")
                        print (f"The Multiplication table for {num}")
                        for i in range (1,13):
                            result = num*i
                            print(f"[{num} x {i}] = {result}")
                game(a,b)
        except ValueError :
            print ("Invalid input. Please enter a valid number or x to exit.")
Multiplication_game()