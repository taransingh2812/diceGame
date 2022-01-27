#     #COMP 10001 - W2020 Final Project by Taran Preet Singh, Student number 000824301 Welcome to my dice game, good luck!       #
#     # I, Taran Preet Singh, student number 000824301, certify that all code submitted is my own work;                                             #
#     #that I have not copied it from any other source.                                                                                                                  #
#    #I also certify that I have not allowed my work to be copied by others.                                                                                    #
###############################################################################################
print("COMP 10001 - W2020 Final Project by Taran Preet Singh, Student number: 000824301 Welcome to my dice game, good luck!")

#defined functions

import random

def rollDie( faces ):
    faces = random.randint(1,face)
    return faces

def validateInt( min, max, prompt ):

    while (not prompt.isdecimal()) or int(prompt) > int(max) or int(prompt) < int(min)  :
        
        print("I'm sorry, that isn't a valid positive integer, please try again." )
        prompt = input("Enter # in the given range [ " + str(min) + " ," + str(max) + "  ]")
        
        
    return (prompt)

def average( inList ):
    su_m = sum(inList)
    y = len(inList)
    y = int(y)
    average_sum = round(su_m/ y,0)
    return average_sum

def calculatePercentage( sides, dices, diceRoll ):
    su_m = sum(diceRoll)
    maxScore  = int(sides)*int(dices)
    percentage = (int(su_m)/float(maxScore))
    return percentage

def isPrime( number ):
    count = 0

    if number%2==0:
        count+=1

    if number%3==0:
        count+=1

    if number%5==0:
        count+=1

    if number%7==0:
        count+=1

    if count != 0:
        return False

    else:
        return True

def pattern1( sides, dices ):
    count = 0
    counter = 0
    while count <len(dices):
        if dices[0]==dices[count]:
            valid = True
            
        else:
            counter +=1
            
        count+=1

    if not (counter >1):
                                  
                                
        bonusFactor=10
        
    else:
        bonusFactor =   0
        

    if bonusFactor ==0:
        print("Pattern 1 not matched in your roll, " + str(dices) + " some dice are differrent.")
        return bonusFactor
    else:
        if sides >=4:
            print("Pattern 1 matched in your roll, " + str(dices) + " all dice are same.")
            bonusFactor=10
            return bonusFactor
        else:
            print("Pattern 1 not matched in your roll, as condition doesn't meet")
            bonusFactor=0
            return bonusFactor
            

def pattern2( sides, count, dice):
    if validity==False:
        print("Pattern 2 not matched,as " + str(count) + " is not prime")
        bonusFactor=0
        return bonusFactor

    else:
        if not (int(sides) >=20):
            print("Pattern 2 not matched as " + str(count) +" , Condition doesn't match ")
            bonusFactor=0
            return bonusFactor

        else:
            if (validity==True and int(sides)>=20):
                bonusFactor =15
                print("Pattern 2 matched,as " + str(count) + " is prime")
                return bonusFactor


    
def pattern3( dices ):

    su_m=sum(dices)
    average_sum= round(int(su_m)/len(dices),0)
 
    if not (len(dices) >=5):
        print("Pattern 3 does not apply since there are less than 5 dice.")
        bonusFactor=0
        return bonusFactor

    else:
        y = len(lists)
        count =0
        for i in lists:
            if i >=average_sum:
                count+=1
               
        if not (count >= y/2):
            print("Pattern 3 not matched! No more than half of " + str(dices) + \
                  (" greater than or equal to the average of ") + str(average_sum) )
            bonusFactor = 0
        else:
            print("Pattern 3 matched! More than half of " + str(dices) + \
                  (" greater than or equal to the average of ") + str(average_sum) )
            bonusFactor =5
            
        return bonusFactor



def pattern4( sides, dices ):
    count = 0
    pattern = 0
    bonusFactor = None
    while count < len(dices):

        counter = 0
        while counter < len(dices):
            if dices[counter]==dices[count]:
                counter+=1
                pattern+=1

            else:
                counter+=1

        count+=1

    if pattern > len(dices):
        print("Pattern 4 not matched! Some of the values in " + str(dices) + " match!")
        bonusFactor=0
        
    else:
        if  not(int(dice) > 4 and int(sides) > int(dice)):
            bonusFactor = 0
            print("Pattern 4 does not apply, either sides <=4 or " + "# sides <= # dice")
            
        else:
            bonusFactor = 8
            print("Pattern 4 is matched! All the values in " + str(dices) + " are different")
            
    return bonusFactor

    
