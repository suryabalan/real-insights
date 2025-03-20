Data Modification Based on User Prompts
This project allows users to modify data in a pandas DataFrame based on natural language prompts. By integrating with OpenAI’s language models, users can specify changes to data in a human-readable format, and the system will automatically apply those changes to the DataFrame.

Overview
This tool leverages the power of artificial intelligence to modify data in real-time. Given a pandas DataFrame and a user prompt describing the desired modification (e.g., changing values, adding rows, or updating specific columns), the AI interprets the prompt and performs the necessary transformation to the DataFrame.

Key Features
Natural Language Processing: The system uses OpenAI’s language models to understand user input and translate it into Python code that manipulates a pandas DataFrame.
Dynamic Data Modifications: Modify values based on conditions like column values, row identifiers, or other parameters.
CSV Support: After modification, the updated DataFrame can be returned as a CSV string for easy export or further processing.
Preprocessing Integration: Designed to work in environments where data is preprocessed and fed into a Python service, and modifications can be made in real-time.
How it Works
Input Data: A pandas DataFrame is provided as input to the system.
User Prompt: The user specifies changes to the data using a natural language prompt (e.g., “Change the ‘asset’ value for deal_id 3 to 500”).
AI Interpretation: The AI interprets the user prompt, identifies the correct modification (e.g., updating values, adding rows), and generates the necessary Python code.
Apply Modification: The system modifies the DataFrame based on the AI's interpretation.
Output: The modified DataFrame is returned in a format that can be further processed (e.g., CSV, pandas DataFrame).
Installation
To run this project locally, make sure you have the following dependencies installed:

bash
Copy
pip install openai pandas
Additionally, ensure you have an OpenAI API key set up to interact with the GPT models. You can obtain an API key by visiting OpenAI’s website.
