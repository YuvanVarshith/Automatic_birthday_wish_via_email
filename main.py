##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import random
import smtplib

import pandas

EMAIL = "kdyyuvan@gmail.com"
PASSWORD = "hzrvwmuetzxuffpk"

dt = dt.datetime.now()
date, month = dt.day, dt.month

data = pandas.read_csv("birthdays.csv")
for key, value in data.iterrows():
    if date == value["day"] and month == value["month"]:
        with open(file=f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter:
            content = letter.read()
            new_content = content.replace("[NAME]", f"{value['name']}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=value["email"], msg=f"Subject: Happy Birthday {value['name']}\n\n {new_content}")
