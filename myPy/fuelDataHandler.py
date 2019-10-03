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

    # gets the total number of Light Trailers in rms fuel data
    nLightTrailers = dfRaw[const.rmsVehTypes.lightTrailers.value].sum()
    # prorates a fraction of the total number of light trailers across the number of scooters
    dfRaw[const.rmsVehTypes.scooters.value] += prorate(int(nLightTrailers*const.userInputs.lightTrailerScooterFactor.value),
                                                      dfRaw[const.rmsVehTypes.scooters.value])
    #dfRaw.to_csv('./tempOutputs/dfRaw.csv', index=False)

    # groups rms vehicles into moves sources (i.e. vehicles)
    dfRmsFuelMovesVeh = groupIntoMovesVehTypes(dfRaw)
    #dfRmsFuelMovesVeh.to_csv('./tempOutputs/dfRmsFuelMovesVeh_1.csv')
    #dfRmsFuelMovesVeh.to_csv('./tempOutputs/dfRmsFuelMovesVeh.csv', index=False)

    # prorates rows 'Unknown' and 'No engine' into other rows
    dfRmsFuelMovesVeh = dfRmsFuelMovesVeh.set_index('fuelType')
    tmpdf = dfRmsFuelMovesVeh.loc['Unknown'] + dfRmsFuelMovesVeh.loc['No engine']
    dfRmsFuelMovesVeh = dfRmsFuelMovesVeh.drop(['Unknown','No engine'])
    for col in list(dfRmsFuelMovesVeh):
        dfRmsFuelMovesVeh[col] = dfRmsFuelMovesVeh[col] + prorate(tmpdf[col],dfRmsFuelMovesVeh[col])
        dfRmsFuelMovesVeh[col] = dfRmsFuelMovesVeh[col].apply(round)
    #dfRmsFuelMovesVeh.to_csv('./tempOutputs/dfRmsFuelMovesVeh_2.csv')

    #dfRmsFuelMovesVeh.loc['MOVESDiesel'] = dfRmsFuelMovesVeh.loc['Diesel'] + dfRmsFuelMovesVeh.loc['Diesel NAT']

    movesFuelsDesc = const.MovesFuelTypes.getAllFuelDesc()
    dfMovesFuelVeh = pd.DataFrame({col: np.zeros(len(movesFuelsDesc)) for col in list(dfRmsFuelMovesVeh)})
    dfMovesFuelVeh['fuelType'] = movesFuelsDesc
    dfMovesFuelVeh = dfMovesFuelVeh.set_index('fuelType')
    #dfMovesFuelVeh.to_csv('./tempOutputs/dfMovesFuelVeh.csv')

    for movesFuel in const.MovesFuelTypes:
        rmsFuelTypes = movesFuel.getRMSFuelTypes()
        for rmsFuel in rmsFuelTypes:
            dfMovesFuelVeh.loc[movesFuel.getFuelDesc()] += dfRmsFuelMovesVeh.loc[rmsFuel]
    #dfMovesFuelVeh.to_csv('./tempOutputs/dfMovesFuelVeh_2.csv')
    return dfMovesFuelVeh

def makeTableAVFT(dfMovesFuelVeh, year=2019):
    avft = []
    for sourceDesc in list(dfMovesFuelVeh):
        sourceTypeID = const.MovesSourceTypes.getSourceTypeByDesc(sourceDesc).getSourceTypeID()
        nVehsThisSource = dfMovesFuelVeh[sourceDesc].sum()
        for fuelDesc in list(dfMovesFuelVeh.index):
            movesFuelID = const.MovesFuelTypes.getFuelbyDesc(fuelDesc).getFuelID()
            engTechID = const.MovesFuelTypes.getFuelbyDesc(fuelDesc).getEngTechID()
            fraction = dfMovesFuelVeh[sourceDesc].loc[fuelDesc]/nVehsThisSource
            avft.append([sourceTypeID, year, movesFuelID, engTechID, fraction])

    dfAVFT = pd.DataFrame(data=avft, columns=[const.avft.col_sourceTypeID.value[0],
                                              const.avft.col_modelYearID.value[0],
                                              const.avft.col_fuelTypeID.value[0],
                                              const.avft.col_engTechID.value[0],
                                              const.avft.col_fuelEngFraction.value[0]])
    return dfAVFT

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



