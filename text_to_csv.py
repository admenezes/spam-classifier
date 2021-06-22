# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:44:28 2021

@author: aston
"""
import pandas as pd
import glob
import os

if __name__ == "__main__":
    masterfile = open('spam_master.txt','a')
    file_location = os.path.join('C:/Users/aston/Desktop/Alston/7th sem/COE70A/Enron/enron1/spam','*.txt')
    filenames = glob.glob(file_location)
    for i in filenames:
        w = open(i,'a')
        w.write('\t1')
        w.close()
    for i in filenames:
        f = open(i,'r', encoding="")
        text = f.read()
        f.close()
        text = text.replace('\n', ' ')
        masterfile.write(text+ '\n')
    masterfile.close()
        
    with open('C:/Users/aston/Desktop/Alston/7th sem/COE70A/spam_master.txt') as m:
        mtext = m.read()
        df = pd.DataFrame(mtext.split("\n"))
        df.columns = ['text']
        df.to_csv('enron_spam.csv',sep='\t',index=False,encoding='utf-8')
   