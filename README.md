# Alphafold Impact Assessment in Canada

This repository contains the code to scrape and analyze the impact of Alphafold in Canada. Follow the instructions below to set up the environment and run the code.

## Prerequisites

1. Install Python 3.7 or higher from the official website: https://www.python.org/downloads/

## Setting up the Environment

1. Download the necessary file from the repository:

   - [Canadianterm.py](https://raw.githubusercontent.com/Williamhsu1999/AlphaFold/main/Beautifulsoup/Canadianterm.py)

   Right-click on the link and choose "Save link as..." to save the file to your Desktop. Make sure is saved as a python file. 

2. Open the command prompt or terminal.

3. If your command prompt or terminal is not already in your user directory, navigate to it using the following command:

cd %userprofile%

4. Navigate to the Desktop where u installed the file:

cd Desktop

5. Install the required Python library by typing the following commands one by one and press Enter after each command:

pip install requests

pip install beautifulsoup4

This will install the necessary Python libraries for the web scraper.

## Running the Scraper

1. Open the command prompt or terminal.
2. Navigate to the Desktop:

cd %userprofile%/Desktop

3. Run the web scraper by typing the following command and pressing Enter:

cd Desktop/Canadianterm
python Canadianterm.py


This script will start fetching the first 100 pages of search results for articles that contain both "Alphafold" or "Alphafold2" and at least one Canadian term. If an article has 2 or more Canadian terms, it will still be scraped as long as it meets the condition of having at least one Canadian term and either "Alphafold" or "Alphafold2". The scraper will check if any of the Canadian terms appear in the article's text, and if it finds a match, the article will be considered relevant and added to the scraped data.

Note: It is essential to remember that web scraping might be against the terms of service for some websites, and Google Scholar may temporarily block your IP address if you make too many requests. It is recommended to use APIs whenever possible and always be respectful of the website's terms of service and rate limits.

## Analyzing the Data

You can now import the generated text file into a data analysis tool or programming language like Python, R, or Excel for further analysis and visualization.







