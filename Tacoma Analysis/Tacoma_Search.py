from craigslist import CraigslistForSale
import pandas as pd
import bs4 as bs
import urllib.request
import lxml
import time

def search(sites,cat,minprice,maxprice,minyear,maxyear,maxmiles):
    CL_FS = CraigslistForSale(site = sites, category = cat,
                        filters={
                        'min_price': minprice,
                        'max_price': maxprice,
                        'make': 'toyota tacoma',
                        'min_year': minyear,
                        'max_year': maxyear,
                        'max_miles': maxmiles})
    cl_list = []

    for cl_result in CL_FS.get_results(sort_by='newest'):
        time.sleep(60)
        cl_list.append(cl_result)
    return cl_list

def main():
    locations = ['sfbay','stockon','portland','pheonix','eugene','chico','fresno','denver','reno','sacromento','modesto','medford','seattle','losangeles','sandiego','bakersfield','lasvegas']
    final_list = []
    for i in locations:
        print('Searching in '+i)
        cl_list = search(i,'cta',15000,35000,2015,2021,100000)
        final_list=final_list.append(cl_list)

    df = pd.DataFrame(final_list)
    df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_list.csv')

if __name__ == '__main__':
    main()
