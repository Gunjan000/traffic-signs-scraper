# Traffic Signs Scraper

`traffic-signs-scraper` is a Python project designed to scrape information about traffic signs in Germany from a Wikipedia page. The scraper uses `BeautifulSoup` to extract structured data such as traffic sign titles, descriptions, image links, and generates custom SVG file names.

## Features

- Extracts traffic sign titles, descriptions, and images.
- Formats traffic sign data with custom SVG file names.
- Saves the data into a CSV file for further use.

## Data Extracted

| Column        | Description                                                     |
|---------------|-----------------------------------------------------------------|
| Title         | The name of the traffic sign (e.g., `Zeichen 626-10`).          |
| Description   | A brief description of the traffic sign.                        |
| ImageLink     | A direct link to the image of the traffic sign on Wikipedia.    |
| SVG_name      | A formatted SVG filename (e.g., `DE_626-10.svg`).               |

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/traffic-signs-scraper.git
2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage
1. Run the script to scrape the data:
    ```bash
    python traffic_signs_scraper.py
    ```
2. The script will generate a CSV file named traffic_signs_with_actual_image_links.csv containing the scraped data.
## File Structure
    ```bash
    traffic-signs-scraper/
    │
    ├── traffic_signs_scraper.py        # Main script for scraping traffic signs
    ├── requirements.txt                # Python dependencies
    └── traffic_signs_with_actual_image_links.csv  # Output data file
    ```
## Requirements
    ```bash
    Python 3.7 or later
    Required Python packages:
    beautifulsoup4
    requests
    pandas
```

### Install dependencies using:

    ```bash
    pip install -r requirements.txt
    ```
## Example Output

| Title           | Description                                      | ImageLink                                                                                                     | SVG_name     |
|:-----------------|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|:-------------|
| Zeichen 626-10  | Leitplatte – Aufstellung rechts; ab 2013 geplant | [Image Link](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Zeichen_626-10.svg/80px-Zeichen_626-10.svg.png) | DE_626-10.svg |
| Zeichen 274-120 | Geschwindigkeitsbegrenzung auf 120 km/h          | [Image Link](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Zeichen_274-120.svg/80px-Zeichen_274-120.svg.png) | DE_274-120.svg |


## Contributions
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.