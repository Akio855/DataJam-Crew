import pandas as pd 
import numpy as np

crime_levels = np.array(['Felony', 'Felony-Misdemeanor', 'Misdemeanor', 'Infraction'])

felony = np.array(['Arson', 'Homicide', ''])
felony_misdemeanor = np.array(['Assault', "Burglary", 'Embezzlement','Drug Violation', 'Fraud', 'Larceny Theft', 'Weapons Offence', 'Weapons Offense', 'Weapons Carrying Etc', "Traffic Violation Arrest",'Stolen Property','Traffic Collision'])
misdemeanor = np.array(['Drug Offense', 'Fire Report', 'Disoderly Conduct', 'Liquor Laws', 'Warrant', 'Vandalism', 'Prostitution', 'Malicious Mischief  '])
infraction = np.array(['Non-Criminal', 'Civil Sidewalks'])


police = pd.read_csv("police_incidents_2018-present.csv")
income = pd.read_csv('income.csv')
police_type_counts = police[["Incident Category","Resolution","Analysis Neighborhood"]]['Analysis Neighborhood'].value_counts()#[(police['Analysis Neighborhood'] == 'NaN')]
#filted_police = police[["Incident Category","Resolution","Analysis Neighborhood"]]
print(police_type_counts)