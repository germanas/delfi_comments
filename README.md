# Delfi.lt comments project
## Introduction
Delfi.lt is the largest news portal in Lithuania. Each of the articles there has a comment section. Lately I noticed a huge
influx of negative comments and trolls replying to normal articles. Mainly the comments spread hatred against Lithuania, NATO
European union. I was interested in finding out the trolls using python, R and D3. 
## Scraping
The first thing to do was to get the comments using beautiful soup 4 python library. When I started this project, I was little
unexperienced with beautiful soup, therefore I scraped everything in one huge string. Each comment was a big string. Total of 
16k comments were scrapped from the site. Since delfi archives the posts, the whole scraping took about a month since I ran the
scrape script each day.  
Files responsible for scraping:  
- Scrape.py - scrapes all comments and outputs a csv file.
- run.bat - runs the script on double click.
- clean.py - cleans dublicate strings.
## Data wrangling
As from the scraper I got a messy string of the data, I had to separate it to collumns using pandas and regex. To map the ip
addresses to locations I used python's geoip library. After the data was kindof clean, I cleaned it once more with R, also added
new columns like total_score.
Files responsible for wrangling:
- Project_vatnik.R - used for wrangling
- Fix_dataset.R - more wrangling
- Wrangle_delfi.py - turns strings to pandas dataframe and then to CSV.
## EDA (explanatory data analysis)
Since I am still cleaning and reviewing data, this part is still in progress.
## Data visualisation
First experiment was to check if comment scores depended on time and locations. Full experiment found here:   
https://github.com/germanas/data_visualisation

## The project is still under developments and will be filled when I will have more time. To be continued..
