import pandas as pd
import pyreadstat
import numpy as np
import matplotlib.pyplot as plt
import collections
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression
from stargazer.stargazer import Stargazer
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf


data, metadata = pyreadstat.read_sav("Religion_India.sav")

df = pd.DataFrame(data)
#print(df.head(5))

#Q30 : CAN A PERSON BE 'HINDU(QREL=1)' IF THEY DISRESPECT INDIA(30.L PART)

# SumQ30l= df.loc[(df['Q30l'] == 2) & (df['QRELSING'] == 1), 'Q30l']

# print("The number of people who said that a person cannot be hindu if they disrespect India are : ",len(SumQ30l))

# #TOTAL NUMBER OF VALUES
# Values_no = len(df['Q30l'])
# print ("\nThe total number of values in the Column Q30l are: ", Values_no)

# #total number of people / people who said sumq30l
# div_1 = (len(SumQ30l)/ Values_no)* 100
# print("\n Proportion of people who are hindus out of 30000 who equate nationalism with religion : ", div_1) #54.3%

# #QDIV : ALL IN ALL, WHAT DO YOU THINK ABOUT INDIA'S DIVERSITY ? (In a bad way)
# SumDIV= df.loc[(df['Q30l'] == 2) & (df['QRELSING'] == 1) & (df['QDIV'] == 2), 'Q30l']

# print("\nThe number of people who said that a person cannot be hindu if they disrespect India and then proceeded to say that ",end = "")
# print("the religious diversity affects India in a bad way : ", len(SumDIV))

# #number of people who think nationalism = religion / people who said religious diversity is bad
# div_2 = (len(SumDIV) / len(SumQ30l))* 100
# print("\n proportion of hindus who said religious diversity is bad and also said cant disrespect india : ", div_2) #21%

# #Q60 : SHOULD MUSLIM MEN BE ABLE TO DIVORCE THEIR WIVES BY SAYING TALAQ 3 TIMES (n0)
# Sum_Q60 = df.loc[(df['Q30l'] == 2) & (df['QRELSING'] == 1) & (df['Q60'] == 2), 'Q30l']

# print("\nThe number of people who said that a person cannot be hindu if they disrespect India and then proceeded to say that ",end = "")
# print("muslim men shouldn't be able to do so : ", len(Sum_Q60))

# Sum_Q60two = df.loc[(df['Q30l'] == 2) & (df['QRELSING'] == 1) & (df['QDIV'] == 2) & (df['Q60'] == 2), 'Q30l']

# print("\nCan't be hindu -> disrespect -> religious diversity is negative -> muslim men shouldn't: ",len(Sum_Q60two))

# SumQ69b = df.loc[(df['Q69f'] == 1) | (df['Q69f'] == 2), 'Q69f']

# print("number of people who chose 1 or 2 in question 69b are: ", len(SumQ69b))

# #people who said no(2) in question 63b (muslim neighbors)

# sumQ63b = df.loc[(df['Q63b'] == 2), 'Q69b']
# print("number of people who chose 1 or 2 in question 69b are: ", len(sumQ63b))

# #people who said diversity harms our country(2) in Qdiv

# sumqdiv = df.loc[(df['QDIV'] == 2), 'QDIV']
# print(" \n number of people who chose 1 or 2 in question qdiv are: ", len(sumqdiv))

# #people who said 2 in question 65(muslim courts)
# sumq65 = df.loc[(df['Q65'] == 2), 'Q65']
# print(" \n number of people who chose 2 in q65 are: ", len(sumq65))

# #people who chose 2 in question 60 (muslim talak)
# sumq60 = df.loc[(df['Q60'] == 2), 'Q60']
# print(" \n number of people who chose 2 in q60 are: ", len(sumq60))

# #people who chose 1 in question 40 (true religion)
# sumq40 = df.loc[(df['Q40'] == 1), 'Q40']
# print(" \n number of people who chose 1 in q40 are: ", len(sumq40))

