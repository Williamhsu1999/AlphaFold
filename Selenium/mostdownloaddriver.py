import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Define the search term
search_term = 'alphafold OR alphafold2'

# Define a list of Canadian universities
universities = [
    "Acadia University",
    "Algoma University",
    "Athabasca University",
    "Bishop's University",
    "Brandon University",
    "Brescia University College",
    "Brock University",
    "Cape Breton University",
    "Capilano University",
    "Carleton University",
    "Concordia University",
    "Concordia University of Edmonton",
    "Dalhousie University",
    "Dominican University College",
    "École de technologie supérieure",
    "École nationale d'administration publique",
    "École Polytechnique de Montréal",
    "Emily Carr University of Art and Design",
    "First Nations University of Canada",
    "Huron University College",
    "Institut national de la recherche scientifique",
    "King's University College at Western University",
    "Kwantlen Polytechnic University",
    "Lakehead University",
    "Laurentian University",
    "MacEwan University",
    "McGill University",
    "McMaster University",
    "Memorial University of Newfoundland",
    "Mount Allison University",
    "Mount Royal University",
    "Mount Saint Vincent University",
    "Nipissing University",
    "Northern Alberta Institute of Technology",
    "Nova Scotia College of Art and Design University",
    "OCAD University",
    "Queen's University",
    "Quest University Canada",
    "Redeemer University",
    "Royal Military College of Canada",
    "Royal Roads University",
    "Ryerson University",
    "Saint Mary's University",
    "Saint Paul University",
    "Saskatchewan Polytechnic",
    "Sheridan College",
    "Simon Fraser University",
    "Southern Alberta Institute of Technology",
    "St. Francis Xavier University",
    "St. Jerome's University",
    "St. Mary's University",
    "St. Thomas More College",
    "St. Thomas University",
    "Télé-université",
    "Thompson Rivers University",
    "Trent University",
    "Trinity Western University",
    "Université de Moncton",
    "Université de Montréal",
    "Université de Sherbrooke",
    "Université du Québec",
    "Université du Québec à Chicoutimi",
    "Université du Québec à Montréal",
    "Université du Québec à Rimouski",
    "Université du Québec à Trois-Rivières",
    "Université du Québec en Abitibi-Témiscamingue",
    "Université du Québec en Outaouais",
    "Université Laval",
    "Université Sainte-Anne",
    "University Canada West",
    "University of Alberta",
    "University of British Columbia",
    "University of Calgary",
    "University of Guelph",
    "University of King's College",
    "University of Lethbridge",
    "University of Manitoba",
    "University of New Brunswick",
    "University of Northern British Columbia",
    "University of Ontario Institute of Technology",
    "University of Ottawa",
    "University of Prince Edward Island",
    "University of Regina",
    "University of Saskatchewan",
    "University of St. Michael's College",
    "University of the Fraser Valley",
    "University of Toronto",
    "University of Trinity College",
    "University of Victoria",
    "University of Waterloo",
    "University of Western Ontario",
    "University of Windsor",
    "University of Winnipeg",
    "Vancouver Island University",
    "Wilfrid Laurier University",
  
]

# Initialize the articles list
articles = []

# Set up the Selenium WebDriver (assuming Chrome)
service = Service(executable_path='C:\\Users\\willi\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Scrape data from Google Scholar for each university
for university_name in universities:
    query = f'{search_term} "{university_name}"'
    url = f'https://scholar.google.com/scholar?q={query}'
    driver.get(url)
    sleep(2)  # Wait for the page to load

    # Iterate through the top 50 pages
    for page in range(50):
        # Extract the article information for the current university and page
        results = driver.find_elements('css selector', 'div.gs_ri')
        for result in results:
            try:
                title = result.find_element('css selector', 'h3.gs_rt a').text
                authors_and_info = result.find_element('css selector', 'div.gs_a').text
                citation_date = authors_and_info.split('-')[-1].strip()
                authors = authors_and_info.split('-')[0].strip()

                articles.append({
                    'title': title,
                    'authors': authors,
                    'date': citation_date,
                    'university': university_name
                })
            except Exception as e:
                print(f"Error processing an article: {e}")

        # Go to the next page
        next_button = driver.find_element_by_link_text('Next')
        if next_button:
            next_button.click()
            sleep(2)  # Wait for the next page to load
        else:
            break

driver.quit()

# Write the article data to a CSV file
with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'authors', 'date', 'university']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in articles:
        writer.writerow(article)

print("Scraping completed. Data has been saved to articles.csv.")

    