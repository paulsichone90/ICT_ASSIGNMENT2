



name = input("Emter your name?: ")
maths_score = int(input("Enter your maths result: "))

bcs_score = int(input("Enter your bcs result: "))

ict_score = int(input("Enter your ict result: "))

total = maths_score + bcs_score + ict_score
average_score = total/ 3

print(f"Name: {name}")
print(f"Total: {total}")

print(f"Avearage score: {round(average_score, 1)}")