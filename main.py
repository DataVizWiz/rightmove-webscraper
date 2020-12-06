import requests
import pandas as pd
from variables import loc_code, index, radius, prop_type
from variables import url_part_1, url_part_2
from bs4 import BeautifulSoup as bs
                
urls = [url_part_1 + l + '&radius=' + str(r) + '&index=' + str(i) + '&propertyTypes=' + p + url_part_2
       for l in loc_code
       for p in prop_type
       for i in index
       for r in radius]

df = pd.DataFrame(columns=['PropertyName', 
                            'ShortDesc', 
                            'StationMiles',
                            'Description',
                            'AddedOrReduced',
                            'Agent',
                            'ContactNumber',
                            'PropertyValue'])

for url in urls:

    page = requests.get(url)
            
    soup = bs(page.content, 'html.parser')
                
    page = soup.prettify()
    
    
    get_property_name = soup.find_all('address', attrs={'class': 'propertyCard-address'})
    
    get_short_desc = soup.find_all('h2', attrs={'class': 'propertyCard-title'})
    
    get_miles_from_station = soup.find_all('div', attrs={'class': 'propertyCard-distance'})
                    
    get_description = soup.find_all('span', attrs={'itemprop': 'description'})
    
    get_added_or_reduced = soup.find_all('span', attrs={'class': 'propertyCard-branchSummary-addedOrReduced'})
    
    get_agent = soup.find_all('div', attrs={'class': 'propertyCard-branchSummary'})
    
    get_contact_number = soup.find_all('a', attrs={'class': 'propertyCard-contactsPhoneNumber'})
    
    get_property_value = soup.find_all('div', attrs={'class': 'propertyCard-priceValue'})
    
    
    property_name = [name.get_text() for name in get_property_name]
    
    short_desc = [short.get_text() for short in get_short_desc]
    
    miles_from_station = [miles.get_text() for miles in get_miles_from_station]
    
    description = [desc.get_text() for desc in get_description]
    
    added_or_reduced = [add_reduc.get_text() for add_reduc in get_added_or_reduced]
    
    agent = [agent.get_text() for agent in get_agent]
    
    contact_number = [num.get_text() for num in get_contact_number]
    
    property_value = [value.get_text() for value in get_property_value]
    
    temp_df = pd.DataFrame(columns=['PropertyName', 
                                    'ShortDesc', 
                                    'StationMiles',
                                    'Description',
                                    'AddedOrReduced',
                                    'Agent',
                                    'ContactNumber',
                                    'PropertyValue'])
    
    temp_df['PropertyName'] = property_name
    temp_df['PropertyName'] = temp_df['PropertyName'].str.strip()
    
    temp_df['ShortDesc'] = short_desc
    temp_df['ShortDesc'] = temp_df['ShortDesc'].str.strip()
    
    temp_df['StationMiles'] = pd.Series(miles_from_station)
    temp_df['StationMiles'] = temp_df['StationMiles'].astype(str).str.strip()
    
    temp_df['Description'] = description
    temp_df['Description'] = temp_df['Description'].str.strip()
 
    temp_df['AddedOrReduced'] = added_or_reduced
    temp_df['AddedOrReduced'] = temp_df['AddedOrReduced'].str.strip()
    
    temp_df['Agent'] = agent
    temp_df['Agent'] = temp_df['Agent'].str.strip()
    temp_df['Agent'] = temp_df['Agent'].str.replace('\n', '')
    
    temp_df['ContactNumber'] = contact_number
    temp_df['ContactNumber'] = temp_df['ContactNumber'].str.strip()
    
    temp_df['PropertyValue'] = property_value
    temp_df['PropertyValue'] = temp_df['PropertyValue'].str.strip()
    
    df = df.append(temp_df)
    
    print('Complete: ' + url)

print(df.head())

df.to_csv('data/property_details.csv')


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            