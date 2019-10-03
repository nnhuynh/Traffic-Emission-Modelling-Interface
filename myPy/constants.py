from enum import Enum
from datetime import datetime

sampleDB_in = 'testrun558a1_in'

class userInputs(Enum):
    newDB_in = 'ku'
    monthID = 7
    yearID = 2019
    zoneID = 203100
    lightTrailerScooterFactor = .1 # i.e. 1 light trailer is equivalent to .1 scooter (in RMS data)
    fuelRegionID = 100000000
    countyID = 1091
    fuelYearID = 2019
    modelYearGroupID = 0


class mySQL(Enum):
    host = '127.0.0.1'
    user = 'root'
    passwd = 'password'



aimsunVehTrajecDataFreq = 0.8 #seconds
defaultRoadTypeID = 5 # residential?

aimsunMovesSources = {53: 21,
                     56: 32,
                     58: 42,
                     62: 21}


class aimsunCols(Enum):
    col_did = 'did'
    col_oid = 'oid'
    col_ent = 'ent'
    col_sectionId = 'sectionId'
    col_laneIndex = 'laneIndex'
    col_xCoord = 'xCoord'
    col_yCoord = 'yCoord'
    col_timeSta = 'timeSta'
    col_speed = 'speed'
    col_travelledDistance = 'travelledDistance'
    col_acceleration = 'acceleration'

class vehTrajecCols(Enum):
    col_oid = 'oid'
    col_sid = 'sid'

class link_timeCols(Enum):
    col_linkID = 'linkID'
    col_avTime_s = 'avTime_s'
    col_roadTypeID = 'roadTypeID'

class pathSummaryCols(Enum):
    col_vehID = 'vehID'
    col_pathID = 'pathID'
    col_linkID = 'linkID'
    col_linkSequenceInPath = 'linkSequenceInPath'
    col_timeOnLink = 'timeOnLink'
    col_timeEnterLink = 'timeEnterLink'

class linkSourceTypeHourCols(Enum):
    col_sourceTypeID = 'sourceTypeID'
    col_linkID = 'linkID'
    col_sourceTypeHourFraction = 'sourceTypeHourFraction'

class rmsFuelTypes(Enum):
    unleadedPetrol = 'Unleaded Petrol'
    petrol = 'Petrol'
    lpg = 'LPG'
    electricPetrol = 'Electric Petrol'
    electricity = 'Electricity'
    petrolLPG = 'Petrol And LPG (Dual Fuel)'
    diesel = 'Diesel'
    dieselLPG = 'Diesel And LPG (Dual Fuel)'
    dieselLPT = 'Diesel  LPT (Torque Topping)'
    dieselNAT = 'Diesel NAT'
    cng = 'Compressed Natural Gas'
    petrolCNG = 'Petrol  Compressed Natural Gas'
    lng = 'Liquid Natural Gas'
    hydrogen = 'Hydrogen'
    kerosene = 'Kerosene'
    petrolKerosene = 'Petrol  Kerosene (Dual Fuel)'
    steamOilPwred = 'Steam (Fuel Oil Powered)'
    steamPetrolPwred = 'Steam (Petrol Powered)'
    steamDieselPwred = 'Steam (Diesel Powered)'
    steamCoalPwred= 'Steam (Coal Burning Powered)'
    unknown = 'Unknown'
    noEngine = 'No engine'

