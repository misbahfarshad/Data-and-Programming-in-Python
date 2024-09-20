# PPHA 30537
# Spring 2023
# Homework 4

# YOUR NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Sunday April 23rd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.
import os
import pandas as pd

data_dir = "/Users/misbaharshad/Documents/GitHub/Live Labs /homework-4-misbahfarshad/"
filename = "NST-EST2022-ALLDATA.csv"
abs_path = os.path.join(data_dir, filename)

df = pd.read_csv(abs_path)


# Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.

import us

def fip_to_abb(fips_code):
    fips_str = str(fips_code).zfill(2)
    if fips_code == 0:
        return "US"
    elif fips_code == 72:
        return "PR"
    elif fips_code in fips_to_abbrev:
        return fips_to_abbrev[fips_code]
    else:
        state = us.states.lookup(fips_str)
        if state is not None:
            return state.abbr

fips_to_abbrev = {
    0: "US", 72: "PR", 1: "AL", 2: "AK", 4: "AZ", 5: "AR", 6: "CA", 8: "CO",
    9: "CT", 10: "DE", 11: "DC", 12: "FL", 13: "GA", 15: "HI", 16: "ID",
    17: "IL", 18: "IN", 19: "IA", 20: "KS", 21: "KY", 22: "LA", 23: "ME",
    24: "MD", 25: "MA", 26: "MI", 27: "MN", 28: "MS", 29: "MO", 30: "MT",
    31: "NE", 32: "NV", 33: "NH", 34: "NJ", 35: "NM", 36: "NY", 37: "NC",
    38: "ND", 39: "OH", 40: "OK", 41: "OR", 42: "PA", 44: "RI", 45: "SC",
    46: "SD", 47: "TN", 48: "TX", 49: "UT", 50: "VT", 51: "VA", 53: "WA",
    54: "WV", 55: "WI", 56: "WY"
}

df['STATE'] = df['STATE'].map(fip_to_abb)


#Question 3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize it for them.  Show 
# some relevant exploration output with print() statements.

print(df.head)
print(df.tail)
print(df.shape)
print(df.describe)
print(df.dtypes)

# Question 4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.
df = df[[c for c in df.columns if c.endswith('2020') or ('2021') or ('2022')]]
df = df.loc[:, ['STATE'] + [c for c in df.columns if c.startswith('POPESTIMATE')]]


# Question 5: Show only the 10 largest states by 2021 population estimates, in
# decending order.
df['POPESTIMATE2021'].sort_values(ascending=False).head(10)

# Question 6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?
def pop_changes22(x):
    return x['POPESTIMATE2022'] - x['POPESTIMATE2020']

df['POPCHANGE'] = df.apply(pop_changes22, axis=1)

gained = (df['POPCHANGE'] > 0).sum()
lost = (df['POPCHANGE'] < 0).sum()

print('number of states that gained population from 2020 to 2022:', gained)
print('number of states that lost population from 2020 to 2022:', lost)

# Question 7: Show all the states that had an estimated change of smaller 
# than 1000 people. (hint: look at the standard abs function)
df[df['POPCHANGE'].abs() < 1000]

# Question 8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.
def popchange_zscore(df):
    popchange_mean = df['POPCHANGE'].mean()
    popchange_std = df['POPCHANGE'].std() 
    zscore = (df['POPCHANGE'] - popchange_mean) / popchange_std
    return df[(zscore.abs() > 1)][['STATE', 'POPCHANGE']].sort_values(by='POPCHANGE', ascending=False)

popchange_zscore(df)
