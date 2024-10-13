# CrewAI Task Automation with Agents

This project automates the process of identifying trends and writing articles using CrewAI, integrating agents like a Senior Researcher and Writer to perform tasks such as research and content creation. Users can provide custom topics, and the agents will analyze and generate the required output using advanced tools.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
  - [Setting up Virtual Environment](#setting-up-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Running the Project](#running-the-project)
-[Important Note](#important-note)

## Project Overview

This project leverages **CrewAI** to automate research and article writing based on user-provided prompts. The system includes:
- A **Senior Researcher Agent** to identify trends, pros, cons, opportunities, and risks.
- A **Writer Agent** to craft engaging and insightful articles.
- Flexible task assignment and seamless flow of information between agents.

## Technologies Used

- **Python 3.8+**: The main programming language.
- **CrewAI**: A framework for managing agents and task execution.
- **Google Generative AI (Gemini Model)**: For natural language processing and content generation.
- **LangChain**: To handle interactions with language models.
- **Serper API**: For advanced web searches.

These technologies were chosen for their ability to:
- Perform complex task orchestration with agents.
- Provide advanced natural language understanding and generation capabilities.
- Seamlessly handle internet search queries and information retrieval.

## Setup and Installation

### 1. Installing Python
First, ensure that Python 3.8 or higher is installed on your system. You can download it from [here](https://www.python.org/downloads/).

To check your Python version, open your terminal (or Command Prompt) and run:
```bash
python --version

```

## Running the project

### Creating a Virtual Environment

Before running the application, it's recommended to create a virtual environment to isolate dependencies and avoid conflicts with other projects.

1. **Install `virtualenv`** (if not already installed):
    ```bash
    pip install virtualenv
    ```

2. **Create a virtual environment**:
    ```bash
    virtualenv venv
    ```
    This will create a directory named `venv` in your project directory, containing the isolated Python environment.

3. **Activate the virtual environment**:
    - **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    - **On macOS and Linux**:
        ```bash
        source venv/bin/activate
        ```

    After activation, your terminal prompt should change to indicate that you are now working within the virtual environment.


4. **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

To run the app:

1. **Go in the ainews Folder:**
   ```bash
   cd ainews
   ```

2. **Run the app.py file:**
    ```bash
    python app.py
    ```
3. ***Open the localhost link from terminal***

### Important Note

- If you get any error make sure to add the Serper API key.
- Configure the API keys and endpoints according to your backend setup.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



