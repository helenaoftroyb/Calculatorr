print("Welcome to the calculator!")
print("!MATH CALCULATOR!")
counter = 0
namem = int(input("Enter your multiples:"))
for i in range(1, 11):
    print(" What is " + str(i) + " x " + str(namem) + " ? ")
    correcta = i * namem
    answer = int(input("Your answer: "))   
    if answer == correcta: 
        print("You did that Gurl") 
        counter += 1 
    else:
        print("Womp, Womp, the correct answer is:", str(correcta))  
print("You scored", str(counter), "out of 10.")
