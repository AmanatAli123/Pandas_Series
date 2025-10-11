import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\pandas series\\RealEstate-USA.csv')
print(df)
# # info() method tell us about the dataframe
print(df.info())
# # dtypes tell about the datatype of each column
print(df.dtypes)
# # describe method tell us about the statistical summary of the dataframe
print(df.describe())
# # shape tell us about the number of rows and columns
print(df.shape)
# # to string method print the entire dataframe
print(df.to_string())
# # now we are using the head() method to print the first 7 columns of the dataframe
print(df.head(7))
# # now we using the tail() method to print the last 9 rows of the dataframe
print(df.tail(9))
# # now we are accessing the whole column by using the name of the column
print(df['city'].to_string())
# # now we are accsssing the other column of the dataframe as per using the name of the column
print(df['street'].to_string())
# now we are accessing the multiple columns of the dataframe by using the only one line
print(df[['street','city']].to_string())


# now we are using the loc and the iloc method to access the rows and the columns of the dataframe
# loc mehtod is used to access the rows and the columns by using the index and the name of the column

# Selecting a single row using .loc 
# With index value 5 , print the returned row and analyze results. 
print(df.loc[5])

# Selecting multiple rows using .loc 
# With index –  value 3 and 5 , 7  , print the returned rows and analyze results. 
print(df.loc[[3,5,7]])

# Selecting a slice of rows using .loc 
# With index – value range of 3 and 9, print the returned row and analyze results. 
print(df.loc[3:9])

# Conditional selection of rows using .loc 
# “price” greater then “100000” 
# , print the returned row and analyze results. 
print(df.loc[df['price']>100000])


# Conditional selection of rows using .loc 
# “city” equal to “Adjuntas” 
# , print the returned row and analyze results. 
print(df.loc[df['city']=='Adjuntas'])


# Conditional selection of rows using .loc 
# “city” equal to “Adjuntas” and “price” is equal to - less then 180500 
# , print the returned row and analyze results. 
print(df.loc[(df['city']=='Adjuntas')  & (df['price']<180500 )])

# Selecting a single column using .loc 
# With index value 7 , only select following columns 
# “city”,”price” , ”street” , ” zip_code” , ” acre_lot” 
# , print the returned row and analyze results. 
print(df.loc[7,['city','price','street','zip_code','acre_lot']])


# Selecting a slice of columns using .loc 
# Form “city” to “zip_code” 
# , print the returned row and analyze results. 
print(df.loc[:,'city':'zip_code'])

# Combined row and column selection using .loc 
# “city” equal to “Adjuntas” and Form “city” to “zip_code” 
# , print the returned row and analyze results. 
print(df.loc[df['city']=='Adjuntas','city':'zip_code' ])

# now the stage of iloc method begins
# iloc method is used to access the rows and the columns by using the index of the rows and the columns

# Selecting a single row using .iloc 
# Select 5th row 
#  print the returned row and analyze results. 
print(df.iloc[5])


# Selecting multiple rows using .iloc 
# Select – 7th row, 9th row and 15th row 
# , print the returned row and analyze results. 
print(df.iloc[[7,9,15]])


# Selecting a slice of rows using .iloc 
# Select from 5th to 13th row 
# , print the returned row and analyze results. 
print(df.iloc[5:14])


#  Selecting a single column using .iloc 
# Select 3rd column 
#  print the returned row and analyze results.

print(df.iloc[:,3])

# Selecting multiple columns using .iloc 
# Select 2nd column, 4th column,  7th columns  
# , print the returned row and analyze results.
print(df.iloc[:,[2,4,7]])



# Selecting a slice of columns using .iloc 
# Range: Select from 2nd column to 5th columns  
# , print the returned row and analyze results. 
print(df.iloc[:,2:6])

# Combined row and column selection using .iloc 
# Select – 7th row, 9th row and 15th row 
# Select 2nd column, 4th column 
#  print the returned row and analyze results. 
print(df.iloc[[7,9,15],[2,4]])


# Combined row and column selection using .iloc 
# Select range : 2nd  row, 6th  row 
# Select range : 2nd column to 4th column 
# , print the returned row and analyze results. 
print(df.iloc[2:7,2:5])

# Add a New Row to a Pandas DataFrame 
# print the returned dataFrame and analyze results.
df.loc[len(df.index)]=[102021,'not for sale',1000310,3,4,0.5,10021,'Adjuntas','Puerto Rico',601,920,123]



# drop method is used to drop the rows and the columns from the dataframe 

# delete row with index 2 
# print the returned dataFrame and analyze results.
print(df.drop(3,axis=0))   

# What if we want to delete the multiple rows 
# delete row with index from 4 to 7th row 
# print the returned dataFrame and analyze results.
print(df.drop([4,5,6,7],axis=0,inplace=True))
print(df)
# and if we want to delete it permanently then we use the inplace parameter


# Delete “house_size” column 
# print the returned dataFrame and analyze results.
# axis=0 means rows and axis=1 means columns 
print(df.drop('house_size',axis=1))


# Delete “house_size” and “state” columns 
# print the returned dataFrame and analyze results. 
print(df.drop(['house_size','state'],axis=1,inplace=True))
print(df)
# Rename column “state”  to “state_Changed” 
# Print the returned dataFrame and analyze results. 
df.rename(columns={'price':'price_changed'},inplace=True)
print(df)

# what if we want to rename the name row index with any name
# Rename label from 3 to 5 
# Print the returned dataFrame and analyze results. 
print(df.rename(index={3:'Third_Row',8:'Eight_Row',9:'Ninth_Row'},inplace=True))
print(df.to_string())

# query() method is used to query the dataframe just like sql
# query() to Select Data 
# where: "price” < 127400 
# “city” not equal to “Adjuntas”  
# Print the returned dataFrame and analyze results. 
print(df.query('price_changed>127400  and city!="Adjuntas"'))



#sort_values() is used to sort the dataframe by asencding and desending order
# sort DataFrame by price in ascending order column “price” 
print(df['price_changed'].sort_values(ascending=True).to_string())

# Below code is the average price of each city
# Groupby() method is used to group the dataframe by any column
# “group the DataFrame by the “city” column and calculate the sum of “price” for each category 
# Print the returned dataFrame and analyze results. 
print(df.groupby('city')['price_changed'].mean())


# dropna() method is used to drop the rows and the columns which have null values
# Drop all rows with null values in "price" column
# subset parameter is used to specify the column name

# use dropna() to remove rows with any missing values 
# Print the returned dataFrame and analyze results. 
print(df.dropna(subset=['price_changed']).to_string())

print(df.isnull().sum())
# fillna() method is used to fill the null values with any value
# Fill all null values in "prev_sold_date" column with the value 1

# filling NaN values with 0 
print(df.fillna(0,inplace=True))
print(df.isnull().sum())
