import glob
import pandas as pd
# defining root path 
path ="E:/TelevisionNews/"
filenames = glob.glob(path + "/*.csv")
# creating empty list
dataFrames = list()
# iterating through CSV file in current directory
for filename in filenames:
    dataFrames.append(pd.read_csv(filename))
# # Concatenate all data into one DataFrame
merged_frame = pd.concat(dataFrames,axis=1)
# print merged dataframe
print(merged_frame)