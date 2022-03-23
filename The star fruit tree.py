import sys

#The story is based loosely on the translation of the Vietnamese folktale "The golden star fruit tree" by vietnammonpaysnatal.fr
#To see the translation, follows this link: https://www.vietnammonpaysnatal.fr/the-golden-star-fruit-tree-an-khe-tra-vang/
#All variables are writen in the snake_case format 
#The first part (snake) will include the data type of the value that the variable stores
#The second part (case) will include the name of the variable


#A variable created with string data type to store the introductory paragraph of this story
#Since this variable contain a paragraph (lots of words), string data type would be the most appropriate
#Since this is the first paragraph/message in the story, and also counting in Python starts from 0, it's named message0
#It's named message to signify that this variable stores a narative, hence it's better than random names like abc or asddf
#The name "message" is also shorter than "paragraph", so it's a better choice
str_message0 = "Once upon the time there were two brothers who divided an inheritance at the death of their parents. "
str_message0 += "The elder, Eugene, who was greedy and stingy, took all the wealth. \n\n"
sys.stdout.write(str_message0)

#Letting the  user name the main character by taking in their input
#A variable created to store input has string data type and is called "name" for easy access (since this name will be used throughout the story)
sys.stdout.write("Enter the younger brother's name: ")
str_name = sys.stdin.readline().strip()

#A list created to store different endings of the story
#Each ending is a paragraph, therefore each item in the list will be in string data type
#The sequence in which these endings are appended follows how they are numbered in the flowchart provided in the user guide
endings = []
endings.append(str_name + " thought that his hut was haunted and decided to move faraway. The end.")
endings.append(str_name + " decided not to tell his brother about the star fruit tree and the raven. Eugene became furious and parted ways with " + str_name + ". They never see each other again. The end.")
endings.append("After being drop on the island, Eugene filled the bag with gold.  On the way back, burdened by the overweight of the bag, the raven, who could not hold any longer, swayed and sent Eugene back to the deserted island. Eugene was stuck there forever for his greed. The end.")
endings.append("After going to the deserted island, Eugene had also became wealthy like his younger brother.  He then contemplated about his past doings and felt bad for his younger brother. He decided to made up with " + str_name + ". The brothers, who are now friends again, dedicated their new found wealth to care for the poor. The end.")


#A new variable to store the second paragraph in the story
#It has string data type and is named "message1" to signal that this paragraph comes after message0
str_message1 = "The younger brother, " + str_name + " was left with only a dilapidated hut and a star fruit tree.\n"
str_message1 += str_name + " took care of the tree and watered it in such a way that it bore lots of fruits. " 
str_message1 += "When the star fruits began to ripe, a ginormous raven came and eat all the fruits."
str_message1 += " Having lost the fruits, the man lamented:\n \n"
str_message1 +="\"Poor me.I count much on was what that star tree brings; Now look,this bird ravaged it all.\"\n\n"
str_message1 += "The raven upon hearing those lamentations, perched down and replied in a human voice: \n\n"
str_message1 += "\"Star fruits I eat, with gold I pay, be ready with a three-foot bag and follow me to get it.\" \n\n"
str_message1 += "Feeling afraid and confused, " + str_name + " decided to:\n"
str_message1 += "1. Do as what the raven told him to do\n2. Abandon his hut and move faraway\n"
sys.stdout.write(str_message1) 

#A variable to store the user's choice between the two pathways presented in the last lines of message1
#We want to take in either a 1 or 2 for the input, therefore this variable has int as its data type
#The choice the user make will affect the outcome of the story
#From now on, the user's inputs to choose between each pathway will be named choice
#This is the first time the story require the user to make a choice, and beacause counting in Python start from 0, the variable used to store the answer is named choice0
#The name "choice" was chose beacause it signify that the user's input will affect the outcome of the story
#Another possible name is "answer" but it isn't as clear as the name "choice" in terms of significance (read the preceeding comment)
#also the name "answer" isn't any more concise than "choice", therefore the name "choice" was chose
int_choice0 = int(sys.stdin.readline())

