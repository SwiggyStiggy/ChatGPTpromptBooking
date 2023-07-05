import openai
import dotenv
import os
import requests
#import flask not finished yet.


dotenv.load_dotenv('.env')
API_AI=os.getenv('API_AI')
openai.api_key=API_AI
rapid_key = os.getenv("RAPID_API_KEY")
rapid_host = os.getenv("RAPID_API_HOST")

def basicGeneration(userPrompt):
    completion=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content



def locations():

    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"

    text = input("search for location:")

    querystring = {
        "name": text,
        "locale": "en-us"
    }

    headers = {
        "X-RapidAPI-Key": rapid_key,
        "X-RapidAPI-Host": rapid_host
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.text



analysis = basicGeneration(locations())

print(analysis)




