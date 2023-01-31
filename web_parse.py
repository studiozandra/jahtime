import openai
import requests
import secret
import flask_app
from bs4 import BeautifulSoup

# Set your OpenAI API key
openai.api_key = secret.key


def getUrl(url):
    return url


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}


def crawl_GPT(url):
    # Send a GET request to the web page and retrieve the HTML content
    try:
        # url = "https://www.japanesecooking101.com/nikujaga/"
        url = url
        print("here's the url " + url)
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(
                "Error retrieving web page: status code {}".format(response.status_code))
        html_content = response.text
    except Exception as e:
        print("Error retrieving web page:", e)
        exit()

    # Use the BeautifulSoup library to parse the HTML and extract the relevant text
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        recipie_text = soup.get_text()
    except Exception as e:
        print("Error parsing HTML:", e)
        exit()

    # Use the openai.Completion.create() method to send your recipie text to GPT-3 and receive the analysis
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Based on this recipe, " + recipie_text +
            " create a shopping list of ingredients.",
            max_tokens=1024,
            temperature=0.5
        )
        # Check if the response object has a "text" field
        if "text" in response["choices"][0]:
            # Extract the text field from the response
            text = response["choices"][0]["text"]
            print(text)
            return text
        else:
            print("Error: response does not have a 'text' field")
            return "error error ha ha"
    except Exception as e:
        print("Error analyzing web page:", e)
        exit()