def bonusFactor( sides, count, dices ):
    totalBonus = sum(dices)
    return totalBonus


def score( maxSides, totalDice, diceRolled ):
    studentNumber = 824301
    Score = (round(maxSides,2)*totalDice + (studentNumber%500) )
   
    return Score


# main program

#asking the user for no. of face.      
face = input("\n" + "Enter # of face [2,20]: " )

while not face.isdecimal():
    print("I'm sorry, that isn't a valid positive integer, please try again.")
    face = input("Enter # of face [2,20]: ")

face = validateInt( 2, 20 ,face)

#asking the user for no. of die.
dice = input("Enter # of dice [3,6]: " )

while not dice.isdecimal():
    print("I'm sorry, that isn't a valid positive integer, please try again.")
    dice = input("Enter # of dice [3,6]: ")

dice = validateInt(3,6,dice)


#Getting random numbers from diceRolls.
#creating a list named lists.

lists = [ ]
face = int(face)
count = 0
while count < int(dice):
    diceRolls=rollDie(face)
    lists.append(diceRolls)
    count+=1
#count increased by 1.
    
#Showing the list containing all outcomes.
print ("You have rolled: " + str(lists) +"\n")

#average value
su_m = sum(lists)
average_sum = average(lists)

print("These die sums to "+ str(su_m) + " have an average rounded value of "+ \
      str(average_sum))

#calculating maximum Score and percentage
percentage = calculatePercentage(face,dice,lists)

maxScore=face*dice
#list to have all bonus values in.
listz =[ ]
#pattern 1

bonusFactor1 = pattern1(face,lists)

listz.append(bonusFactor1)
#adding the bonusFactor value in listz


#pattern 2 
validity = isPrime(su_m)

bonusFactor2 =pattern2(maxScore,su_m,listz)

listz.append(bonusFactor2)
#adding the bonusFactor value in listz


#pattern 3

bonusFactor3 = pattern3(lists)

listz.append(bonusFactor3)
#adding the bonusFactor value in listz


#pattern 4
    
bonusFactor4 = pattern4(face,lists)

listz.append(bonusFactor4)
#adding the bonusFactor value in listz

#removing if any None element present in the listz.
if None in listz:
    listz.remove(None)
    
#pattern 5
bonusFactor5 = 0

if sum(listz) > 0:
    bonusFactor5 = 0
    print("Since you matched a pattern, pattern 5 is not matched!")

else:
    bonusFactor5 =1
    print("Since no pattern matched, therefore pattern 5 matched!! ")

listz.append(bonusFactor5)
#adding the bonusFactor value in listz

#total bonus factor
totalBonus = bonusFactor(face, dice, listz )
print("Your bonus factor is " + str(totalBonus))

#score
#averageScore list as empty to store all the Score in each roll.
averageScore = [ ]

Score = score(percentage, totalBonus , lists)


averageScore.append(Score)

print("These dice are worth " + str(Score) + " points." + "\n")

gamePlay = 1

###################################################################
#above line is to given to improve readability. 


#ask the user if user wants to reroll the die or not.
user_input = input("\n" + "Do you want to reroll any dice with your choice? [ 'yes' , 'no'] :  ")
lists1 = [ ]#store true and false list
count=0
lists3 = [ ]
cout = 0

while not (user_input.upper() =="YES" or user_input.upper()=="NO") :
    print("I am sorry!! Your entered choice is not valid!! ") 
    user_input = input("\n" + "Do you want to reroll any dice with your choice? [ 'yes' , 'no'] :  ")


