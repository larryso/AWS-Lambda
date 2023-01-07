import pandas as pd

wb_permission_excel = pd.ExcelFile(r"../Redshift Permission Template.xlsx")
print(wb_permission_excel.sheet_names)

for sheet_name in wb_permission_excel.sheet_names:
    print(sheet_name)
    if sheet_name == "Group Permission Templete":
        df = pd.read_excel(r"../Redshift Permission Template.xlsx", sheet_name=sheet_name)
        for details in df:
            print(details[0])




