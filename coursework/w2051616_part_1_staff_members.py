# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20230282
# UoW Student ID : w2051616
# Date: 1/12/2023

from graphics import *     #importing codes from graphic.py to produce a 'histogram'
Progress = 0
Progress_mt = 0
Module_ret = 0
Exclude = 0
tot_outcomes = 0

def get_credits(name):     #a function to input credits
    while choice == "y":
        Credits = input( f"please enter your total {name} credits :-")     #use string formatting method to input data
        try :
            Credits = int(Credits)
            if 0 > Credits or Credits > 120 or Credits  % 20 != 0  :
                print("Out of range")     #validate the out of range error
            else :
                return Credits     #return credits for the other uses
                break
        except ValueError :
            print("Integer required")     #validate the value error

    
print(" \t\t\t Welcome to our university page !!!\n \t\t\t ACADEMIC PROGRESSION OF STUDENTS")     #Display the introduction phrase of the page
print("\n")
choice = input("\n Do you want to start?( enter 'y' for yes or 'q' for quite) :" )     #input y or q to start or exit from the programme
while True:
    if choice == 'y':
        while True:
            print("Please enter your credits properly")     # display a message for the user
            Pass = get_credits("Pass")      #calling the function to input number of pass credits
            Defer = get_credits("Defer")    #calling the function to input number of defer credits
            Fail = get_credits("Fail")      #calling the function to input number of fail credits
            print(f"your credits are: \n  pass - {Pass} \n  Defer - {Defer} \n  Fail - {Fail}")     #use string formatting method to display all the credits
            total_credits = Pass + Defer + Fail
            if total_credits == 120:     #checking if total credits are equal to 120
                print("you have entered correctly ")     #Display a message for the user
                print("\n")
                if Pass == 120:
                    print("PROGRESS")     #Display the prediction of the student's progress
                    Progress += 1
                elif Pass == 100 :
                    print("PROGRESS(MODULE TRAILER)")     #Display the prediction of the student's progress
                    Progress_mt += 1
                elif Fail >= 80:
                    print("EXCLUDE")     #Display the prediction of the student's progress
                    Exclude += 1
                else:
                    print("DO NOT PROGRESS-MODULE RETRIEVER")     #Display the prediction of the student's progress
                    Module_ret += 1
                print ("---------------------------------------------------------------------------------------")  
                choice = input("\n Would you like to enter another set of data?(enter 'y' for yes or 'q' for quite ) :" )     #input y or q to continue
                break
            else:
                print("credit total was incorrect \n")     #display if total not equal to 120
                print ("---------------------------------------------------------------------------------------")
                choice = input("\n Would you like to enter another set of data?(enter 'y' for yes or 'q' for quite ) :" )     #input y or q to continue
                break
    elif choice == 'q':
        print("EXIT")     #stop adding data to the programme
        tot_outcomes = Progress + Progress_mt + Module_ret + Exclude
        print("Total outcomes are ", str(tot_outcomes))
        break
    else:
        choice = input("require y or q. \n Do you want to continue? (enter 'y' for yes or 'q' for quite ) :")   #validating the error if user inputs something other than y or q
print ("---------------------------------------------------------------------------------------")


####creating histogram
win = GraphWin("histogram", 700, 700)   #create the histograms' name and size
win.setBackground("Mint Cream")     #Set the background color of the histogram

X_axis = Line(Point(0,610) , Point(700,610))     #Create the X asis line
X_axis.setWidth(2)
X_axis.draw(win)

Y_axis = Line(Point(120,5) , Point(120,690))     #Create the Y asis line
Y_axis.setWidth(2)
Y_axis.draw(win)

text = Text(Point(190,620) ,"Progress")     #Naming the rectangle "Progress"
text.draw(win)
text1 = Text(Point(280,620) , "Trailer")     #Naming the rectangle "Trailer"
text1.draw(win)
text2 = Text(Point(490,620) ,"Exclude")     #Naming the rectangle "Exclude"
text2.draw(win)
text3 = Text(Point(390,620) , "Retriever")     #Naming the rectangle "Retriever" 
text3.draw(win)
if tot_outcomes != 0:
    text4 = Text(Point(280,660) , str(tot_outcomes)+ "  "+ "outcomes in total")     #display the number of total outcomes
    text4.draw(win)
else :
    text4 = Text(Point(280,660) , " 0 outcomes in total")     #display the number of total outcomes
    text4.draw(win)
    print("EXIT")
text5 = Text(Point(70,300) , "Number \n of \n students")     #Display the Y axis representation
text5.draw(win)
text6 = Text(Point(190,590- Progress * 20) , str(Progress))     #display student count of progress
text6.draw(win)
text7 = Text(Point(290,590- Progress_mt * 20) , str(Progress_mt))   #display student count of module trailer
text7.draw(win)
text8 = Text(Point(390,590- Module_ret * 20) , str(Module_ret))     #display student count of module retriever
text8.draw(win)
text9 = Text(Point(490,590- Exclude * 20) , str(Exclude))      #display student count of exclude
text9.draw(win)

Progress = Rectangle(Point(150, 600-Progress * 20), Point(230,600))     #Create the rectangle that represents the "Progress" students
Progress.setFill("Green")        #set the colour of the rectangle as green
Progress.setOutline("Black")     #set the colour of the outline of the rectangle    
Progress.draw(win)

Progress_mt = Rectangle(Point(250, 600-Progress_mt * 20), Point(330,600))     #Create the rectangle that represents the "Module Trailer" students
Progress_mt.setFill("Blue")        #set the colour of the rectangle as blue
Progress_mt.setOutline("Black")    #set the colour of the outline of the rectangle
Progress_mt.draw(win)

Module_ret = Rectangle(Point(350, 600-Module_ret * 20), Point(430,600))     #Create the rectangle that represents the "Module retriever" students
Module_ret.setFill("Orange")       #set the colour of the rectangle as orange
Module_ret.setOutline("Black")     #set the colour of the outline of the rectangle
Module_ret.draw(win)

Exclude = Rectangle(Point(450, 600-Exclude * 20), Point(530,600))     #Create the rectangle that represents the "Exclude" students 
Exclude.setFill("Red")          #set the colour of the rectangle as red
Exclude.setOutline("Black")     #set the colour of the outline of the rectangle
Exclude.draw(win)

