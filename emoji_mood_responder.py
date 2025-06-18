mood_responses = {
    "happy": ("😊", "Glad to hear you’re happy! Keep smiling!"),
    "sad": ("😢", "It's okay to feel sad sometimes. Better days are coming!"),
    "angry": ("😡", "Take a deep breath. It will get better!"),
    "excited": ("🤩", "Woohoo! Keep up the good vibes!"),
    "tired": ("😴", "You should get some rest. Take care!"),
    "confused": ("😕", "It’s okay, things will clear up soon!")
}

mood = input("How are you feeling today? ").lower()

if mood in mood_responses:
    emoji, message = mood_responses[mood]
    print(f"{emoji} {message}")
else:
    print("🤗 I may not understand that mood, but I hope you have a great day!")