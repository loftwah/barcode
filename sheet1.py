import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from tkinter.ttk import Notebook

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
database = client.open("database").sheet1
customer = client.open("customer").sheet1
billing = client.open("billing").sheet1


def ui():
    w = 0
    c = 0
    k = 0
    root = Tk()
    root.title("Product Details")
    root.geometry("700x450+0+0")
    frame2 = Frame(root)
    frame2.pack(fill="both")


    tablayout = Notebook(frame2)

    tab1 = Frame(tablayout)
    tab1.pack(fill="both")
    for w in range(1, r + 2):
        newrow = customer.row_values(w)
        k = 1
        for c in newrow:
            Label(tab1, text=c, width=15, bg="white", fg="black", padx=3, pady=3).grid(row=w, column=k, sticky="nsew", padx=1, pady=1)
            # Entry(tab1, bg=c, width=10).grid(row=r,column=1)
            k = k + 1
    Label(tab1, text="Total Amount", width=15, bg="white", fg="black", padx=3, pady=3).grid(row=w + 1, column=k - 6,
                                                                                            sticky="nsew", padx=1,
                                                                                            pady=1)
    Label(tab1, text=sum, width=15, bg="white", fg="black", padx=3, pady=3).grid(row=w + 1, column=k - 5, sticky="nsew",
                                                                                 padx=1, pady=1)
    tablayout.add(tab1)
    tablayout.pack(fill="both")
    root.mainloop()

while True:
    sum = 0
    newrow = 0
    barcode = input("scan barcode: ")
    cell = database.find(barcode)
    newrow = database.row_values(cell.row)
    billing.append_row(newrow)
    customer.append_row(newrow)
    rows = customer.get_all_records()
    r = len(rows)
    # print(r)
    for a in range(2, r + 2):
        sum = sum + int(customer.cell(a, 2).value)
    ui()
