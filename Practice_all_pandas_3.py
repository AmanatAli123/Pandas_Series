import pandas as pd
df=pd.read_csv('C:\\Users\\lenovo\\Desktop\\pandas series\\macro_monthly.csv')
# print(df.to_string())



# Call following method/properties of DataFrame, print output and analyze the output. 
# .info() 
# .dtypes 
# .describe() 
# .shape 
# print(df.info())
# print(df.shape)
# print(df.describe())
print(df.dtypes)


# On given DataFrame – select top 4 rows, and print – verify, debug, analyze the output.
print(df.head(4))


# On given DataFrame – select bottom 4 rows, and print – verify, debug, anzlyze 
print(df.tail(4))


# On Given DataFrame – access the Name column for “Industrial_Production” and print whole 
# column– verify, debug, analyze 
print(df['Industrial_Production'])

# Then next, access the name column for “Manufacturers_New_Orders: Durable Goods” and print 
# whole column 
print(df['Manufacturers_New_Orders: Durable Goods'])



# On Given DataFrame – access access multiple columns like “Industrial_Production” and 
# “Manufacturers_New_Orders: Durable Goods” 
# Print it- – verify, debug, analyze 
print(df[['Industrial_Production','Manufacturers_New_Orders: Durable Goods']])


# Selecting a single row using .loc 
# With auto index  value 3 , print the returned row and analyze results- – verify, debug, analyze 
print(df.loc[3])

# Selecting multiple rows using .loc 
# With auto index value 3 , 5, 7 , print the returned rows and analyze results. 
print(df.loc[[3,5,7]])



# Selecting a slice of rows using .loc 
# With auto index value range of 5 to 15 , print the returned row and analyze results. 
print(df.loc[5:15])

# Conditional selection of rows using .loc 
# “Year” equal “1993” or “1994” or “1997” And “Unemployment_Rate” not less than 1 
# , print the returned row and analyze results. 
# print(df.loc[(df['Year']==['2003'])  & (df['Unemployment_Rate']<1)])  the main error in this line is that we are using the list in the condition instead of the string
print(df.loc[(df['Year'] == '2003') & (df['Unemployment_Rate'] < 1)])


# Selecting a single column using .loc– auto index column value 9 , only select following columns 
# “Industrial_Production”,”Retail_Sales” , ” Manufacturers_New_Orders: Durable Goods” , 
# ”Personal_Consumption_Expenditures”  
# , print the returned row and analyze results. 
print(df.loc[9,['Industrial_Production','Retail_Sales','Manufacturers_New_Orders: Durable Goods','Personal_Consumption_Expenditures']])


# Selecting a slice of columns using .loc 
# Form “Industrial_Production” <= 0.5 
#  print the returned row and analyze results. 
print(df.loc[(df['Industrial_Production']<=0.5)])

# Selecting a single row using .iloc 
# Select 4th row 
#  print the returned row and analyze results. 
print(df.iloc[4])

# Selecting multiple rows using .iloc 
# Select – 2th row, 7th row, 8th row, 36th row, and 9th row 
#  print the returned row and analyze results.
print(df.iloc[[2,7,8,36,9]])

# Selecting a slice of rows using .iloc 
# Select from 10th to 23th row 
#  print the returned row and analyze results. 
print(df.iloc[10:23])

#  Selecting a single column using .iloc 
# Select 5th  column 
#  print the returned row and analyze results. 
print(df.iloc[:,5])



# Selecting multiple columns using .iloc 
# Select 2nd column, 3th column,  8th columns  
#  print the returned row and analyze results. 
print(df.iloc[:,[2,3,8]])


# Selecting a slice of columns using .iloc 
# Range: Select from 2nd column to 8th columns  
#  print the returned row and analyze results. 
print(df.iloc[:,2:9])


# Combined row and column selection using .iloc 
# Select – 4th row, 5th row. 7th row, and 25th row 
# Select 3rd  column, 5th column , 7th  column 
# , print the returned row and analyze results. 
print(df.iloc[[4,5,7,25],[3,5,7]])

# Combined row and column selection using .iloc 
# Select range : 3nd  row, 34th  row 
# Select range : 3rd column to 6th column 
# , print the returned row and analyze results. 
print(df.iloc[3:35,3:7])


#  Add a New Row to a Pandas DataFrame 
# print the returned dataFrame and analyze results. 
df.loc[len(df.index)]=[1994,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
print(df.tail(4))


# delete row with index 4 
# print the returned dataFrame and analyze results. 
df.drop(4,axis=0,inplace=True)
print(df.head(5))


# delete row with index from 5 to 9th row 
# print the returned dataFrame and analyze results.
# The below code doing the same work, you can use any one of them 
df.drop([5,6,7,8],axis=0,inplace=True)
df.drop(df.index[5:9],axis=0,inplace=True)
print(df.head(10))


#  Delete “All_Employees” column 
# print the returned dataFrame and analyze results. 
df.drop('All_Employees(Total_Nonfarm)',axis=1,inplace=True)
print(df.info())


# Delete “Personal_Consumption_Expenditures” and “National_Home_Price_Index” columns 
# print the returned dataFrame and analyze results. 
df.drop(['Personal_Consumption_Expenditures','National_Home_Price_Index'],axis=1,inplace=True)
print(df.info())



# Rename column “Personal_Income”  to 
# “Personal_Income_Changed” 
df.rename(columns={'Personal_Income':'Personal_Income_changed'},inplace=True)
print(df.info())

# Rename label from 5 to 8 
# Print the returned dataFrame and analyze results. 
df.rename(columns={'Unemployment_Rate':'Unemployment_Rate_changed','Retail_Sales':'Retail_Sales_changed','Producer_Price_Index':'Producer_Price_Index_changed','Consumer_Price Index':'Consumer_Price_Index'},inplace=True)
print(df.info())

# query() to Select Data 
# where: “Industrial_Production” <= 0.5 
# and Columns  “Consumer_Price Index” > 0.2 
# and “Year” = “1992” 
# Print the returned dataFrame and analyze results. 
print(df.query("Industrial_Production <= 0.5 and Year== 1992 and Consumer_Price_Index > 0.2"))
print(df.info())


# sort DataFrame by “Consumer_Price Index” in ascending order  
print(df.sort_values(by='Consumer_Price_Index',ascending=True))


# group the DataFrame by the “Year” column and calculate the sum of 
# “National_Home_Price_Index” for each category 
# Print the returned dataFrame and analyze results. 
print(df.groupby('Year')['Consumer_Price_Index'].sum())

print(df.isnull().sum())


# there is not any single values which is null in the dataframe so we will not using the dropna() method here
# and also there is not any single values which is null in the dataframe so we will not using the fillna() method here

