import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import tkinter as tk

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
database = client.open("database").sheet1
customer = client.open("customer").sheet1
billing =   client.open("billing").sheet1 
 
# Open the spreadhseet
#data = billing.get_all_records()  # Get a list of all records
#row = sheet.row_values(3)  # Get a specific row
#col = sheet.col_values(3)  # Get a specific column
#cell = sheet.cell(1,2).value  # Get the value of a specific cell
##sheet.append_row("row")  # Insert the list as a row at index 4
sum=0
newrow = 0
while True:
	barcode =raw_input("scan barcode: ")
	cell = database.find(barcode)
	newrow= database.row_values(cell.row)
	billing.append_row(newrow)
	customer.append_row(newrow)
	sum= sum +int(customer.cell(cell.row, 2).value)
	pprint(sum)
     	a=len(customer.row_values(1))
	print(a)
	b=len(customer.col_values(1))
	print(b)
	
	
	w = 0
	c = 0
	k=0
		
	for w in range(a):
		newrow =customer.row_values(w+1)
		k=0
		for c in newrow:
			tk.Label(text = c , relief=tk.RIDGE, width=15).grid(row=w,column=k)
			##tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
			k=k+1
	
tk.mainloop() 
