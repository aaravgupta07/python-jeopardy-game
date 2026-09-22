points = 0

print("          WELCOME TO JEOPARDY!")
print()
print("Categories:")
print("  1 - Science")
print("  2 - History")
print()
print("Point Values:")
print("  200 points")
print("  400 points")
print()
print("Enter 3 at any time to quit the game.")
print("=" * 40)

user_choice_cat = int(input("Choose a category (1 or 2): "))

while user_choice_cat != 3:

    while user_choice_cat != 1 and user_choice_cat != 2 and user_choice_cat != 3:
        print("Invalid choice. Please enter 1, 2, or 3.")
        user_choice_cat = int(input("Choose a category (1 or 2): "))

    if user_choice_cat == 3:
        print()
        print("Thank you for playing Jeopardy!")
        print("Your final score is:", points)
        break

    user_choice_points = int(input("Choose a point value (200 or 400): "))

    while user_choice_points != 200 and user_choice_points != 400:
        print("Invalid point value. Please enter 200 or 400.")
        user_choice_points = int(input("Choose a point value (200 or 400): "))

    if user_choice_cat == 1:
        if user_choice_points == 200:
            user_answer = input("What planet is known as the Red Planet? ")

            if user_answer.lower() == "mars":
                points = points + user_choice_points
                print("Correct! You earned", user_choice_points, "points.")
            else:
                print("Wrong answer, try again!")

        elif user_choice_points == 400:
            user_answer = input("What gas do humans need to breathe? ")

            if user_answer.lower() == "oxygen":
                points = points + user_choice_points
                print("Correct! You earned", user_choice_points, "points.")
            else:
                print("Wrong answer, try again!")

    if user_choice_cat == 2:
        if user_choice_points == 200:
            user_answer = input("Who was the first President of the United States? ")

            if user_answer.lower() == "george washington":
                points = points + user_choice_points
                print("Correct! You earned", user_choice_points, "points.")
            else:
                print("Wrong answer, try again!")

        elif user_choice_points == 400:
            user_answer = input("In which year did World War II end? ")

            if user_answer.lower() == "1945":
                points = points + user_choice_points
                print("Correct! You earned", user_choice_points, "points.")
            else:
                print("Wrong answer, try again!")

    print()
    print("Current score:", points)
    print()

    user_choice_cat = int(input("Choose another category (1 or 2), or type 3 to quit: "))

    if user_choice_cat == 3:
        print()
        print("Thank you for playing Jeopardy!")
        print("Your final score is:", points)

print()
print("Game over!")
