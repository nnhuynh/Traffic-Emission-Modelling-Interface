from enum import Enum

class Tables(Enum):
    hotellingActivityDistribution = "CREATE TABLE hotellingactivitydistribution (" \
                                    "beginModelYearID smallint(6) NOT NULL," \
                                    "endModelYearID smallint(6) NOT NULL," \
                                    "opModeID smallint(6) NOT NULL," \
                                    "opModeFraction float NOT NULL," \
                                    "PRIMARY KEY (beginModelYearID,endModelYearID,opModeID)" \
                                    ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    imCoverage = "CREATE TABLE imcoverage (" \
                 "polProcessID int(11) NOT NULL DEFAULT '0'," \
                 "stateID smallint(6) NOT NULL DEFAULT '0'," \
                 "countyID int(11) NOT NULL DEFAULT '0'," \
                 "yearID smallint(6) NOT NULL DEFAULT '0'," \
                 "sourceTypeID smallint(6) NOT NULL DEFAULT '0'," \
                 "fuelTypeID smallint(6) NOT NULL DEFAULT '0'," \
                 "IMProgramID smallint(6) NOT NULL DEFAULT '0'," \
                 "begModelYearID smallint(6) NOT NULL DEFAULT '0'," \
                 "endModelYearID smallint(6) NOT NULL DEFAULT '0'," \
                 "inspectFreq smallint(6) DEFAULT NULL," \
                 "testStandardsID smallint(6) NOT NULL DEFAULT '0'," \
                 "useIMyn char(1) NOT NULL DEFAULT 'Y'," \
                 "complianceFactor float DEFAULT NULL," \
                 "PRIMARY KEY (polProcessID,stateID,countyID,yearID,sourceTypeID,fuelTypeID,IMProgramID)" \
                 ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    driveScheduleSecondLink = "CREATE TABLE driveschedulesecondlink (" \
                              "linkID int(11) NOT NULL," \
                              "secondID smallint(6) NOT NULL," \
                              "speed float DEFAULT NULL," \
                              "grade float NOT NULL DEFAULT '0'," \
                              "PRIMARY KEY (linkID,secondID)," \
                              "KEY secondID (secondID,linkID)" \
                              ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    link = "CREATE TABLE link (" \
           "linkID int(11) NOT NULL DEFAULT '0'," \
           "countyID int(11) NOT NULL DEFAULT '0'," \
           "zoneID int(11) DEFAULT NULL," \
           "roadTypeID smallint(6) NOT NULL DEFAULT '0'," \
           "linkLength float DEFAULT NULL," \
           "linkVolume float DEFAULT NULL," \
           "linkAvgSpeed float DEFAULT NULL," \
           "linkDescription varchar(50) DEFAULT NULL," \
           "linkAvgGrade float DEFAULT NULL," \
           "PRIMARY KEY (linkID)," \
           "KEY countyID (countyID)," \
           "KEY zoneID (zoneID)," \
           "KEY roadTypeID (roadTypeID)" \
           ") ENGINE=MyISAM DEFAULT CHARSET=latin1"


    offNetworkLink = "CREATE TABLE offnetworklink (" \
                     "sourceTypeID smallint(6) NOT NULL," \
                     "zoneID int(11) NOT NULL DEFAULT '0'," \
                     "vehiclePopulation float DEFAULT NULL," \
                     "startFraction float DEFAULT NULL," \
                     "extendedIdleFraction float DEFAULT NULL," \
                     "parkedVehicleFraction float DEFAULT NULL," \
                     "PRIMARY KEY (zoneID,sourceTypeID)," \
                     "KEY sourceTypeID (sourceTypeID,zoneID)" \
                     ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    onRoadRetrofit = "CREATE TABLE onroadretrofit (" \
                     "pollutantID smallint(6) NOT NULL," \
                     "processID smallint(6) NOT NULL," \
                     "fuelTypeID smallint(6) NOT NULL," \
                     "sourceTypeID smallint(6) NOT NULL," \
                     "retrofitYearID smallint(6) NOT NULL," \
                     "beginModelYearID smallint(6) NOT NULL," \
                     "endModelYearID smallint(6) NOT NULL," \
                     "cumFractionRetrofit double NOT NULL DEFAULT '0'," \
                     "retrofitEffectiveFraction double NOT NULL DEFAULT '0'," \
                     "PRIMARY KEY (pollutantID,processID,fuelTypeID,sourceTypeID,retrofitYearID,beginModelYearID,endModelYearID)," \
                     "KEY retrofitYearID (retrofitYearID)" \
                     ") ENGINE=MyISAM DEFAULT CHARSET=latin1"