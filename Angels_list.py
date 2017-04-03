#python3
#List of Angels
import bs4 as bs
import urllib.request
import csv
import lxml
import pandas as pd


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


def write_angel_csv(oak_list, sf_list):
    angel_list = sf_list + oak_list
    df = pd.DataFrame(angel_list)
    df.to_csv('angel_list.csv')


def main():
    sf_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=san%20francisco&entriesperpage=50').read()
    oak_sauce = urllib.request.urlopen('http://www.legacy.com/ns/obitfinder/obituary-search.aspx?Page=1&countryid=1&daterange=Last3Days&stateid=7&keyword=Oakland&entriesperpage=50').read()
    sf_soup = bs.BeautifulSoup(sf_sauce, 'lxml')
    oak_soup = bs.BeautifulSoup(oak_sauce, 'lxml')
    sf_data = sf_soup.find_all('div', class_='obitName')
    oak_data = oak_soup.find_all('div', class_='obitName')
    sf_list = san_fran(sf_data)
    oak_list = oak(oak_data)
    write_angel_csv(oak_list, sf_list)


if __name__ == '__main__':
    main()
