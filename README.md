# COVID-19 Data and Number-to-Words Converter

This Python script serves a dual purpose: fetching COVID-19 data globally or for a specific country and presenting numeric figures in words for improved readability.

## Usage

1. **Clone the Repository:**
   - Clone the repository locally:
     ```bash
     git clone https://github.com/sulujulianto/covid19-data-retrieval.git
     cd covid19-data-retrieval
     ```

2. **Install Dependencies:**
   - Install the required packages:
     ```bash
     pip install requests
     ```

3. **Run the Script:**
   - Execute the script:
     ```bash
     python covid19_data.py
     ```

4. **Follow Prompts:**
   - Enter a country name or 'global' for worldwide data.

## Code Structure

### Data Retrieval Functions

- **`get_country_data` and `get_global_data` Functions:**
   - Utilize the `requests` library to fetch COVID-19 data from Disease.sh API.
   - Handle country-specific or global data retrieval.
   - Check for invalid country names or data unavailability.

### Formatting and Printing Functions

- **`format_number` and `convert_and_print` Functions:**
   - `format_number`: Add commas for better readability.
   - `convert_and_print`: Print numeric value and its word representation.

### Number-to-Words Conversion Functions

- **`convert_below_thousand` and `num_to_words` Functions:**
   - `convert_below_thousand`: Convert a number less than 1000 into words.
   - `num_to_words`: Convert numeric data into words, handling different magnitudes.

### Main Execution Function

- **`main` Function:**
   - Take user input for a country name or 'global'.
   - Call functions to retrieve and display COVID-19 data.

## Example Output

- **User Input:**
  ```bash
  Enter a country name (or type 'global' for worldwide data): Indonesia
