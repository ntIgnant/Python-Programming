# Import the urllib.request module
import urllib.request


def main():
	url = str(input("Enter a URL: "))
	if not url.startswith("https://"):
		transfer_protocol = "https://"
		url = transfer_protocol + url

	# Specify the user agent to avoid HTTP error 406
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

	req = urllib.request.Request(url, headers = headers)

	try:
		# Open the URL with headers
		with urllib.request.urlopen(req) as response:
			content = response.read().decode(errors='ignore')
			return content
	except urllib.error.HTTPError as e:
		print(f"HTTP Error: {e.code} - {e.reason}")
		return ""

def occurences(text, word):
	word_count = text.count(word) # .count() will count the num of occurrences that the text has of the word

	return word_count

content = main()
print(content)
word_occurences = occurences(content, "<div")

print(word_occurences)