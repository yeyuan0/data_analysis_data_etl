import pandas as pd
import censusdata
def get_data_in_state(variables, state='36', county='*', block='*', data_type='acs5', year=2018):
    if block:
        datas = []
        geos = censusdata.geographies(censusdata.censusgeo([('state', state),('county', county)]), 'acs5', 2015)
        for geo in list(geos.values())[:3]:
            cur_data = censusdata.download(
                    data_type, year,
                    censusdata.censusgeo([('state', state), ('county', geo.params()[1][1]), ('block group', block)]),
                    list(variables.keys()))
            datas.append(cur_data)
        data = pd.concat(datas)
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

variables = {'B02001_001E': 'total_population',
             'B03001_003E': 'hispanic_or_latino',
             'B02001_002E': 'white',
             'B02001_003E': 'black_or_African',
             'B02001_004E': 'indian_and_alaska_native',
             'B02001_005E': 'asian',
             'B02001_006E': 'native_hawaiian_and_other_pacific_islander',
             'B09019_001E': 'total_in_living_units',
             'B09019_002E': 'total_in_households',
             'B09019_003E': 'in_family_households',
             'B06011_001E': 'median_income',
             'B01002_001E': 'median_age',
             'B23013_001E': 'aggregate_usual_work_hours',
             'C24050_001E': 'total_employed',
             'C24050_004E': 'manufacturing_employed',
             'C24050_007E': 'transportation_warehousing_utilities_employed'
            }

if __name__ == '__main__':
    data = get_data_in_state(variables, state='36', county='*', block='*', data_type='acs5', year=2018)
    
    data['State'] = [data.index[i].params()[0][1] for i in range(data.shape[0])]
    data['County'] = [data.index[i].params()[1][1] for i in range(data.shape[0])]
    data['Tract'] = [data.index[i].params()[2][1] for i in range(data.shape[0])]
    data['BlockGroup'] = [data.index[i].params()[3][1] for i in range(data.shape[0])]
    data.reset_index(drop=True, inplace=True)
    
    data.to_csv('acs_data_yeyuan2.csv')
