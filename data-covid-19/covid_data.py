import requests

def format_number(number):
    return "{:,}".format(number)

def convert_below_thousand(num):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if num == 0:
        return ""
    elif num < 10:
        return units[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + " " + units[num % 10]
    else:
        return units[num // 100] + " Hundred " + convert_below_thousand(num % 100)

def num_to_words(number):
    if number == 0:
        return "Zero"

    trillion = number // 1_000_000_000_000
    billion = (number % 1_000_000_000_000) // 1_000_000_000
    million = (number % 1_000_000_000) // 1_000_000
    thousand = (number % 1_000_000) // 1_000
    remaining = number % 1_000

    result = ""
    if trillion:
        result += convert_below_thousand(trillion) + " Trillion "
    if billion:
        result += convert_below_thousand(billion) + " Billion "
    if million:
        result += convert_below_thousand(million) + " Million "
    if thousand:
        result += convert_below_thousand(thousand) + " Thousand "
    if remaining:
        result += convert_below_thousand(remaining)

    return result.strip()

def convert_and_print(value, label):
    formatted_value = format_number(value)
    words_value = num_to_words(value)
    print(f"{label}: {formatted_value}")
    print(f"{label} (In Words): {words_value}")

def get_country_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country.lower()}?yesterday=false&strict=true"
    response = requests.get(url)
    data = response.json()

    if 'message' not in data:
        country_name = data['country']
        convert_and_print(data['cases'], "Confirmed Cases")
        convert_and_print(data['deaths'], "Deaths")
        convert_and_print(data['recovered'], "Recovered")
        convert_and_print(data['active'], "Active Cases")
    else:
        print("Data not found or invalid country name.")

def get_global_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    data = response.json()

    if data:
        convert_and_print(data['cases'], "Total Cases")
        convert_and_print(data['deaths'], "Total Deaths")
        convert_and_print(data['recovered'], "Total Recovered")
        convert_and_print(data['active'], "Active Cases")
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
