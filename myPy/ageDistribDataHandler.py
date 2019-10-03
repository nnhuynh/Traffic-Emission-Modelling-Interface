import csv
import pandas as pd
import constants as const
import numpy as np

ageDistribCols = ['year',
                  const.rmsVehTypes.passengerVehicles.value, #'Passenger Vehicles'
                  const.rmsVehTypes.offroadVehicles.value, #'Off-road Vehicles',
                  const.rmsVehTypes.peopleMovers.value, #'People movers ',
                  const.rmsVehTypes.smallBuses.value, #'Small Buses ',
                  const.rmsVehTypes.mobileHomes.value, #'Mobile Homes ',
                  const.rmsVehTypes.motorCycles.value, #'Motor cycles ',
                  const.rmsVehTypes.scooters.value, #'Scooters ',
                  const.rmsVehTypes.lightTrucks.value, #'Light Trucks ',
                  const.rmsVehTypes.lightPlants.value, #'Light Plants ',
                  const.rmsVehTypes.lightTrailers.value, #'Light Trailers',
                  const.rmsVehTypes.otherVehicles.value, #'Other Vehicles',
                  const.rmsVehTypes.buses.value, #'Buses ',
                  const.rmsVehTypes.heavyTrucks.value, #'Heavy Trucks ',
                  const.rmsVehTypes.primeMovers.value, #'Prime Movers ',
                  const.rmsVehTypes.heavyPlants.value, #'Heavy Plants ',
                  const.rmsVehTypes.heavyTrailers.value] #'Heavy Trailers'

def prorate(val, distribList):
    distrib = np.asarray(distribList)
    distrib = val*distrib/np.sum(distrib)
    return distrib

def readAgeDistribData(ageDistribFile, firstLineYrUnknown=True):
    with open(ageDistribFile,'r') as f:
        reader = csv.reader(f)
        listAgeDistrib = list(reader)

    # ignore the header line
    listAgeDistrib = listAgeDistrib[1:]
    dfAgeDisRaw = pd.DataFrame(listAgeDistrib, columns=ageDistribCols)
    if firstLineYrUnknown:
        dfYrUnknown = dfAgeDisRaw.iloc[0]
        dfAgeDisRaw = dfAgeDisRaw.iloc[1:].astype(int)
        for col in ageDistribCols[1:]:
            valYrUnknown = int(dfYrUnknown[col])
            dfAgeDisRaw[col] = dfAgeDisRaw[col] + prorate(valYrUnknown,dfAgeDisRaw[col])
            dfAgeDisRaw[col] = dfAgeDisRaw[col].apply(round)

    # adds values in column 'Light Trailers' into Scooters using user input factor in const.userInputs.lightTrailerScooterFactor
    dfAgeDisRaw[const.rmsVehTypes.scooters.value] += const.userInputs.lightTrailerScooterFactor.value * \
                                                     dfAgeDisRaw[const.rmsVehTypes.lightTrailers.value]
    dfAgeDisMOVES = groupAgeDisByMovesTypes(dfAgeDisRaw)
    dfAgeFrac = calAgeDistribFrac(dfAgeDisMOVES)

    return dfAgeFrac

def groupAgeDisByMovesTypes(dfAgeDisRaw):
    '''
    :param dfAgeDisRaw: this dataframe should have all columns as specified in ageDistribCols
    :return:
    '''
    dfAgeDisMOVES = pd.DataFrame()
    dfAgeDisMOVES['year'] = dfAgeDisRaw['year']
    for movesType in const.MovesSourceTypes:
        typeDesc = movesType.getDesc()
        rmsTypes = movesType.getRMSVehTypes()
        if rmsTypes:
            dfAgeDisMOVES[typeDesc] = 0
            for rmsType in rmsTypes:
                dfAgeDisMOVES[typeDesc] += dfAgeDisRaw[rmsType]

    return dfAgeDisMOVES


def calAgeDistribFrac(dfAgeDisMOVES):
    validSourceTypes = list(dfAgeDisMOVES)
    validSourceTypes.remove('year')
    for typeDesc in validSourceTypes:
        dfAgeDisMOVES[typeDesc] = dfAgeDisMOVES[typeDesc]/dfAgeDisMOVES[typeDesc].sum()

    dfAgeDisMOVES['ageID'] = const.userInputs.yearID.value - dfAgeDisMOVES['year']
    dfAgeDisMOVES['ageID'] = dfAgeDisMOVES['ageID'].apply(lambda x: min(x, 30))
    dfAgeDisMOVES = dfAgeDisMOVES.drop('year', axis=1)

    dfAgeDisMOVES.set_index('ageID')
    dfAgeDisMOVES = dfAgeDisMOVES.groupby('ageID').sum()
    #dfAgeDisMOVES.to_csv('./tempOutputs/dfAgeDisMOVES_frac.csv')

    newdf = pd.DataFrame()
    for typeDesc in validSourceTypes:
        tmpdf = pd.DataFrame()
        tmpdf[const.sourceTypeAgeDistribution.col_ageID.value[0]] = dfAgeDisMOVES.index
        tmpdf[const.sourceTypeAgeDistribution.col_ageFraction.value[0]] = dfAgeDisMOVES[typeDesc]
        tmpdf[const.sourceTypeAgeDistribution.col_yearID.value[0]] = const.userInputs.yearID.value
        tmpdf[const.sourceTypeAgeDistribution.col_sourceTypeID.value[0]] = \
            const.MovesSourceTypes.getSourceTypeByDesc(typeDesc).getSourceTypeID()
        newdf = pd.concat([newdf,tmpdf])

    #newdf.to_csv('./tempOutputs/newdf.csv', index=False)
    return newdf


