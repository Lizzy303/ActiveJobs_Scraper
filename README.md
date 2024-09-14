![ai](ai.jpg)

# Active Jobs Scraper

#  Overview
This Python script allows you to search for job listings related to "cyber security" within the United States using the Active Jobs API. The script retrieves job data from the API, processes it to exclude unnecessary fields, and saves the filtered information into a CSV file. This can be particularly useful for job seekers, data analysts, or anyone interested in aggregating job data for further analysis.

# Tools Used
The project utilizes the Acdtive Jobs-db api from rapidapi.com. Other tools that are use to complete the project are Visual Studio Code or Googl Colab, the requests and pandas libraries from Python.

# Requirements
Python 3.8+
Visual Studio Code / Google Colab
Request
Pandas
Works on Linux, Windows, macOS

## Links
<!-- links -->
[Visual Studio Code](https://code.visualstudio.com/download)

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
requests: For making HTTP requests to the API.
pandas: For data manipulation and exporting to CSV.

Sign up on RapidAPI and subscribe to the Active Jobs DB API to get your API key. Replace the placeholder key in the script with your actual key.

# Usage
Import the libraries first as shown above. Next, place the code snippet 
Configure the API Key

In the script, update the x-rapidapi-key in the headers dictionary with your API key.

Run the Script

Save the script to a file, for example, job_search_to_csv.py, and run it using Python:

```
python job_search_to_csv.py
```
Check the Output

After running the script, check the current directory for the jobs_data.csv file, which contains the filtered job data.

# Credits
API Source: Active Jobs API via RapidAPI
Libraries Used:
requests (https://pypi.org/project/requests/)
pandas (https://pandas.pydata.org/)
