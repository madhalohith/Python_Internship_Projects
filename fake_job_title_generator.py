import random

adjectives = ["Senior", "Certified", "Dynamic", "Innovative", "Global", "Virtual", "Elite", "Strategic", "Chief"]
roles = ["Meme", "Unicorn", "Ninja", "Happiness", "Synergy", "Cloud", "Brand", "AI", "Marketing"]
suffixes = ["Engineer", "Strategist", "Consultant", "Guru", "Manager", "Specialist", "Architect"]

def generate_job_title():
    adj = random.choice(adjectives)
    role = random.choice(roles)
    suffix = random.choice(suffixes)
    return f"{adj} {role} {suffix}"

while True:
    print("\nYour fake job title is:", generate_job_title())
    another = input("Do you want another one? (yes/no): ").lower()
    if another != "yes":
        print("Good luck with your new fake career! 🚀")
        break
