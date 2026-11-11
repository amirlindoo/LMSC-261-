
import requests

# Function to format and print artwork
def format_and_print(data, min, max):
    art_data = data['data']

    for d in art_data:
        title = d.get('title', 'Unknown Title')
        artist = d.get('artist_display', 'Unknown Artist')
        year = d.get('date_display', 'Unknown Year')

        # Find a year in the artwork's date
        import re
        years = re.findall(r'\b\d{4}\b', year)

        if years:
            artwork_year = int(years[0])

            if min <= artwork_year <= max:
                print(f"{title} is by {artist} which was displayed on {year}")


# Ask the user for input
search = input("What would you like to search? ")
min_year = int(input("What's the minimum year you'd like to search? "))
max_year = int(input("What's the maximum year you'd like to search? "))

# API headers
headers = {
    "AIC-User-Agent": "museum-crawler (aharper3@berklee.edu)",
    "User-Agent": "museum-crawler (aharper3@berklee.edu)"
}

# Search parameters
params = {
    'q': search,
    'fields': 'title,artist_display,date_display'
}

# Request artwork from the museum API
response = requests.get(
    "https://api.artic.edu/api/v1/artworks/search",
    params=params,
    headers=headers
)

# Print the results
if response.status_code == 200:
    format_and_print(response.json(), min_year, max_year)
else:
    print("Something went wrong!")
