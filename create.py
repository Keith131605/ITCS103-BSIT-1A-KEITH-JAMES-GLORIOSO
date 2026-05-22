import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active


sheet['A1'] = "Order ID"
sheet['A2'] = 1
sheet['A3'] = 2
sheet['A4'] = 3
sheet['A5'] = 4
sheet['A6'] = 5

sheet['B1'] = "Costumer Name"
sheet['B2'] = "Juan Dela Cruz"
sheet['B3'] = "Maria Santos"
sheet['B4'] = "Carlo Reyes"
sheet['B5'] = "Angela Lopez"
sheet['B6'] = "Kevin Ramos"

sheet['C1'] = "Product"
sheet['C2'] = "Burger"
sheet['C3'] = "Fries"
sheet['C4'] = "Pizza"
sheet['C5'] = "Milktea"
sheet['C6'] = "Spaghetti"

sheet['D1'] = "Quantity"
sheet['D2'] = 2
sheet['D3'] = 3
sheet['D4'] = 1
sheet['D5'] = 4
sheet['D6'] = 2

sheet['E1'] = "Price"
sheet['E2'] = 75
sheet['E3'] = 50
sheet['E4'] = 350
sheet['E5'] = 120
sheet['E6'] = 95

sheet['F1'] = "Total"
sheet['F2'] = 150
sheet['F3'] = 150
sheet['F4'] = 350
sheet['F5'] = 480
sheet['F6'] = 190

workbook.save("ordersDB.xlsx")