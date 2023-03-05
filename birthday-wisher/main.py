import smtplib
import datetime as dt
import pandas as pd

# Grab date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays
data = pd.read_csv('birthdays.csv')
birthday_dict = {(data_row["month"], data_row["day"])
                  : data_row for (index, data_row) in data.iterrows()}

# SMTP
email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

# Send birthday wishes
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]["name"]
    birthday_email = birthday_dict[today_tuple]["email"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email,
                            birthday_email,
                            msg=f'Subject:Happy Birthday!!\n\nHappy Birthday {birthday_person}!! I hope you have a great day!')
