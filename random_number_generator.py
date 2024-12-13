import random

# Define the ASCII art banner using a raw string
ascii_art = r"""
.------..------..------..------..------..------..------.        
|P.--. ||O.--. ||K.--. ||E.--. ||M.--. ||O.--. ||N.--. |        
| :/\: || :/\: || :/\: || (\/) || (\/) || :/\: || :(): |        
| (__) || :\/: || :\/: || :\/: || :\/: || :\/: || ()() |        
| '--'P|| '--'O|| '--'K|| '--'E|| '--'M|| '--'O|| '--'N|        
`------'`------'`------'`------'`------'`------'`------'        
.------..------..------..------.                                
|C.--. ||A.--. ||R.--. ||D.--. |                                
| :/\: || (\/) || :(): || :/\: |                                
| :\/: || :\/: || ()() || (__) |                                
| '--'C|| '--'A|| '--'R|| '--'D|                                
`------'`------'`------'`------'                                
.------..------..------..------..------..------..------..------.
|G.--. ||I.--. ||V.--. ||E.--. ||A.--. ||W.--. ||A.--. ||Y.--. |
| :/\: || (\/) || :(): || (\/) || (\/) || :/\: || (\/) || (\/) |
| :\/: || :\/: || ()() || :\/: || :\/: || :\/: || :\/: || :\/: |
| '--'G|| '--'I|| '--'V|| '--'E|| '--'A|| '--'W|| '--'A|| '--'Y|
`------'`------'`------'`------'`------'`------'`------'`------'  
"""

def print_goodbye_ascii():
    # Print the custom goodbye ASCII art with larger font
    goodbye_ascii = r"""
   _____   ____    ____   _____   ____ __     __ ______  _  _  _ 
  / ____| / __ \  / __ \ |  __ \ |  _ \\ \   / /|  ____|| || || |
 | |  __ | |  | || |  | || |  | || |_) |\ \_/ / | |__   | || || |
 | | |_ || |  | || |  | || |  | ||  _ <  \   /  |  __|  | || || |
 | |__| || |__| || |__| || |__| || |_) |  | |   | |____ |_||_||_|
  \_____| \____/  \____/ |_____/ |____/   |_|   |______|(_)(_)(_)

    """
    print(goodbye_ascii)

def main():
    # Display ASCII art banner
    print(ascii_art)

    while True:
        print("Let's generate 10 random numbers!")

        # Ask for range input
        range_input = input("Please enter the range in the format 'start-end' (e.g., 1-1000): ").strip()
        
        try:
            # Parse the range input
            start, end = map(int, range_input.split('-'))
            if start >= end:
                print("Invalid range. The start must be less than the end.")
                continue
        except ValueError:
            print("Invalid format. Please enter the range as 'start-end' (e.g., 1-1000).")
            continue
        
        # Generate and display 10 random numbers
        random_numbers = [random.randint(start, end) for _ in range(10)]
        print("\nHere are your 10 random numbers:")
        for number in random_numbers:
            print(number)

        # Ask if the user wants to generate numbers again
        again = input("\nWould you like to generate 10 more numbers? (yes/no): ").strip().lower()
        
        if again not in ["yes", "y", "yessir", "sure"]:
            print_goodbye_ascii()  # Display goodbye ASCII art
            break

# Run the script
if __name__ == "__main__":
    main()
