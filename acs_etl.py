import pandas as pd
import censusdata
def get_tract_data_in_state(variables, state='36', county='*', tract='*', data_type='acs5', year=2018, table_type='profile'):
    if tract:
        data = censusdata.download(
                data_type, year,
                censusdata.censusgeo([('state', state), ('county', county), ('tract', tract)]),
                list(variables.keys()),
                tabletype=table_type)
    elif county:
        data = censusdata.download(
                data_type, year,
                censusdata.censusgeo([('state', state), ('county', county)]),
                list(variables.keys()),
                tabletype=table_type)
    else:
        data = censusdata.download(
                data_type, year,
                censusdata.censusgeo([('state', state)]),
                list(variables.keys()),
                tabletype=table_type)
    data.rename(columns=variables, inplace=True)
    return data

variables = {'DP05_0070E': 'Estimate!!HISPANIC OR LATINO AND RACE!!Total population',
             'DP05_0071E': 'Hispanic or Latino (any race)',
             'DP05_0077E': 'White alone',
             'DP05_0078E': 'Black or African American alone',
             'DP05_0079E': 'American Indian and Alaska Native alone',
             'DP05_0080E': 'Asian alone',
             'DP05_0081E': 'Native Hawaiian and Other Pacific Islander alone',
             'DP02_0001E': 'Estimate!!HOUSEHOLDS BY TYPE!!Total households',
             'DP02_0002E': 'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Family households (families)',
             'DP03_0062E': 'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)',
             'DP03_0063E': 'Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)',
             'DP03_0096E': 'Estimate!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!With health insurance coverage',
             'DP05_0018E': 'Estimate!!SEX AND AGE!!Total population!!Median age (years)',
             'DP03_0032E': 'Estimate!!INDUSTRY!!Civilian employed population 16 years and over',
             'DP03_0035E': 'Estimate!!INDUSTRY!!Civilian employed population 16 years and over!!Manufacturing',
            }

if __init__ == '__main__':
    data = get_tract_data_in_state(
                variables, state='36', county='*', tract='*', data_type='acs5', 
                year=2018, table_type='profile'
           )
    
    data['State'] = [data.index[i].params()[1][1] for i in range(data.shape[0])]
    data['County'] = [data.index[i].params()[1][1] for i in range(data.shape[0])]
    data['Tract'] = [data.index[i].params()[2][1] for i in range(data.shape[0])]
    data.reset_index(drop=True, inplace=True)
    
    data.to_csv('acs_data_yeyuan2.csv')
    
