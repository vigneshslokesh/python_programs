class StringHelper:
    def count_vowels(s): #function to count the number of vowels for a given input 
        vowels = "aAeEiIoOuU"
        return sum(1 for char in s if char in vowels)
    
    def reverse_string(s): #function to return the reverse of a input string
        return s[::-1]

helper = StringHelper #assigning the helper class to a variable called helper

ip = input("Enter the String : ")
choice = input("Select your choice : \n(a) count vowels --> a\n(b) reverse string --> b\n").lower()
if choice == "a" :
    print(f"The number of vowles are : {helper.count_vowels(ip)}")
elif choice == "b" :
    print(f"The reverse string is : {helper.reverse_string(ip)}")
else : 
    print("Invalid choice")

