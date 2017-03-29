#python3
#List of Angels
import bs4 as bs
import urllib.request
import csv
import lxml

#def San_Fran():
SF_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last24Hrs&stateid=7&keyword=san%20francisco&entriesperpage=50').read()
SF_soup = bs.BeautifulSoup(SF_sauce, 'lxml')
SF_data = SF_soup.find_all('div', class_='obitName')
angel_list=[]

for div in SF_data:
    name = (div.text)
    angel=[name]
    angel_list.append(angel)

with open('SF_angles.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in angel_list:
        csv_writer.writerow(row)

OAK_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Oakland&entriesperpage=50').read()
OAK_soup = bs.BeautifulSoup(OAK_sauce, 'lxml')
OAK_data = OAK_soup.find_all('div', class_='obitName')
angel_list=[]

for div in OAK_data:
    name = (div.text)
    angel=[name]
    angel_list.append(angel)

with open('OAK_angles.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in angel_list:
        csv_writer.writerow(row)

SJ_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=San%20Jose&entriesperpage=50')
SJ_soup = bs.BeautifulSoup(SJ_sauce, 'lxml')
SJ_data = SJ_soup.find_all('div', class_='obitName')
angel_list=[]

for div in SJ_data:
    name = (div.text)
    angel=[name]
    angel_list.append(angel)

with open('SJ_angels.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in angel_list:
        csv_writer.writerow(row)





#python3
#List of Angels
import bs4 as bs
import urllib.request
import csv
import lxml
import pandas as pd


def San_Fran(SF_data):
    angel_list=[]
    for div in SF_data:
        name = (div.text)
        angel=[name]
        angel_list.append(angel)
    return angel_list


def Oak(Oak_data):
    angel_list = []
    for div in OAK_data:
        name = (div.text)
        angel=[name]
        angel_list.append(angel)
    return angel_list

def write_csv(angel_list):
    raw_data = angel_list
    df = pd.DataFrame(raw_data)
    df.to_csv('Angels.csv')
#        with open('Angles.csv', 'w') as file:
#            csv_writer = csv.writer(file)
#            for row in angel_list:
#                csv_writer.writerow(row)


def main():
    SF_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last24Hrs&stateid=7&keyword=san%20francisco&entriesperpage=50').read()
    SF_soup = bs.BeautifulSoup(SF_sauce, 'lxml')
    SF_data = SF_soup.find_all('div', class_='obitName')
    OAK_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Oakland&entriesperpage=50').read()
    OAK_soup = bs.BeautifulSoup(OAK_sauce, 'lxml')
    OAK_data = OAK_soup.find_all('div', class_='obitName')
    SF_list = San_Fran(SF_data)
    Oak_list = Oak(OAK_data)
    write_csv(angel_list)
