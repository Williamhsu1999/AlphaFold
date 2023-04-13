import requests
from bs4 import BeautifulSoup
import time
import datetime

def get_google_scholar_results(queries, start_page, num_pages):
    base_url = "https://scholar.google.com/scholar"
    all_results = []
    unique_titles = set()

    for query in queries:
        for i in range(start_page, start_page + num_pages):
            params = {
                "q": query,
                "start": (i - 1) * 10
            }
            response = requests.get(base_url, params=params)
            soup = BeautifulSoup(response.text, "html.parser")
            search_results = soup.find_all("div", class_="gs_ri")

            for result in search_results:
                title = result.find("h3", class_="gs_rt").text

                if title not in unique_titles:
                    unique_titles.add(title)

                    author_info = result.find("div", class_="gs_a").text
                    snippet = result.find("div", class_="gs_rs").text

                    all_results.append({
                        "title": title,
                        "author_info": author_info,
                        "snippet": snippet
                    })

            print(f"Fetching page {i} for query '{query}'...")
            time.sleep(2)

    return all_results

if __name__ == "__main__":
    canadian_terms = [
    "Canada",
    "Canadian",
    "Ontario",
    "Quebec",
    "British Columbia",
    "Alberta",
    "Manitoba",
    "Saskatchewan",
    "Nova Scotia",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Prince Edward Island",
    "Northwest Territories",
    "Yukon",
    "Nunavut",

    #uni list 
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

# canadian funding agencies 

    "Canadian Institutes of Health Research",
    "Natural Sciences and Engineering Research Council",
    "Social Sciences and Humanities Research Council",
    "Canada Foundation for Innovation",
    "Genome Canada",
    "Canada Research Chairs",
    "Ontario Graduate Scholarship",
    "Ontario Trillium Scholarship",
    "Vanier Canada Graduate Scholarships",
    "Banting Postdoctoral Fellowships",
    "Canada Excellence Research Chairs",
    "Canada First Research Excellence Fund",
    "Networks of Centres of Excellence",
    "Canadian Space Agency",
    "National Research Council Canada",
    "Canadian Cancer Society",
    "Canadian Diabetes Association",
    "Canadian Heart and Stroke Foundation",
    "Innovation, Science and Economic Development Canada",
    "Mitacs",
    "Fonds de recherche du Québec",
    "Michael Smith Foundation for Health Research",
    "New Brunswick Health Research Foundation",
    "Nova Scotia Health Research Foundation",
    "Saskatchewan Health Research Foundation",
    "Alberta Innovates",
    "Research Manitoba",
    "Ontario Research Fund",

]

    queries = [f"({term}) (alphafold OR alphafold2)" for term in canadian_terms]

    start_page = 1
    num_pages = 20

    all_results = get_google_scholar_results(queries, start_page, num_pages)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("alphafold_results.txt", "w", encoding="utf-8") as file:
        file.write(f"Scraped on: {current_time}\n")
        file.write(f"Found {len(all_results)} articles:\n")
        for result in all_results:
            file.write(f"Title: {result['title']}\nAuthor Info: {result['author_info']}\nSnippet: {result['snippet']}\n\n")
