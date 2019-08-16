###########################################################
    #  Algorithm
    #    prompt the user to enter a flag they want to draw until they want to quit
    #    input a string of the first three letters of the flag or all
    #       The rectangle, circle, crescent, star functions draw shapes for each flag       
    #       TUN draws Tunisia flag
    #       TUR draws Turkey flag
    #       LBY draws Libya flag
    #       SGP draws Singapore flag
    #       ALL draws all the flags on the screen 
    #       main function interacts with user with what flag they want to draw
    #       Q prints a message and terminates the loop
    #       Entering an invalid response will make the program prompt the user to pick again    
    #    displays flags the user wants to be drawn and clears after each one is drawn 
    ###########################################################

import turtle,math #importing turtle in order to draw, importing math for drawing star
#function draws a rectangle 
def rectangle(x,y,length,height,color): 
    turtle.penup()
    turtle.goto(x,y) #goes to position to draw rectangle 
    turtle.pendown() #starts drawing with a border 
    turtle.fillcolor(color) #indicating that a specific color will be filled in the rectangle 
    turtle.begin_fill()
    turtle.forward(length) #starts drawing rectangle 
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90) #finishes drawing rectangle 
    turtle.end_fill() #fills the rectangle with the specific color 

#function draws a circle 
def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y) # goes to position to draw circle 
    turtle.fillcolor(color) #indicating that a specific color will be filled in the circle
    turtle.begin_fill() 
    turtle.circle(radius) #draws circle of a specific radius 
    turtle.end_fill() #fills the circle with the specific color 
   
#function draws a crescent 
def crescent(x1,y1,x2,y2,R1,R2,color1,color2):
    turtle.penup()
    turtle.goto(x1,y1) #goes to position to draw first circle for crescent  
    turtle.fillcolor(color1)#indicating that a specific color will be filled in the cirlce
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(R1) #draws first circle with specified radius
    turtle.end_fill()#fills the circle with specific radius
    turtle.penup()
    turtle.goto(x2,y2) #goes to position to draw second circle for crescent 
    turtle.fillcolor(color2) #indicating that a specific color will be filled in the cirlce
    turtle.begin_fill()
    turtle.circle(R2)#draws second circle with specified radius 
    turtle.end_fill() #fills the circle with specific color 
    
#function to draw a star
def star (x,y,size,color,theta):
    turtle.penup()  
    turtle.goto(x,y) #goes to position to draw star  
    turtle.fillcolor(color) #indicating that a specific color will be filled in the star
    turtle.begin_fill()
    for i in range(5):      #for loop to draw all five sides of the star 
        turtle.forward(size) #moves a specific length for first side of star 
        turtle.left(theta) #turns a specific angle when drawing star 
        turtle.forward(size)
        turtle.left((360/5)-theta) 
    turtle.end_fill() #fills the star with specific color 

#function draws the Tunisia flag 
def Tunisia_flag (x,y,height):
    length = 1.5*height #length of the rectangle 
    rectangle(x,y,length, height,'red') #calls rectangle function to draw rectangle with specific parameters 
    #position of circle 
    x_circle = x + length/2 
    y_circle = y + height/4
    radius = height/4 #radius of circle 
    circle(x_circle, y_circle,radius,'white') #calls circle function to draw circle with specific paramenters
    #position of crescent 
    x_crescent_circle1 = x +((length/2) + (height/20) + (((9*height)/40)/2))
    y_crescent1 = y+ (height/2)
    x_crescent_circle2 = x+ ((length/2) + (height/20) + ((3*height)/10)/2)
    #radius of the two circles 
    radius1 = ((3*height)/8)/2
    radius2 = ((3*height)/10)/2
    #calls crescent fucntion to draw crescent with specific parameters 
    crescent(x_crescent_circle1,y_crescent1,x_crescent_circle2,y_crescent1,radius1,radius2,'red','white')
    #position of star 
    x_star = x+ ((length/2) + ((height/20)/2))
    y_star = y+ ((height/2) - ((height/20)/2))
    #math for specific dimensions of each side of the star 
    each_angle_in_star = 180/5
    outer_angle = 180 - each_angle_in_star
    angle_triangle = 180 - outer_angle
    altitude = (((9*height)/40)/2) - ((height/20)/2)
    star_size = altitude/(math.sin(angle_triangle))
    #calls star function to draw star with specific parameters
    star(x_star,y_star,star_size, 'red' ,outer_angle)

