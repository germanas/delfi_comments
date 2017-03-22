import pprint
import pandas as pd
import re

data_frame = pd.read_csv('delfiOutput.csv', sep='\t')

def new_data_frame(data_frame):
    shaped_dataframe = pd.DataFrame(data_frame)
    shaped_dataframe = shaped_dataframe.drop('string', 1)
    shaped_dataframe = shaped_dataframe.drop('Unnamed: 0', 1)
    return shaped_dataframe


def shape_data(data_frame, shaped_dataframe):

    shaped_dataframe['date'] = data_frame['string'].str.extract('(....-..-.. ..:..)', expand=True)
    shaped_dataframe['ip address'] = data_frame['string'].str.extract('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', expand=True)
    shaped_dataframe['date'], shaped_dataframe['time'] = shaped_dataframe['date'].str.split(' ', 1).str
    shaped_dataframe['text'] = data_frame['string'].str.extract('<div class="comment-content-inner">([\s\S]*?)<\/div>', expand=True)
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('\r\n\t\t\t\t\t\t\t\t\t', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('\r\n\t\t\t\t\t\t\t', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('<br />', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('<br/>', '')
    #print data_frame['string'].str.contains('(\d{2,3}.\d{3}.\d{3}.\d{3})', regex=True)
    return shaped_dataframe

good_data_set = shape_data(data_frame, new_data_frame(data_frame))

print sum(pd.isnull(good_data_set['ip address']))
print good_data_set
good_data_set.to_csv('delfiout.csv', sep='\t', encoding='utf-8')