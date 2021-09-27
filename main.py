import pandas as pd
import os
import time
#, ["nok","ownership","id","type","voting"]
dfpath = os.path.join(os.getcwd(), "investments.csv")
df = pd.read_csv(dfpath)

fileColumns = list(df.columns)

def delColumns(dataFrame):
    del dataFrame["nok"]
    del dataFrame["ownership"]
    del dataFrame["id"]
    del dataFrame["type"]
    del dataFrame["voting"]

    dataFrame.to_csv(dfpath, index = False)

    return fileColumns

def chooseSectors(dataFrame):
    allsectors = list(set(dataFrame["sector"])) #['Consumer Services','Telecommunications',  'Oil & Gas', 'Consumer Goods', 'Health Care', 'Utilities', 'Technology', 'Basic Materials','Industrials','Financials']
    wantedSectors = [
    'Telecommunications', 
    'Health Care', 
    'Technology', 
    ]

    #Get unwanted sectors
    unwantedSectors = []
    for sector in allsectors:
        if sector not in wantedSectors:
            unwantedSectors.append(sector)
        else:
            continue
    unwantedSectors = list(set(unwantedSectors))

    #eliminate unwantedsectors from csv file
    for unwantedSector in unwantedSectors:
        dataFrame = dataFrame[dataFrame.sector != unwantedSector]

    #Save editions

    return dataFrame.to_csv(dfpath, index = False)
        
def chooseContries(dataFrame):
    allcountries = list(set(dataFrame["country"])) #['Israel', 'Russia', 'Canada', 'Poland', 'France', 'Peru', 'Kyrgyzstan', 'Oman', 'Colombia', 'Moldova', 'United Kingdom', 'China', 'Ukraine', 'Thailand', 'Cyprus', 'Mexico', 'Ireland', 'Belgium', 'Romania', 'Australia', 'Netherlands', 'Morocco', 'Greece', 'Finland', 'Portugal', 'Bangladesh', 'Sweden', 'Indonesia', 'Latvia', 'India', 'Singapore', 'Egypt', 'Bahrain', 'Chile', 'Austria', 'Estonia', 'Hong Kong', 'Nigeria', 'Sri Lanka', 'Turkey', 'Kuwait', 'Qatar', 'Slovenia', 'Czech Republic', 'Switzerland', 'Brazil', 'South Africa', 'Saudi Arabia', 'Iceland', 'Taiwan', 'Croatia', 'Vietnam', 'Germany', 'Mauritius', 'South Korea', 'Kenya', 'Philippines', 'United States', 'Japan', 'United Arab Emirates', 'Denmark', 'Malaysia', 'Tunisia', 'New Zealand', 'Botswana', 'Italy', 'Lithuania', 'Hungary', 'Spain']
    wantedCountries = ['Israel', 'Canada', 'Poland', 'France','United Kingdom', 'Ireland', 
    'Belgium', 'Australia', 'Netherlands', 'Greece', 'Finland', 'Portugal', 
    'Sweden', 'India', 'Austria', 'Estonia', 'Slovenia', 'Czech Republic', 
    'Switzerland', 'Iceland', 'Taiwan', 'Germany', 'South Korea', 'United States', 
    'Japan', 'Denmark', 'New Zealand', 'Italy', 'Lithuania', 'Hungary', 'Spain']

    #Get unwanted Contries
    unwantedCountries = []
    for country in allcountries:
        if country not in wantedCountries:
            unwantedCountries.append(country)
        else:
            continue
    unwantedCountries = list(set(unwantedCountries))

    #Eliminate unwanted contries
    for unwantedCountry in unwantedCountries:
        dataFrame = dataFrame[dataFrame.country != unwantedCountry] #https://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value#18173074
    
    return dataFrame.to_csv(dfpath, index = False)

def sortValues(dataFrame):
    dataFrame.sort_values(by=['usd'], ascending=False)
    return dataFrame.to_csv(dfpath, index= False)

def intColumnValuesRedable(dataframe, columnName):
    roundedValue = []
    finalValues = []

    for value in dataframe[columnName]:
        value = int(value)
        value = round(value)
        roundedValue.append(value)

    for value in roundedValue:
        value = format(value, ',d')
        finalValues.append(value)

    dataframe[columnName] = finalValues
    return dataframe.to_csv(dfpath, index= False)


delColumns(df)
chooseSectors(df)
chooseContries(df)
sortValues(df)
intColumnValuesRedable(df, 'usd')