# sumq12 = df.loc[(df['Q12'] == 1) | (df['Q12'] == 2), 'Q12']
# print(" \n number of people who chose 1 in Q12 are: ", len(sumq12))

############################################################################
#binary for question 65
sum_one_65 =0
sum_zero_65 = 0

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_65
  global sum_zero_65
  for value in df[column_name]:
    if value == 2:
      my_list.append(1)
      sum_one_65 += 1
    else:
      my_list.append(0)
      sum_zero_65 += 1

  # print("\n sum of 1: ",sum_one)
  # print("\n sum pf 0: ",sum_zero)

  return my_list

binary_list_65 = binary_function('Q65', [])
#print(binary_list_65)
print(sum_one_65)
print(sum_zero_65)

##############################################################################

############################################################################
#binary for question 63b,div
sum_one_63 =0
sum_zero_63 = 0

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_63
  global sum_zero_63
  for value in df[column_name]:
    if value == 2:
      my_list.append(1)
      sum_one_63 += 1
    else:
      my_list.append(0)
      sum_zero_63 += 1

  # print("\n sum of 1: ",sum_one)
  # print("\n sum pf 0: ",sum_zero)

  return my_list

binary_list_63 = binary_function('Q63b', [])
#print(binary_list_65)
print(sum_one_63)
print(sum_zero_63)

##############################################################################

############################################################################
#binary for question 65
sum_one_DIV =0
sum_zero_DIV = 0

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_DIV
  global sum_zero_DIV
  for value in df[column_name]:
    if value == 2:
      my_list.append(1)
      sum_one_DIV += 1
    else:
      my_list.append(0)
      sum_zero_DIV += 1

  # print("\n sum of 1: ",sum_one)
  # print("\n sum pf 0: ",sum_zero)

  return my_list

binary_list_DIV = binary_function('QDIV', [])
#print(binary_list_DIV)
print(sum_one_DIV)
print(sum_zero_DIV)

##############################################################################

############################################################################
#binary for question 40
sum_one_40 =0
sum_zero_40= 0

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_40
  global sum_zero_40
  for value in df[column_name]:
    if value == 1:
      my_list.append(1)
      sum_one_40 += 1
    else:
      my_list.append(0)
      sum_zero_40 += 1

  # print("\n sum of 1: ",sum_one)
  # print("\n sum pf 0: ",sum_zero)

  return my_list

binary_list_40 = binary_function('Q40', [])
#print(binary_list_40)
print(sum_one_40)
print(sum_zero_40)

##############################################################################



def scale_function(list1, list2,list3, list4):
  scale_result = []
  for i in range(len(list1)):
          scale_result.append(list1[i] +list2[i] + list3[i] +list4[i])

  return scale_result

tolerance_scale = scale_function(binary_list_40,binary_list_63, binary_list_65, binary_list_DIV)

#print("\n The scale of the tolerance is: ", tolerance_scale )

# def sum_tolerance(list_result):
#   for value in range(len(list_result)):
#     if(value == 0)

counted_tolerance = collections.Counter(tolerance_scale)
print(counted_tolerance)

############################################################################

############################################################################
#THIS IS FOR QUESTION Q69B (main 2nd variable)


#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_age
  global sum_zero_age
  for value in df[column_name]:
    my_list.append(value)

  return my_list

binary_list_age = binary_function('QAGErec', [])
#print(binary_list_40)


counted_age = collections.Counter(binary_list_age)
print("\n", counted_age)

###################################################################################################################

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  for value in df[column_name]:
    if value == 2 or value == 3:
      my_list.append(1)
    else:
      my_list.append(0)
  return my_list

binary_list_85 = binary_function('Q85', [])
#print(binary_list_40)


counted_85 = collections.Counter(binary_list_85)
print("\n", counted_85)
###################################################################################################################
#THIS IS FOR QUESTION Q69B (main 2nd variable)

