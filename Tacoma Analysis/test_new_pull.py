import pandas as pd

# def scrape(urllist):
#     drive_pattern = re.compile(r'(<span>drive:.*?<b>)(.*?)(<\/b><\/span>)')
#     condition_pattern = re.compile(r'(<span>condition:.*?<b>)(.*?)(<\/b><\/span>)')
#     odometer_pattern = re.compile(r'(<span>odometer:.*?<b>)(.*?)(<\/b><\/span>)')
#     title_pattern = re.compile(r'(<span>title status:.*?<b>)(.*?)(<\/b><\/span>)')
#
#     biglist = []
#
#     for i in range(len(urllist)):
#         row= ['NaN','NaN','NaN', 'NaN']
#
#         print('Iteration: {}'.format(i))
#
#         sauce = urllib.request.urlopen(urllist[i])
#         soup = bs.BeautifulSoup(sauce,'lxml')
#         data = soup.find_all('div', class_='mapAndAttrs')
#
#         for result in data:
#             for child in result.children:
#                 status_result = title_pattern.search(str(child))
#                 dri_result = drive_pattern.search(str(child))
#                 cond_result = condition_pattern.search(str(child))
#                 odo_result = odometer_pattern.search(str(child))
#
#                 if status_result:
#                     a = (status_result.group(2))
#                     row[0]=a
#                     print('Found status!')
#
#                 if dri_result:
#                     a = (dri_result.group(2))
#                     row[1]=a
#                     print('Found drive!')
#
#
#                 if cond_result:
#                     b = (cond_result.group(2))
#                     row[2]=b
#                     print('Found condition!')
#
#
#                 if odo_result:
#                     c = (odo_result.group(2))
#                     row[3] = c
#                     print('Found odometer!')
#
#         biglist.append(row)
#         print(row)
#
#
#         print('Waiting...')
#         time.sleep(randint(20,45))
#
#     return biglist


def main():
    df = pd.read_csv('C:/Users/Scott/Desktop/Data/Tacoma_Data/Tacoma_New1.csv')
    urllist = df["url"].tolist()

    i = 1
    while i < 100:
        x = 'list_'
        x = x + str(i)
        print(x)
        x = []
        i = i+1
    for u in urllist:
        u 


    #biglist = scrape(urllist)
    #Compiling new columns and export DF to new csv
    #new_df = pd.DataFrame(biglist)
    #new_df.columns = ['status','drive','condition','odometer']
    #df = pd.concat([df,new_df], axis=1)
    #df.to_csv('C:/Users/Scott/Desktop/Data/Tacoma_Data/Tacoma_New.csv')
    print('Done')

if __name__ == '__main__':
    main()
