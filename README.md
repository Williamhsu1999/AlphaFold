# Alphafold Impact Assessment in Canada

This repository contains the code to scrape and analyze the impact of Alphafold in Canada. Follow the instructions below to set up the environment and run the code.

## Prerequisites

1. Install Python 3.7 or higher from the official website: https://www.python.org/downloads/

## Setting up the Environment

1. Download the necessary files from the repository:

   - [scraper.py](https://raw.githubusercontent.com/Williamhsu1999/AlphaFold/main/beautifulsoup/Canadianterm/scraper.py)
   - [convert_to_csv.py](https://raw.githubusercontent.com/Williamhsu1999/AlphaFold/main/beautifulsoup/Canadianterm/convert_to_csv.py)
   - [requirements.txt](https://raw.githubusercontent.com/Williamhsu1999/AlphaFold/main/beautifulsoup/Canadianterm/requirements.txt)

   Right-click on each link and choose "Save link as..." to save the files to your local machine.

2. Create a new folder on your local machine (e.g., `alphafold`) and move the downloaded files into this folder.

3. Open the command prompt or terminal and navigate to the new folder:

cd path/to/alphafold


Replace `path/to/alphafold` with the actual path to the folder you created.

4. Install the required Python libraries:

pip install -r requirements.txt


## Running the Scraper

1. Open the command prompt or terminal.
2. Navigate to the folder containing the scraper script:

cd path/to/alphafold


Replace `path/to/alphafold` with the actual path to the folder you created.

3. Run the scraper script:

python scraper.py


This script will scrape the relevant data and save it in a text file (e.g., `scraped_data.txt`).

## Converting the Scraped Data to CSV

1. Open the command prompt or terminal.
2. Navigate to the folder containing the conversion script:

cd path/to/alphafold


Replace `path/to/alphafold` with the actual path to the folder you created.

3. Run the conversion script:

python convert_to_csv.py


This script will parse the text file containing the scraped data and save it as a CSV file (e.g., `scraped_data.csv`).

## Analyzing the Data

You can now import the generated CSV file into a data analysis tool or programming language like Python, R, or Excel for further analysis and visualization.




