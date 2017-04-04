#python3
#List of Angels
import bs4 as bs
import urllib.request
import csv
import lxml
import pandas as pd


def ala(ala_data):
    ala_list = []
    for div in ala_data:
        name = (div.text)
        angel=[name]
        ala_list.append(angel)
    return ala_list


def berk(berk_data):
    berk_list = []
    for div in berk_data:
        name = (div.text)
        angel=[name]
        berk_list.append(angel)
    return berk_list


def san_jose(sj_data):
    sj_list = []
    for div in sj_data:
        name = (div.text)
        angel=[name]
        sj_list.append(angel)
    return sj_list


def san_fran(sf_data):
    sf_list = []
    for div in sf_data:
        name = (div.text)
        angel=[name]
        sf_list.append(angel)
    return sf_list


def oak(oak_data):
    oak_list = []
    for div in oak_data:
        name = (div.text)
        angel=[name]
        oak_list.append(angel)
    return oak_list


def write_angel_csv(ala_list, berk_list, sj_data, sf_list, oak_list):
    angel_list = sf_list + oak_list
    df = pd.DataFrame(angel_list)
    df.to_csv('angel_list.csv')


def main():
    ala_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Alameda&entriesperpage=50').read()
    berk_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Berkeley&entriesperpage=50').read()
    sj_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=San%20Jose&entriesperpage=50').read()
    sf_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=san%20francisco&entriesperpage=50').read()
    oak_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Oakland&entriesperpage=50').read()
    ala_soup = bs.BeautifulSoup(ala_sauce, 'lxml')
    berk_soup = bs.BeautifulSoup(berk_sauce, 'lxml')
    sj_soup = bs.BeautifulSoup(sj_sauce, 'lxml')
    sf_soup = bs.BeautifulSoup(sf_sauce, 'lxml')
    oak_soup = bs.BeautifulSoup(oak_sauce, 'lxml')
    ala_data = ala_soup.find_all('div', class_='obitName')
    berk_data = berk_soup.find_all('div', class_='obitName')
    sj_data = sj_soup.find_all('div', class_='obitName')
    sf_data = sf_soup.find_all('div', class_='obitName')
    oak_data = oak_soup.find_all('div', class_='obitName')
    ala_list = ala(ala_data)
    berk_list = berk(berk_data)
    sj_list = san_jose(sj_data)
    sf_list = san_fran(sf_data)
    oak_list = oak(oak_data)
    write_angel_csv(ala_list, berk_list, sj_list, sf_list, oak_list)


if __name__ == '__main__':
    main()
