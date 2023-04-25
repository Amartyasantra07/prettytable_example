from prettytable import PrettyTable

columns = ["Student Name", "Class", "Section", "Percentage"]

myTable = PrettyTable()

# Add Columns
myTable.add_column(columns[0], ["Amartya", "Snehasish", "Ram",
                                "Shyam", "Jodu", "Raj", "Modhu"])
myTable.add_column(columns[1], ["Xii", "Xii", "Xii", "Xii", "Xii", "Xii", "Xii"])
myTable.add_column(columns[2], ["B", "C", "A", "D", "A", "B", "B"])
myTable.add_column(columns[3], ["91.2 %", "63.5 %", "90.23 %", "92.7 %",
                                "98.2 %", "88.1 %", "95.0 %"])

print(myTable)