class MovesFuelTypes(Enum):
    gasoline = {'desc': 'Gasoline', 'fuelTypeID': 1,
                'rmsFuelTypes': [rmsFuelTypes.unleadedPetrol.value,
                                 rmsFuelTypes.petrol.value,
                                 rmsFuelTypes.lpg.value,
                                 rmsFuelTypes.electricPetrol.value,
                                 rmsFuelTypes.petrolLPG.value,
                                 rmsFuelTypes.petrolCNG.value,
                                 rmsFuelTypes.kerosene.value,
                                 rmsFuelTypes.petrolKerosene.value,
                                 rmsFuelTypes.steamOilPwred.value,
                                 rmsFuelTypes.steamPetrolPwred.value],
                'engTechID': 1}
    diesel = {'desc': 'Diesel Fuel', 'fuelTypeID': 2,
              'rmsFuelTypes': [rmsFuelTypes.diesel.value,
                               rmsFuelTypes.dieselLPG.value,
                               rmsFuelTypes.dieselLPT.value,
                               rmsFuelTypes.dieselNAT.value,
                               rmsFuelTypes.steamDieselPwred.value,
                               rmsFuelTypes.steamCoalPwred.value],
              'engTechID': 1}
    cng = {'desc': 'Compressed Natural Gas(CNG)', 'fuelTypeID': 3,
           'rmsFuelTypes': [rmsFuelTypes.cng.value,
                            rmsFuelTypes.lng.value,
                            rmsFuelTypes.hydrogen.value],
           'engTechID': 1}
    ethanol = {'desc': 'Ethanol(E - 85)', 'fuelTypeID': 5,
               'rmsFuelTypes': [],
               'engTechID': 1}
    electricity = {'desc': 'Electricity', 'fuelTypeID': 9,
                   'rmsFuelTypes': [rmsFuelTypes.electricity.value],
                   'engTechID': 30}

    def getRMSFuelTypes(self):
        return self.value['rmsFuelTypes']

    def getFuelID(self):
        return self.value['fuelTypeID']

    def getFuelDesc(self):
        return self.value['desc']

    def getEngTechID(self):
        return self.value['engTechID']

    @classmethod
    def getFuelbyDesc(cls,desc):
        for fuel in cls:
            if fuel.getFuelDesc()==desc:
                return fuel
        return None

    @classmethod
    def getAllFuelDesc(cls):
        fuelDesc = []
        for fuel in cls:
            fuelDesc.append(fuel.getFuelDesc())
        return fuelDesc

class rmsVehTypes(Enum):
    passengerVehicles = 'Passenger Vehicles'
    offroadVehicles = 'Off-road Vehicles'
    peopleMovers = 'People movers'
    smallBuses = 'Small Buses'
    mobileHomes = 'Mobile Homes'
    motorCycles = 'Motor cycles'
    scooters = 'Scooters'
    lightTrucks = 'Light Trucks'
    lightPlants = 'Light Plants'
    lightTrailers = 'Light Trailers'
    otherVehicles = 'Other Vehicles'
    buses = 'Buses'
    heavyTrucks = 'Heavy Trucks'
    primeMovers = 'Prime Movers'
    heavyPlants = 'Heavy Plants'
    heavyTrailers = 'Heavy Trailers'


class MovesSourceTypes(Enum):
    motorcycle = {'desc': 'Motorcycle', 'sourceTypeID': 11,
                  'rmsVehTypes': [rmsVehTypes.motorCycles.value, rmsVehTypes.scooters.value]}
    passengerCar = {'desc': 'Passenger Car', 'sourceTypeID': 21,
                    'rmsVehTypes': [rmsVehTypes.passengerVehicles.value]}
    passengerTruck = {'desc': 'Passenger Truck', 'sourceTypeID': 31,
                      'rmsVehTypes': [rmsVehTypes.offroadVehicles.value]}
    lightCommercialTruck = {'desc': 'Light Commercial Truck', 'sourceTypeID': 32,
                            'rmsVehTypes': [rmsVehTypes.lightTrucks.value, rmsVehTypes.lightPlants.value]}
    intercityBus = {'desc': 'Intercity Bus', 'sourceTypeID': 41,
                    'rmsVehTypes': []}
    transitBus = {'desc': 'Transit Bus', 'sourceTypeID': 42,
                  'rmsVehTypes': [rmsVehTypes.peopleMovers.value, rmsVehTypes.smallBuses.value, rmsVehTypes.buses.value]}
    schoolBus = {'desc': 'School Bus', 'sourceTypeID': 43,
                 'rmsVehTypes': []}
    refuseTruck = {'desc': 'Refuse Truck', 'sourceTypeID': 51,
                   'rmsVehTypes': []}
    sglUnitShortTruck = {'desc': 'Single Unit Short-haul Truck', 'sourceTypeID': 52,
                         'rmsVehTypes': [rmsVehTypes.heavyTrucks.value, rmsVehTypes.primeMovers.value]}
    sglUnitLongTruck = {'desc': 'Single Unit Long-haul Truck', 'sourceTypeID': 53,
                        'rmsVehTypes': []}
    motorHome = {'desc': 'Motor Home', 'sourceTypeID': 54,
                 'rmsVehTypes': [rmsVehTypes.mobileHomes.value]}
    combShortTruck = {'desc': 'Combination Short-haul Truck', 'sourceTypeID': 61,
                      'rmsVehTypes': [rmsVehTypes.heavyPlants.value]}
    combLongTruck = {'desc': 'Combination Long-haul Truck', 'sourceTypeID': 62,
                     'rmsVehTypes': []}

    def getSourceTypeID(self):
        return self.value['sourceTypeID']

    def getDesc(self):
        return self.value['desc']

    def getRMSVehTypes(self):
        return self.value['rmsVehTypes']

    @classmethod
    def getSourceTypeByDesc(cls, sourceDesc):
        for source in cls:
            if sourceDesc==source.getDesc():
                return source
        return None


