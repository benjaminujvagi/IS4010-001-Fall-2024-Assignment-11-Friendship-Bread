#zip code package
import requests
def update_zip_codes(self): 
    for index, row in self.df[self.df['Zip Code'].isnull()].iterrows(): 
        city = row['City'] 
        zip_code = self.fetch_zip_code(city) 
        self.df.at[index, 'Zip Code'] = zip_code

def fetch_zip_code(self, city): 
    api_key = 'your_api_key' 
    response = requests.get(f"https://app.zipcodebase.com/api/v1/search?apikey={api_key}&city={city}") 
    data = response.json() 
    return data['results'][0]['postal_code'] if data['results'] else None
