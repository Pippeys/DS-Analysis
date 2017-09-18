from craigslist import CraigslistForSale
import pandas as pd
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
    return port_list

def write_csv(sf_list,f_list,stock_list,port_list):
    cl_list = sf_list + f_list + stock_list + port_list
    df = pd.DataFrame(cl_list)
    df.to_csv('Tacoma_List.csv')

def main():
    sf_list = sf_tacomas()
    f_list = fresno_tacomas()
    stock_list =stockton_tacomas()
    port_list = portland_tacomas()
    write_csv(sf_list,f_list,stock_list,port_list)

if __name__ == '__main__':
    main()
