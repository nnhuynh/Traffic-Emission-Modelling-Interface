from enum import Enum
from datetime import datetime

sampleDB_in = 'testrun558a1_in'

class userInputs(Enum):
    newDB_in = 'ku'
    monthID = 7
    yearID = 2019
    zoneID = 203100


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
                                 rmsFuelTypes.steamPetrolPwred.value,
                                 ]}
    diesel = {'desc': 'Diesel Fuel', 'fuelTypeID': 2,
              'rmsFuelTypes': [rmsFuelTypes.diesel.value,
                               rmsFuelTypes.dieselLPG.value,
                               rmsFuelTypes.dieselLPT.value,
                               rmsFuelTypes.dieselNAT.value,
                               rmsFuelTypes.steamDieselPwred.value,
                               rmsFuelTypes.steamCoalPwred.value]}
    cng = {'desc': 'Compressed Natural Gas(CNG)', 'fuelTypeID': 3,
           'rmsFuelTypes': [rmsFuelTypes.cng.value,
                            rmsFuelTypes.lng.value,
                            rmsFuelTypes.hydrogen.value]}
    ethanol = {'desc': 'Ethanol(E - 85)', 'fuelTypeID': 5,
               'rmsFuelTypes': []}
    electricity = {'desc': 'Electricity', 'fuelTypeID': 9,
                   'rmsFuelTypes': [rmsFuelTypes.electricity.value]}

    def getRMSFuelTypes(self):
        return self.value['rmsFuelTypes']

    def getFuelDesc(self):
        return self.value['desc']

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