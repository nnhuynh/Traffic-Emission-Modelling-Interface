from enum import Enum


class Tables(Enum):
    avft = "CREATE TABLE avft (" \
           "sourceTypeID smallint(6) NOT NULL," \
           "modelYearID smallint(6) NOT NULL," \
           "fuelTypeID smallint(6) NOT NULL," \
           "engTechID smallint(6) NOT NULL," \
           "fuelEngFraction double NOT NULL," \
           "PRIMARY KEY (sourceTypeID,modelYearID,fuelTypeID,engTechID)," \
           "KEY sourceTypeID (sourceTypeID)," \
           "KEY modelYearID (modelYearID)," \
           "KEY fuelTypeID (fuelTypeID)," \
           "KEY engTechID (engTechID)" \
           ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    fuelFormulation = "CREATE TABLE fuelformulation (" \
                      "fuelFormulationID smallint(6) NOT NULL DEFAULT '0'," \
                      "fuelSubtypeID smallint(6) NOT NULL DEFAULT '0'," \
                      "RVP float DEFAULT NULL," \
                      "sulfurLevel float NOT NULL DEFAULT '30'," \
                      "ETOHVolume float DEFAULT NULL," \
                      "MTBEVolume float DEFAULT NULL," \
                      "ETBEVolume float DEFAULT NULL," \
                      "TAMEVolume float DEFAULT NULL," \
                      "aromaticContent float DEFAULT NULL," \
                      "olefinContent float DEFAULT NULL," \
                      "benzeneContent float DEFAULT NULL," \
                      "e200 float DEFAULT NULL," \
                      "e300 float DEFAULT NULL," \
                      "volToWtPercentOxy float DEFAULT NULL," \
                      "BioDieselEsterVolume float DEFAULT NULL," \
                      "CetaneIndex float DEFAULT NULL," \
                      "PAHContent float DEFAULT NULL," \
                      "T50 float DEFAULT NULL," \
                      "T90 float DEFAULT NULL," \
                      "PRIMARY KEY (fuelFormulationID)" \
                      ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    fuelSupply = "CREATE TABLE fuelsupply (" \
                 "fuelRegionID int(11) NOT NULL DEFAULT '0'," \
                 "fuelYearID smallint(6) NOT NULL DEFAULT '0'," \
                 "monthGroupID smallint(6) NOT NULL DEFAULT '0'," \
                 "fuelFormulationID smallint(6) NOT NULL DEFAULT '0'," \
                 "marketShare float DEFAULT NULL," \
                 "marketShareCV float DEFAULT NULL," \
                 "PRIMARY KEY (fuelRegionID,fuelFormulationID,monthGroupID,fuelYearID)," \
                 "KEY fuelRegionID (fuelRegionID)," \
                 "KEY yearID (fuelYearID)," \
                 "KEY monthGroupID (monthGroupID)," \
                 "KEY fuelSubtypeID (fuelFormulationID)" \
                 ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

    fuelUsageFraction = "CREATE TABLE fuelusagefraction (" \
                        "countyID int(11) NOT NULL," \
                        "fuelYearID int(11) NOT NULL," \
                        "modelYearGroupID int(11) NOT NULL," \
                        "sourceBinFuelTypeID smallint(6) NOT NULL," \
                        "fuelSupplyFuelTypeID smallint(6) NOT NULL," \
                        "usageFraction double DEFAULT NULL," \
                        "PRIMARY KEY (countyID,fuelYearID,modelYearGroupID,sourceBinFuelTypeID,fuelSupplyFuelTypeID)" \
                        ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

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

    zoneMonthHour = "CREATE TABLE zonemonthhour (" \
                    "monthID smallint(6) NOT NULL DEFAULT '0'," \
                    "zoneID int(11) NOT NULL DEFAULT '0'," \
                    "hourID smallint(6) NOT NULL DEFAULT '0'," \
                    "temperature float DEFAULT NULL," \
                    "temperatureCV float DEFAULT NULL," \
                    "relHumidity float DEFAULT NULL," \
                    "heatIndex float DEFAULT NULL," \
                    "specificHumidity float DEFAULT NULL," \
                    "relativeHumidityCV float DEFAULT NULL," \
                    "PRIMARY KEY (hourID,monthID,zoneID)," \
                    "KEY monthID (monthID)," \
                    "KEY zoneID (zoneID)," \
                    "KEY hourID (hourID)" \
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