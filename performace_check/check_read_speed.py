import pyasdf
import numpy as np 
import time

'''
this script compares the speed of reading ASDF files with different size
the ultimate goal is to find the best way to read a chunck of data stored in the xxx
'''

def read_data(sfile,nseg,data_type,path):
    with pyasdf.ASDFDataSet(sfile,mode='r') as ds:
        data_types = ds.auxiliary_data.list()
        if data_type not in data_types:
            raise ValueError('%s not in the data_type list'%data_type)
        paths = ds.auxiliary_data[data_type].list()
        if path not in paths:
            raise ValueError('%s not in the path list'%path)
        Nfft = ds.auxiliary_data[data_type][path].parameters['nfft']
        data = np.zeros((nseg,Nfft),dtype=np.complex64)
        data = ds.auxiliary_data[data_type][path].data[:]

def read_data1(sfile,indx1,indx2,data_type,path):
    with pyasdf.ASDFDataSet(sfile,mode='r') as ds:
        data_types = ds.auxiliary_data.list()
        if data_type not in data_types:
            raise ValueError('%s not in the data_type list'%data_type)
        paths = ds.auxiliary_data[data_type].list()
        if path not in paths:
            raise ValueError('%s not in the path list'%path)
        Nfft = ds.auxiliary_data[data_type][path].parameters['nfft']
        nseg = indx2-indx1+1
        data = np.zeros((nseg,Nfft),dtype=np.complex64)
        data = ds.auxiliary_data[data_type][path].data[indx1:indx2,:]

sfile1 = '/Users/chengxin/Documents/Harvard/Kanto_basin/Mesonet_BW/FFT/test/E.AYHM.h5'
sfile2 = '/Users/chengxin/Documents/Harvard/Kanto_basin/Mesonet_BW/FFT/E.AYHM.h5'
seg1   = 10
seg2   = 47
type1  = 'HNU'
type2  = 'HNU'
tag1   = '2010_12_20_1'
tag2   = '2010_12_20'

for ii in range(4):
    %time read_data(sfile1,seg1,type1,tag1)
    %time read_data1(sfile2,10,20,type2,tag2)
    %time read_data(sfile2,seg2,type2,tag2)
