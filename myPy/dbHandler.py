import mysql.connector
from mysql.connector import Error
import sqlCommands
import constants as const

#=======================================================================================================================
def testConnection(hostname, username, password, dbname):
    try:
        mydb = mysql.connector.connect(host=hostname,user=username,passwd=password,database=dbname)
        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = mydb.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

#=======================================================================================================================
def mkNewDb(hostname, username, password, newDBname):
    try:
        connection = mysql.connector.connect(host=hostname,user=username,passwd=password)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % newDBname)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#=======================================================================================================================
def execSQLs(hostname, username, password, dbname, sqlCommands):
    try:
        mydb = mysql.connector.connect(host=hostname, user=username, passwd=password, database=dbname)
        if mydb.is_connected():
            cursor = mydb.cursor()
            for sqlCommand in sqlCommands:
                cursor.execute(sqlCommand)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

#=======================================================================================================================
def initDB(hostname, username, password, newDBname):
    mkNewDb(hostname, username, password, newDBname)

    mkTableCommands = []
    mkTableCommands.append(const.zoneMonthHourAttribs.createTableQuery.value)
    mkTableCommands.append(const.sourceTypeAgeDistribution.createTableQuery.value)
    mkTableCommands.append(const.linkSourceTypeHour.createTableQuery.value)
    mkTableCommands.append(const.opModeDistribution.createTableQuery.value)
    mkTableCommands.append(const.avft.createTableQuery.value)
    mkTableCommands.append(const.FuelFormulation.createTableQuery.value)
    mkTableCommands.append(const.FuelSupply.createTableQuery.value)
    mkTableCommands.append(const.FuelUsageFraction.createTableQuery.value)
    #for table in sqlCommands.Tables:
    #    mkTableCommands.append(table.value)
    execSQLs(hostname, username, password, newDBname, mkTableCommands)

