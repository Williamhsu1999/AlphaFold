import csv
import requests

api_key = "AIzaSyDoyA33aZRenHpxwD3aoavgv61w7taqVUk"
search_engine_id = "102beab6c66db4fec"

provinces = [
    "Alberta",
    "British Columbia",
    "Manitoba",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Northwest Territories",
    "Nova Scotia",
    "Nunavut",
    "Ontario",
    "Prince Edward Island",
    "Quebec",
    "Saskatchewan",
    "Yukon",
]

def google_search(province_name):
    query = f'("alphafold" OR "alphafold2" OR "alphafold 2") AND "{province_name}"'
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}'
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['error']['message']}")
        return 0

    if 'searchInformation' not in data:
        print(f"No search information found for {province_name}.")
        return 0

    return data['searchInformation']['totalResults']

results = []

for province_name in provinces:
    result_count = google_search(province_name)
    results.append({"Province/Territory": province_name, "Results": result_count})

with open("province_results.csv", "w", newline="") as csvfile:
    fieldnames = ["Province/Territory", "Results"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)

print("Search completed and results saved to province_results.csv.")