#function draws the Libya flag 
def Libya_flag (x,y,height):
    length = 1.5*height #length of rectangle 
    #calls rectangle function to draw with specific parameters
    rectangle(x,y,length,height,'red')
    #position of black rectangle 
    y_black_rectangle = y+(height/4)
    #height of black rectangle 
    height_black_rectangle = height/2
    #draws black rectangle with specific parameters 
    rectangle(x,y_black_rectangle,length,height_black_rectangle,'black')
    #height of green rectangle 
    height_green_rectangle = height/4
    #draws green rectangle with specific parameters 
    rectangle(x,y,length,height_green_rectangle,'lime green')
    #position of the crescent 
    x_crescent_circle1 = x + (((3*height)/4)+((height/4)/2))
    y_crescent1 = y + (height/2)
    x_crescent_cirlce2 = x + (((3*height)/4)+(height/24) + ((height/5)/2))
    #radius of the two circles 
    radius1 = (height/4)/2
    radius2 = (height/5)/2
    #calls crescent function to draw with specific parameters 
    crescent(x_crescent_circle1,y_crescent1,x_crescent_cirlce2,y_crescent1,radius1,radius2,'white','black')
    #position of star 
    x_star = x + ((length/2) + ((height/4)/2))
    y_star = y + ((height/2) - ((height/24)/2)) 
    #math for specific dimensions of each star 
    each_angle_in_star = 180/5
    outer_angle = 180 - each_angle_in_star
    angle_triangle = 180 - outer_angle
    altitude = (((height)/8)/2) - ((height/24)/2)
    star_size = altitude/(math.sin(angle_triangle))
    #calls star function to draw star with specific parameters 
    star(x_star,y_star,star_size, 'white' ,outer_angle)

#function draws the Turkey flag     
def Turkey_flag(x,y,height):
    length = (1.5*height) + (height/30) #length of rectangle 
    #calls rectangle function to draw with specific parameters 
    rectangle(x,y,length, height,'red')
    length_white_rectangle = height/30 #length of white rectangle strip 
    #draws white rectangle strip with specific parameters 
    rectangle(x,y,length_white_rectangle, height,'white')
    #position of crescent 
    x_crescent_circle1 = x + ((height/2) + ((height/2)/2) + (height/30))
    y_crescent1 = y + (height/2)
    x_crescent_circle2 = x + ((height/30) + (height/2) +(height/16) + (((height*2)/5)/2))
    #radius of the two circles 
    radius1 = (height/2)/2
    radius2 = ((2*height)/5)/2
    #calls crescent function to draw with specific parameters
    crescent(x_crescent_circle1,y_crescent1,x_crescent_circle2,y_crescent1,radius1,radius2,'white','red')
    #position of star 
    x_star = x + ((height/30) + (height/2) + ((height/2)/2))
    y_star = y + ((height/2) - ((height/16)/2))
    #math for specific dimensions of each star 
    each_angle_in_star = 180/5
    outer_angle = 180 - each_angle_in_star
    angle_triangle = 180 - outer_angle
    altitude = (((height)/4)/2) - ((height/16)/2)
    star_size = altitude/(math.sin(angle_triangle))
    #calls star function to draw star with specific parameters 
    star(x_star,y_star,star_size, 'white' ,outer_angle)

