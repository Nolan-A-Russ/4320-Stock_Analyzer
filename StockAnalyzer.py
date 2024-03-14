import requests
import pygal
import webbrowser
from lxml import html
from datetime import datetime



#Getting Stock Symbol

stk_symbl = input("Enter the stock symbol: ")

#Getting Chart Type
while True;
  print("\n----------Chart Type----------\n------------------\n 1) Line\n 2) Bar\n")
  chrt_type = input("Enter Chart Type 1) Line chart\n2) Bar chart")
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
    start_date = input("\nEnter Start Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        break
    except ValueError:
          print("\nInvalid date format. Please use YYYY-MM-DD format.")
        
# End Date
while True:
    end_date = input("\nEnter End Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(end_date, '%Y,%m,%d')
            if end_date >= start_date:
                break
            else:
                print("The end date shound't be before the start date")
        except ValueError:
            print("\nInvalid date format. Please use YYYY-MM-DD format")

print(stk_symbl, chrt_type, T_series, start_date, end_date)

api_key = "QGB4RG9L7AWT1713"

url = f'https://www.alphavantage.co/query?function={T_series}&symbol={stk_symbl}&apikey={api_key}'

response = requests.get(url)
data = response.json()
print(data)

#Creating Line Graph

#Creating Bar Graph


