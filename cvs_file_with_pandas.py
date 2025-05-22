import pandas as pd

# Read the CSV file
df=pd.read_csv('students.csv')


# Print the full DataFrame
print("\n student data:\n",df)

#avarage marks 
print("\n average marks :",df['Marks'].mean())

#highest and lowesr marks 

high=df['Marks'].max()
low=df['Marks'].min()
print("\n highest marks :",high)
print("\n lowest marks :",low)

#toppers name 

top=df[df['Marks']==high]['Name'].values[0]
print("\n toppers name :",top)
#lowest marks name  
low=df[df['Marks']==low]['Name'].values[0]
print("\n lowest marks name :",low)
