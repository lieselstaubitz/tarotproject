import random
#Welcome Statement
print("\nHi, welcome to your tarot card reading!")
print("Madame Lieselle Sparkelle will tell you about your past, present, and future! Then she will advise on your love life!\n")

#Get User Name
name = input("Please, tell me your name: ")
print("\nPleased to be meeting you, " + name + "!\n")

#Get User Gender
gender = input("Now, please tell Madame... do you identify as a female/feminine person? Tell me yes or no: ").lower()
print("\nFirst, I will pull a card that shall represent your divine energy...\n")
#Assign Queen Card
if gender == "yes":
    queen_card = random.randint(1, 4)
    if queen_card == 1:
        print(name + ", you are the Queen of Wands... marked by your creativity and energy, you are warm and kind. You are a born leader and a true artist. ")
    elif queen_card == 2:
        print(name + ", you are the Queen of Pentacles... marked by your business and action, you get work done and aren't afraid to dive right in to projects. You are hard working and may one day become a business owner.")
    elif queen_card == 3:
        print(name + ", you are the Queen of Swords... marked by your intelligence and courage, you are highly intelligent and possess a deep wisdom. You have suffered, but have always learned from it. You are fair and wise.")
    else:
        print(name + ", you are the Queen of Cups... marked by your love and health, you care for others with a maternal glow. Your intentions are guided by love, but sometimes you can be shy and reserved.")
#Assign King Card
else: 
    king_card = random.randint(1, 4)
    if king_card == 1:
        print(name + ", you are the King of Cups... marked by your protection and love, you are a person of deep knowledge and good will. You are virtuous and would make an excellent doctor or artist.")
    elif king_card == 2:
        print(name + ", you are the King of Pentacles... marked by your desire for wealth and security, you have gained your knowledge and wisdom slowly over time. Security makes you strong and you would be best suited to a career in science or business.")
    elif king_card == 3:
        print(name + ", you are the King of Swords... marked by your belief in destiny and justice, you are severe but fair. You can be serious and rigid at times, but your intelligence and consistency make you a great leader.")
    else: 
        print(name + ", you are the King of Wands... marked by your charisma and loyalty, you are a strong and charming person who is a master of speech. You are loyal and always respect loyalty in return.")

#Past Card Output
int_past = random.randint(1, 5)
past_card = ""
past_card_meaning = ""
#print(int_past)
if int_past == 1:
    past_card = "The World Card"
    past_card_meaning = "fulfillment, harmony, completion"
elif int_past == 2:
    past_card = "The Queen of Wands Card"
    past_card_meaning = "courage, determination, joy"
elif int_past == 3:
    past_card = "The Ace of Cups Card"
    past_card_meaning = "new feelings, spirituality, intuition"
elif int_past == 4:
    past_card = "The Two of Swords Card"
    past_card_meaning = "difficult choices, indecision, stalemate"
else:
    past_card = "The Judgement Card"
    past_card_meaning= "reflection, reckoning, awakening"

print("\nNow I will turn over the card that represents your past.") 
meaning_past = input("Press enter to reveal your past ")
print("\nYou got " + past_card)
print("Very interesting... this means that your past was shrouded in feelings of " + past_card_meaning + ".")


#Present Card Output
int_present = random.randint(1, 5)
#print(int_present)
present_card = ""
present_card_meaning = ""
if int_present == 1:
    present_card = "The Sun Card"
    present_card_meaning = "joy, success, celebration, positivity"
elif int_present == 2:
    present_card = "The Queen of Cups Card"
    present_card_meaning = "compassion, calm, comfort"
elif int_present == 3:
    present_card = "The Nine of Pentacles Card"
    present_card_meaning = "fruits of labor, rewards, luxury"
elif int_present == 4:
    present_card = "The King of Swords Card"
    present_card_meaning = "head over heart, discipline, truth"
else:
    present_card = "The Moon Card"
    present_card_meaning= "unconscious, illusions, intuition"

print("\nNext I will turn over the card that represents your present.") 
meaning_present = input("Press enter to reveal your present state ")
print("\nYou got " + present_card)
print("I see... this means that your present is marked by feelings of " + present_card_meaning + ".")