if user_input.upper()=="YES":
       
    while count < len(lists):

           if user_input.upper()=="YES":
        
              diceInput = input("Do you want to reroll this die? (was " + str(lists[count]) +" ) ['y' , 'n']  " )
           
              while not (diceInput.upper() == "Y" or diceInput.upper() =="N"):
                     print("I'm sorry, the choices are [ 'y' , 'n' ]. Please pick one of them.  ")
                     diceInput = input("Do you want to reroll this die? (was " + str(lists[count]) +" ) ['y' , 'n']  " )

              if diceInput.upper() == "N":
                     lists1.append(False)

              else:
                     lists1.append(True)

           count+=1

    # asking user again
    ask = input("Are You Sure? [ ' yes ' , ' no ']: " + "\n")

    while not (ask.upper() =="YES" or ask.upper()=="NO") :
       print("I'm sorry, the choices are [ 'yes' , 'no' ]. Please pick one of them.  ") 
       ask = input("Are You Sure? [ ' yes ' , ' no ']: " + "\n")

    if ask.upper()=="NO":
           #score
           print("Your score was " +str(max(averageScore)) + "points on turn " + str(gamePlay)+" . " + "\n")
           
               

    else:
           while cout < len(lists1):
               if lists1[cout]==True:
                      diceRolls=rollDie(face)
                      lists.insert(cout, diceRolls)
                      del lists[cout+1]
                      #Here I have used functions called insert and del.
                      #Here I used insert function to add number/face of die ata particular position in lists.
                      #Similarly del is used here to remove a particular element at a particular position in list.
                      #Here I have presented the link from where I learnt this from.
                      #https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/

               cout+=1

           print ( "\n" + "Now you have rolled: " + str(lists) + "\n")



           #average value
           #initializing all variables below.
           bonusFactor1= 0
           bonusFactor2= 0
           bonusFactor3= 0
           bonusFactor4= 0
           bonusFactor5= 0
           su_m=0
           maxScore=0
           average_sum=0
                  
           su_m = sum(lists)
           average_sum = average(lists)

           print("These die sums to "+ str(su_m) + " have an average rounded value of "+ \
                   str(average_sum))

           #calculating maximum Score
           percentage = calculatePercentage(face,dice,lists)
           maxScore=face*dice

           listz =[ ]
           
           bonusFactor1 = pattern1(face,lists)

           listz.append(bonusFactor1)
           
           #pattern 2 
           validity = isPrime(su_m)

           bonusFactor2 =pattern2(maxScore,su_m,listz)

           listz.append(bonusFactor2)
                 
           #pattern 3


           bonusFactor3 = pattern3(lists)

           listz.append(bonusFactor3)


           #pattern 4
           pattern = 0
           count = 0
           bonusFactor4 = pattern4(face,lists)
           listz.append(bonusFactor4)


           #pattern 5
           
           if sum(listz) > 0:
               bonusFactor5 = 0
               print("Since you matched a pattern, pattern 5 is not matched!")

           else:
               bonusFactor5 =1
               print("Since no pattern matched, therefore pattern 5 matched!! ")

           listz.append(bonusFactor5)

           #total bonus factor
           totalBonus = bonusFactor(face, dice, listz )
           print("Your bonus factor is " + str(totalBonus))

           #score

           Score = score(percentage, totalBonus , lists)
           print("These dice are worth " + str(Score) + " points." + "\n")
           averageScore.append(Score)

else:
       #score
       print("Your score was " +str(max(averageScore)) + " on turn " + str(gamePlay)+" . " + "\n")
       


###################################################################
#above line is to given to improve readability.
       

print("\n" +"This was your first turn!! Let's Go Again!! " + "\n")

#############################################

#loop for the second and many plays to continue.
play = False
while not play:

    gamePlay+=1

    #random numbers
    lists = [ ]
    face = int(face)
    count = 0
    while count < int(dice):
        diceRolls=rollDie(face)
        lists.append(diceRolls)
        count+=1


    print ("\n" +"You have rolled: " + str(lists) +"\n")
    
    #average value
    su_m = sum(lists)
    average_sum = average(lists)

    print("These die sums to "+ str(su_m) + " have an average rounded value of "+ \
          str(average_sum))

    #calculating maximum Score
    percentage = calculatePercentage(face,dice,lists)

    maxScore=face*dice

    
    #listz that contains all values of bonus factor in it.
    listz =[ ]
    
    #pattern 1
    bonusFactor1 = pattern1(face,lists)

    listz.append(bonusFactor1)


    #pattern 2 
    validity = isPrime(su_m)

    bonusFactor2 =pattern2(maxScore,su_m,listz)

    listz.append(bonusFactor2)
    

    #pattern 3

    bonusFactor3 = pattern3(lists)

    listz.append(bonusFactor3)


    #pattern 4
    
    bonusFactor4 = pattern4(face,lists)

    listz.append(bonusFactor4)


    #pattern 5
    if None in listz:
        listz.remove(None)

    bonusFactor5 = 0

    if sum(listz) > 0:
        bonusFactor5 = 0
        print("Since you matched a pattern, pattern 5 is not matched!")

    else:
        bonusFactor5 =1
        print("Since no pattern matched, therefore pattern 5 matched!! ")

    listz.append(bonusFactor5)

    #total bonus factor
    totalBonus = bonusFactor(face, dice, listz )
    print("Your bonus factor is " + str(totalBonus))

    #score

    Score = score(percentage, totalBonus , lists)
    print("These dice are worth " + str(Score) + " points." + "\n")

    averageScore.append(Score)


