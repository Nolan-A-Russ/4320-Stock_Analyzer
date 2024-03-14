import requests
import pygal
import webbrowser
from lxml import html
from datetime import datetime

api_key = "

#Getting Stock Symbol

stk_symbl = input("Enter the stock symbol: ")

#Getting Chart Type
while True;
  print("\n----------Chart Type----------\n------------------\n 1) Bar\n 2) Line\n")
  chrt_type = input("Enter Chart Type 1) Bar chart\n2) Line chart")
  if chrt_type in ["1", "2"]:
      break
  else:
    print("\nInvalid Input\n")

#Getting Time Series
while True:
    print("\n-----------Time Series-----------\n ----------------------\n 1) Intraday\n 2) Daily\n 3) Weekly\n 4) Monthly\n")
    usr_time_series = input("Enter time series:\n 1\n 2\n 3\n 4\n Selection: ")
    if usr_time_series in ["1","2","3","4"]:
        break
    else: 
        print("\nInvalid Input\n")

if usr_time_series == "1":
    T_series = "Time_Series_Intraday"
    T_series_output = "Time Series (5min)"
if usr_time_series == "2":
    T_series = "Time_Series_Daily"
    T_series_output = "Time Series (Daily)"
if usr_time_series == "3":
    T_series = "Time_Series_Weekly"
    T_series_output = "Weekly Time Series"
if usr_time_series == "4":
    T_series = "Time_Series_Monthly"
    T_series_output = "Monthly Time Series"
# Start Date
while True:
    start_date = input("\nEnter start date (YYYY-MM-DD): ")
    try:
        datetime.strptime(start_date, '%Y-%M-%d')
        break
    except ValueError:
          print("\nInvalid date format. Please use YYYY-MM-DD format.")
        
# End Date

