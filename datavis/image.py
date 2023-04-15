import folium
import json
import csv
import requests

# Load the results from the CSV file
results = {}
with open("province_results.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        results[row["Province/Territory"]] = int(row["Results"])

# Download the GeoJSON file for Canadian provinces and territories
geojson_url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries/CAN/ADM1.geo.json"
response = requests.get(geojson_url)
geo_data = response.json()

# Function to get the result count for each province/territory in the GeoJSON file
def get_result_count(province_name):
    return results.get(province_name, 0)

# Create a Folium map centered on Canada
m = folium.Map(location=[56.130366, -106.346771], zoom_start=4)

# Create a Choropleth layer for the heatmap
folium.Choropleth(
    geo_data=geo_data,
    name="choropleth",
    data=results,
    columns=["Province/Territory", "Results"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="AlphaFold Related Research Results",
    highlight=True,
).add_to(m)

# Add labels with the results count to each province/territory
style_function = lambda x: {"fillColor": "#ffffff", "stroke": False, "fillOpacity": 0}
highlight_function = lambda x: {"fillColor": "#000000", "stroke": False, "fillOpacity": 0}
labels = folium.features.GeoJson(
    geo_data,
    style_function=style_function,
    control=False,
    highlight_function=highlight_function,
    tooltip=folium.features.GeoJsonTooltip(
        fields=["name"],
        aliases=["Province/Territory: "],
        labels=True,
        sticky=False,
        style="font-size: 12px;",
    ),
)
m.add_child(labels)
m.keep_in_front(labels)

# Save the heatmap to an HTML file
m.save("heatmap.html")

print("Heatmap saved to heatmap.html.")
