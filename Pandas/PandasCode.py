#To read a csv file
#The index_col=0 is when pick up the data from index 0 
variable_name = pd.read_csv("../input/wine-reviews/file_name_of_the_csv_file.csv", index_col=0)

#We can use the shape attribute to check how large the resulting DataFrame is:
variable_name.shape

#So our new DataFrame has 130,000 records split across 14 different columns. That's almost 2 million entries!
#We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
variable_name.head()
