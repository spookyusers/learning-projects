# ---
# Link Search App
# link_search.py
# Python search app to pull the first several links of a DDGo search query
# ---

# ---
# Additional Resources for modifying code if needed:
# - HTTP Status Codes: MDN Web Docs - HTTP response status codes
#	- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Requests Library Documentation: Requests: HTTP for Humans
#	- https://pypi.org/project/requests/
# - BeautifulSoup Documentation: Beautiful Soup Documentation
#	- https://pypi.org/project/beautifulsoup4/
# ---


# Import required libraries.
import requests # Handle HTTP requests to search engine.
from bs4 import BeautifulSoup # Parse HTML content.

# Define function to fetch search results.
def get_search_results(query):
	# Construct search URL by appending query to DuckDuckGo HTML search endpoint.
	url = 'https://html.duckduckgo.com/html/?q=' + query
	
	# Define headers to mimic a browser request
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
		'AppleWebKit/537.36 (KHTML, like Gecko) '
		'Chrome/58.0.3029.110 Safari/537.3'
}
	
	# Send a GET request to the URL to retrieve the page content.
	response = requests.get(url, headers=headers)
	
	# Check if the request was successful
	print(f"HTTP Response Status Code: {response.status_code}")
	if response.status_code != 200:
		print("Failed to retrieve search results.")
		return[]
	
	# Parse the HTML content
	soup = BeautifulSoup(response.text, 'html.parser')
	
	# Find result links; all <a> tags with class result__a, which contain the result links
	results = []
	for link in soup.find_all('a', class_='result__a'):
		href = link.get('href')
		results.append(href)
		
	return results

# Add a "Main Block" to execute the script

if __name__ == "__main__": # Ensures code runs only when script is executed directly, not when imported as a module.
	
	# Prompt the user for a search query
	query = input("Enter your search query: ")
	
	# Get search results
	links = get_search_results(query)
	
	# Print the first few links
	print("\nTop search results:")
	for i, link in enumerate(links[:10], start=1):
		print(f"{i}. {link}")
		
	
	
