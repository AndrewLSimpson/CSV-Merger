#Python CSV Merger
#Merges multiple csv files from a selected folder
#Andrew Simpson - andrewsimpson.dev

import glob
import os
import pandas as pd
import tkinter
from tkinter.filedialog import askdirectory

# Ask to open Folder
directorypath = askdirectory(title='Select a Folder') # shows dialog box and return the path
# get all the csv files
csvfiles = glob.glob(os.path.join(directorypath, '*.csv'))
# loop through the files and read them in with pandas
dataframes = []  # a list to hold all the individual pandas DataFrames
for csvfile in csvfiles:
    frames = pd.read_csv(csvfile)
    dataframes.append(frames)
# concatenate them all together
result = pd.concat(dataframes, ignore_index=True)
# print out to a new csv file
result.to_csv(directorypath + '\\combined-csv.csv')