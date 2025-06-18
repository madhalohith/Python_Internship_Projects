# fake_job_title_generator.py

import random

# Step 1: Create lists of adjectives, roles, and suffixes
adjectives = ["Senior", "Certified", "Dynamic", "Innovative", "Global", "Virtual", "Elite", "Strategic", "Chief"]
roles = ["Meme", "Unicorn", "Ninja", "Happiness", "Synergy", "Cloud", "Brand", "AI", "Marketing"]
suffixes = ["Engineer", "Strategist", "Consultant", "Guru", "Manager", "Specialist", "Architect"]

# Function to generate a fake job title
def generate_job_title():
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adj} {role} {suffix}"

# Step 4: Main loop
while True:
    print("\nYour fake job title is:", generate_job_title())
    another = input("Do you want another one? (yes/no): ").lower()
    if another != "yes":
        print("Good luck with your new fake career! 🚀")
        break

