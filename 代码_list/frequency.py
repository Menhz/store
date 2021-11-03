from collections import Counter
import pandas as pd
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
list_frequency = Counter(List)
print(list_frequency)

list_frequency_2 = pd.value_counts(List)

print('-'*30)
print(list_frequency_2)