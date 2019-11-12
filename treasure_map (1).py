
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9965661
#    Student name: Victor Wang 
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    write(' Put your legend here', align = 'left',
          font=('Arial', 24, 'normal'))    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.


# FOLLOW THE PATH AS PER THE PROVIDED DATASET 

##Provide a list of fillcolors to fill for different tokens

list_of_colours = ['black', 'white', 'red', 'navy blue', 'light blue']

##Provide a list of token names to be displayed in the legend, in correct order 

list_of_token_names = ['SHIELD', 'Avengers', 'Captain America', 'Fantastic Four', 'Deadpool']

##Provide your list of tokens in the correct number order, for indexing 

list_of_tokens = [0, 1, 2, 3, 4]

##Diameter of each token 

diameter = 100

##Set up variables to store & count the number of instances your individual token functions has been called, and intialize them to 0

shield_logo_counter= 0

avengers_logo_counter= 0

captain_america_shield_counter = 0

fantastic_four_logo_counter = 0

deadpool_logo_counter= 0

##Create a function to draw Marvel's SHIELD logo. Set two parameters to store the x and y coordinates and do this for each token.

def draw_shield(x, y):

##  Set the heading to default east to make sure the turtle walks in a circle centered in the grid square, and do this all for each token function.
    setheading(0)
##  Use a global variable to access the list of fillcolors to be used, that are outside of your token functions, including this one.
    global list_of_colours
##  Use a global variable to access the counter variable for this token that is outside of the function, to count the number of times the function has been
##  called
    global shield_logo_counter
##  Move the pen up before moving to the intended circle's perimeter 
    penup()
    goto(x+50, y-100)
##  Put the pen down to start drawing
    pendown()
##  The fillcolor would be the first colour from the list  
    fillcolor(list_of_colours[0])
##  Begin filling the circle with your chosen colour
    begin_fill()
    circle(50)
##  Fill up the circle 
    end_fill()

##  Draw the second circle
##  Put your pen up each time you move from one coordinate to the next
    penup()
##  Move to one of your next coordinates required to help draw the shape of the token 
    goto(x+50, y-95)
    pendown()
    fillcolor(list_of_colours[1])
    begin_fill()
    circle(45)
    end_fill()

    penup()
##  Move to the second set of coordinates
    goto(x+75, y-85)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+58, y-61)
    goto(x+50, y-69)
    goto(x+42, y-61)
    goto(x+25, y-85)
    goto(x+75, y-85)
    end_fill()
    
##  Move to the third set of coordinates 
    penup()
    goto(x+18, y-79)
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+35, y-58)
    goto(x+29, y-51)
    goto(x+12, y-69)
    goto(x+18, y-79)
    end_fill()

## Move to the fourth set of coordinates 
    penup()
    goto(x+82, y-79)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+65, y-58)
    goto(x+71, y-51)
    goto(x+88, y-69)
    goto(x+82, y-79)
    end_fill()

##Move to the fifth set of coordinates

    penup()
    goto(x+11, y-67)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+29, y-48)
    goto(x+21, y-39)
    goto(x+7, y-53)
    goto(x+11, y-67)
    end_fill()

##Move to the sixth set of coordinates 
    penup()
    goto(x+89, y-67)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+71, y-48)
    goto(x+79, y-39)
    goto(x+93, y-53)
    goto(x+89, y-67)
    end_fill()

##Move to the seventh set of coordinates 
    penup()
    goto(x+20, y-38)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+12, y-29)
    goto(x+7, y-45)
    goto(x+20, y-38)
    end_fill()

##Move to the eigth set of coordinates 
    penup()
    goto(x+80, y-38)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+88, y-29)
    goto(x+93, y-45)
    goto(x+80, y-38)
    end_fill()

##Move to your final set of coordinates for this token
    penup()
    goto(x+86, y-26)
    pendown()
    begin_fill()
    fillcolor(list_of_colours[0])
    goto(x+79, y-19)
    goto(x+60, y-34)
    goto(x+55, y-29)
    goto(x+60, y-29)
    goto(x+47, y-18)
    goto(x+40, y-34)
    goto(x+21, y-19)
    goto(x+14, y-26)
    goto(x+50, y-67)
    goto(x+86, y-26)
    end_fill()

##After finishing drawing each token, make sure you move the turtle back to its starting position in the grid square 
    penup()
    goto(x, y-100)

##Each time this token function is called, add 1 to the counter variable initialized
    shield_logo_counter = shield_logo_counter + 1

##Use a return statement to ensure the value counted could be accessed outside of this function after its called 
    return shield_logo_counter


##Create a function to draw Marvel's Avengers logo
    
