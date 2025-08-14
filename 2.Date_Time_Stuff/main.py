import datetime,bday_messages
today_date = datetime.date.today()
next_birthday = datetime.date(2003, 2, 7)
days_away = today_date - next_birthday
if today_date == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My birthday is {days_away} days away!")