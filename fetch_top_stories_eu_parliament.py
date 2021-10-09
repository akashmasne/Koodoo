import requests
import xml.etree.ElementTree as ET
import pandas as pd
import argparse
import logging
import os

#Below variables can be also be taken as user input/arguments OR from a config file as required.
#url = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'
#output_csv_filename='eu-rss.csv'
xml_data_filename='eu-topstories.xml'


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

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
      '--url',
      dest='url',
      default='https://www.europarl.europa.eu/rss/doc/top-stories/en.xml',
      help='RSS endpoint for top stories')
      
    parser.add_argument(
      '--output_csv_filename',
      dest='output_csv_filename',
      default='eu-rss.csv',
      help='output_csv_filename for ouput')
      
    #known_args, other_args = parser.parse_known_args(argv)
    known_args=parser.parse_args()
    rssurl=known_args.url
    rss_output_csv_filename=known_args.output_csv_filename


    try:  # error handling
        resp = requests.get(rssurl)
        with open(xml_data_filename, 'wb') as f:
            f.write(resp.content)
        newsitems = parseXML(xml_data_filename)
        df=pd.DataFrame(newsitems)
        df.to_csv(rss_output_csv_filename)

        os.remove(xml_data_filename)

    except Exception as e: 
        print("Error:",str(e))

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
