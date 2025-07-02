import datetime
import os

def notify(title, message):
    message = message.replace('"', '\\"')
    title = title.replace('"', '\\"')
    os.system(f'''
          osascript -e 'display notification "{message}" with title "{title}"'
    ''')

festivals = {
    "Diwali": "2025-10-29",
    "Dussehra": "2025-10-02",
    "Christmas": "2025-12-25",
    "New Year": "2026-01-01"
}

today = datetime.date.today()
print("📅 Today's Date:", today)
print("\n🎊 Upcoming Festivals:\n")

for name, date_str in festivals.items():
    fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    days_left = (fest_date - today).days

    if days_left > 0:
        print(f"📌 {name} is in {days_left} day(s) — on {fest_date}")
        if days_left in [1, 3, 5, 7]:
            notify(f"⏰ Upcoming Festival: {name}", f"{days_left} day(s) left until {name} 🎊")
    elif days_left == 0:
        print(f"🎉 Reminder: Today is {name}!")
        notify(f"🎉 {name} Today!", "Celebrate and enjoy the day! 🎊")

add = input("\nDo you want to add a new festival? (yes/no): ").lower()
if add == "yes":
    try:
        fest_name = input("Enter festival name: ")
        fest_date = input("Enter date (YYYY-MM-DD): ")
        datetime.datetime.strptime(fest_date, "%Y-%m-%d")
        festivals[fest_name] = fest_date
        print(f"✅ '{fest_name}' added successfully!")
        notify("🆕 Festival Added", f"{fest_name} on {fest_date}")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD.")
