import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to crawl
url = 'https://vi.wikipedia.org/wiki/Trang_Ch%C3%ADnh'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract textual content from the page
    text_content = soup.get_text()

    # Print or process the textual content as needed
    print(text_content)
else:
    print('Failed to retrieve the web page.')

# Close the HTTP session
response.close()
