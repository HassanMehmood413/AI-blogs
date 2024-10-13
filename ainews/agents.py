from crewai import Agent
from ainews.tools import tool  # Updated import for tools
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logging.basicConfig(level=logging.INFO)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=True,
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

try:
    llm = create_llm()

    news_researcher = Agent(
        role="Senior Researcher",
        goal='Uncover groundbreaking technologies in {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "Driven by curiosity, you're at the forefront of "
            "innovation, eager to explore and share knowledge that could change "
            "the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
    )

    news_writer = Agent(
        role='Writer',
        goal='Narrate compelling tech stories about {topic}',
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft "
            "engaging narratives that captivate and educate, bringing new "
            "discoveries to light in an accessible manner."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=False
    )
except Exception as e:
    logging.error(f"Error initializing agents: {str(e)}")
    news_researcher = news_writer = None
