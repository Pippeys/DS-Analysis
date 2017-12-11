from craigslist import CraigslistForSale
import urllib.request
import bs4 as bs
import lxml
import time
import re


import pandas as pd
import numpy as np

import time


def sf_tacomas():
    CL_FS = CraigslistForSale(site = 'sfbay', category = 'cta',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    sf_list = []

    for sf_result in CL_FS.get_results(sort_by='newest'):
        print('SF')
        time.sleep(60)
        sf_list.append(sf_result)
    return sf_list

def fresno_tacomas():
    CL_FS = CraigslistForSale(site = 'fresno',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    f_list = []

    for f_result in CL_FS.get_results(sort_by='newest'):
        print('Fresno')
        time.sleep(60)
        f_list.append(f_result)
    return f_list

def stockton_tacomas():
    CL_FS = CraigslistForSale(site = 'stockton',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    stock_list = []

    for stock_result in CL_FS.get_results(sort_by='newest'):
        time.sleep(60)
        print('Stockton')
        stock_list.append(stock_result)
    return stock_list

def portland_tacomas():
    CL_FS = CraigslistForSale(site = 'portland',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    port_list = []
    for port_result in CL_FS.get_results(sort_by='newest'):
        port_list.append(port_result)
        print('Portland')
        time.sleep(60)
    return port_list

def reno_tacomas():
    CL_FS = CraigslistForSale(site = 'reno',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    reno_list = []
    for reno_result in CL_FS.get_results(sort_by='newest'):
        reno_list.append(reno_result)
        print('reno')
        time.sleep(60)
    return reno_list

def lv_tacomas():
    CL_FS = CraigslistForSale(site = 'lasvegas',
                        filters={
                        'min_price': 5000,
                        'max_price': 20000,
                        'make': 'toyota tacoma',
                        'min_year': 2010,
                        'max_year': 2017,
                        'max_miles': 100000})
    lv_list = []
    for lv_result in CL_FS.get_results(sort_by='newest'):
        lv_list.append(lv_result)
        print('las vegas')
        time.sleep(60)
    return lv_list


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
                    print('Found drive!')

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
        time.sleep(60)

    return biglist

def main():
#CraigslistForSale search and parse
    sf_list = sf_tacomas()
    f_list = fresno_tacomas()
    stock_list =stockton_tacomas()
    port_list = portland_tacomas()
    reno_list = reno_tacomas()
    lv_list = lv_tacomas()
#Compiling lists
    cl_list = sf_list + f_list + stock_list + port_list + reno_list + lv_list
#Transforming into DataFrame
    df = pd.DataFrame(cl_list)

#Load in Tacoma List without Odometer measurement
    del df ['geotag']
    urllist = df["url"].tolist()
    biglist = scrape(urllist)
#Compiling new columns and export DF to new csv
    new_df = pd.DataFrame(biglist)
    new_df.columns = ['status','drive','condition','odometer']
    df = pd.concat([df,new_df], axis=1)
    df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_New.csv')
    print('Done')

if __name__ == '__main__':
    main()
