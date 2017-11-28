from craigslist import CraigslistForSale
import urllib.request
import bs4 as bs
import lxml
import time
import re


import pandas as pd
import numpy as np

import time
from random import randint




def finder(places):
    finder_list = []
    for x in places:
        CL_FS = CraigslistForSale(site = x, category = 'cta',
                        filters={
                        'min_price': 2000,
                        'max_price': 30000,
                        'make': 'toyota tacoma',
                        'min_year': 2000,
                        'max_year': 2017,
                        'max_miles': 200000})
        x_list = []

        for x_result in CL_FS.get_results(sort_by='newest'):
            finder_list.append(x_result)
            print(x)
            time.sleep(randint(10,30))

    return finder_list


def scrape(urllist):
    drive_pattern = re.compile(r'(<span>drive:.*?<b>)(.*?)(<\/b><\/span>)')
    condition_pattern = re.compile(r'(<span>condition:.*?<b>)(.*?)(<\/b><\/span>)')
    odometer_pattern = re.compile(r'(<span>odometer:.*?<b>)(.*?)(<\/b><\/span>)')
    title_pattern = re.compile(r'(<span>title status:.*?<b>)(.*?)(<\/b><\/span>)')

    biglist = []

    for i in range(len(urllist)):
        row= ['NaN','NaN','NaN', 'NaN']

        print('Iteration: {}'.format(i))

        sauce = urllib.request.urlopen(urllist[i])
        soup = bs.BeautifulSoup(sauce,'lxml')
        data = soup.find_all('div', class_='mapAndAttrs')

        for result in data:
            for child in result.children:
                status_result = title_pattern.search(str(child))
                dri_result = drive_pattern.search(str(child))
                cond_result = condition_pattern.search(str(child))
                odo_result = odometer_pattern.search(str(child))

                if status_result:
                    a = (status_result.group(2))
                    row[0]=a
                    print('Found status!')

                if dri_result:
                    a = (dri_result.group(2))
                    row[1]=a
                    print('Found drive!')


                if cond_result:
                    b = (cond_result.group(2))
                    row[2]=b
                    print('Found condition!')


                if odo_result:
                    c = (odo_result.group(2))
                    row[3] = c
                    print('Found odometer!')

        biglist.append(row)
        print(row)


        print('Waiting...')
        time.sleep(randint(45,70))

    return biglist

def main():
#CraigslistForSale search and parse
    places = ['sfbay','fresno','sacramento','chico','merced','modesto','siskiyou','redding','stockton','visalia','hanford','bakersfield','slo','losangeles','palmsprings','sandiego','portland','southbend','medford','seattle','reno','lasvegas','phoenix','tucson']
    finder_list = finder(places)
#Transforming into DataFrame
    df = pd.DataFrame(finder_list)
    df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_Data/Tacoma_New.csv')
#Load in Tacoma List without Odometer measurement
    del df ['geotag']
    urllist = df["url"].tolist()
    biglist = scrape(urllist)
#Compiling new columns and export DF to new csv
    new_df = pd.DataFrame(biglist)
    new_df.columns = ['status','drive','condition','odometer']
    df = pd.concat([df,new_df], axis=1)
    df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_Data/Tacoma_New.csv')
    print('Done')

if __name__ == '__main__':
    main()
