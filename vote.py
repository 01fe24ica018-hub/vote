def check_voter_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")


check_voter_eligibility()
