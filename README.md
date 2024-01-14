# COVID-19 Data Retrieval

This Python script is designed to facilitate the retrieval of COVID-19 data globally or for a specific country, with an additional feature to present numeric figures in words for enhanced readability.

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

```markdown
Enter a country name (or type 'global' for worldwide data): Indonesia

### Script Output:
- **`Country: Indonesia`**
  - Confirmed Cases: 5,000,000
  - Confirmed Cases (In Words): Five Million
  - Deaths: 100,000
  - Deaths (In Words): One Hundred Thousand
  - Recovered: 4,500,000
  - Recovered (In Words): Four Million Five Hundred Thousand
  - Active Cases: 400,000
  - Active Cases (In Words): Four Hundred Thousand

