import turtle  # Importing the turtle module for graphics
import pandas  # Importing pandas for data handling

# Setting up the screen with the U.S. map
screen = turtle.Screen()  # Create a screen object
screen.setup(width=725, height=491)  # Set the size of the screen
screen.title("U.S. States Game")  # Set the title of the window
image = 'blank_states_img.gif'  # File name of the U.S. map image
screen.bgpic(image)  # Set the background picture to the U.S. map

# Reading the data from the CSV file
data = pandas.read_csv('50_states.csv')  # Read the CSV file into a DataFrame
states = data['state'].to_list()  # Convert the 'state' column to a list

correct_guess = []  # List to store correctly guessed states
left_over_states = []  # List to store states that were not guessed

# Relationship between main.py and 50_states.csv: This CSV file contains the 50 states of the United States and their x and y coordinates. These coordinates are used to display the name of each state in the correct location on a map image of the United States. The main.py script reads this file and displays the state name at the corresponding coordinates when the user guesses the state name.

# Relationship between main.py and states_to_learn.csv: Save a list of the states that the user failed to guess in the game to this CSV file. This file is created at the end of the game and can be referenced by the user for further study.

# Main game loop
while len(correct_guess) < 50:
    # Get user input for a state name
    answer_state = screen.textinput(title=f'{len(correct_guess)}/50 States Correct',
                                    prompt="What's another state's name?").title()

    # Check if the input state is in the list of states
    if answer_state in states:
        correct_guess.append(answer_state)  # Add the state to correct guesses
        location = data[data['state'] == answer_state]  # Find the state in the DataFrame
        x_cor = location['x'].item()  # Get the x coordinate
        y_cor = location['y'].item()  # Get the y coordinate

        # Write the state name on the map
        turtle.hideturtle()  # Hide the turtle icon
        turtle.penup()  # Lift the pen to move without drawing
        turtle.goto(x_cor, y_cor)  # Move to the specified coordinates
        turtle.pendown()  # Place the pen down to start drawing
        turtle.write(answer_state, font=("Arial", 12, "normal"))  # Write the state name
    elif answer_state == 'Exit':
        # Create a list of states that were not guessed
        left_over_states = [state for state in states if state not in correct_guess]
        new_data = pandas.DataFrame(left_over_states)
        new_data.to_csv('states_to_learn.csv', index=True)  # Save the list to a CSV file
        break  # Exit the game loop
