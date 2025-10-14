import pandas as pd


# first we are going to create a dataframe
df=pd.DataFrame({'X':[23,45,32,67,59],'Y':[2364,56,23,65,76]})
print(df)
# As we the length of the two columns is not same it will raise an error

df=pd.DataFrame({'X':[23,45,32,67,59],'Y':[2364,56,23,65,76]})

# So if we want to create a dataframe that does not raise an error we have to make single dataframe for each column each time

df_1=pd.DataFrame({'X':[23,45,32,67,59]})
df_2=pd.DataFrame({'Y':[2364,56,23,65]}) 
df=pd.concat([df_1,df_2],axis=1)
print(df)



# Now we are creating a dataframe which is different from the above one
# with the specified columns and index  
exam_data=pd.DataFrame({'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
                        'score':[12.5,9,16.5,None,9,20,14.5,None,8,19],'attempts':[1,3,2,3,2,3,1,1,2,1],
                        'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']},index=['a','b','c','d','e','f','g','h','i','j'])
print(exam_data)

print(exam_data.info())
print(exam_data.describe())
print(exam_data.shape)


# Selecting the First 3 Rows 
print(df.loc[0:3]) 


# Selecting 'name' and 'score' Columns - Write a Pandas program to select the 'name' and 'score' columns 
# from the following DataFrame. ?
print(exam_data[['name','score']])



# Selecting Specific Columns and Rows - Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the given 
# data frame. 
print(exam_data.loc[['b','d','f','g'],['name','score']])

# Write a Pandas program to select the rows where the number of attempts in the examination is 
# greater than 2. 
exam_data.loc[exam_data['attempts']>2]

print(exam_data.shape)


# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
print(exam_data.loc[(exam_data['score']>15) & (exam_data['score']<=20)])



# Write a Pandas program to select the rows where number of attempts in the examination is less than 2 
# and score greater than 15.
print(exam_data.loc[(exam_data['score']>15) & (exam_data['attempts']<=2)])


# Write a Pandas program to change the score in row 'd' to 11.5. 
exam_data.loc['d','score']=11.5
print(exam_data)


# Write a Pandas program to calculate the mean of all students' scores. Data is stored in a dataframe. 
print(exam_data['score'].mean())

# Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now 
# delete the new row and return the original DataFrame. 
exam_data.loc['k']=['Suresh',15.5,1,'yes']
print(exam_data)
exam_data.drop('k',inplace=True)
print(exam_data)


# Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in 
# ascending order. 
exam_data.sort_values(by='name',ascending=False,inplace=True)
print(exam_data)
exam_data.sort_values(by='score',ascending=True,inplace=True)

# Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and 
# False. 
exam_data['qualify'].replace({'yes':True,'no':False},inplace=True)
print(exam_data)

# Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame. 
print(exam_data['name'].replace({'James':'Suresh'}))


# Write a Pandas program to delete the 'attempts' column from the DataFrame. 
print(exam_data.drop('attempts',axis=1))


