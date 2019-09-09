import csv
import pandas as pd
import constants as const

def getHourInt(x):
    '''
    :param x: hour in string format hh:mm, e.g. 01:00
    :return: hour in integer format, e.g. 1.
    '''
    return int(x.split(':')[0])

def readMeteoData(meteoFile):
    '''
    :param meteoFile: csv file for an OEH weather station downloaded from
    https://www.environment.nsw.gov.au/AQMS/search.htm
    Note that this csv file has 4 columns, date, hour, temperature (oC), relative humidity (%) in this order.
    :return: pandas dataframe of the meteorology data with the below columns
    hourID (sqlCommands.zoneMonthHourCols.hourID.name)
    temperature (sqlCommands.zoneMonthHourCols.temperature.name)
    relHumidity (sqlCommands.zoneMonthHourCols.relHumidity.name)
    '''
    with open(meteoFile,'r') as f:
        reader = csv.reader(f)
        listMeteo = list(reader)

    # ignores the header
    listMeteo = listMeteo[1:]

    dfMeteo = pd.DataFrame(listMeteo, columns=['date','hour','temp','humid'])
    dfMeteo[const.zoneMonthHourAttribs.col_hourID.value[0]] = dfMeteo['hour'].apply(getHourInt)
    dfMeteo[const.zoneMonthHourAttribs.col_temperature.value[0]] = pd.to_numeric(dfMeteo['temp'])
    dfMeteo[const.zoneMonthHourAttribs.col_relHumidity.value[0]] = pd.to_numeric(dfMeteo['humid'])

    dfMeteo = dfMeteo.drop(columns=['date','hour','temp','humid'])

    dfMeteo[const.zoneMonthHourAttribs.col_monthID.value[0]] = const.userInputs.monthID.value
    dfMeteo[const.zoneMonthHourAttribs.col_zoneID.value[0]] = const.userInputs.zoneID.value

    return dfMeteo
