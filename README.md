![ai](ai.jpg)

# Active Jobs Scraper

#  Project Description
This Python script allows you to search for job listings related to "cyber security" within the United States using the Active Jobs API. The script retrieves job data from the API, processes it to exclude unnecessary fields, and saves the filtered information into a CSV file. This can be particularly useful for job seekers, data analysts, or anyone interested in aggregating job data for further analysis.

# Installation
To run this script, you'll need Python and the following libraries:

requests: For making HTTP requests to the API.
pandas: For data manipulation and exporting to CSV.

# Install Required Libraries

Use pip to install the required libraries. Open your terminal or command prompt and run:

bash
Copy code
pip install requests pandas
Obtain API Key

Sign up on RapidAPI and subscribe to the Active Jobs API to get your API key. Replace the placeholder key in the script with your actual key.

# Usage
Configure the API Key

In the script, update the x-rapidapi-key in the headers dictionary with your API key.

Run the Script

Save the script to a file, for example, job_search_to_csv.py, and run it using Python:

bash
Copy code
python job_search_to_csv.py
Check the Output

After running the script, check the current directory for the jobs_data.csv file, which contains the filtered job data.

# Credits
API Source: Active Jobs API via RapidAPI
Libraries Used:
requests (https://pypi.org/project/requests/)
pandas (https://pandas.pydata.org/)
