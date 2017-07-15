# Madlibs.py
#Madlibs project from codecademy

#This program takes an input of things, verbs and numbers to fill spaces in a story.


print("I am Sergio Ferro and I approve this Mad Libs")

Things = input("Please write five objects you like, singular, separated by commas ->").split(',')

Verbs = input("And three things you like to do, just the verb, separated by commas ->").split(',')

Adjectives = input("Now write three emotions, comma separated ->").split(',')

Places = input("Two places you like ->").split(',')

Friends = input("Your two best friends ->").split(',')

Animals = input("And two animals :) ->").split(',')

Numbers = input("Before I show you the story, what year will humans go to mars? ->")


#The template for the story

STORY = "Oh I'm so hungry I wish I had a %s. I gotta get home so I can %s my %s. Just kidding. This morning I woke up and felt %s, so I thought of going to the %s. On the other side of the %s were many %ss protesting to keep %ss in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. My friend %s tried to %s us into the sewers and found many %s rats. Needing help, %s quickly called %s. %s appeared and saved us by flying to %s and dropping %s and me into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (Things[0].strip(), Verbs[0].strip(), Things[1].strip(), Adjectives[0].strip(), Places[0].strip(), Places[0].strip(), Animals[0].strip(), Things[2].strip(), Verbs[1].strip(), Things[3].strip(), Animals[1].strip(), Adjectives[1].strip(), Friends[0].strip(), Verbs[2].strip(), Adjectives[2].strip(), Friends[0].strip(), Friends[1].strip(), Friends[1].strip(), Places[1].strip(), Friends[0].strip(), Things[4].strip(), Friends[1].strip(), str(Numbers), Animals[0].strip())

print(STORY)