#########################################################
##above line is to given to improve readability.

    
    user_input = input("Do you want to reroll any dice ? [ 'yes' , 'no'] :  ")

    while not (user_input.upper()=="YES" or user_input.upper()=="NO"):

        print("I'm sorry, the choices are [ 'yes' , 'no' ]. Please pick one of them.  ")
        user_input = input("Do you want to reroll any dice?['yes' , 'no']:  ")

    count = 0
    lists1 = [ ]
    if user_input.upper()=="YES":
        

        while count < len(lists):

            diceInput = input("Do you want to reroll this die? (was " + str(lists[count]) +" ) ['y' , 'n']  " )
    
            while not (diceInput.upper() == "Y" or diceInput.upper() =="N"):
                print("I'm sorry, the choices are [ 'y' , 'n' ]. Please pick one of them.  ")
                diceInput = input("Do you want to reroll this die? (was " + str(lists[count]) +" ) ['y' , 'n']  " )

            if diceInput.upper() == "N":
                lists1.append(False)

            else:
                lists1.append(True)

            count+=1

            
        cout = 0
        while cout < len(lists1):
            if lists1[cout]==True:
                diceRolls=rollDie(face)
                lists.insert(cout, diceRolls)
                del lists[cout+1]

            cout+=1

        print("Your score of " + str(max(averageScore)) + " on turn " + str(gamePlay)+" was average compared to other turns today.")
        print ( "\n" + "Now you have rolled: " + str(lists) + "\n")



        
        #average value
        bonusFactor1= 0
        bonusFactor2= 0
        bonusFactor3= 0
        bonusFactor4= 0
        bonusFactor5= 0
        su_m=0
        maxScore=0
        average_sum=0
    
        su_m = sum(lists)
        average_sum = average(lists)

        print("These die sums to "+ str(su_m) + " have an average rounded value of "+ \
                str(average_sum))

        #calculating maximum Score
        percentage = calculatePercentage(face,dice,lists)
        maxScore=face*dice
        #listz that contains all values of bonus factor in it.

        listz =[ ]
    
        bonusFactor1 = pattern1(face,lists)

        listz.append(bonusFactor1)
    
        #pattern 2 
        validity = isPrime(su_m)

        bonusFactor2 =pattern2(maxScore,su_m,listz)

        listz.append(bonusFactor2)
          
        #pattern 3


        bonusFactor3 = pattern3(lists)

        listz.append(bonusFactor3)


        #pattern 4
        pattern = 0
        count = 0
        bonusFactor4 = pattern4(face,lists)
        listz.append(bonusFactor4)


        #pattern 5
    
        if sum(listz) > 0:
            bonusFactor5 = 0
            print("Since you matched a pattern, pattern 5 is not matched!")

        else:
            bonusFactor5 =1
            print("Since no pattern matched, therefore pattern 5 matched!! ")

        listz.append(bonusFactor5)

        #total bonus factor
        totalBonus = bonusFactor(face, dice, listz )
        print("Your bonus factor is " + str(totalBonus))

        #score

        Score = score(percentage, totalBonus , lists)
        print("These dice are worth " + str(Score) + " points." + "\n")

        averageScore.append(Score)



    elif user_input.upper()=="NO":
        print("Your score of " +str(max(averageScore)) + " points on turn " + str(gamePlay)+" was average comapared to other turns today.")
        askAgain =input("Would you like to play another turn? [ 'y' , 'n' ]:  ")

        while not (askAgain.upper()=="Y" or askAgain.upper()=="N"):

            print("I'm sorry, the choices are [ 'y' , 'n' ]. Please pick one of them.  ")
            askAgain = input("Would you like to play another turn? ['y' , 'n']:  ")

        if askAgain.upper()=="N":

            play= True
            #if no then exits loop.

        elif askAgain.upper()=="Y":

            play = False
            #if yes then goes again in the loop.

##########################################
#above line is to given to improve readability.

#At last, showing the number of turns and average of all scores.
totalAverage = round(average(averageScore),0)
print("\n"+"You Played " + str(gamePlay) + " turns today with an average score of " + str(totalAverage) +" points." )        

            

         

