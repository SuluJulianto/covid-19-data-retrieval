# COVID-19 Data Retrieval

This Python script retrieves the latest COVID-19 data globally or for a specific country using the `disease.sh` API.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## How to Use

1. Clone or download the repository to your local machine.
2. Install the requests library if you haven't already: `pip install requests`
3. Run the script: `python covid_data.py`
4. Input the country name when prompted. If you want global data, input 'global'.

## Output

- For a specific country:
  - Confirmed cases
  - Deaths
  - Recovered cases
  - Active cases

- For global data:
  - Total confirmed cases worldwide
  - Total deaths worldwide
  - Total recovered cases worldwide
  - Active cases worldwide

## Example Usage

- To get data for a specific country: Enter a country name: Indonesia
- To get global data: Enter a country name (or type 'global' for worldwide data): global

## Notes

- The data is sourced from `disease.sh` API and is updated regularly.
- The API might have slight delays in data updates.

## Contributions

Feel free to contribute by enhancing the functionality or adding new features. Create a pull request to suggest improvements.
