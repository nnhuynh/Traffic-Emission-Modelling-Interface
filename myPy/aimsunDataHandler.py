import pandas as pd
import constants as const


def readVehDetailedTrajec(vehDetailedTrajecFile, vehTrajecFile):
    dfVehDetailedTrajec = pd.read_csv(vehDetailedTrajecFile)

    pathSummary = makePathSummary(dfVehDetailedTrajec)
    # pathSummary.to_csv('./tempOutputs/pathSummary.csv', index=False)
    link_time = makeLinkTime(pathSummary)
    #link_time.to_csv('./tempOutputs/link_time.csv', index=False)

    linkSourceTypeHour = makeLinkSourceTypeHour(pathSummary, vehTrajecFile)
    #linkSourceTypeHour.to_csv('./tempOutputs/linkSourceTypeHour.csv', index=False)

    return pathSummary, link_time, linkSourceTypeHour


def makeLinkSourceTypeHour(pathSummary, vehTrajecFile):
    dfVehTrajec = pd.read_csv(vehTrajecFile,
                              usecols=[const.vehTrajecCols.col_oid.value, const.vehTrajecCols.col_sid.value])
    mergePathSummary = pd.merge(left=pathSummary[[const.pathSummaryCols.col_vehID.value,
                                                  const.pathSummaryCols.col_linkID.value,
                                                  const.pathSummaryCols.col_timeOnLink.value]],
                                right=dfVehTrajec,
                                how='left',
                                left_on=const.pathSummaryCols.col_vehID.value,
                                right_on=const.vehTrajecCols.col_oid.value)
    dfVehTrajec.drop([const.vehTrajecCols.col_oid.value,const.vehTrajecCols.col_sid.value], axis=1)
    # mergePathSummary.to_csv('./tempOutputs/mergePathSummary.csv',index=False)

    linkSourceTypeHour = pd.DataFrame()
    for linkID in mergePathSummary[const.pathSummaryCols.col_linkID.value].unique():
        dfThisLink = mergePathSummary.loc[mergePathSummary[const.pathSummaryCols.col_linkID.value] == linkID]
        dfThisLink['movesSource'] = dfThisLink[const.vehTrajecCols.col_sid.value].map(const.aimsunMovesSources)

        newdf = pd.DataFrame()
        newdf[const.linkSourceTypeHourCols.col_sourceTypeHourFraction.value] = \
            dfThisLink.groupby('movesSource').sum()[const.pathSummaryCols.col_timeOnLink.value] / \
            dfThisLink[const.pathSummaryCols.col_timeOnLink.value].sum()
        newdf[const.linkSourceTypeHourCols.col_linkID.value] = linkID
        newdf[const.linkSourceTypeHourCols.col_sourceTypeID.value] = newdf.index
        # newdf.to_csv('./tempOutputs/newdfLink%d.csv' % linkID, index=False)

        linkSourceTypeHour = pd.concat([linkSourceTypeHour, newdf])

    return linkSourceTypeHour


def makeLinkTime(pathSummary):
    link_time = pd.DataFrame()
    link_time['vehCounts'] = pathSummary.groupby('linkID').count()[const.pathSummaryCols.col_vehID.value]
    link_time['sumTimeOnLink'] = pathSummary.groupby('linkID').sum()[const.pathSummaryCols.col_timeOnLink.value]
    link_time[const.link_timeCols.col_avTime_s.value] = link_time['sumTimeOnLink'] / link_time['vehCounts']
    link_time[const.link_timeCols.col_roadTypeID.value] = const.defaultRoadTypeID
    link_time = link_time.drop(['vehCounts', 'sumTimeOnLink'], axis=1)
    link_time[const.link_timeCols.col_linkID.value] = link_time.index
    return link_time


def makePathSummary(dfRaw):
    pathSummary = pd.DataFrame()
    colsUsed = [const.aimsunCols.col_oid.value,
                const.aimsunCols.col_ent.value,
                const.aimsunCols.col_sectionId.value,
                const.aimsunCols.col_timeSta.value]

    for vehID in dfRaw[const.aimsunCols.col_oid.value].unique():
        vehPaths = dfRaw[colsUsed].loc[dfRaw[const.aimsunCols.col_oid.value] == vehID]
        vehPaths['path'] = (vehPaths['ent'] < vehPaths['ent'].shift(1)).astype(int).cumsum()
        for pathID in vehPaths['path'].unique():
            vehPath = vehPaths.loc[vehPaths['path'] == pathID]
            pathSum = pd.DataFrame()

            pathSum[const.pathSummaryCols.col_timeEnterLink.value] = \
                vehPath.groupby(const.aimsunCols.col_sectionId.value).min()[const.aimsunCols.col_timeSta.value]

            pathSum[const.pathSummaryCols.col_timeOnLink.value] = \
                vehPath.groupby(const.aimsunCols.col_sectionId.value).max()[const.aimsunCols.col_timeSta.value] - \
                pathSum[const.pathSummaryCols.col_timeEnterLink.value]

            pathSum[const.pathSummaryCols.col_timeOnLink.value] = pathSum[const.pathSummaryCols.col_timeOnLink.value].\
                apply(lambda x: max(x, const.aimsunVehTrajecDataFreq))

            pathSum[const.pathSummaryCols.col_vehID.value] = vehID
            pathSum[const.pathSummaryCols.col_pathID.value] = pathID
            pathSum[const.pathSummaryCols.col_linkID.value] = pathSum.index
            pathSum = pathSum.sort_values(by=[const.pathSummaryCols.col_timeEnterLink.value])

            pathSum[const.pathSummaryCols.col_linkSequenceInPath.value] = \
                range(0, len(pathSum[const.pathSummaryCols.col_linkID.value]))

            # pathSum.to_csv('./tempOutputs/vehID%d_%d.csv' % (vehID,pathID))
            pathSummary = pd.concat([pathSummary, pathSum])

    return pathSummary
