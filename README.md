# COVID-19 Data Retrieval

This Python script is designed to facilitate the retrieval of COVID-19 data globally or for a specific country, with an additional feature to present numeric figures in words for enhanced readability.

## Code Structure

### COVID-19 Data Retrieval Functions

- **`get_country_data` and `get_global_data` Functions:**
   - Utilize the `requests` library to fetch real-time COVID-19 data from the Disease.sh API.
   - `get_country_data`: Retrieve country-specific COVID-19 data.
   - `get_global_data`: Fetch global COVID-19 data.
   - Handle invalid country names or data unavailability gracefully.

### Formatting and Printing Functions

- **`format_number` and `convert_and_print` Functions:**
   - `format_number`: Add commas for better readability to numeric values.
   - `convert_and_print`: Display both the numeric value and its word representation.

### Number-to-Words Conversion Functions

- **`convert_below_thousand` and `num_to_words` Functions:**
   - `convert_below_thousand`: Convert a number less than 1000 into words.
   - `num_to_words`: Convert numeric data into words, handling different magnitudes.

### Main Execution Function

- **`main` Function:**
   - Take user input for a country name or 'global'.
   - Call functions to retrieve and display COVID-19 data.

## Example Output

Enter a country name (or type 'global' for worldwide data): Indonesia

### Script Output (Example):
- **Country: Indonesia**
  - Confirmed Cases: 5,000,000
  - Confirmed Cases (In Words): Five Million
  - Deaths: 100,000
  - Deaths (In Words): One Hundred Thousand
  - Recovered: 4,500,000
  - Recovered (In Words): Four Million Five Hundred Thousand
  - Active Cases: 400,000
  - Active Cases (In Words): Four Hundred Thousand

## COVID-19 Data Retrieval

### Functions

#### `get_country_data(country)`

- Retrieves and displays COVID-19 data for a specific country.
- Uses the Disease.sh API for data retrieval.

#### `get_global_data()`

- Retrieves and displays global COVID-19 data.
- Uses the Disease.sh API for data retrieval.

### Usage

- Call these functions based on user input to fetch and present COVID-19 data.

## Notes

- This script uses the Disease.sh API to fetch real-time COVID-19 data.

## Contribute

- Feel free to contribute by opening issues or submitting pull requests. Your contributions are highly appreciated!
