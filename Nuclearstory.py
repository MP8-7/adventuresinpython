#Simple text based adventure game


#intro
name = input("Please enter your name:")
print ("")
print("You awaken in a grassy field.")
print("In front of you, the ashes and remains of a desolate city destroyed by a nuclear attack is a mile north from you.")
print("Behind you is a bunker about a quarter mile south that might have food, water,  and supplies.")
print("Do you go north to the city (N), or south to the bunker (S)?")
print("")

#1 input
firstinput = input("Please type your choice:")
print("")
# 1 if

if firstinput.upper() == "N":
    print("As you continue towards the city, you find the air strange.")
    print("It's hard to breathe, it feels hot")
    print("But you are determined to see if there are any survivors to help you.")
    print("You fall to the ground, heavy radiation is still lingering.")
    print("GAME OVER")
else:
    print("You run to the bunker, opening the door, you find other people.")
    print("At first, they are scared, as a Fallout player would be after a nuclear blast, but then they are happy to see another human being.")
    print("After a quick meeting of deciding what to do, you and the other people have todecide between 2 options.")
    print("Option 1: Don hazmat suits and explore the wreckage, or #2: Stay in the bunkerlong enough for the radiation to at least mellow.")
    print("Do you choose #1 (1), or #2 (2)?")
    print("")
    #2 input
    secondinput = input("Please type your choice:")
    print("")
    

    #2 if
    if secondinput.upper() == "2":
        print("You wait, and wait, and wait.")
        print("The radiation hasn't mellowed")
        print("It turns out, since the half-life of plutonium is 7,000 years, you die of age.")
        print("GAME OVER")
    else:
        print("You and 2 others get in hazmat suits and start to explore the ruins of the city.")
        print("Apparently this was the first large casualty of Wprld War 3")
        print("There is only 1 part of the city that was unharmed.")
        print("You quickly rush there, trying to find a vehicle.")
        print("One of the people in your group goes back to tell the other to come get in the van.")
        print("Do you: Drive to another city (D) or stay in the bunker (B)?")

        #3 input
        thirdinput = input("Please type your choice:")
        print("")

        #3 if
        if thirdinput.upper() == "D":
            print("You and everybody from the bunker are on the van.")
            print("After a few hours of driving, you find a city completely unharmed.")
            print("All of you try to settle down in the new city when, after just a few days, suddenly alarms start blaring!")
            print("Another bomb, streaking towards the city.")
            print("Attempting to run away from the blast radius, a bright light envelops the entire building you are in.")
            print("Suddenly, you hear a voice")
            print("'Hey, you, your finally awake!  You were trying to cross the border, right?  Walked right into that ambush same as us.'")
            print("THE END")
            print("NEUTRAL END, TRY TO GET THE GOOD AND BAD ONES," + name + " (There are 3 'endings')")
        else:
            print("You stay in the bunker. You're safe from nuclear attacks.")
            print("After seems like an eternity of waiting, you rise up from the bunker and about 3 feet of ash to find an almost destroyed world.")
            print("As you explore, it's clear what to do.")
            print(" 1: Rule the remaining rest of the world with an iron fist. (1)")
            print(" 2: Move into the rest of the world, live the rest of your life, maybe have a family. (2)")

            #4 input
            fourthinput = input("Please type your choice:")

            #4 if
            if fourthinput.upper() == "1":
                print("As you rose up, you decided to rule the remailning world with an iron fist.")
                print("Everybody obeyed you, but no matter how much many people you enslaved, or how much money you had, there was always an emptyness inside.")
                print("You never had the chance to just settle down from the chaos in the world, it drives you crazy, wishing you would have done that.")
                print("BAD ENDING, TRY TO GET THE GOOD AND NEUTRAL ONES," + name + " (There are 3 endings.)")

            else:
                    print("You decide to settle down and live a nice life for a while.")
                    print("You find a person that loves you, and decide to start a family.")
                    print("You feel happy and accomplished in life.")
                    print("GOOD ENDING, TRY TO GET THE BAD AND NEUTRAL ONES," + name + ". (There are 3 endings.)")




