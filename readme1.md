![image](ai.jpg)

# ActiveJobs_Scraper

# Overview
The Job Search API Data Processor is a Python script designed to fetch job listings related to "cyber security" from an API, process the data, and save it in a CSV format. It uses the requests library to interact with the API and pandas for data manipulation and export. This tool helps users to efficiently collect and structure job data for analysis or reporting.

# Installation Instructions
To use this script, you need to have Python installed on your machine. You will also need to install the required Python libraries.

# Clone the repository:

bash
Copy code
git clone https://github.com/your-username/job-search-api-data-processor.git
cd job-search-api-data-processor
Install the required libraries:

bash
Copy code
pip install requests pandas
Obtain an API key:

Sign up at RapidAPI to obtain an API key for the job search API. Replace the placeholder API key in the script with your own key.

# Usage Instructions
Configure the API key:

Edit the script and replace "e538ff38fdmshd466fa5f6d3ef96p180282jsn8cfa9a012cb1" with your actual API key.

python
Copy code
headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}
Run the script:

Execute the script using Python:

bash
Copy code
python job_search_api_data_processor.py
Check the output:

After running the script, you will find the processed job data saved as jobs_data.csv in the same directory.

# Credits
Christopher Rouse and Tyrell McCollin
