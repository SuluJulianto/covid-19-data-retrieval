import requests

def get_country_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country.lower()}?yesterday=false&strict=true"
    response = requests.get(url)
    data = response.json()
    
    if 'message' not in data:
        country_name = data['country']
        confirmed_cases = data['cases']
        deaths = data['deaths']
        recovered = data['recovered']
        active_cases = data['active']
        
        print(f"Country: {country_name}")
        print(f"Confirmed Cases: {confirmed_cases}")
        print(f"Deaths: {deaths}")
        print(f"Recovered: {recovered}")
        print(f"Active Cases: {active_cases}")
    else:
        print("Data not found or invalid country name.")

def get_global_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()
    
    if data:
        total_cases = data['cases']
        total_deaths = data['deaths']
        total_recovered = data['recovered']
        active_cases = data['active']
        
        print("Global COVID-19 Data:")
        print(f"Total Cases: {total_cases}")
        print(f"Total Deaths: {total_deaths}")
        print(f"Total Recovered: {total_recovered}")
        print(f"Active Cases: {active_cases}")
    else:
        print("Global data not available.")

def main():
    selected_country = input("Enter a country name (or type 'global' for worldwide data): ")
    
    if selected_country.lower() == 'global':
        get_global_data()
    else:
        get_country_data(selected_country)

if __name__ == "__main__":
    main()
