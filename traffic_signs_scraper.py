import pandas as pd
import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = 'https://de.wikipedia.org/wiki/Bildtafel_der_Verkehrszeichen_in_der_Bundesrepublik_Deutschland_seit_2017'
webpage = requests.get(url).text
soup = BeautifulSoup(webpage, 'lxml')

# Target the main content div
content_div = soup.find('div', id='mw-content-text')

# Initialize an empty list to store data
data = []

# Find all relevant <ul> tags within the content div
if content_div:
    gallery_lists = content_div.find_all('ul', class_='gallery mw-gallery-traditional')

    # Iterate through all <ul> tags
    for gallery in gallery_lists:
        items = gallery.find_all('li', class_='gallerybox')
        for item in items:
            # Extract image link from the src attribute
            img_tag = item.find('img')
            if img_tag:
                # Extract the actual image link
                src = img_tag['src']  # Use the 'src' attribute for the image link
                # Make sure the link is absolute
                image_link = f"https:{src}"

            # Extract bold title
            bold_text = item.find('b')
            title = bold_text.text if bold_text else None

            # Extract description text
            description_tag = item.find('div', class_='gallerytext')
            description = description_tag.text.strip() if description_tag else None

            # Append to the data list
            data.append([title, description, image_link])

# Create a DataFrame
columns = ['Title', 'Description', 'ImageLink']
df = pd.DataFrame(data, columns=columns)

# Add the SVG_name column
def generate_svg_name(title):
    if not title:
        return None
    # Extract the number part after "Zeichen"
    number_part = title.replace("Zeichen ", "").strip()
    return f"DE_{number_part}.svg"

df['SVG_name'] = df['Title'].apply(generate_svg_name)

# Display the DataFrame shape and preview
print("DataFrame Shape:", df.shape)


# Optionally save to a CSV
df.to_csv('traffic_signs_with_actual_image_links.csv', index=False)
#df.sample(75)