#function draws the Singapore flag 
def Singapore_flag(x,y,height):
    length = 1.5*height #length of rectangle 
    #calls rectangle function to draw with specific parameters
    rectangle(x,y,length,height,'red')
    height_white_rectangle = height/2 #height of white rectangle 
    #draws white rectangle with specific parameters
    rectangle(x,y,length,height_white_rectangle,'white')
    #position of first circle 
    x_circle1 = x + (height/3)
    y_circle2 = y + ((height/2) + ((height/2)-((10*height)/27))/2)
    #radius of first circle 
    radius1 = ((10*height)/27)/2
    #calls first circle function to draw with specific parameters
    circle(x_circle1,y_circle2,radius1,'white')
    #position of second circle 
    x_circle2 = x + ((height/3) + (height/10))
    y_circle2 = y + ((height/2) + ((height/2)-((2*height)/5))/2)
    #radius of second circle 
    radius2 = ((2*height)/5)/2
    #calls second circle function to draw with specific parameters 
    circle(x_circle2, y_circle2, radius2, 'red')
    #math for specific dimensions of each star 
    each_angle_in_star = 180/5
    outer_angle = 180 - each_angle_in_star
    angle_triangle = 180 - outer_angle
    altitude = (((4*height)/45)/2)
    star_size = altitude/(math.sin(angle_triangle))
    #position of first star
    x_star1 = x +((height/3)+(height/10) +(altitude/4))
    y_star1 = y + ((height/2) + (((height/2)-(height/9))/2)+(height/9) + (((4*height)/45)/2) + (altitude))
    #draws first star with specific parameters
    star(x_star1,y_star1,star_size, 'white' ,outer_angle)
    #position of second star 
    x_star2 = x + (x_star1 +(height/10))
    y_star2 = y + ((height/2) +(height/4) + (((height/4) - ((4*height)/45))/2) - (((4*height)/45)/2) - (altitude/4))
    #draws second star with specific parameters
    star(x_star2,y_star2,star_size, 'white' ,outer_angle)
    #position of third star 
    x_star3 = x + ((height/3)+(height/10) +((height/10)/4) )
    y_star3 = y + ((height/2) + (((height/2)-(height/9))/2) - (altitude/2))
    #draws third star with specific parameters 
    star(x_star3,y_star3,star_size, 'white' ,outer_angle)
    #position of fourth star 
    x_star4 = x + (height/3)
    y_star4 = y + ((height/2) + (((height/2)- (height/9))/2) + (altitude/2))
    #draws fourth star with specific parameters 
    star(x_star4,y_star4,star_size, 'white' ,outer_angle)
    #position of fifth star 
    x_star5 = x + ((height/3) - (altitude/2))
    y_star5 = y + ((height/2) + (height/4) + (((height/4) - ((4*height)/45))/2) +(altitude/4))
    #draws fifth star with specific parameters 
    star(x_star5,y_star5,star_size, 'white' ,outer_angle)

#main function that interacts with the user 
def main():
    #prompts user to pick a flag they want to draw, draw all flags, or quit
    PROMPT = '''Select one of the following options:
        TUN: Tunisia
        LBY: Libya
        TUR: Turkey
        SGP: Singapore
        ALL: All flags
        Q: Quit
        Your choice: '''
    user_choice = input(PROMPT)
    user_choice_lower = user_choice.lower() #makes input lower case for ease in comparision
    while True:
        if (user_choice_lower == 'tun'): #for the Tunisia flag 
            turtle.home()#goes to (0,0)
            Tunisia_flag(0,0,240)
            turtle.clear() #clears after flag is drawn 
        elif(user_choice_lower == 'lby'): #for the Libya flag 
            turtle.home()#goes to (0,0)
            Libya_flag(0,0,240)
            turtle.clear() #clears after flag is drawn 
        elif(user_choice_lower == 'tur'): #for the Turkey flag 
            turtle.home()#goes to (0,0)
            Turkey_flag(0,0,240)
            turtle.clear()#clears after flag is drawn 
        elif(user_choice_lower == 'sgp'): #for the Singapore flag 
             turtle.home()#goes to (0,0)
             Singapore_flag(0,0,240)
             turtle.clear()#clears after flag is drawn 
        elif (user_choice_lower == 'all'):#for all the flags 
            turtle.home()#goes to (0,0)
            Turkey_flag(0,0,240) #draws first flag 
            turtle.up()
            turtle.home() #goes to (0,0)
            turtle.goto(-370,0) #goes to next position to draw flag (numbers from trial and error)
            turtle.down()
            Tunisia_flag(-370,0, 240) #draws second flag 
            turtle.up()
            turtle.home()#goes to (0,0)
            turtle.goto(-370,-250)#goes to next position to draw flag (numbers from trial and error)
            turtle.down()
            Libya_flag(-370,-250,240)#draws third flag
            turtle.up()
            turtle.home()#goes to (0,0)
            turtle.goto(0,-250)#goes to next position to draw flag (numbers from trial and error)
            turtle.down()
            Singapore_flag(0, -250,240)#draws fourth flag
            turtle.clear()
        elif (user_choice_lower == 'q'): #executes if user wants to quit 
            print("Bye") #goodbye message 
            break #terminates the loop and program 
        else:
            print("invalid response") #prints if user enters invalid response 
            
        user_choice = input(PROMPT) #keeps prompting until user wants to quit
        user_choice_lower = user_choice.lower()
            
if __name__ == "__main__":  #lets main function run
    main()
    




            

    
    
    
    
    
