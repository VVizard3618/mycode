import random

# Define the global dictionary of bender types and traits
bender_types = {
    "Water": ["adaptive", "calm", "resourceful", "compassionate", "flexible", "intuitive", "supportive",
              "empathetic", "nurturing", "reflective", "peaceful", "patient", "harmonious", "diplomatic",
              "healing", "resilient", "observant", "gentle", "caring", "meditative"],

    "Earth": ["strong-willed", "stubborn", "resilient", "dependable", "grounded", "practical", "persistent",
              "unyielding", "determined", "loyal", "courageous", "honest", "direct", "stable", "independent",
              "disciplined", "realistic", "protective", "hard-working", "responsible"],

    "Fire": ["passionate", "intense", "driven", "ambitious", "bold", "energetic", "confident", "courageous",
             "quick-tempered", "determined", "competitive", "charismatic", "assertive", "strong-minded",
             "willful", "powerful", "impulsive", "focused", "daring", "adventurous"],

    "Air": ["peaceful", "free-spirited", "easygoing", "creative", "wise", "humble", "optimistic", "light-hearted",
            "flexible", "playful", "detached", "tranquil", "patient", "open-minded", "insightful", "adventurous",
            "non-judgmental", "spiritual", "curious", "joyful"]
}


# Function to let the user choose a general bender type
def choose_bender_type():
    print("Choose the bender type that you feel resonates most with your personality.")
    print("1. Water - Calm, adaptable, and compassionate.")
    print("2. Earth - Strong-willed, dependable, and grounded.")
    print("3. Fire - Passionate, ambitious, and bold.")
    print("4. Air - Free-spirited, peaceful, and open-minded.")

    while True:
        try:
            choice = int(input("Enter the number of the bender type that resonates most with you (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


# Function to suggest traits based on the chosen bender type
def suggest_traits(bender_choice):
    bender_names = ["Water", "Earth", "Fire", "Air"]
    chosen_bender = bender_names[bender_choice - 1]
    traits = bender_types[chosen_bender]

    # Randomly select 3 traits to display to the user
    selected_traits = random.sample(traits, 3)
    print(f"Here are some traits often associated with {chosen_bender} benders:")
    print(", ".join(selected_traits))

    # Ask if the user resonates with any of these traits
    response = input("Do any of these traits resonate with you? (yes/no): ").strip().lower()
    if response == "yes":
        return chosen_bender
    elif response == "no":
        print("Let's try again or choose a different type.")
        return None
    else:
        print("Please answer with 'yes' or 'no'.")
        return None


# Main function to run the program
def main():
    print("Welcome to the Bender Type Finder!")
    while True:
        choice = choose_bender_type()
        bender_type = None

        # Continue suggesting traits until the user confirms a match or changes their choice
        while bender_type is None:
            bender_type = suggest_traits(choice)

            if bender_type:
                print(f"Based on your responses, you might be a {bender_type} bender!")
            else:
                retry = input("Would you like to try a different bender type? (yes/no): ").strip().lower()
                if retry == "yes":
                    choice = choose_bender_type()
                elif retry != "no":
                    print("Please answer with 'yes' or 'no'.")

        # Ask if the user wants to try again
        retry = input("Would you like to try for a different type? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thank you for using the Bender Type Finder!")
            break


# Run the program
if __name__ == "__main__":
    main()

