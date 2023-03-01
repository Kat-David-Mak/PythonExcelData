import pandas as pd

read_file = pd.read_excel('Basotho_food_Class.xlsx',sheet_name='Sheet1')
read_file.to_csv('Basotho_Food_CSV.csv', index=None, header=True)
basotho_data = pd.read_csv('Basotho_Food_CSV.csv')
#display the first five rows 
print(basotho_data.head()) 
#display all rows 
print(basotho_data) 