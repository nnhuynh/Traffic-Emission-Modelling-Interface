import mysql.connector
from mysql.connector import Error
import sqlCommands
import constants as const

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


def initDB(hostname, username, password, newDBname):
    mkNewDb(hostname, username, password, newDBname)
    mkTableCommands = []
    for table in sqlCommands.Tables:
        mkTableCommands.append(table.value)
    execSQLs(hostname, username, password, newDBname, mkTableCommands)


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