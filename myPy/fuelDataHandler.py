import pandas as pd
import numpy as np

import constants as const

fuelDistribCols = ['fuelType',
                   const.rmsVehTypes.passengerVehicles.value,  # 'Passenger Vehicles'
                   const.rmsVehTypes.offroadVehicles.value,  # 'Off-road Vehicles',
                   const.rmsVehTypes.peopleMovers.value,  # 'People movers ',
                   const.rmsVehTypes.smallBuses.value,  # 'Small Buses ',
                   const.rmsVehTypes.mobileHomes.value,  # 'Mobile Homes ',
                   const.rmsVehTypes.motorCycles.value,  # 'Motor cycles ',
                   const.rmsVehTypes.scooters.value,  # 'Scooters ',
                   const.rmsVehTypes.lightTrucks.value,  # 'Light Trucks ',
                   const.rmsVehTypes.lightPlants.value,  # 'Light Plants ',
                   const.rmsVehTypes.lightTrailers.value,  # 'Light Trailers',
                   const.rmsVehTypes.otherVehicles.value,  # 'Other Vehicles',
                   const.rmsVehTypes.buses.value,  # 'Buses ',
                   const.rmsVehTypes.heavyTrucks.value,  # 'Heavy Trucks ',
                   const.rmsVehTypes.primeMovers.value,  # 'Prime Movers ',
                   const.rmsVehTypes.heavyPlants.value,  # 'Heavy Plants ',
                   const.rmsVehTypes.heavyTrailers.value]  # 'Heavy Trailers'

def readInFuelDistrib(csvFile):
    dfRaw = pd.read_csv(csvFile, names=fuelDistribCols, skiprows=1) # skips the header of the file

    # groups rms vehicles into moves sources (i.e. vehicles)
    dfFuelByMovesVeh = groupIntoMovesVehTypes(dfRaw)

    # prorates rows 'Unknown' and 'No engine' into other rows
    dfFuelByMovesVeh = dfFuelByMovesVeh.set_index('fuelType')
    tmpdf = dfFuelByMovesVeh.loc['Unknown'] + dfFuelByMovesVeh.loc['No engine']
    dfFuelByMovesVeh = dfFuelByMovesVeh.drop(['Unknown','No engine'])
    for col in list(dfFuelByMovesVeh):
        dfFuelByMovesVeh[col] = dfFuelByMovesVeh[col] + prorate(tmpdf[col],dfFuelByMovesVeh[col])
        dfFuelByMovesVeh[col] = dfFuelByMovesVeh[col].apply(round)

    # groups rms fuels into moves fuels
    movesFuelsDict = {'movesFuelType' : [fuel.getFuelDesc() for fuel in const.MovesFuelTypes]}
    dfMovesFuelsVeh = pd.DataFrame(movesFuelsDict)
    '''
    for movesFuel in const.MovesFuelTypes:
        movesFuelDesc = movesFuel.getFuelDesc()
        rmsFuelTypes = movesFuel.getRMSFuelTypes()
        if rmsFuelTypes:
            tmpdf = pd.DataFrame()
            for rmsFuelType in rmsFuelTypes:
                tmpdf += dfFuelByMovesVeh.loc[rmsFuelType]
            tmpdf.to_csv('./tempOutputs/%s.csv' % )
            dfMovesFuelsVeh = pd.concat([dfMovesFuelsVeh,tmpdf])

    # newdf.to_csv('./tempOutputs/newdf.csv')
    #dfRaw.to_csv('./tempOutputs/out_fuelDistrib.csv')
    dfFuelByMovesVeh.to_csv('./tempOutputs/dfFuelByMovesVeh_3.csv')
    '''
    dfMovesFuelsVeh.to_csv('./tempOutputs/dfMovesFuelsVeh.csv')


def prorate(val, distribList):
    distrib = np.asarray(distribList)
    distrib = val*distrib/np.sum(distrib)
    return distrib


def groupIntoMovesVehTypes(dfRaw):
    '''
    :param dfRaw:
    :return:
    '''
    dfFuelByMovesType = pd.DataFrame()
    dfFuelByMovesType['fuelType'] = dfRaw['fuelType']
    for movesType in const.MovesSourceTypes:
        typeDesc = movesType.getDesc()
        rmsTypes = movesType.getRMSVehTypes()
        if rmsTypes:
            dfFuelByMovesType[typeDesc] = 0
            for rmsType in rmsTypes:
                dfFuelByMovesType[typeDesc] += dfRaw[rmsType]

    return dfFuelByMovesType