def draw_avengers(x, y):

    setheading(0) 
    global list_of_colours
    global avengers_logo_counter 
    penup()
    goto(x+50, y-92)
    pendown() 
    fillcolor(list_of_colours[1])
    begin_fill()
    circle(43, extent = 315)
    end_fill()
    
    penup()
    goto(x+50, y-86)
    setheading(0)
    pendown()
    fillcolor(list_of_colours[0])
    begin_fill()
    circle(37)
    end_fill()

    penup()
    goto(x+38, y-68)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    goto(x+27, y-92)
    goto(x+13, y-92)
    goto(x+54, y-13)
    goto(x+66, y-13)
    goto(x+65, y-56)
    goto(x+56, y-49)
    goto(x+55, y-27)
    goto(x+44, y-57)
    goto(x+55, y-57)
    goto(x+56, y-53)
    goto(x+66, y-63)
    goto(x+55, y-72)
    goto(x+55, y-68)
    goto(x+38, y-68)
    end_fill()

    penup()
    goto(x+54, y-77)
    pendown()
    fillcolor(list_of_colours[1])
    begin_fill()
    goto(x+66, y-69)
    goto(x+66, y-77)
    goto(x+54, y-77)
    end_fill()

    penup()
    goto(x, y-100)

    avengers_logo_counter= avengers_logo_counter + 1
    return avengers_logo_counter

##Create a function to draw Captain America's logo

def draw_captain_america_shield(x,y):

    setheading(0)
    global list_of_colours
    global captain_america_shield_counter 
    penup()
    goto(x+50, y-100)
    pendown()
    fillcolor(list_of_colours[2])
    begin_fill()
    circle(50)
    end_fill()
    
    penup()
    goto(x+50, y-91)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    circle(41)
    end_fill()

    penup()
    goto(x+50, y-82)
    fillcolor(list_of_colours[2])
    begin_fill()
    pendown()
    circle(32)
    end_fill()

    penup()
    goto(x+50, y-72)
    fillcolor(list_of_colours[3])
    begin_fill()
    pendown()
    circle(22)
    end_fill()

    penup()
    goto(x+60, y-65)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    goto(x+58, y-52)
    goto(x+68, y-43)
    goto(x+55, y-43)
    goto(x+50, y-30)
    
    goto(x+44, y-43)
    goto(x+31, y-43)
    goto(x+41, y-52)
    goto(x+38, y-65)
    goto(x+50, y-58)
    goto(x+60, y-65)
    end_fill()

    penup()
    goto(x, y-100)

    captain_america_shield_counter= captain_america_shield_counter + 1
    return captain_america_shield_counter


##Create a function to draw Marvel's Fantastic Four logo

def draw_fantastic_four_logo(x,y):

    setheading(0)
    global list_of_colours
    global fantastic_four_logo_counter
    penup()
    goto(x+50, y-100)
    pendown()
    fillcolor(list_of_colours[1])
    begin_fill()
    circle(50)
    end_fill()
    
    penup()
    goto(x+50, y-94)
    fillcolor(list_of_colours[4])
    begin_fill()
    pendown()
    circle(44)
    end_fill()

    penup()
    goto(x+50, y-90)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    circle(40)
    end_fill()

    penup()
    goto(x+65, y-87)
    fillcolor(list_of_colours[4])
    begin_fill()
    pendown()
    goto(x+65, y-67)
    goto(x+23, y-67)
    goto(x+23, y-62)
    goto(x+70, y-15)
    goto(x+76, y-19)
    goto(x+76, y-56)
    goto(x+89, y-56)
    goto(x+87, y-67)
    goto(x+76, y-67)
    goto(x+76, y-82)
    goto(x+65, y-87)
    end_fill()

    penup()
    goto(x+65, y-57)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    goto(x+65, y-30)
    goto(x+38, y-56)
    goto(x+65, y-57)
    end_fill()

    penup()
    goto(x, y-100)

    fantastic_four_logo_counter= fantastic_four_logo_counter + 1
    return fantastic_four_logo_counter

    
##Create a function to draw Marvel's Deadpool logo

def draw_deadpool(x,y):

    setheading(0)
    global list_of_colours
    global deadpool_logo_counter 
    penup()
    goto(x+50, y-100)
    pendown()
    fillcolor(list_of_colours[2])
    begin_fill()
    circle(50)
    end_fill()

    penup()
    goto(x+58, y-90)
    fillcolor(list_of_colours[0])
    begin_fill()
    pendown()
    circle(40, extent= 180)
    goto(x+58, y-90)
    end_fill()

    penup()
    goto(x+42, y-10)
    setheading(180)
    fillcolor(list_of_colours[0])
    begin_fill()
    pendown()
    circle(40, extent= 180)
    goto(x+42, y-10)
    end_fill()
    
    penup()
    goto(x+36, y-55)
    fillcolor(list_of_colours[1])
    begin_fill()
    pendown()
    goto(x+17, y-45)
    goto(x+23, y-55)
    goto(x+36, y-55)
    end_fill()

    penup()
    goto(x+64, y-55)
    fillcolor(list_of_colours[1])
    begin_fill() 
    pendown()
    goto(x+80, y-45)
    goto(x+76, y-55)
    goto(x+64, y-55)
    end_fill()

    penup()
    goto(x, y-100)

    deadpool_logo_counter= deadpool_logo_counter + 1
    return deadpool_logo_counter