#A new variable created to store the next paragraph in the story
#It has string data type and is called message2 to signal that this paragraph comes after message1
#This message appearance depends on the pathway taken between the two presented in message1
str_message2 = str_name + " thought to himself that he had nothing left so why shouldn't he take the chance. "
str_message2 += "So he sew a three-foot bag from old clothes and waited.\n\n"
str_message2 += "A few days later, the raven came back and invited him to take a seat on its back with the bag. "
str_message2 += "Then the bird took him to a deserted island full of precious stone. He was free to take whatever he could.\n\n "
str_message2 += "He filled the bag and the raven took him back to his home.  "
str_message2 += "From then on, he became wealthy and often give help to the poor. "
str_message2 += "On the occasion of commemoration of their parents' death, " + str_name + " invited his older brother to come over. "
str_message2 += "Suprised to see his younger brother's opulence and wealth, Eugene tried to ask " + str_name + " his secret.\n\n"
str_message2 += str_name + " decided to: \n"
str_message2 += "1. Tell Eugene what happened.\n2. Don't tell Eugene what happened.\n "

#A new variable to store the next paragraph in the story
#It has string data type and is called message3 to signal that this paragraph comes after message2
#This message appearance depends on the pathway taken between the two presented in message2
str_message3 = str_name + "  decided to tell his brother about the star fruit tree and the raven. "
str_message3 += "Eugene then came up with a plan and proposed an exchange of his fortune for only the hut and the star fruit tree. " + str_name + " agreed. \n\n"
str_message3 += "One day, the raven came back to eat the star fruits and gave the same recommendation: a three-foot bag to look for gold. "
str_message3 += "Eugene, greedy and curious, prepared a six-foot bag. "
str_message3 += "Having known about this, " + str_name + " tried to stop his brother from bringing such a large bag. "
str_message3 += "Eugene, however, tried to deceive his younger brother by saying that his bag is actually a 1.8-meter bag, not a six-foot bag. \n\n"  
str_message3 += str_name + ", knows that 1 foot is equal to 0.3 meters, replied: \n "
str_message3 += "\"No, you're wrong. Since 1 foot is equal to 0.3 meters, your bag should be a "

#A new variable to store the next line in the story
#It has string data type and is called message4 to signal that this sentence comes after message3
#This message apperance depends on the user's answer to the question at the end of message3
str_message4 = "Exposed by his brother, Eugene admitted that he was wrong and sew a three-foot bag instead.\n"

#A new variable to store the paragraph in the story
#It has string data type and is called message4_2 to signal that this sentence comes after message3
#This paragraph appearance depends on the user's answer to the question at the end of message3
#This message will appear in a pathway parallel to the pathway that contain message4, therefore it isn't named message5 but rather message4_2
str_message4_2 = "Eugene easily spotted that " + str_name + " had got the math wrong. "
str_message4_2 += "Eugene pointed that out and use it as a reason not to listen to his brother. "
str_message4_2 += "He kept his six-foot bag and waited. \n"

#The next code block will execute only if the user had taken the first pathway presented in message1
if int_choice0 == 1:
  
  #message2 belongs to the pathway chosen, therefore it's included inside
  #message2 is presented first to show the user the next two pathways
  sys.stdout.write(str_message2)
  
  #Taking in the user's choice between the two pathways presented in message2
  #This is the second time the user need to choose between two pathways
  #therefore the variable used to store the input this time was named choice1
  int_choice1 = int(sys.stdin.readline())
  
  #this next block of code will execute only if the user had taken the first pathway presented in message2
  if int_choice1 == 1:
    
    #message3 belongs to the pathway chosen 
    #message3 is presented first to show the user the question that will either take them to the third or fourth ending
    sys.stdout.write(str_message3)
    
    #Taking in the user's answer for the question at the end of message3
    #This is a small math question that will require the user to input a float number as the answer
    #therefore the data type should be float
    float_answer = float(sys.stdin.readline())
    sys.stdout.write("-meter bag, not a 1.8 one.\"\n")
    
    #the next code block will execute only if the user's answer to the question in message3 is correct
    if float_answer == 0.9:
      
      #message4 goes together with (and before) the fourth ending to make the full fourth ending
      #therefore it's included in the code block and showed before the final ending
      sys.stdout.write(str_message4)
      sys.stdout.write(endings[3])
      
    #the next code block will execute only if the user's answer to the question in message3 is wrong
    else:
      
      #message4_2 goes together with the third ending to make the full third ending
      #therefore it's included in the code block and showed before the final ending
      sys.stdout.write(str_message4_2)
      sys.stdout.write(endings[2])
      
  #this next block of code will execute only if the user had taken the second pathway presented in message2
  elif int_choice1 == 2:
    
    sys.stdout.write(endings[1])
    
#This code block will execute only if the user had taken the second pathway presented in message1
elif int_choice0 == 2 :
  sys.stdout.write(endings[0])


