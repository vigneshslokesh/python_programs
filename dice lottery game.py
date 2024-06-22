import useful_tools

num = int(input("Enter the dice size : "))
counter = 0
end_counter = 2
numbers = [3,6,8,9,11]

while counter < end_counter:   
    counter += 1


    dice_result = useful_tools.roll_dice(num)
    if  dice_result in numbers:
        print(f"The dice rolled: {dice_result}")
        print("You won the lottery")
        break
    else:
        
        print(f"The dice rolled: {dice_result}")
        if counter <end_counter:
            print(f"You have {end_counter - counter} chances left")
            print("Sorry try again!")
            num = int(input("Enter the dice size : "))
        else:
            print("You lost, No more chances left. Game over.")


