import pandas as pd
df = pd.read_csv('Cryptocurrency Dataset.csv')
n = 0
for i in df['Name']:
    a = int(len(i)/2)
    b = ''
    for j in range(a):
        b += i[j]
    df.loc[n, 'Name'] = b
    n+=1
print(df)
df.to_csv("Cryptocurrency Dataset.csv", index=False)
