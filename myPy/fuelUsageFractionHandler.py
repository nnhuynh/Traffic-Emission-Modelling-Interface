import pandas as pd
import constants as const

fuelTypeIDs = [1, 2, 3, 4, 5, 9]


def prepareFuelUsageFrac():
    fUsageFrac = []
    for sourceBinFuelTypeID in fuelTypeIDs:
        if sourceBinFuelTypeID!=5:
            fuelID = sourceBinFuelTypeID
            fUsageFrac.append([const.userInputs.countyID.value,
                               const.userInputs.fuelYearID.value,
                               const.userInputs.modelYearGroupID.value,
                               sourceBinFuelTypeID,
                               fuelID,
                               1])
        else:
            fuelID = 1
            fUsageFrac.append([const.userInputs.countyID.value,
                               const.userInputs.fuelYearID.value,
                               const.userInputs.modelYearGroupID.value,
                               sourceBinFuelTypeID,
                               fuelID,
                               1])

            fuelID = 5
            fUsageFrac.append([const.userInputs.countyID.value,
                               const.userInputs.fuelYearID.value,
                               const.userInputs.modelYearGroupID.value,
                               sourceBinFuelTypeID,
                               fuelID,
                               0])

    dfUsageFrac = pd.DataFrame(data=fUsageFrac, columns=[const.FuelUsageFraction.col_countyID.value[0],
                                                         const.FuelUsageFraction.col_fuelYearID.value[0],
                                                         const.FuelUsageFraction.col_modelYearGroupID.value[0],
                                                         const.FuelUsageFraction.col_sourceBinFuelTypeID.value[0],
                                                         const.FuelUsageFraction.col_fuelSupplyFuelTypeID.value[0],
                                                         const.FuelUsageFraction.col_usageFraction.value[0]])
    return dfUsageFrac



