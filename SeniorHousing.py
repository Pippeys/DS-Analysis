#python3
#SeniorHousing
import bs4 as bs
import urllib.request
import csv
import lxml

num_pages = []
Senior_add=[]
Senior_Housing=[]

while MorePages:


    while moreinfo:
        get_info()

    next_page()

Senior_Sauce = urllib.request.urlopen('http://www.seniorhousingnet.com/seniorliving-search/oakland_ca')
Senior_Soup = bs.BeautifulSoup(Senior_Sauce, 'lxml')
Senior_Data = Senior_Soup.find('a', class_='next')


for a in Senior_Data:
    numOFpages = (a.text)
    num = [numOFpages]
    num_pages.append(num)
print(len(num_pages))

SeniorHousing_Sauce = urllib.request.urlopen('http://www.seniorhousingnet.com/seniorliving-search/oakland_ca')
SeniorHousing_Soup = bs.BeautifulSoup(SeniorHousing_Sauce, 'lxml')
SeniorHousing_Data = SeniorHousing_Soup.find_all('a', class_='ComName srpFont')


for a in SeniorHousing_Data:
    propname = (a.text)
    Housing=[propname]
    Senior_Housing.append(Housing)


Senioradd_Sauce = urllib.request.urlopen('http://www.seniorhousingnet.com/seniorliving-search/oakland_ca')
Senioradd_Soup = bs.BeautifulSoup(Senioradd_Sauce, 'lxml')
Senioradd_Data = Senioradd_Soup.find_all('span', itemprop="streetAddress")


for span in Senioradd_Data:
    address = (span.text)
    add = [address]
    Senior_add.append(add)


next_page_links = []
for page in soup.find_all('a', href=re.compile('/pg-2/')):
    temp_link = base_url+page.get('href')
    next_page_links.append(temp_link)
for next_page in next_page_links:
    print


PropandAdd = [Senior_Housing,Senior_add]
with open('SeniorHousing.csv', 'w') as file:
    csv_writer = csv.writer(file)
    for row in PropandAdd:
        csv_writer.writerow(row)
