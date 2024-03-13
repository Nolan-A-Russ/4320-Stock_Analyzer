from datetime import datetime
import requests
from lxml import html
import pygal
import webbrowser

#Get the user information 

#Getting Stock Symbol

stk_symbl = input("Enter the stock symbol: ")

#Getting Chart Type
while True;
  print("\n----------Chart Type----------\n------------------\n 1) Bar\n 2) Line\n")
  chrt_type = input("1) Bar chart\n2) Line chart")
  if chrt_type in ["1", "2"]:
      break
  else:
    print("\nInvalid Input\n")

#Getting Time Series

# Start Date

# End Date

