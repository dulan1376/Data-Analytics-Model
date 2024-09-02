import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")


# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")



# Print the data
ign_data # Your code here


# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score = 7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'



# Bar chart showing average score for racing games by platform
# Your code here
plt.figure(figsize=(40,6))
# Add title
plt.title("average score for racing games by platform")
# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=ign_data.index, y=ign_data['Racing'])
plt.ylabel("Average Score")


# Heatmap showing average game score by platform and genre
 # Your code here
plt.figure(figsize=(14, 10))
plt.title('Average Game Score by platform and genre')
sns.heatmap(data=ign_data, annot=True)

plt.xlabel('Average Game Score')

