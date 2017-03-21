import pprint
import pandas as pd

data_frame = pd.read_csv('delfiOutput.csv', sep='\t')

def new_data_frame(data_frame):
    shaped_dataframe = pd.DataFrame(data_frame)
    shaped_dataframe = shaped_dataframe.drop('string', 1)
    shaped_dataframe = shaped_dataframe.drop('Unnamed: 0', 1)
    return shaped_dataframe

def shape_data(data_frame, shaped_dataframe):

    #shaped_dataframe['time'] = data_frame['string'].str.extract('(....-..-.. ..:..)', expand=True)
    shaped_dataframe['ip adress'] = data_frame['string'].str.extract('(\d{2,3}.\d{3}.\d{3}.\d{3})', expand=True)
    #print data_frame['string'].str.contains('(\d{2,3}.\d{3}.\d{3}.\d{3})', regex=True)
    return shaped_dataframe

print shape_data(data_frame, new_data_frame(data_frame))
pprint