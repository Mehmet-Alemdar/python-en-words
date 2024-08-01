import pandas as pd
import os
from datetime import datetime

text = """
apple - elma
"""

lines = text.strip().split('\n')

words_before_dash = []
words_after_dash = []

for line in lines:
    if "-" in line:
        parts = line.split(" - ")
        words_before_dash.append(parts[0].strip())
        words_after_dash.append(parts[1].strip())
    else:
        words_before_dash.append(line.strip())
        words_after_dash.append('')

# DataFrame oluştur
df_new = pd.DataFrame({
    'İngilizce': words_before_dash,
    'Türkçe': words_after_dash
})

os.makedirs('words', exist_ok=True)

file_name = 'words/en-words.xlsx'

if os.path.exists(file_name):
    df_existing = pd.read_excel(file_name)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
else:
    df_combined = df_new

df_combined.to_excel(file_name, index=False)

print(f"Excel dosyası {file_name} olarak güncellendi.")