#=======================================================================================================================
def insertData_ZoneMonthHour(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index,row in dfData.iterrows():
        monthID = row[const.zoneMonthHourAttribs.col_monthID.value[0]]
        zoneID = row[const.zoneMonthHourAttribs.col_zoneID.value[0]]
        hourID = row[const.zoneMonthHourAttribs.col_hourID.value[0]]
        temp = row[const.zoneMonthHourAttribs.col_temperature.value[0]]
        humid = row[const.zoneMonthHourAttribs.col_relHumidity.value[0]]
        sqlQuery = """ INSERT INTO %s (%s, %s, %s, %s, %s) VALUES (%d,%d,%d,%f,%f)""" % \
                      (const.zoneMonthHourAttribs.tablename.value,
                       const.zoneMonthHourAttribs.col_monthID.value[0],
                       const.zoneMonthHourAttribs.col_zoneID.value[0],
                       const.zoneMonthHourAttribs.col_hourID.value[0],
                       const.zoneMonthHourAttribs.col_temperature.value[0],
                       const.zoneMonthHourAttribs.col_relHumidity.value[0],
                       monthID, zoneID, hourID, temp, humid)
        sqlQueries.append(sqlQuery)

    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_SourceTypeAgeDistribution(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index,row in dfData.iterrows():
        ageID = row[const.sourceTypeAgeDistribution.col_ageID.value[0]]
        yearID = row[const.sourceTypeAgeDistribution.col_yearID.value[0]]
        sourceTypeID = row[const.sourceTypeAgeDistribution.col_sourceTypeID.value[0]]
        ageFrac = row[const.sourceTypeAgeDistribution.col_ageFraction.value[0]]
        sqlQuery = """ INSERT INTO %s (%s, %s, %s, %s) VALUES (%d,%d,%d,%f)""" % \
                   (const.sourceTypeAgeDistribution.tablename.value,
                    const.sourceTypeAgeDistribution.col_ageID.value[0],
                    const.sourceTypeAgeDistribution.col_yearID.value[0],
                    const.sourceTypeAgeDistribution.col_sourceTypeID.value[0],
                    const.sourceTypeAgeDistribution.col_ageFraction.value[0],
                    ageID, yearID, sourceTypeID, ageFrac)
        sqlQueries.append(sqlQuery)

    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_LinkSourceTypeHour(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index,row in dfData.iterrows():
        sourceTypeID = row[const.linkSourceTypeHour.col_sourceTypeID.value]
        linkID = row[const.linkSourceTypeHour.col_linkID.value]
        fraction = row[const.linkSourceTypeHour.col_sourceTypeHourFraction.value]
        sqlQuery = """ INSERT INTO %s (%s, %s, %s) VALUES (%d,%d,%f)""" % \
                   (const.linkSourceTypeHour.tablename.value,
                    const.linkSourceTypeHour.col_linkID.value,
                    const.linkSourceTypeHour.col_sourceTypeID.value,
                    const.linkSourceTypeHour.col_sourceTypeHourFraction.value,
                    linkID, sourceTypeID, fraction)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_opMode(hostname, username, password, dbname, dfData):
    # "sourceTypeID", "hourDayID", "linkID", "polProcessID", "opModeID", "opModeFraction"
    sqlQueries = []
    for index, row in dfData.iterrows():
        sourceTypeID = row[const.opModeDistribution.col_sourceTypeID.value[0]]
        hourDayID = row[const.opModeDistribution.col_hourDayID.value[0]]
        linkID = row[const.opModeDistribution.col_linkID.value[0]]
        polProcessID = row[const.opModeDistribution.col_polProcessID.value[0]]
        opModeID = row[const.opModeDistribution.col_opModeID.value[0]]
        opModeFraction = row[const.opModeDistribution.col_opModeFraction.value[0]]
        sqlQuery = """ INSERT INTO %s (%s, %s, %s, %s, %s, %s) VALUES (%d,%d,%d,%d,%d,%f)""" % \
                   (const.opModeDistribution.tablename.value,
                    const.opModeDistribution.col_sourceTypeID.value[0],
                    const.opModeDistribution.col_hourDayID.value[0],
                    const.opModeDistribution.col_linkID.value[0],
                    const.opModeDistribution.col_polProcessID.value[0],
                    const.opModeDistribution.col_opModeID.value[0],
                    const.opModeDistribution.col_opModeFraction.value[0],
                    sourceTypeID, hourDayID, linkID, polProcessID, opModeID, opModeFraction)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_avft(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index,row in dfData.iterrows():
        sourceTypeID = row[const.avft.col_sourceTypeID.value[0]]
        modelYearID = row[const.avft.col_modelYearID.value[0]]
        fuelTypeID = row[const.avft.col_fuelTypeID.value[0]]
        engTechID = row[const.avft.col_engTechID.value[0]]
        fraction = row[const.avft.col_fuelEngFraction.value[0]]
        sqlQuery = """ INSERT INTO %s (%s, %s, %s, %s, %s) VALUES (%d,%d,%d,%d,%f)""" % \
                     (const.avft.tablename.value,
                      const.avft.col_sourceTypeID.value[0],
                      const.avft.col_modelYearID.value[0],
                      const.avft.col_fuelTypeID.value[0],
                      const.avft.col_engTechID.value[0],
                      const.avft.col_fuelEngFraction.value[0],
                      sourceTypeID, modelYearID, fuelTypeID, engTechID, fraction)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_FuelFormulation(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index, row in dfData.iterrows():
        fuelFormulationID = row[const.FuelFormulation.col_fuelFormulationID.value[0]]
        fuelSubtypeID = row[const.FuelFormulation.col_fuelSubtypeID.value[0]]
        RVP = row[const.FuelFormulation.col_RVP.value[0]]
        sulfurLevel = row[const.FuelFormulation.col_sulfurLevel.value[0]]
        ETOHVolume = row[const.FuelFormulation.col_ETOHVolume.value[0]]
        MTBEVolume = row[const.FuelFormulation.col_MTBEVolume.value[0]]
        ETBEVolume = row[const.FuelFormulation.col_ETBEVolume.value[0]]
        TAMEVolume = row[const.FuelFormulation.col_TAMEVolume.value[0]]
        aromaticContent = row[const.FuelFormulation.col_aromaticContent.value[0]]
        olefinContent = row[const.FuelFormulation.col_olefinContent.value[0]]
        benzeneContent = row[const.FuelFormulation.col_benzeneContent.value[0]]
        e200 = row[const.FuelFormulation.col_e200.value[0]]
        e300 = row[const.FuelFormulation.col_e300.value[0]]
        volToWtPercentOxy = row[const.FuelFormulation.col_volToWtPercentOxy.value[0]]
        BioDieselEsterVolume = row[const.FuelFormulation.col_BioDieselEsterVolume.value[0]]
        CetaneIndex = row[const.FuelFormulation.col_CetaneIndex.value[0]]
        PAHContent = row[const.FuelFormulation.col_PAHContent.value[0]]
        T50 = row[const.FuelFormulation.col_T50.value[0]]
        T90 = row[const.FuelFormulation.col_T90.value[0]]
        sqlQuery = """ INSERT INTO %s (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) VALUES (%d,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f)""" % \
                   (const.FuelFormulation.tablename.value,
                    const.FuelFormulation.col_fuelFormulationID.value[0],
                    const.FuelFormulation.col_fuelSubtypeID.value[0],
                    const.FuelFormulation.col_RVP.value[0],
                    const.FuelFormulation.col_sulfurLevel.value[0],
                    const.FuelFormulation.col_ETOHVolume.value[0],
                    const.FuelFormulation.col_MTBEVolume.value[0],
                    const.FuelFormulation.col_ETBEVolume.value[0],
                    const.FuelFormulation.col_TAMEVolume.value[0],
                    const.FuelFormulation.col_aromaticContent.value[0],
                    const.FuelFormulation.col_olefinContent.value[0],
                    const.FuelFormulation.col_benzeneContent.value[0],
                    const.FuelFormulation.col_e200.value[0],
                    const.FuelFormulation.col_e300.value[0],
                    const.FuelFormulation.col_volToWtPercentOxy.value[0],
                    const.FuelFormulation.col_BioDieselEsterVolume.value[0],
                    const.FuelFormulation.col_CetaneIndex.value[0],
                    const.FuelFormulation.col_PAHContent.value[0],
                    const.FuelFormulation.col_T50.value[0],
                    const.FuelFormulation.col_T90.value[0],
                    fuelFormulationID,fuelSubtypeID,RVP,sulfurLevel,ETOHVolume,MTBEVolume,ETBEVolume,TAMEVolume,
                    aromaticContent,olefinContent,benzeneContent,e200,e300,volToWtPercentOxy,BioDieselEsterVolume,
                    CetaneIndex,PAHContent,T50,T90)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_FuelSupply(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index, row in dfData.iterrows():
        fuelRegionID = row[const.FuelSupply.col_fuelRegionID.value[0]]
        fuelYearID = row[const.FuelSupply.col_fuelYearID.value[0]]
        monthGroupID = row[const.FuelSupply.col_monthGroupID.value[0]]
        fuelFormulationID = row[const.FuelSupply.col_fuelFormulationID.value[0]]
        marketShare = row[const.FuelSupply.col_marketShare.value[0]]
        marketShareCV = row[const.FuelSupply.col_marketShareCV.value[0]]
        sqlQuery = """ INSERT INTO %s (%s,%s,%s,%s,%s,%s) VALUES (%d,%d,%d,%d,%f,%f)""" % \
                   (const.FuelSupply.tablename.value,
                    const.FuelSupply.col_fuelRegionID.value[0],
                    const.FuelSupply.col_fuelYearID.value[0],
                    const.FuelSupply.col_monthGroupID.value[0],
                    const.FuelSupply.col_fuelFormulationID.value[0],
                    const.FuelSupply.col_marketShare.value[0],
                    const.FuelSupply.col_marketShareCV.value[0],
                    fuelRegionID, fuelYearID, monthGroupID, fuelFormulationID, marketShare, marketShareCV)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)

#=======================================================================================================================
def insertData_FuelUsageFrac(hostname, username, password, dbname, dfData):
    sqlQueries = []
    for index, row in dfData.iterrows():
        countyID = row[const.FuelUsageFraction.col_countyID.value[0]]
        fuelYearID = row[const.FuelUsageFraction.col_fuelYearID.value[0]]
        modelYearGroupID = row[const.FuelUsageFraction.col_modelYearGroupID.value[0]]
        sourceBinFuelTypeID = row[const.FuelUsageFraction.col_sourceBinFuelTypeID.value[0]]
        fuelSupplyFuelTypeID = row[const.FuelUsageFraction.col_fuelSupplyFuelTypeID.value[0]]
        usageFraction = row[const.FuelUsageFraction.col_usageFraction.value[0]]
        sqlQuery = """ INSERT INTO %s (%s,%s,%s,%s,%s,%s) VALUES (%d,%d,%d,%d,%d,%f)""" % \
                   (const.FuelUsageFraction.tablename.value,
                    const.FuelUsageFraction.col_countyID.value[0],
                    const.FuelUsageFraction.col_fuelYearID.value[0],
                    const.FuelUsageFraction.col_modelYearGroupID.value[0],
                    const.FuelUsageFraction.col_sourceBinFuelTypeID.value[0],
                    const.FuelUsageFraction.col_fuelSupplyFuelTypeID.value[0],
                    const.FuelUsageFraction.col_usageFraction.value[0],
                    countyID, fuelYearID, modelYearGroupID, sourceBinFuelTypeID, fuelSupplyFuelTypeID, usageFraction)
        sqlQueries.append(sqlQuery)
    execSQLs(hostname, username, password, dbname, sqlQueries)





def execSQLs2(hostname, username, password, dbname, tablename, createTblSQL, sqlCommands):
    try:
        mydb = mysql.connector.connect(host=hostname, user=username, passwd=password, database=dbname)
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM %s" % tablename)
            if ~cursor.fetchone():
                cursor.execute(createTblSQL)

            for sqlCommand in sqlCommands:
                cursor.execute(sqlCommand)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")
