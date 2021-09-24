import pandas as pd
df = pd.read_json (r'C:\Users\Erica\OneDrive\Ambiente de Trabalho\Efrei\Python\hi-python\ex01_json2csv\Data.json')
df.to_csv (r'C:\Users\Erica\OneDrive\Ambiente de Trabalho\Efrei\Python\hi-python\ex01_json2csv\Data.csv', index = None)
print("fichier convertie")