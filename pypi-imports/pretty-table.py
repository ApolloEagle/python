from prettytable import PrettyTable
# Init table
table = PrettyTable()

# Add columns
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# Change attributes
table.align = 'l'

print(table)