class APSFuelTypes(Enum):
    ron95_97 = {'desc': '95-97 RON', 'fuelSubTypeID': 10, 'FuelFormulationID': 10, 'fuelTypeID': 1}
    ronOver98 = {'desc': '98+ RON', 'fuelSubTypeID': 10, 'FuelFormulationID': 10, 'fuelTypeID': 1}
    ronUnder95 = {'desc': '<95 RON', 'fuelSubTypeID': 10, 'FuelFormulationID': 10, 'fuelTypeID': 1}
    e10 = {'desc': 'Ethanol-blended fuel', 'fuelSubTypeID': 12, 'FuelFormulationID': 1002, 'fuelTypeID': 1}
    diesel = {'desc': 'Diesel oil', 'fuelSubTypeID': 20, 'FuelFormulationID': 20, 'fuelTypeID': 2}

    def getDesc(self):
        return self.value['desc']

    def getFuelTypeID(self):
        return self.value['fuelTypeID']

    @classmethod
    def getDescSameFuelTypeID(cls):
        descTypeID = {}
        for type in cls:
            if type.getFuelTypeID() not in descTypeID:
                descTypeID[type.getFuelTypeID()] = [type.getDesc()]
            else:
                descThisType = descTypeID[type.getFuelTypeID()]
                descThisType.append(type.getDesc())
                descTypeID[type.getFuelTypeID()] = descThisType
        return descTypeID


class sourceTypeAgeDistribution(Enum):
    tablename = 'sourcetypeagedistribution'
    col_sourceTypeID = ['sourceTypeID']
    col_yearID = ['yearID']
    col_ageID = ['ageID']
    col_ageFraction = ['ageFraction']
    createTableQuery = "CREATE TABLE sourcetypeagedistribution (" \
                                "sourceTypeID smallint(6) NOT NULL DEFAULT '0'," \
                                "yearID smallint(6) NOT NULL DEFAULT '0'," \
                                "ageID smallint(6) NOT NULL DEFAULT '0'," \
                                "ageFraction double DEFAULT NULL," \
                                "PRIMARY KEY (ageID,sourceTypeID,yearID)," \
                                "KEY sourceTypeID (sourceTypeID)," \
                                "KEY yearID (yearID)," \
                                "KEY ageID (ageID)" \
                                ") ENGINE=MyISAM DEFAULT CHARSET=latin1"


class zoneMonthHourAttribs(Enum):
    tablename = 'zonemonthhour'
    col_monthID = ['monthID']
    col_zoneID = ['zoneID']
    col_hourID = ['hourID']
    col_temperature = ['temperature']
    col_temperatureCV = ['temperatureCV']
    col_relHumidity = ['relHumidity']
    col_heatIndex = ['heatIndex']
    col_specificHumidity = ['specificHumidity']
    col_relativeHumidityCV = ['relativeHumidityCV']
    createTableQuery = "CREATE TABLE zonemonthhour (" \
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

class linkSourceTypeHour(Enum):
    tablename = 'linksourcetypehour'
    col_linkID = 'linkID'
    col_sourceTypeID = 'sourceTypeID'
    col_sourceTypeHourFraction = 'sourceTypeHourFraction'
    createTableQuery = "CREATE TABLE linksourcetypehour (" \
                         "linkID int(11) NOT NULL," \
                         "sourceTypeID smallint(6) NOT NULL," \
                         "sourceTypeHourFraction float DEFAULT NULL," \
                         "PRIMARY KEY (linkID,sourceTypeID)," \
                         "KEY sourceTypeID (sourceTypeID,linkID)" \
                         ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

