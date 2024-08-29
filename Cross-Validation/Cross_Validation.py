from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)

print("Average MAE score (across experiments):")
print(scores.mean())


#Begin by writing a function get_score() that reports the average (over three cross-validation folds) MAE of a machine learning pipeline that uses:

the data in X and y to create folds,
SimpleImputer() (with all parameters left as default) to replace missing values, and
RandomForestRegressor() (with random_state=0) to fit a random forest model.
The n_estimators parameter supplied to get_score() is used when setting the number of trees in the random forest model.
def get_score(n_estimators):
    """Return the average MAE over 3 CV folds of random forest model.

    
    Keyword argument:
    n_estimators -- the number of trees in the forest
    """
    # Replace this body with your own code
    pass
    model = RandomForestRegressor(n_estimators=n_estimators, random_state=0)
    pipeline = Pipeline(steps=[('imputer',SimpleImputer()), 
                             ('model', model)
                             ])
    scores = cross_val_score(pipeline, X, y,
                            cv = 3,
                            scoring = 'neg_mean_absolute_error')
    return -1 * scores.mean()


#Test different parameter values
results = {} # Your code here
for i in range(1,9):
    results[50*i] = get_score(50*i)

import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(list(results.keys()), list(results.values()))
plt.show()
