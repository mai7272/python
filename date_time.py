from datetime import datetime

#Question1
mai_date = datetime.now()

#Question2'

current_time_date = mai_date.strftime("%d:%m:%y %H:%M:%S")
print("Current Date,Time =", current_time_date)

current_year = mai_date.strftime("%Y")
print ("Current year =", current_year)

current_MonthName = mai_date.strftime("%B")
print ("Current month name =", current_MonthName)

current_DayName = mai_date.strftime("%A")
print ("Current day name =", current_DayName)

#Question3
print("")
current_DayOfYear = mai_date.strftime("%j")
print ("The day number of the year =", current_DayOfYear)
print (".... 001 is frist day in the year , 366 last day in the year ....")

#Question4
print("")
current_WeekOfYear = mai_date.strftime("%U")
print ("The week number of the year =", current_WeekOfYear)
print ("Sunday as frist day of the week")
print (".... 00 is frist week in the year , 53 is last week in the year ....")

