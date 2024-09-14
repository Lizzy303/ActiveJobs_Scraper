import requests
import pandas as pd

# Define API endpoint for job search
url = "https://active-jobs-db.p.rapidapi.com/active-ats"

# Set up query parameters for the API request
querystring = {
    "title":"\"cyber security\"", # Search for jobs with the title containing "cyber security"
    "location":"\"United States\"",  # Specify job location search
    "offset":"0" # Offset for pagination; start from the first result
}

# Set up request headers, including API key and host information
headers = {
	"x-rapidapi-key": "e538ff38fdmshd466fa5f6d3ef96p180282jsn8cfa9a012cb1",
	"x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}

# Send GET request to the API with headers and query parameters
response = requests.get(url, headers=headers, params=querystring)

# Check for successful response
if response.status_code == 200:
    job_data = response.json()

    # Convert JSON data to DataFrame
    # This might need adjustment based on the JSON structure
    df = pd.json_normalize(job_data)

    # Drop specified columns
    columns_to_drop = ['orglogo', 'datevalidthrough', 'locations_raw', 'locationtype', 'locationrequirements_raw', 'salary_raw']
    df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

    # Convert the DataFrame to a CSV file
    df.to_csv('jobs_data.csv', index=False)

    # Print confirmation message
    print("Conversion complete! CSV file saved as 'jobs_data.csv'.")
else:
    # Print an error message if the request was not successful
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")