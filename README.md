
# AI Code Review Assistant

The AI Code Review Assistant is a web-based tool built using Streamlit that provides automated code reviews powered by artificial intelligence. This application enables developers to receive insights and feedback about their code in real-time, improving code quality and productivity.
--------------------------------
## Features

AI-Powered Code Review: Perform code reviews using an AI model with support for multiple programming languages.
Review History: View the most recent code reviews in the sidebar.
Code Quality Score: Extract and display a quality score for the reviewed code.
Database Integration: Save and retrieve code review history from a database.
Customizable Language Options: Choose the programming language for more accurate reviews.

--------------------------
## Installation

Prerequisites
- Python 3.10 or higher
- Recommended: A virtual environment (e.g., venv)
### Steps
1- Clone the repository:
git clone https://github.com/yourusername/ai-code-review-assistant.git
cd ai-code-review-assistant
2- Install dependencies:
pip install -r requirements.txt
3- Set up environment variables:
- Ensure any required environment variables for database connections or APIs are set.
- Example:
    export DATABASE_URL="sqlite:///reviews.db"
    export MLFLOW_TRACKING_URI="http://localhost:5000"
4- Run the application:
streamlit run src/app.py
-------------------
## Usage

1- Run the app: Use the command above to start the Streamlit server.
2- Interact with the UI:
   - Choose a programming language from the dropdown.
   - Paste your code into the text area.
   - Click the "Review Code" button to initiate the AI review process.
3-View results:
  - The AI feedback and code quality score will be displayed on the screen.
  - The history of reviews can be accessed via the sidebar.

--------------------

## Dependencies

- Streamlit: For building the web-based UI.
- MLflow: To track experiments and AI model outputs.
- Database (SQLite): For storing and retrieving code reviews.
- Other libraries:
  - time: To handle delays in the UI.
  - re: To process and extract code quality scores from text.
- Install all dependencies using:

  - pip install -r requirements.txt

--------------------
## How It Works

1- User Input:
  - The user selects a programming language and pastes their code into the provided text box.
2- AI Processing:
  - The AI model analyzes the code and generates a review along with a quality score.
3- Database Interaction:
  - Reviews are stored in a database for future reference.
4- User Feedback:
  - The review, including suggestions and a quality score, is displayed to the user.
---------------------
## Customization

- Add new programming languages:
  - Edit the PROGRAMMING_LANGUAGES list in config.py to include new languages.
- AI Model Configuration:
  - Modify the function perform_code_review_with_ollama in ai.py to use a different AI model or API.
------------------
## Contributing

Contributions are welcome! Please follow these steps:

1- Fork the repository.
2- Create a new branch for your feature or bug fix.
3- Submit a pull request with a clear description of your changes.
------------------
## License

This project is licensed under the MIT License. See the LICENSE file for details.
----------------
## Contact

For any questions or issues, please reach out to:

- Name: Rafat Jamal Alzakout
- Email: rafat.j.alzakout@hotmail.com
- Location: Grünheide (Mark), Brandenburg, Germany

## Enjoy coding with the AI Code Review Assistant! 🎉
