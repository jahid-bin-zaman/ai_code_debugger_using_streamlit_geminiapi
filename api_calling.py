from google import genai
from dotenv import load_dotenv
import os

# loading the environment variable
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# initialze a client
client = genai.Client(api_key=gemini_api_key)


# hints generator
def hint_generator(images):
    
    prompt = """Find the error or mistakes from the images and just give me hints how can i solve it.
    Don't give the solution directly. Give the answer in markdown format, short and to the point"""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text
    
    
# solution generator
def solution_generator(images):
    
    prompt = """Find the error or mistakes from the images and give me the solution of it.
    Give the answer in markdown format, short and to the point"""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text