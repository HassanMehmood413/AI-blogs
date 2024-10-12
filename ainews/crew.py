from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
import logging

logging.basicConfig(level=logging.INFO)

def generate_news(topic):
    try:
        crew = Crew(
            agents=[news_researcher, news_writer],
            tasks=[research_task, write_task],
            process=Process.sequential,
        )

        result = crew.kickoff(inputs={'topic': topic})
        
        # Read the content of the generated file
        with open('new-blog-post.md', 'r') as file:
            content = file.read()
        
        return content
    except Exception as e:
        logging.error(f"Error in generate_news: {str(e)}")
        raise