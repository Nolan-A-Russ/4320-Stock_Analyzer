from datetime import datetime
import requests
from lxml import html
import pygal
import webbrowser

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

if usr_time_series == "2":

if usr_time_series == "3":

if usr_time_series == "4":
  
# Start Date
# End Date