#this function is for question Q65 only
def binary_function(column_name, my_list ):

  for value in df[column_name]:
    if value == 1:
      my_list.append(1)
    else:
      my_list.append(0)

  return my_list

binary_list_edu = binary_function('QEDU', [])
#print(binary_list_40)

counted_edu = collections.Counter(binary_list_edu)
print("\n", counted_edu)
###############################################################################################################3

#THIS IS FOR QUESTION Q69B (main 2nd variable)
sum_one_69 =0
sum_zero_69= 0

#this function is for question Q65 only
def binary_function(column_name, my_list ):
  global sum_one_69
  global sum_zero_69
  for value in df[column_name]:
    if value == 1 or value == 2:
      my_list.append(1)
      sum_one_69 += 1
    else:
      my_list.append(0)
      sum_zero_69 += 1

  # print("\n sum of 1: ",sum_one)
  # print("\n sum pf 0: ",sum_zero)

  return my_list

binary_list_69 = binary_function('Q69b', [])
#print(binary_list_40)
# print(sum_one_69)
# print(sum_zero_69)

counted_69 = collections.Counter(binary_list_69)
print("\n", counted_69)

##############################################################################

######bar graph#########


counts = collections.Counter(tolerance_scale)
categories = list(counts.keys())
frequencies = list(counts.values())

# group the data by the two variables and count the occurrences
counts = df.groupby([binary_list_69,tolerance_scale]).size().unstack(fill_value=0)

# create the stacked bar chart
ax = counts.plot(kind='bar', stacked=True, color=['orange', 'blue', 'red', 'green', 'pink'])

# add labels and titles
ax.set_xlabel('Ideology of "Hindutva"')
ax.set_ylabel('Count')
ax.set_title('Relationship between Hindutva and Religious Tolerance')

# display the chart
plt.show()


###############################GRAPH######################################

#################Chi-squared test#####################


# Create a contingency table from the two variables
contingency_table = pd.crosstab(pd.Series(binary_list_69), pd.Series(tolerance_scale))

chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
# print(p_value)
# print(chi2)
# print(dof)

###################################REGRESSION#########################################

# df = pd.DataFrame({'independent' : binary_list_69, 'dependent' : tolerance_scale})
#
# model = LogisticRegression().fit(df[['independent']], df['dependent'])
#
# # print model coefficients
# print('Intercept:', model.intercept_[0])
# print('Coefficient:', model.coef_[0][0])
#
# stargazer_tab = Stargazer([model])



d = { "x": pd.Series(binary_list_69), "y": pd.Series(tolerance_scale) ,"z": pd.Series(binary_list_age),"t": pd.Series(binary_list_edu), "j": pd.Series(binary_list_85)}
df = pd.DataFrame(d)
mod = smf.ols('y ~ x + z + t + j', data=df)
res = mod.fit()
print(res.summary())
# Graph_choice = input("Which bar graph do you want ? (1= Q30l, 2= QDIV, 3= Q60)")

# if(Graph_choice == '1'):

#     value_counts = df["Q30l"].value_counts()

#     #THIS IS FOR A BAR GRAPH OF Q30L, YOU CAN MAKE A DIFFERENT KIND OF A GRPAH TOO
#     value_counts.plot.bar()
#     plt.xlabel("Value")
#     plt.ylabel("Frequency")
#     plt.title("Q30l demographic variation graph")
#     plt.show()

# elif(Graph_choice == '2'):

#     value_counts = df["QDIV"].value_counts()

#     value_counts.plot.bar()
#     plt.xlabel("Value")
#     plt.ylabel("Frequency")
#     plt.title("QDIV demographic variation graph")
#     plt.show()

# else:
#     value_counts = df["Q60"].value_counts()

#     value_counts.plot.bar()
#     plt.xlabel("Value")
#     plt.ylabel("Frequency")
#     plt.title("Q60 demographic variation graph")
#     plt.show()
