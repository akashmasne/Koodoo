#Libs required for the task
import requests
import xml.etree.ElementTree as ET
import pandas as pd

#Below variables can be also be taken as user input/arguments OR from a config file as required.
url = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'
xml_data_filename='eu-topstories.xml'
output_csv_filename='eu-rss.csv'

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    
    for item in root.findall('./channel/item'):
        news={}
        for child in item:
            news[child.tag] = child.text
        newsitems.append(news)

        # return list of all the news items, where each element is dict for a news item
    return newsitems

def main():
    # error handling
    try:
        resp = requests.get(url)
        #Storing xml response in local temporarily,can be deleted after use
        with open(xml_data_filename, 'wb') as f:
            f.write(resp.content)
        newsitems = parseXML(xml_data_filename)
        df=pd.DataFrame(newsitems)
        df.to_csv(output_csv_filename)
    except Exception as e: 
        print("Error:",str(e))

if __name__ == "__main__":
    main()
