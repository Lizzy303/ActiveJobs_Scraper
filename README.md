![ai](ai.jpg)

# Active Jobs Scraper

#  Overview
This Python script allows you to search for job listings related to "cyber security" within the United States using the Active Jobs API. The script retrieves job data from the API, processes it to exclude unnecessary fields, and saves the filtered information into a CSV file. This can be particularly useful for job seekers, data analysts, or anyone interested in aggregating job data for further analysis.

# Tools Used
The project utilizes the Acdtive Jobs-db api from [rapidapi.com](https://rapidapi.com/fantastic-jobs-fantastic-jobs-default/api/active-jobs-db/playground/apiendpoint_bbaf2569-9650-4b39-bb27-ff69f7916a4b). Other tools that are use to complete the project are Visual Studio Code or Googl Colab, the requests and pandas libraries from Python.

# Requirements
* [Python 3.8+](https://www.python.org/downloads/)
* [Visual Studio Code](https://code.visualstudio.com/download) / [Google Colab](https://colab.research.google.com/)
* Requests
* Pandas
* Works on Linux, Windows, macOS

# Installation
To run this script, you'll need Python. Use pip to install the required libraries. Open your terminal or command prompt and run:

```python
pip install requests
pip install pandas
```
After installing these libraries import them into your script.

```python
import requests
import pandas as pd
```
* requests: For making HTTP requests to the API.
* pandas: For data manipulation and exporting to CSV.

Sign up on RapidAPI and subscribe to the Active Jobs DB API to get your API key. Replace the placeholder key in the script with your actual key.

# Usage
Import the libraries first as shown above. Next, place the Active Jobs API code snippet from rapidapi into the text editor.

```
url = "https://active-jobs-db.p.rapidapi.com/active-ats"

querystring = {"title":"\"Data Engineer\"","location":"\"United States\""}

headers = {
	"x-rapidapi-key": "YOUR API KEY",
	"x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
```

To ensure that the api is working use:
```
# Check for successful response
if response.status_code == 200:
    job_data = response.json()
```

This script will produce a json file. 
To convert the output to a csv file use the following code.

```
 # Convert JSON data to DataFrame
    # This might need adjustment based on the JSON structure
    df = pd.json_normalize(job_data)

    # Drop specified columns
    columns_to_drop = ['orglogo', 'datevalidthrough', 'locations_raw', 'locationtype', 'locationrequirements_raw', 'salary_raw']
    df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

    # Convert the DataFrame to a CSV file
    df.to_csv('jobs_data.csv', index=False)
```
This transforms the structure of the data into a standardized format, filters the job data and outputs a csv file.

Save the script to a file, for example, job_search_to_csv.py, and run it using Python:

```
python job_search_to_csv.py
```
After running the script, check the current directory for the jobs_data.csv file, which contains the filtered job data.

# Credits
* API Source: Active Jobs API via RapidAPI
* Libraries Used:
* requests (https://pypi.org/project/requests/)
* pandas (https://pandas.pydata.org/)
* Text Editor: (https://code.visualstudio.com/download) / (https://colab.research.google.com/)
