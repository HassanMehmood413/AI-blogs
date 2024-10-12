from dotenv import load_dotenv
load_dotenv()
import os
import logging
from crewai_tools import SerperDevTool

logging.basicConfig(level=logging.INFO)

try:
    os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
    tool = SerperDevTool()
except Exception as e:
    logging.error(f"Error initializing tools: {str(e)}")
    tool = None