#To read a csv file
#The index_col=0 is when pick up the data from index 0 
variable_name = pd.read_csv("../input/wine-reviews/file_name_of_the_csv_file.csv", index_col=0)

#We can use the shape attribute to check how large the resulting DataFrame is:
variable_name.shape

#So our new DataFrame has 130,000 records split across 14 different columns. That's almost 2 million entries!
#We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
variable_name.head()


import pandas as pd

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
fruits

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples':[35, 41], 'Bananas':[21, 34]}, index=['2017 Sales', '2018 Sales'])
fruit_sales

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can',],index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
ingredients

reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv",index_col=0)
reviews

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
animals.to_csv('cows_and_goats.csv')

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

reviews.head()

desc = reviews['description']

first_description = reviews['description'][0]

first_row = reviews.iloc[0]

first_descriptions = reviews['description'].head(10)
first_descriptions

sample_reviews = reviews.loc[[1,2,3,5,8]]
sample_reviews

df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
df

df = reviews.iloc[:100][['country', 'variety']]
df

italian_wines = reviews.loc[reviews.country == 'Italy']


top_oceania_wines = reviews[(reviews['country'].isin(['Australia', 'New Zealand'])) & (reviews['points'] >= 95)]
top_oceania_wines