##Create a function to draw the treasure map path where the tokens would be found 

def follow_path(path):

##  Use index 0 to access the first sublist within the random path of instructions given, which in this case is the one that specifies the starting position
##  on the treasure map

    starting_position = path[0]

##  Use conditional statements to tell the turtle which x and y coordinates to go to, depending on the random direction accessed from index 1,
##  which is the second item in this particular sublist
    
    if starting_position[1] == 'Top left':
        goto(0, 600)
    elif starting_position[1] == 'Top right':
        goto(600, 600)
    elif starting_position[1] == 'Bottom left':
        goto(0, 100)
    elif starting_position[1] == 'Bottom right':
        goto(600, 0)
##  If all the other options are not true in this instance of the random path, then start at the 'Centre' of the treasure map 
    else:
        goto(300,300)

##    Use conditonal statements to call your different token functions, depending on the token number returned (from the third item of the sublist)  
    if starting_position[2] == 0:
##      When calling the token functions, take into account the current x and y coordinates the turtle is located. We need to add 100 to the current y
##      coordinate because otherwise we wouldn't be able to draw our token starting from the top-left of the grid square the turtle is currently in 
        draw_shield(xcor(), ycor()+100)
    elif starting_position[2] == 1:
        draw_avengers(xcor(), ycor()+100)
    elif starting_position[2] == 2:
        draw_captain_america_shield(xcor(), ycor()+100)
    elif starting_position[2] == 3:
        draw_fantastic_four_logo(xcor(), ycor()+100)
    else:
        draw_deadpool(xcor(), ycor()+100)


##  Use indicing to slice the starting path from the rest of the instructions, which mainly specifies the direction the turtle would move in.
    path = path[1:]

##  Use a for-each loop in this specified path to access the aforementioned instructions 
    for directions in path:

##  Set the turtle's heading depending on the direction     
        if directions[0] == 'North':
            setheading(90)
        elif directions[0] == 'South':
            setheading(270)
        elif directions[0] == 'East':
            setheading(0)
        else:
            setheading(180)

##    Move the turtle by this number of squares, multipled by 100 pixels        
        if directions[1]:
            forward(directions[1] * 100)    
        if directions[2] == 0:
            draw_shield(xcor(), ycor() + 100)
        elif directions[2] == 1:
            draw_avengers(xcor(), ycor() + 100)
        elif directions[2] == 2:
            draw_captain_america_shield(xcor(), ycor() + 100)
        elif directions[2] == 3:
            draw_fantastic_four_logo(xcor(), ycor() + 100)
        else:
            draw_deadpool(xcor(), ycor() + 100)

##    Set up variables that would add up the total number of tokens in the treasure map & create a list of the current values for each token variable       

    total_tokens_counter = shield_logo_counter + avengers_logo_counter + captain_america_shield_counter + fantastic_four_logo_counter + deadpool_logo_counter
    total_tokens_counter

    list_of_token_counter_values = [shield_logo_counter, avengers_logo_counter, captain_america_shield_counter, fantastic_four_logo_counter, deadpool_logo_counter]
    list_of_token_counter_values

##    Enclose the function to draw the legend that displays the themes of the tokens
    
    def draw_legend():
        global list_of_colours
        penup()
        goto(750, 0)
        fillcolor(list_of_colours[4])
        begin_fill()
##        Draw the legend shape
        forward(400)
        setheading(90)
        forward(675)
        setheading(90)
        forward(400)
        setheading(90)
        forward(675)
        end_fill()

##        Move to the position where you want to start drawing your tokens in the legend 
        goto(900,25)
##        For each iteration called, draw the corresponding token number, and write them their names and display the total number of tokens and the number
##        of instances each tokens appears as you go along
        for index in range(5):
            if list_of_tokens[index] == 0:
                draw_shield(xcor(), ycor()+100)
            elif list_of_tokens[index] == 1:
                draw_avengers(xcor(), ycor()+100)
            elif list_of_tokens[index] == 2:
                draw_captain_america_shield(xcor(), ycor()+100)
            elif list_of_tokens[index] == 3:
                draw_fantastic_four_logo(xcor(), ycor()+100)
            else:
                draw_deadpool(xcor(), ycor()+100)
            setheading(0)
            forward(diameter + 10)
            write(list_of_token_names[index] + ' ' + str(list_of_token_counter_values[index]))
            setheading(180)
            forward(diameter)
            setheading(90)
            forward(diameter + 25)
        goto(950, 650)
        write('Marvel Superheros' + ' ' + str(total_tokens_counter))
        
    return draw_legend()


#--------------------------------------------------------------------#

#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Marvel Superheros token game")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
# follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
