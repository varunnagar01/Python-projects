'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# logical Operators
# if we use "and" operator both condition A and B should be True

# if we use "or" operator A can be true and B can be false or vice versa

# if we use "not"operator then we can the result
# Love Calculator

print("welcome to the print calculator!")
name_1=input("what is your name?\n")
name_2=input("what is name?\n")

combined_string= name_1+name_2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true=t+r+u+e

L=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love=L+o+v+e

love_score=int(str(true) + str(love))


if (love_score<10) or (love_score>90):
    print(f"you score is {love_score}, you go together like coke and mentos")
elif(love_score>40)and(love_score<55):
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")
    
