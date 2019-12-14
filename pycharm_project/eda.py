#================== Wifi fingerprinting ====================
#Libraries
import pandas as pd
import matplotlib.pyplot as plt

trainset = pd.read_csv(
    "C:/Users/edison/Documents/Ubiqum/Data Analytics Course/Module_III_Wifi/pycharm_project/data/trainingData.csv",
    header = 0)

trainset.head()