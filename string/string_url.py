#url is present in a string
def url_in_string(text):
    return "http://" in text or "https://" in text or "www" in text

text = "Visit our blog at https://example.com for more updates."
if url_in_string(text):
    print("url is present in the string")
else:
    print("url is not present in the string")