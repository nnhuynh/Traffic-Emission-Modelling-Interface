import pandas as pd
import constants as const

def prepareFuelSupply(fuelSalesFile, fuelRegionID=const.userInputs.fuelRegionID.value,
                      fuelYearID=const.userInputs.yearID.value, monthGroupID=const.userInputs.monthID.value):
    dfRaw = pd.read_csv(fuelSalesFile)
    ronSum = dfRaw['95-97 RON'] + dfRaw['98+ RON'] + dfRaw['<95 RON']
    ethanolSum = dfRaw['Ethanol-blended fuel']
    petrolSum = ronSum + ethanolSum
    dieselSum = dfRaw['Diesel oil']

    fuelSupply = []
    fuelSupply.append([fuelRegionID, fuelYearID, monthGroupID, 10, float(ronSum/petrolSum), 0.5])
    fuelSupply.append([fuelRegionID, fuelYearID, monthGroupID, 1002, float(ethanolSum/petrolSum), 0.5])
    fuelSupply.append([fuelRegionID, fuelYearID, monthGroupID, 20, float(dieselSum/dieselSum), 0.5])
    print(fuelSupply)

    dfFuelSupply = pd.DataFrame(data=fuelSupply, columns=[const.FuelSupply.col_fuelRegionID.value[0],
                                                          const.FuelSupply.col_fuelYearID.value[0],
                                                          const.FuelSupply.col_monthGroupID.value[0],
                                                          const.FuelSupply.col_fuelFormulationID.value[0],
                                                          const.FuelSupply.col_marketShare.value[0],
                                                          const.FuelSupply.col_marketShareCV.value[0]])
    '''
    descByTypeID = const.APSFuelTypes.getDescSameFuelTypeID()

    for key in descByTypeID.keys():
        colList = descByTypeID[key]
        dfRaw[colList].sum()

    '''

    return dfFuelSupply
