import dbHandler
import constants as const
import meteoDataHandler as meteoData
import ageDistribDataHandler as ageDistribData
import aimsunDataHandler as aimsunData
import opModeMaker
import fuelDataHandler as fuelData

import pandas as pd

if __name__=='__main__':
    '''
    dbHandler.initDB(const.mySQL.host.value, const.mySQL.user.value, 
                    const.mySQL.passwd.value, const.userInputs.newDB_in.value)
    '''

    '''
    dfData = meteoData.readMeteoData('../data/meteo/aberdeen.csv')
    dbHandler.insertData_ZoneMonthHour(const.mySQL.host.value,
                                      const.mySQL.user.value,
                                      const.mySQL.passwd.value,
                                      const.userInputs.newDB_in.value,
                                      dfData)
    '''

    '''
    dfSourceAgeFrac = ageDistribData.readAgeDistribData('../data/registered vehicles/ageDistrib.csv')
    dbHandler.insertData_SourceTypeAgeDistribution(const.mySQL.host.value,
                                         const.mySQL.user.value,
                                         const.mySQL.passwd.value,
                                         const.userInputs.newDB_in.value,
                                         dfSourceAgeFrac)
    '''

    '''
    pathSummary, link_time, dfLinkSourceTypeHour = aimsunData.readVehDetailedTrajec(
        '../data/wccAimsun/csvs/mivehdetailedtrajectory.csv', '../data/wccAimsun/csvs/mivehtrajectory.csv')
    pathSummary.to_csv('./tempOutputs/pathSummary.csv', index=False)
    link_time.to_csv('./tempOutputs/link_time.csv', index=False)
    dfLinkSourceTypeHour.to_csv('./tempOutputs/linkSourceTypeHour.csv', index=False)
    dbHandler.insertData_LinkSourceTypeHour(const.mySQL.host.value, const.mySQL.user.value,
                                            const.mySQL.passwd.value, const.userInputs.newDB_in.value,
                                            dfLinkSourceTypeHour)
    '''

    '''
    dfOpMode = opModeMaker.makeOpMode('../data/CUEDC/driveFreeway.csv',
                           '../data/CUEDC/driveResidential.csv',
                           '../data/CUEDC/driveArterial.csv',
                           '../data/CUEDC/driveCongested.csv',
                           './tempOutputs/link_time.csv',
                           '../data/VSP_vehicle.csv',
                           './tempOutputs/pathSummary.csv')
    #dfOpMode.to_csv('./tempOutputs/opMode.csv', index=False)
    dbHandler.insertData_opMode(const.mySQL.host.value,
                                const.mySQL.user.value,
                                const.mySQL.passwd.value,
                                const.userInputs.newDB_in.value,
                                dfOpMode)
    '''

    fuelData.readInFuelDistrib('../data/rms/fuelDistrib.csv')

    print('yay')