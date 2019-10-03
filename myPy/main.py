import dbHandler
import constants as const
import meteoDataHandler as meteoData
import ageDistribDataHandler as ageDistribData
import aimsunDataHandler as aimsunData
import opModeMaker
import fuelDataHandler as fuelData
import fuelFormulationHandler as fuelFormulation
import fuelSupplyHandler as fuelSupply
import fuelUsageFractionHandler as fuelUsageFrac

import pandas as pd

if __name__=='__main__':
    
    dbHandler.initDB(const.mySQL.host.value, const.mySQL.user.value, 
                    const.mySQL.passwd.value, const.userInputs.newDB_in.value)
    print('finish initDB')

    
    dfData = meteoData.readMeteoData('../data/meteo/aberdeen.csv')
    dbHandler.insertData_ZoneMonthHour(const.mySQL.host.value, const.mySQL.user.value,
                                      const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                      dfData)
    print('finish insertData_ZoneMonthHour')


    dfSourceAgeFrac = ageDistribData.readAgeDistribData('../data/rms/ageDistrib.csv')
    dbHandler.insertData_SourceTypeAgeDistribution(const.mySQL.host.value, const.mySQL.user.value,
                                         const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                         dfSourceAgeFrac)
    print('finish insertData_SourceTypeAgeDistribution')


    pathSummary, link_time, dfLinkSourceTypeHour = aimsunData.readVehDetailedTrajec(
        '../data/wccAimsun/csvs/mivehdetailedtrajectory.csv', '../data/wccAimsun/csvs/mivehtrajectory.csv')
    pathSummary.to_csv('./tempOutputs/pathSummary.csv', index=False)
    link_time.to_csv('./tempOutputs/link_time.csv', index=False)
    dfLinkSourceTypeHour.to_csv('./tempOutputs/linkSourceTypeHour.csv', index=False)
    dbHandler.insertData_LinkSourceTypeHour(const.mySQL.host.value, const.mySQL.user.value,
                                            const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                            dfLinkSourceTypeHour)
    print('finish insertData_LinkSourceTypeHour')


    dfOpMode = opModeMaker.makeOpMode('../data/CUEDC/driveFreeway.csv', '../data/CUEDC/driveResidential.csv',
                           '../data/CUEDC/driveArterial.csv', '../data/CUEDC/driveCongested.csv',
                           './tempOutputs/link_time.csv', '../data/VSP_vehicle.csv', './tempOutputs/pathSummary.csv')
    #dfOpMode.to_csv('./tempOutputs/opMode.csv', index=False)
    dbHandler.insertData_opMode(const.mySQL.host.value, const.mySQL.user.value,
                                const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                dfOpMode)
    print('finish insertData_opMode')


    dfMovesFuelVeh = fuelData.readInFuelDistrib('../data/rms/fuelDistrib.csv')
    dfAVFT = fuelData.makeTableAVFT(dfMovesFuelVeh)
    #dfAVFT.to_csv('./tempOutputs/dfAVFT.csv', index=False)
    dbHandler.insertData_avft(const.mySQL.host.value, const.mySQL.user.value,
                              const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                              dfAVFT)
    print('finish insertData_avft')
    

    dfFuelForm = fuelFormulation.readInFile('../data/movesDefaultFuelFormulation.csv')
    dbHandler.insertData_FuelFormulation(const.mySQL.host.value, const.mySQL.user.value,
                                         const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                         dfFuelForm)
    print('finish insertData_FuelFormulation')



    dfFuelSupply = fuelSupply.prepareFuelSupply('../data/fuelSalesNSWJul2019_APS.csv')
    #dfFuelSupply.to_csv('./tempOutputs/dfFuelSupply.csv', index=False)
    dbHandler.insertData_FuelSupply(const.mySQL.host.value, const.mySQL.user.value,
                                    const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                    dfFuelSupply)


    dfUsageFrac = fuelUsageFrac.prepareFuelUsageFrac()
    #dfUsageFrac.to_csv('./tempOutputs/dfUsageFrac.csv', index=False)
    dbHandler.insertData_FuelUsageFrac(const.mySQL.host.value, const.mySQL.user.value,
                                    const.mySQL.passwd.value, const.userInputs.newDB_in.value, dfUsageFrac)

    print('yay')