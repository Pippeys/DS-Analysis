import bs4 as bs
import urllib.request
import lxml
import pandas as pd
import numpy as np
import re
import time

#Scraping CL for type of drive
def drive_scrape(urllist):
    drive_pattern = re.compile(r'(<span>drive:.*?<b>)(.*?)(<\/b><\/span>)')
    dri = []
    for i in urllist:
        time.sleep(60)
        sauce = urllib.request.urlopen(i)
        soup = bs.BeautifulSoup(sauce,'lxml')
        data = soup.find_all('div', class_='mapAndAttrs')
        for result in data:
            for child in result.children:
                results = drive_pattern.search(str(child))
                if results:
                    a = (results.group(2))
                    dri.append(a)
                else:
                    a = 'NaN'
                    dri.append(a)
    return dri

#Scraping CL for condition
def condition_scrape(urllist):
    condition_pattern = re.compile(r'(<span>condition:.*?<b>)(.*?)(<\/b><\/span>)')
    cond = []
    for i in urllist:
        time.sleep(60)
        sauce = urllib.request.urlopen(i)
        soup = bs.BeautifulSoup(sauce,'lxml')
        data = soup.find_all('div', class_='mapAndAttrs')
        for result in data:
            for child in result.children:
                results = condition_pattern.search(str(child))
                if results:
                    a = (results.group(2))
                    cond.append(a)
                else:
                    a = 'NaN'
                    cond.append(a)
    return cond

#Scraping CL for odometer measurement
def odometer_scrape(urllist):
    odometer_pattern = re.compile(r'(<span>odometer:.*?<b>)(.*?)(<\/b><\/span>)')
    odo = []
    for i in urllist:
        time.sleep(60)
        sauce = urllib.request.urlopen(i)
        soup = bs.BeautifulSoup(sauce,'lxml')
        data = soup.find_all('div', class_='mapAndAttrs')
        for result in data:
            for child in result.children:
                results = odometer_pattern.search(str(child))
                if results:
                    a = (results.group(2))
                    odo.append(a)
                else:
                    a = 'NaN'
                    odo.append(a)
    return odo




#Load in Tacoma List without Odometer measurement
def main():
    trucks = 'C:/Users/Scott/Desktop/Data/Tacoma_list.csv'
    df = pd.read_csv(trucks)
    del df ['geotag']
    del df ['Unnamed: 0']
    urllist = df["url"].tolist()
    dri = drive_scrape(urllist)``
    cond = condition_scrape(urllist)
    odo = odometer_scrape(urllist)
#Compiling new columns and export DF to new csv
    se = pd.Series(dri)
    df['drive'] = se.values
    se = pd.Series(cond)
    df['condition'] = se.values
    se = pd.Series(odo)
    df['odometer'] = se.values

    df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_full_db.csv')

if __name__ == '__main__':
    main()
