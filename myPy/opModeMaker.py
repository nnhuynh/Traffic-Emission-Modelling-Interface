import csv
import math
import pandas as pd
import getpass
from datetime import datetime
from enum import Enum

import constants as const

# value specifies congested state on a link. If congestIndex > congestion, drive cycle is congested
congestion = 2
resolutionOutHour = 'hour'
resolutionOutSec = 'second'
#outSecFile = 'outSec.csv'
#outHourFile = 'OpModes{}{}{}{}{}.csv'.format(datetime.now().day, '.', datetime.now().month, '.', datetime.now().year)
resolutionOut = resolutionOutHour

# pollution processses required for selected pollutants, here just CO, NOx & SO2
polProcesses = [
	201, 202, 215, 216, 217, 290, 291,
	301, 302, 315, 316, 317, 390, 391,
	3101, 3102, 3115, 3116, 3117, 3190, 3191,
	9101, 9102, 9190, 9191
	]

class trafficCols(Enum):
    timeEnterLink = 'timeEnterLink'
    timeOnLink = 'timeOnLink'
    vehID = 'vehID'
    pathID = 'pathID'
    linkID = 'linkID'
    linkSequencePath = 'linkSequenceInPath'


def makeOpMode(freeDriveFile, resDriveFile, artDriveFile, congDriveFile, linksFile, vspDataFile, trafficFile):
    '''
    :param freeDriveFile: '../data/CUEDC/driveFreeway.csv'
    :param resDriveFile: '../data/CUEDC/driveResidential.csv'
    :param artDriveFile: '../data/CUEDC/driveArterial.csv'
    :param congDriveFile: '../data/CUEDC/driveCongested.csv'
    :param linksFile: './tempOutputs/link_time.csv'
    :param vspDataFile: '../data/VSP_vehicle.csv'
    :param trafficFile: './tempOutputs/pathSummary.csv'
    :return:
    '''
    freeDrive = readInCSVFile(freeDriveFile)
    resDrive = readInCSVFile(resDriveFile)
    artDrive = readInCSVFile(artDriveFile)
    congDrive = readInCSVFile(congDriveFile)
    #links = readInCSVFile(linksFile)
    dfLinks = pd.read_csv(linksFile)
    dfLinks[const.link_timeCols.col_linkID.value] = dfLinks[const.link_timeCols.col_linkID.value].astype(int)
    dfLinks[const.link_timeCols.col_avTime_s.value] = dfLinks[const.link_timeCols.col_avTime_s.value].astype(float)
    dfLinks[const.link_timeCols.col_roadTypeID.value] = dfLinks[const.link_timeCols.col_roadTypeID.value].astype(int)
    #links = dict(zip(dfLinks[const.link_timeCols.col_linkID.value],
    #                 dfLinks[[const.link_timeCols.col_avTime_s.value, const.link_timeCols.col_roadTypeID.value]]))
    links = dfLinks.set_index(const.link_timeCols.col_linkID.value).to_dict()

    vspData = readInCSVFile(vspDataFile)
    #traffic = readInCSVFile(trafficFile) #vehicleID, linkID, timeEnterLink, timeOnLink, pathID, linkSequenceInPath
    traffic = pd.read_csv(trafficFile)

    srcTypes = [21]  # vehicles included in run, 21 = passenger car
    VSPDataDict = {}
    indx = 0
    for type in srcTypes:
        VSPDataDict[type] = vspData[indx]
        indx += 1

    opModeDict = {}  # accumulate counts of opmodes
    opOutRow = []

    for idx,veh in traffic.iterrows():
        currSourceType = 21  # CHANGE BACK WHEN CORRECT VEHICLE NUMBERING IS IN
        #  PLACEint(veh[0][:2])  # extract MOVES source type

        currLinkID = abs(int(veh[trafficCols.linkID.value]))  # ignore -ve direction term
        linkStartTime = float(veh[trafficCols.timeEnterLink.value])  # simulation time (secs) vehicle enters link
        currVehLinkTime = float(veh[trafficCols.timeOnLink.value])  # time vehicle spends on link

        linkExitTime = int(round(linkStartTime + currVehLinkTime))

        # retrieve link data
        #currLinkData = links[currLinkID]
        ## congestion index
        #congestIndex = currVehLinkTime / float(currLinkData[1])
        #currLinkType = int(currLinkData[2])
        congestIndex = currVehLinkTime / links[const.link_timeCols.col_avTime_s.value][currLinkID]
        currLinkType = links[const.link_timeCols.col_roadTypeID.value][currLinkID]

        #  identify appropriate drive cycle
        #  if currSourceType < 100:   # ****use smaller number here when heavy
        #  vehicles are installed. Currently only for cars & motorcycles
        if congestIndex > congestion:
            driveCycle = congDrive  # congestion drive cycle
        elif currLinkType == 5:
            driveCycle = resDrive  # residential drive cycle
        elif currLinkType == 2:
            driveCycle = artDrive  # arterial drive cycle
        else:
            driveCycle = freeDrive  # freeway drive cycle

        time = linkStartTime
        if currLinkID not in opModeDict:
            opModeDict[currLinkID] = {}
        if currSourceType not in opModeDict[currLinkID]:
            opModeDict[currLinkID][currSourceType] = {}

        if currVehLinkTime <= len(driveCycle):
            repeatCycle = 1
        else:
            repeatCycle = int(round(currVehLinkTime / len(driveCycle))) + 1

        for repeats in range(repeatCycle):  # repeat drive cycle for long & slow
            while time < linkExitTime:
                leave = False
                while not leave:
                    for sec in driveCycle:
                        '''
                        if const.userInputs.resolutionOut == resolutionOutHour:  # integer hour
                            timeRes = min(24, int(math.ceil(time / 3600 + 0.0001)))
                        elif const.userInputs.resolutionOut == resolutionOutSec:
                            timeRes = time
                        '''
                        timeRes = time # default const.userInputs.resolutionOut == resolutionOutSec
                        if resolutionOut == resolutionOutHour:  # integer hour
                            timeRes = min(24, int(math.ceil(time / 3600 + 0.0001)))

                        if timeRes not in opModeDict[currLinkID][currSourceType]:
                            opModeDict[currLinkID][currSourceType][timeRes] = {}

                        currSpeed = float(sec[1])
                        # if currSpeed is 0, use standing still, idling opmodes
                        opEvap = 300
                        opTyWr = 400
                        opPwr = 1
                        if currSpeed != 0:
                            opEvap, opTyWr = EvTyOpmodes(currSpeed)
                            #  calculate VSP using parameters from vehicle + drive
                            #  cycle files def VSP (A, B, C, M, v, v2, v3, a):
                            #  drive cycle: [time, speed, speed2, speed3, accel]
                            VSPParams = map(float,
                                            VSPDataDict[currSourceType][3:6]
                                            + sec[1:5])
                            #  currVSPData + currDriveData
                            #  calculate vehicle specific power:
                            #  (include gradient later)
                            currVSP = VSP(*VSPParams)
                            #  calculate power opmode
                            opPwr = PwrOpmode(currVSP, currSpeed)

                        for mode in [opEvap, opTyWr, opPwr, "countDiv3"]:
                            if mode not in opModeDict[currLinkID][currSourceType][timeRes]:
                                opModeDict[currLinkID][currSourceType][timeRes][mode] = 1
                            else:
                                opModeDict[currLinkID][currSourceType][timeRes][mode] += 1

                        time += 1
                        if time >= linkExitTime:
                            leave = True
                            break

    return writeModes(opModeDict)

