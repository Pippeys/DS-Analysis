# Data Science Analysis
This Repo holds all data science projects.

NAI NorCal folder contains some BS4 web scrapping.

Tacoma Analysis folder contain all scripts involving a tacoma truck analysis.
  - Tacoma_Puller.py is the newest script for creating the dataframe for analysis. 
        - Tacoma_Puller uses https://github.com/juliomalegria/python-craigslist to find and scrape data according to parameters, then a csv is created to save the info.
        - Tacoma_Puller then uses the info from earlier to searches for the odometer, condition, and drive of the Tacoma using Regular Expressions. After the dataframe has been updated with the new columns, it is transferred back into a CSV file for later use. 
The Goal of this project is to find a sweet spot between all the variables and price.
  - Tacoma_Analysis.ipynb uses the .csv file to do analysis on the Tacomas'
  
LibraryAnalysisExplore.ipynb seeks to find basic understanding of library patrons.
  - Understand Attributes
  - Graphs
  - Intial Hypothesis for Classification

LibraryAnalysisPastYears.ipynb dives deeper to answer the business question of: "What segment classification can be seen with lost patrons."
  - K-Means Clustering
  - SVM Classification
