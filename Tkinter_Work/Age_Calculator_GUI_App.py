import datetime
from dateutil import relativedelta
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import urllib.request
import io

fd1 = urllib.request.urlopen(
    "https://lh3.googleusercontent.com/qx26xfG5iVcAH1zakfNCJUGWYFcC9T_BLgE2b4cXmKiHISAt9qWSejwRb8Hau10NqQ=h900")
image_file1 = io.BytesIO(fd1.read())

# creating the frame
window = tk.Tk()
window.geometry("330x550")
window.title("AGE CALCULATOR APP")

# creating labels and entry fields
welcome_label = tk.Label(text="Welcome!!!")
welcome_label.grid(column=1, row=0)

first_label = tk.Label(text="Enter Your Full Name and Birthdate")
first_label.grid(column=1, row=2)

name_label = tk.Label(text=" Your Name: ")
name_label.grid(column=0, row=3)
name_entry = tk.Entry()
name_entry.grid(column=1, row=3)

year_label = tk.Label(text="Year: ")
year_label.grid(column=0, row=4)
year_entry = tk.Entry()
year_entry.grid(column=1, row=4)

month_label = tk.Label(text="Month: ")
month_label.grid(column=0, row=5)
month_entry = tk.Entry()
month_entry.grid(column=1, row=5)

day_label = tk.Label(text="Day: ")
day_label.grid(column=0, row=6)
day_entry = tk.Entry()
day_entry.grid(column=1, row=6)

text_answer = tk.Text(master=window, height=10, width=25)
text_answer.grid(column=1, row=8)


# function to show output and gather details
def calculate_age():
    date_of_birth = datetime.date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    your_name = name_entry.get()
    your_details = Person(your_name, date_of_birth)
    text_answer.delete("1.0", tk.END) # to delete previous text in the box
    text_answer.insert(tk.END, "{} is {} old!!!!".format(your_details.name, your_details.age()))  # shows output in box


# creating calculate button
calculate_button = tk.Button(text="Calculate Now!!", command=calculate_age)
calculate_button.grid(column=1, row=7)


# class for actually calculating the age
class Person:
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB

    def age(self):  # to calculate age
        self.todays_date = datetime.date.today()
        self.difference = relativedelta.relativedelta(self.todays_date,
                                                      self.DOB)  # outputs difference in years, months and days
        return "{} years, {} months and {} days".format(self.difference.years,
                                                        self.difference.months,
                                                        self.difference.days)
        # for extra knowledge
        # self.years=self.difference.years  # returns only years
        # self.months=self.difference.months
        # self.days=self.difference.days
        # months=difference.years*12 + difference.months  # for age in months only
        # print(months)
        # ageindays = todays_date-birthdate     # for age in days only
        # print(ageindays.days)


# for images
image1 = Image.open(image_file1)
image1.thumbnail((150, 150), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
label_image1 = tk.Label(image=photo1)
label_image1.grid(column=1, row=1)


# extra stuff
# blog label
def my_blog(event):
    webbrowser.open_new_tab("https://programmedtocode.wordpress.com")


myblog_label = tk.Label(text="My Blog:")
myblog_label.grid(column=0, row=10)
myblog = tk.Button(text="programmedtocode.com")
myblog.grid(column=1, row=10)
myblog.bind("<Button-1>", my_blog)


# github label
def click_for_github(event):
    webbrowser.open_new_tab("https://github.com/ineffablelucky")


github_label = tk.Label(text="GitHub:")
github_label.grid(column=0, row=11)
github = tk.Button(text="ineffablelucky")
github.grid(column=1, row=11)
github.bind("<Button-1>", click_for_github)

window.mainloop()
