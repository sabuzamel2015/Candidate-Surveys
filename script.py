import codecademylib

#Imported numpy and Matplotlib libraries
import numpy as np

from matplotlib import pyplot as plt

#Dataset of the responses to the survey
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

#Total of the survey responses that siad they would vote for Ceballos
total_ceballos = sum([1 for c in survey_responses 
if c == 'Ceballos'])

#Percentage of survey responses that said they would vote for Ceballos
percentage_ceballos = 100 * total_ceballos/len(survey_responses)

#Using binomial distribution to determine if the real result was reasonable or if there is something wrong with the poll
possible_surveys = np.random.binomial(70, 0.54, size = 10000)/70.

#Created a histogram of the possible surveys
plt.hist(possible_surveys, range = (0.4,0.8), bins = 20)

#Percentage of surveys that would have Ceballos receiving less than 50 percent of votes
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)

#Used binomial distribution to see if the poll would be more inaccurate with 7,000 people being surveyed
large_survey = np.random.binomial(70, 0.54, size = 7000)/70.

#Percentage of surveys that would have Ceballos receiving less than 50 percent of the votes with 7,000 people being surveyed
ceballos_loss_new = 100 * np.mean(possible_surveys < 0.5)

#show the histogram
plt.show()

print(ceballos_loss_new)
