import pyshorteners

url = input("Enter long URL: ")

shortener = pyshorteners.Shortener()

short_url = shortener.tinyurl.short(url)

print("Short URL:", short_url)