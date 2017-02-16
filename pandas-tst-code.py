# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:25:38 2017

@author: roger_taylor
"""

#urllib3 (note that urllib2 is for python ver 2.x)
#for https certs use certifi package which uses Mozilla's root cert bundle

import pandas as pd
import pandas_datareader as web
from pandas import DataFrame, read_csv
import matplotlib as plt
from matplotlib import style
import numpy as np
import urllib3
from urllib.request import urlretrieve
import certifi

style.use("ggplot")

#Create pool manager that handles http requests and https requests.
http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED',
                           ca_certs = certifi.where())

#Create variable that will contain the link with the file
webdata ='http://sdw.ecb.europa.eu/export.do?trans=N&node=bbn2889&exportType=csv&SERIES_KEY=124.MIR.M.U2.B.L21.A.R.A.2240.EUR.N'
#Pull the file from the url pool and save as data.csv
urlretrieve(webdata , 'data.csv')
#Create column names for import into pandas
Colnames = ["date", "percent"]
#import file into pandas with column names set to "date" and "percent"
eurodata = pd.read_csv('data.csv', sep=",", header=None,
                       names=Colnames)
#clean data to remove first 5 rows (usless str data not needed for computation)
eurodata.drop(eurodata.index[[0,1,2,3,4]], inplace=True)
#reset index after row drop
eurodata = eurodata.reset_index(drop=True)

#Create cleaned dataset into a dataframe.
subeurodata =pd.DataFrame(eurodata, columns=Colnames)



