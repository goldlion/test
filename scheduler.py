#Kevin Howald (kmh287@cornell.edu)
#scheduler.py
#7/12/14
#Small tool to find the optimal time to have a meeting
#when dealing with people with different schedules. 

#Global variables
ESSENTIAL = 10000

#Class for a person, contains that person's availability
#for the week
class Person(object):
    """
    - Name is the name of the person represented by this object
    - Importance is an int determining how essential it is that
    this person attend the meeting. 1 is least important. Essential
    people will have very high importance. 
    """
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance 
        self.schedule = [] 


#Main function 
if __name__ == '__main__':
    input("Welcome to the scheduler. Press enter to begin\n")
    
    #Ask for the number of people
    numPeople = None 
    while(numPeople == None):
        try:
            inputNumPeople = int(input("How many people wish to attend?\n"))
            if inputNumPeople > 0:
                numPeople = inputNumPeople
            else:
                print("""Invalid input: number of attendees
                      must be greater than 0.""")
        except ValueError:
            print("That wasn't a number. Please try again.\n")
            
    #Create a list of attendees
    attendees = [] 
    
    #Loop over each person, get their name, essential score, and
    #availability times.
    for i in range(numPeople):
        
        #Get name 
        name = None
        while(name == None): 
            inputName = input("Please give a name for person "
                              + str(i+1) + "\n")
            if (inputName == ""):
                print("A person cannot have an empty name.\n")
            else:
                name = inputName
                
        #Get Score
        score = None 
        while(score == None):
            try:
                #Store prompt in its own var to increase readability
                scorePrompt = ("How essential is this person? \n"
                               "Enter a number between 1 (least important) to " + 
                                str(ESSENTIAL) + 
                                " (most important)\n")
                inputScore = int(input(scorePrompt))
                if (inputScore < 1):
                    print("A person must have a positive score.\n")
                elif (inputScore > ESSENTIAL):
                    print("A person's score must be below " + str(ESSENTIAL)) 
                else:
                    score = inputScore 
            except ValueError:
                print("That wasn't a number. Please try again.\n")
        
        
    
    
    
    
    
    
    
    
    