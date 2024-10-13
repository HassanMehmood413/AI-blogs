from crewai import Task
from ainews.tools import tool  # Updated import for tools
from ainews.agents import news_researcher, news_writer  # Updated import for agents
import logging

logging.basicConfig(level=logging.INFO)

try:
    research_task = Task(
        description=(
            "Identify the next big trend in {topic}. "
            "Focus on identifying pros and cons and the overall narrative. "
            "Your final report should clearly articulate the key points, "
            "its market opportunities, and potential risks."
        ),
        expected_output='A comprehensive 3-paragraph report on the latest trends.',
        tools=[tool],
        agent=news_researcher,
    )

    write_task = Task(
        description=(
            "Compose an insightful article on {topic}. "
            "Focus on the latest trends and how it's impacting the industry. "
            "This article should be easy to understand, engaging, and positive."
        ),
        expected_output='A 4-paragraph article on {topic} advancements formatted as markdown.',
        tools=[tool],
        agent=news_writer,
        async_execution=False,
        output_file='new-blog-post.md'
    )
except Exception as e:
    logging.error(f"Error initializing tasks: {str(e)}")
    research_task = write_task = None
