# accept user name

print("hello world")
name = input("Emter your name?: ")
# accept user math score
maths_score = int(input("Enter your maths result: "))
#accept user bcs score
bcs_score = int(input("Enter your bcs result: "))
# accept user ict score
ict_score = int(input("Enter your ict result: "))

# calculate total and average scores;
total = maths_score + bcs_score + ict_score
average_score = total/ 3

#print the results
print(f"Name: {name}")
print(f"Total: {total}")

print(f"Avearage score: {round(average_score, 1)}")
