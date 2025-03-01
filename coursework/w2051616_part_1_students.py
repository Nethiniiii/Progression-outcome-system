# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20230282
# UoW Student ID : w2051616
# Date: 1/12/2023

def get_credits(name):      #a function to input credits
    while True:
        Credits = input(f"please enter your credits at {name}:- ")     #use string formatting method to input data
        try :
            Credits  = int(Credits)
            if 0 > Credits or Credits  > 120 or Credits % 20 != 0  :
                print("Out of range")      #validate the out of range error
            else :
                return Credits     #return credits for the other uses
                break
        except ValueError :
            print("Integer required")      #validate the value error
            
print(" \t\t\t Welcome to our university page!!!\n \t\t\t ACADEMIC PROGRESSION ")      #Display the introduction phrase of the page

print("\n")
choice = input("\n Do you want to start?( enter 'y' for yes or 'q' for quite) :" )     #input y or q to start or exit from the programme
while True:
    if choice == 'y':
        print("Please enter your credits properly")      # display a message for the user
        Pass = get_credits("Pass")       #calling the function to input number of pass credits
        Defer = get_credits("Defer")     #calling the function to input number of defer credits
        Fail = get_credits("Fail")       #calling the function to input number of fail credits
        print(f"your credits are: \n  pass - {Pass} \n  Defer - {Defer} \n  Fail - {Fail}")     #use string formatting method to display all the credits
        total_credits = Pass + Defer + Fail
        if total_credits == 120:     #checking if total credits are equal to 120
            print("you have entered credits correctly")     #Display a message for the user
            print("\n")
            if Pass == 120:
                print("PROGRESS")    #Display the prediction of the student's progress
                break        
            elif Pass == 100 :
                print("PROGRESS(MODULE TRAILER)")     #Display the prediction of the student's progress
                break        
            elif Fail >= 80:
                print("EXCLUDE")     #Display the prediction of the student's progress
                break            
            else:
                print("DO NOT PROGRESS-MODULE RETRIEVER")     #Display the prediction of the student's progress
                break
        else:
            print("credit total was incorrect \n")      #display if total not equal to 120
            print ("---------------------------------------------------------------------------------------")
            choice = input("wrong inputs; Do you want to start again? (enter 'y' for yes or 'q' for quite ) :")     #input y or q to continue
    elif choice == 'q':
        print("EXIT")
        break     
    else:
        choice = input("require y or q. \n Do you want to start again? (enter 'y' for yes or 'q' for quite ) :")    #validating the error if user inputs something other than y or q
    
      
