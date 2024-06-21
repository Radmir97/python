import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head()) # Исходный

# Перевод в one hot вид
one_hot = pd.DataFrame()

for category in data['whoAmI'].unique():
    one_hot[category] = (data['whoAmI'] == category).astype(int)

print("\nOne hot DataFrame:")
print(one_hot.head()) # Итог
