def summation():
    print("\nwelcom to the sum-avarage game")
    print("-----[ press 'x' to exit ]-----\n")
    while True:
        try:
            print("_______________________________________________")
            user_input = input("tell me How many numbers do you want to collect: ")
            if user_input.lower() == "x":
                print("_______________________________\n\nExiting the program. Thank you!\n_______________________________\n")
                break
            num = int(user_input)
            numbers = []
            for x in range(num):
                while True:
                    user_num = input(f"enter mumber [{x+1}]")
                    if user_num.lower() == "x":
                        print("_______________________________\n\nExiting the program. Thank you!\n_______________________________\n")
                        return
                    try:
                        user_num = int(user_num)
                        numbers.append(user_num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number or x to exit.")
            number_sum = sum(numbers)
            avarage = number_sum / num
            print("\nCollected numbers: ", numbers)
            print(f"sum  = {number_sum}")
            print(f"avarage  = {avarage} \n")
        except ValueError:
            print("Invalid input. Please enter a valid number or x to exit.")


summation()
