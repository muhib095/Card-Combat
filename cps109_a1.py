"""

Problem: 

My project involves creating a simple card game that involves the user going against the computer. 
There are no ties so the user must input an odd number of rounds. The user and computer are dealt random cards that range from 1-13. 
You must have a greater card than the computer to win the round. You can re-roll your card once per round. 

There are 2 win conditions. First, you must win a majority of the rounds. If there are 3 rounds, you must win 2 of them. 
Lastly, you must accumulate more than 30 points. You start with 20 points. 
Points are accumulated by calculating the difference between the player’s card value and the computer's card value

Good Luck!


"""

# Importing necessary libraries
import random

# Function to read instructions from a file
def point_system(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to save entries to a file
def save_log(log_text, filename):
    with open(filename, "a") as file:
        file.write(log_text)

# Define the 'task' function with a user-defined round parameter
def task(rounds, log):
    # Initialize variables to keep track of user's wins and points
    user_wins = 0
    points = 20

  # Loop through the defined number of rounds set  by user
    for i in range(rounds):
        # Generate random card values for the user and the computer
        user = random.randint(1, 13)
        computer = random.randint(1, 13)
        
        # Display the user's card
        print("Your card:", user)
        
        # Ask the user if they want to draw another card
        choice = input("Do you want to pick another card (yes/no)? ").strip().lower()
        log.write(f"Round {i + 1}: Your card - {user}\nUser's choice - {choice}\n")  # Output to file

        # If the user chooses to draw another card, generate a new card value
        if choice == "yes":
            new_user_card = random.randint(1, 13)
            print("New card:", new_user_card)
            user = new_user_card
            log.write(f"New card - {new_user_card}\n")  # Output to file 

        # Check if the user's card value is greater than the computer's
        if user > computer:
            user_wins += 1
            points += user - computer

        # Display the computer's card and the user's total points
        print(f"Computer's card: {computer}")
        print(f"Your points: {points}\n")

        log.write(f"Computer's card - {computer}\nYour points - {points}\n\n")  # Output to file

    # Return the number of user wins and the total points
    return user_wins, points

# Define the 'black_clover' function
def black_clover():
    print("Welcome to the Card Game!")
    
    # Ask the user if they want to see the points system
    print("Do you want to see the points system (yes/no)?")
    show_points = input().strip().lower()

    # If the user chooses to see the points system
    if show_points == "yes":
        points_txt = point_system("point_system.txt") 
        print(points_txt) #Reads from point_system.txt and displays information

    # Start loop for the game
    while True:
        
        rounds = int(input("How many rounds would you like to play (must be odd)? ")) # Taking input from the user 
        
        #Checks to see if user inputs an odd number of rounds. NO TIES!
        if rounds % 2 == 0:
            print("Number of rounds must be odd to avoid ties.")
            continue
        
        #Starts a new game in the log 
        with open("cps109_a1_output.txt", "a") as log:
            log.write("New Game\n")  # Output to file 

            user_wins, points = task(rounds, log)
            
            # Check if the user meets the win condition
            if user_wins >= rounds // 2 + 1 and points >= 30:
                print("Congratulations! You have completed the game.")
                log.write("Game Completed\n")  # Output to file 
                break 
            else:
                # If the user hasn't won, ask if they want to restart or exit
                choice = input("You have not won. Do you want to restart (yes/no)? ").strip().lower()
                log.write("Game Not Completed\n")  # Output to file
                if choice != "yes":
                    print("Goodbye!")
                    break

if __name__ == "__main__":
    black_clover() # Calling the main function to start the game