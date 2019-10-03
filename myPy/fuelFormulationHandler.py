import pandas as pd

def readInFile(fuelFormulationFile):
    dfFuelForm = pd.read_csv(fuelFormulationFile)
    dfFuelForm = dfFuelForm.fillna(-1)
    return dfFuelForm