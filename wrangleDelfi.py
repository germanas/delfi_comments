import pprint
import pandas as pd
import re
from geoip import geolite2
import win_inet_pton
import ctypes
import numpy as np

data_frame = pd.read_csv('delfiOutput.csv', sep='\t')

def new_data_frame(data_frame):
    shaped_dataframe = pd.DataFrame(data_frame)
    shaped_dataframe = shaped_dataframe.drop('string', 1)
    shaped_dataframe = shaped_dataframe.drop('Unnamed: 0', 1)
    return shaped_dataframe

def find_country_from_ip(ip):
    newip = str(ip)
    match = geolite2.lookup(newip)
    if match is not None:
        return match.country





def shape_data(data_frame, shaped_dataframe, find_country_from_ip):

    shaped_dataframe['date'] = data_frame['string'].str.extract('(....-..-.. ..:..)', expand=True)
    shaped_dataframe['ip address'] = data_frame['string'].str.extract('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', expand=True)
    shaped_dataframe['date'], shaped_dataframe['time'] = shaped_dataframe['date'].str.split(' ', 1).str
    shaped_dataframe['text'] = data_frame['string'].str.extract('<div class="comment-content-inner">([\s\S]*?)<\/div>', expand=True)
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('\r\n\t\t\t\t\t\t\t\t\t', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('\r\n\t\t\t\t\t\t\t', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('<br />', '')
    shaped_dataframe['text'] = shaped_dataframe['text'].str.replace('<br/>', '')
    shaped_dataframe['thumbs_down'] = data_frame['string'].str.extract('<a href=\"javascript:void\(1\);\" onclick=\"CommentList\.voteThumbsDown\(.........\)\">([\s\S]*?)<\/a>', expand=True)
    shaped_dataframe['thumbs_down'] = shaped_dataframe['thumbs_down'].str.replace('\r\n\t\t\t\t\t\t\t ', '')
    shaped_dataframe['thumbs_down'] = shaped_dataframe['thumbs_down'].str.replace('\r\n<span></span>', '')
    shaped_dataframe['thumbs_down'] = shaped_dataframe['thumbs_down'].str.replace('\r\n\t\t\t\t\t\t\t', '')

    shaped_dataframe['thumbs_up'] = data_frame['string'].str.extract('<a href=\"javascript:void\(1\);\" onclick=\"CommentList\.voteThumbsUp\(.........\)\">([\s\S]*?)<\/a>', expand=True)
    shaped_dataframe['thumbs_up'] = shaped_dataframe['thumbs_up'].str.replace('\r\n\t\t\t\t\t\t\t ', '')
    shaped_dataframe['thumbs_up'] = shaped_dataframe['thumbs_up'].str.replace('\r\n<span></span>', '')
    shaped_dataframe['thumbs_up'] = shaped_dataframe['thumbs_up'].str.replace('\r\n\t\t\t\t\t\t\t', '')
    shaped_dataframe['country'] = shaped_dataframe['ip address']
    shaped_dataframe['country'] = shaped_dataframe['country'].astype(str)
    df_not_missing = shaped_dataframe.dropna()
    df_not_missing['country'] = df_not_missing['country'].apply(find_country_from_ip)
    #print data_frame['string'].str.contains('(\d{2,3}.\d{3}.\d{3}.\d{3})', regex=True)

    return df_not_missing

good_data_set = shape_data(data_frame, new_data_frame(data_frame),  find_country_from_ip)

print sum(pd.isnull(good_data_set['ip address']))
print good_data_set
good_data_set.to_csv('delfiout.csv', sep='\t', encoding='utf-8')

#good_data_set['country']