class opModeDistribution(Enum):
    tablename = 'opmodedistribution'
    col_sourceTypeID = ['sourceTypeID']
    col_hourDayID = ['hourDayID']
    col_linkID = ['linkID']
    col_polProcessID = ['polProcessID']
    col_opModeID = ['opModeID']
    col_opModeFraction = ['opModeFraction']
    col_opModeFractionCV = ['opModeFractionCV']
    col_isUserInput = ['isUserInput']
    createTableQuery = "CREATE TABLE opmodedistribution (" \
                         "sourceTypeID smallint(6) NOT NULL DEFAULT '0'," \
                         "hourDayID smallint(6) NOT NULL DEFAULT '0'," \
                         "linkID int(11) NOT NULL DEFAULT '0'," \
                         "polProcessID int(11) NOT NULL DEFAULT '0'," \
                         "opModeID smallint(6) NOT NULL DEFAULT '0'," \
                         "opModeFraction float DEFAULT NULL," \
                         "opModeFractionCV float DEFAULT NULL," \
                         "isUserInput char(1) NOT NULL DEFAULT 'N'," \
                         "PRIMARY KEY (hourDayID,linkID,opModeID,polProcessID,sourceTypeID)," \
                         "KEY sourceTypeID (sourceTypeID)," \
                         "KEY hourDayID (hourDayID)," \
                         "KEY linkID (linkID)," \
                         "KEY polProcessID (polProcessID)," \
                         "KEY opModeID (opModeID)" \
                         ") ENGINE=MyISAM DEFAULT CHARSET=latin1"

class avft(Enum):
    tablename = 'avft'
    col_sourceTypeID = ['sourceTypeID']
    col_modelYearID = ['modelYearID']
    col_fuelTypeID = ['fuelTypeID']
    col_engTechID = ['engTechID']
    col_fuelEngFraction = ['fuelEngFraction']
    createTableQuery = "CREATE TABLE avft (" \
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

class FuelFormulation(Enum):
    tablename = 'fuelformulation'
    col_fuelFormulationID = ['fuelFormulationID']
    col_fuelSubtypeID = ['fuelSubtypeID']
    col_RVP = ['RVP']
    col_sulfurLevel = ['sulfurLevel']
    col_ETOHVolume = ['ETOHVolume']
    col_MTBEVolume = ['MTBEVolume']
    col_ETBEVolume = ['ETBEVolume']
    col_TAMEVolume = ['TAMEVolume']
    col_aromaticContent = ['aromaticContent']
    col_olefinContent = ['olefinContent']
    col_benzeneContent = ['benzeneContent']
    col_e200 = ['e200']
    col_e300 = ['e300']
    col_volToWtPercentOxy = ['volToWtPercentOxy']
    col_BioDieselEsterVolume = ['BioDieselEsterVolume']
    col_CetaneIndex = ['CetaneIndex']
    col_PAHContent = ['PAHContent']
    col_T50 = ['T50']
    col_T90 = ['T90']
    createTableQuery = "CREATE TABLE fuelformulation (" \
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

class FuelSupply(Enum):
    tablename = 'fuelsupply'
    col_fuelRegionID = ['fuelRegionID']
    col_fuelYearID = ['fuelYearID']
    col_monthGroupID = ['monthGroupID']
    col_fuelFormulationID = ['fuelFormulationID']
    col_marketShare = ['marketShare']
    col_marketShareCV = ['marketShareCV']
    createTableQuery = "CREATE TABLE fuelsupply (" \
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

class FuelUsageFraction(Enum):
    tablename = 'fuelusagefraction'
    col_countyID = ['countyID']
    col_fuelYearID = ['fuelYearID']
    col_modelYearGroupID = ['modelYearGroupID']
    col_sourceBinFuelTypeID = ['sourceBinFuelTypeID']
    col_fuelSupplyFuelTypeID = ['fuelSupplyFuelTypeID']
    col_usageFraction = ['usageFraction']
    createTableQuery = "CREATE TABLE fuelusagefraction (" \
                        "countyID int(11) NOT NULL," \
                        "fuelYearID int(11) NOT NULL," \
                        "modelYearGroupID int(11) NOT NULL," \
                        "sourceBinFuelTypeID smallint(6) NOT NULL," \
                        "fuelSupplyFuelTypeID smallint(6) NOT NULL," \
                        "usageFraction double DEFAULT NULL," \
                        "PRIMARY KEY (countyID,fuelYearID,modelYearGroupID,sourceBinFuelTypeID,fuelSupplyFuelTypeID)" \
                        ") ENGINE=MyISAM DEFAULT CHARSET=latin1"