#Future Card Output
int_future = random.randint(1, 5)
#print(int_future)
future_card = ""
future_card_meaning = ""
if int_future == 1:
    future_card = "The Star Card"
    future_card_meaning = "hope, faith, rejuvenation"
elif int_future == 2:
    future_card = "The King of Wands Card"
    future_card_meaning = "big picture, leadership, overcoming challenges"
elif int_future == 3:
    future_card = "The Six of Wands Card"
    future_card_meaning = "victory, success, public reward"
elif int_future == 4:
    future_card = "The Chariot Card"
    future_card_meaning = "direction, control, willpower"
else:    
    future_card = "The Tower Card"
    future_card_meaning= "sudden upheaval, broken pride, disaster"

print("\nTime for the future, now I will turn over the card that represents your future.") 
meaning_future = input("Press enter to reveal your future ")
print("\nYou got " + future_card)
print("Oh wow, Madame Lieselle doesn't see this too often... this means that your future might be defined by feelings of " + future_card_meaning + ".")

#Love Card -- Get realtionship staus
print("\nFinally, let's find out where you stand in matters of the heart...")
relationship_status = input("Madame Lieselle must know are you in a relationship? answer yes or no: ").lower()
love_card = input("Beautiful, now I will ask you to choose a color to find out about what is in the cards for your love life... select red, blue, yellow, green, or pink: ").lower()

#In a relationship
if relationship_status == "yes":
    if love_card == "red":
        print("\nYou have selected The Fool Card.") 
        print("This means that despite being in a relationship, you often believe you deserve better and you constantly seek new experiences. You must deeply reflect on your current relationship to uncover if you are truly satisfied.")
    elif love_card == "pink":
        print("\nYou have selected the Magician Card.")
        print("This means you are in a relationship with someone who really gets you. They know who you are and what makes you tick! You have plenty to talk about, you make each other laugh and have common interests. This person is your ideal partner and you should stay together forever.")
    elif love_card == "yellow":
        print("\nYou have selected the High Priestess Card.")
        print("You require intellectual stimulation at all times and honestly might be bored with your current partner. You tend to day-dream away from reality and you tend to always yearn for more. It is time to reflect on your current relationship and reevaluate what you truly need.")
    elif love_card == "green":
        print("\nYou have selected the Emperor Card.")
        print("This means you are in a relationship with someone who is in some ways stronger and bolder than you are. This person doesn't always let you in, so you must work hard to peel back the layers of their personality. Only then will you be fulfilled in your relationship.")
    else:
        print("\nYou have selected the Empress Card.")
        print("You are in a very healthy and prosperous relationship that is positive, optimistic, and fun. As long as you and your partner work together, you will be extremely lucky and have many blessings.")
#Single
else:
    if love_card == "red":
        print("\nYou have selected The Fool Card.")
        print("This means you are a bit foolish and immature in regards to love. You crave freedom and tend to jump around to different people. Enjoy your time to yourself and get to know you. A relationship is not right at this time.")
    elif love_card == "pink":
        print("\nYou have selected the Magician Card.")
        print("This means you are about to meet someone who really gets you. They know who you are and what makes you tick! You will have plenty to talk about, you will make each other laugh and have common interests. This person is your ideal partner and you should stay together forever.")
    elif love_card == "yellow":
        print("\nYou have selected the High Priestess Card.")
        print("You require intellectual stimulation at all times and you tend to day-dream away from reality. You will soon meet a partner who will both intellectually stimulate you and ground you in reality, but be careful not to overlook this person on first impression.")
    elif love_card == "green":
        print("\nYou have selected the Emperor Card.")
        print("This means you are soon going to meet a potential partner who is very strong and worldly, but do not be intimidated. This person will introduce you to new things and experiences, but you must hold on to your own power and remember that you also have a lot to contribute.")
    else:
        print("\nYou have selected the Empress Card.")
        print("You will one day meet a wonderful person who will be extremely popular, family-oriented, optimistic, and positive! This person will be your ideal partner, but you will need to wait at least one full year before this person will enter your life.")

#Goodbye Statement
print("\nBut, always remember sweet, " + name + ", the future is not set in stone. It is yours to create.")
print("Madame Lieselle Sparkelle wishes you a beautiful future... enjoy!")