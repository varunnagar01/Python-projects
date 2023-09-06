'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
'''




print("Welcome to the Treasure island!\nyour mission is to find the road. ")
road=input("You are at a cross road.Where do you want to go? left or right\n")
if road == "left":
    across=input ("you come to a lake.There is an island in the middle of the lake.type 'wait' to wait for a boat.type 'swim' to swim across.\n")
    if across=="wait":
        
       door=input("you have arrived at island unharmed. There is a house with 3 doors.one red,one yellow,one blue.which door would you choose?\n")
       if door=="red":
          print("your room is on fire.game over")
       elif door=="yellow":
          print("you win!!")
       elif door=="blue":
          print("you room is full of beasts.game over")
       else:
          print("you fell into a hole.game over")
    else:
        print("you are attacked by lion.game over")
        
else:
    print("the road is blocked.game over")
