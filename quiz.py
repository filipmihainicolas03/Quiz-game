print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("OK, byebye :(")
    quit()

print("Yey! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM stand for? ").lower()
if answer == "read-only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does LAN stand for? ").lower()
if answer == "local area network":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does HTTP stand for? ").lower()
if answer == "hypertext transfer protocol":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is Python? ").lower()
if answer == "programming language":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is an IDE? ").lower()
if answer == "integrated development environment":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does OOP stand for? ").lower()
if answer == "object-oriented programming":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You answered " + str(score) + " question/s correctly!")
print("And you got " + str((score / 10) * 100) + "%.")