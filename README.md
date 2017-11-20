# Webber
Web Scraper with py.BS4

Angels.py creates a list of recent deaths in location specified in script

Bart Proxy.py is used to find location (coordinates) distance from all BART stations

Tacoma_Puller.py is the newest script for creating the dataframe for analysis. 
Tacoma_Puller uses https://github.com/juliomalegria/python-craigslist to find and scrape data according to parameters, then a csv is created to save the info.
Tacoma_Puller then uses the info from earlier to searches for the odometer, condition, and drive of the Tacoma using Regular Expressions. After the dataframe has been updated with the new columns, it is transferred back into a CSV file for later use. 
The Goal of this project is to find a sweet spot between all the variables and price.
