from openpyxl import load_workbook

# 1-Lê pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatório"]

# 2-Acessando um valor específico
print(sheet["A3"].value)
print(sheet["B3"].value)

# 3-