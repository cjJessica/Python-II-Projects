#import random library
import random

#I put different lists inside a dictionary based on the topic. The topics are the keys and the lists are the values
happy_fortune = {"Romance" : ["You will meet the love of your life soon", "You and your partner will work things out", "Singleness will bring you the most joy"],
           "School" : ["You will get into the school of your dreams", "You will find good friends instead of good grades", "Your dedication will pay off"],
           "Money" : ["A job may come and go, but your family never leaves", "A promotion is in your future", "Don't get greedy and be content"]}

#I made a basic dictionary for angry fortunes having the toic be the keys
angry_fortune = {"Romance" : "You will forever be alone", "School" : "Your lack of ambition will cost you everything", "Money" : "Your past deeds will catch up to you"}

#Class creation
class FortuneTeller:
    #initialize attributes
    def __init__(self, name="John Doe", topic="Romance", mood="happy"):
        self.name = name
        self.topic = topic
        self.mood = mood

    #Asks the user to choose a topic and returns it.
    def topic_chooser(self):
        topic_input = input("Please enter the topic you want your fortune to be about - Romance, School, Money: ")
        
        #Input validation
        while topic_input != "Romance" and topic_input != "School" and topic_input != "Money":
            topic_input = input("That topic is not a part of today's deal. Please enter Romance, School, or Money: ")
        return topic_input

    #This method will ask if the user has tipped or not. If they did the mood will be happy and if they didn't the teller's mood will be angry
    def tellers_mood(self):
        tip = input("Before we give you your next fortune, did you remember to tip your fortune teller? y/n: ")
        
        #Input validation
        while tip != "y" and tip != "n":
            tip = input("That is an invalid input, please type y or n: ")

        if tip == "y":
            print("\nThank you so much, your fortune teller is now happy and will proceed with the next reading!\n")
            self.mood = "happy"
        else:
            print("\nYou have now angered your fortune teller! They will now tell you your new fortune.\n")
            self.mood = "angry"

    #If the mood is happy the method will go into the dictionary and find the key that matches the topic and go to it's value. It will then choose randomly one of the items in the value's list.
    #But if the mood isn't happy it will randomly choose an item from the angry_fortune dictionary.
    def fortune_printer(self):
        if self.mood == "happy":
            print(f"\n{self.name}, your fortune is:\n{random.choice(happy_fortune[self.topic])}.\n")
        else:
            print(f"\n{self.name}, your fortune is:\n{angry_fortune[self.topic]}.\n")




#Creates an instance of FortuneTeller
your_fortune = FortuneTeller()

print("Come on in, we have a special deal! Get 2 fortune tellings for cheap price of $$\n")

#Gets the user's info
name_input = input("What is your name: ")
topic_input = your_fortune.topic_chooser()

your_fortune = FortuneTeller(name_input, topic_input)

#Prints out the user's first fortune
your_fortune.fortune_printer()

#Gets the teller's mood
your_fortune.tellers_mood()

#User chooses a topic again
your_fortune.topic = your_fortune.topic_chooser()

#Prints out the user's final fortune
your_fortune.fortune_printer()

print("\nThank you so much for your business! And remember, always tip your fortune teller.")