def PwrOpmode(p, s):
    '''
    converts a vehicle VSP and speed to power opmode (numbers 11 to 40)
    Contacted US EPA re opmodes 16 and 26, both appear to be made redundant
    by the opmodes that follow them. 16 and 26 are currently not generated by
    this function
    NOTE: modified minimum speed for opmodes 12 through 16, from 1 mph to 0.5,
     to allow for Australian CUEDEC containing 0.6 mph. Consider modifying
     drive cycles instead?
    '''
    if p < 0:
        if s >= 0.5 and s < 25:
            opP = 11
        elif s >= 25 and s < 50:
            opP = 21
        else: #s >= 50:
            opP = 33
    elif s >= 0.5 and s < 25:
        opP = min(math.ceil(p/3 + 1.00001), 6) + 10
    elif s >= 25 and s < 50:
        if p < 12:
            opP = math.ceil(p/3 + 1.00001) + 20
        else:
            opP = min(math.ceil(p/6 + 4.00001), 10) + 20
    else: #s >= 50:
        if p < 6:
            opP = 33
        elif p >= 6 and p < 12:
            opP = 35
        else:
            opP = min(math.ceil(p/6 + 4.00001), 10) + 30
    return int(opP)


def VSP(A, B, C, v, v2, v3, a):
    '''
    calculates vehicle specific power required for MOVES opmodes
    parameters for A, B & C have been divided by M (mass) already
    NO GRADIENT YET- modify here & for calculation when gradient included
    '''
    # return ((A * v + B * v2 + C * v3) / M + (a + 9.8 * grade) * v)
    return (A * v + B * v2 + C * v3 + a*v)


def EvTyOpmodes(v):
    '''
    converts a vehicle speed to evaporative and tyre wear opmode numbers
    (301 to 316 and 401 to 416)
    '''
    mode = int(min(300 + math.ceil(v-2.49)/5+1, 316))
    return mode, 100 + mode

def readInCSVFile(filename):
    '''
    reads in csv files with unspecified delimiters, ignores header,
    if present. Output is list of lists delimited by newline
    characters & commas
    '''
    inFile = []
    with open(filename) as csvfile:
        hasHeader = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        dialect = csv.Sniffer().sniff(csvfile.read(10*1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)  # dialect defines delimiters
        if hasHeader:
            next(reader, None)
        else:
            csvfile.seek(0)
        for row in reader:
            inFile.append(row)
    return inFile


def writeModes(modeCount):
    '''
    convert counts of opmodes to fractions for each hour or second
    & output to MOVES csv datafile
    '''
    rows = []
    header = [const.opModeDistribution.col_sourceTypeID.value[0],
              const.opModeDistribution.col_hourDayID.value[0],
              const.opModeDistribution.col_linkID.value[0],
              const.opModeDistribution.col_polProcessID.value[0],
              const.opModeDistribution.col_opModeID.value[0],
              const.opModeDistribution.col_opModeFraction.value[0]]
    for linkOut in modeCount:
        for sourceTypID in modeCount[linkOut]:
            for second in modeCount[linkOut][sourceTypID]:
                modesOut = []
                secDict = modeCount[linkOut][sourceTypID][second]
                total = secDict.pop("countDiv3")  # extract opmode counter
                for key in secDict:
                    operModeFrac = int(secDict[key]) / (3 * int(total))
                    modesOut.append([key, operModeFrac])
                    # field names in opModeCount dictionary:
                    # [linkOut][sourceTypID][second]["countDiv3"]
                    # output fieldnames for csv file = [
                    # 'sourceTypeID', 'hourDayID', 'linkID',
                    # 'polProcessID', 'opModeID', 'opModeFraction']
                for process in polProcesses:
                    for modeResult in modesOut:
                        rows.append([sourceTypID, second, linkOut, process, modeResult[0], modeResult[1]])
    return pd.DataFrame.from_records(rows,columns=header)

