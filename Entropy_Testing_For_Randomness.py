#chi_square_testing
import csv
import secrets
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plot

#Open CSV file and store data to lists
filename = '/home/chris/Documents/Mechanical_Entropy_Source_Test/Wheel_Tests_1000.csv'
with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
#        print(header_row)

        test_number = []
        d6 = []
        d12 = []
        wheel = []

        for row in reader:
            test_number.append(row[0])
            d6.append(row[1])
            d12.append(row[2])
            wheel.append(row[3])


pass_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'd', 'e', 'g', 'h', 'i', 'j', 'q', 'r', 't', '0', '1', '2',
    '3', '4', '5', '6', '7', '8', '9', '~', '!', '#', '%', '&', '*', '+',
    '=', '-', '[', ']', '?', '@', '$' ]

#Loop through pass_characters and append 'random' choice to list
secrets_1 = []

active = True
while active:
    if len(secrets_1) == 1000:
        break
    else:
        temp_character = secrets.choice(pass_characters)
        secrets_1.append(temp_character)

#Tally Results and store in dictionary
def tally(result, dictionary):
    for i in result:
        if i in dictionary:
            dictionary[i] +=1
        else:
            dictionary[i] = 1

#Calculate Chi-Squared Statistic
def chisq_test(dictionary):
    expected_value = 1000 / len(dictionary.keys())
    expected_value_list = [expected_value] * len(dictionary.keys())
    chi_value_list = []
    v_list = []
    df = len(dictionary.keys()) - 1
    for k, v in dictionary.items():
        chi_square = ((int(v) - expected_value) **2) / expected_value
        chi_value_list.append(chi_square)
        v_list.append(v)
    chi_statistic = sum(chi_value_list)

    #Check null hypothesis
    upper_value = stats.chi2.ppf(.95, df)
    lower_value = stats.chi2.ppf(.05, df)
    p_result = stats.chisquare(v_list, expected_value_list)
    p_percent = '{:.2%}'.format(p_result.pvalue)
    p_formatted = '{:.4f}'.format(p_result.pvalue)
    #Display results
    print("Chi-Squared Statistic: " + str(chi_statistic))
    print("Statistic Max Accepted: " + str(upper_value))
    print("P-Value: " + str(p_formatted))

    pass_message = ("Result: PASS\nThere is insufficient evidence to conclude deviation" +
            " from randomness. Further testing suggested to increase confidence.\n\n")

    fail_message = ("Result: FAIL\nThere is sufficient evidence to conclude deviation" +
            " from randomness from this sample. This result would be observed " +
            str(p_percent) + " of the time from a 'random' entropy source.")

    if chi_statistic <= upper_value:
        print(pass_message)
    else:
        print(fail_message)

#Empty dictionaries for tally and chisq_test functions
d6_results = {}
d12_results = {}
wheel_results = {}
secrets_results = {}

print("\tD6 Results")
tally(d6, d6_results)
chisq_test(d6_results)

print("\tD12 Results")
tally(d12, d12_results)
chisq_test(d12_results)

print("\tSystem Entropy Results")
tally(secrets_1, secrets_results)
chisq_test(secrets_results)

print("\tPassword Generator Wheel")
tally(wheel, wheel_results)
chisq_test(wheel_results)

#Function to build dataframes
def build_dataframe(dictionary, title):
    df = pd.DataFrame({'Keys': dictionary.keys(), 'Values': dictionary.values(), 'Expected': [1000 / len(dictionary.keys())] * len(dictionary.keys())})
    ax = df[['Expected']].plot(y='Expected', linestyle='-', color='red')
    df[['Keys', 'Values']].plot(x='Keys', y='Values', kind='bar', ax=ax, title=title + " Results", rot=0)

#Call dataframe function and plot results
build_dataframe(d6_results, 'D6')
build_dataframe(d12_results, 'D12')
build_dataframe(secrets_results, 'System')
build_dataframe(wheel_results, 'Wheel')
plot.show(block=True)
