import random

first = input("Enter your first name: ")
last = input("Enter your last name: ")

nicknames = [
    first[:3] + last[-3:],
    last[:3] + first[-3:],
    first.capitalize() + last.lower(),
    first[0].upper() + "_" + last,
    first[::-1] + last,
    first + str(random.randint(10, 99)),
    first + "_" + last + "_x",
    first[:2].upper() + last[-2:].lower(),
    first + last[0] + str(random.randint(100, 999))
]

style = input("Preferred style? (short / fun / formal / any): ").lower()

if style == "short":
    nicknames = [n for n in nicknames if len(n) <= 8]
elif style == "formal":
    nicknames = [first.capitalize() + " " + last.capitalize()]

print("\n🎉 Your Nickname Suggestions:")
for name in nicknames:
    print("🔹", name)

save = input("\nDo you want to save these nicknames to a file? (yes/no): ").lower()
if save == "yes":
    with open("nicknames.txt", "w") as f:
        for name in nicknames:
            f.write(name + "\n")
    print("✅ Saved to nicknames.txt!")
