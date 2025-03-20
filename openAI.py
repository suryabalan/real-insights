from io import StringIO

import openai
import pandas as pd

# Set up OpenAI API key
openai.api_key = "my_api_key"

# Example DataFrame
data = {'deal_id': [1, 2, 3, 4],
        'asset': [100, 200, 300, 400],
        'email_count': [5, 10, 15, 20],
        'share': [0.5, 0.6, 0.7, None]}

df = pd.DataFrame(data)


# Function to interact with GPT model and modify the DataFrame
def modify_dataframe_with_prompt(df, prompt):
    # Prepare the DataFrame in text format to pass as context to the AI model
    df_str = df.to_string(index=False)

    # Send the prompt to GPT to modify the data based on the user's instruction
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or gpt-3.5-turbo
        messages=[
            {"role": "system",
             "content": "You are an AI that modifies data in pandas DataFrames based on user prompts."},
            {"role": "user",
             "content": f"The following is a pandas DataFrame:\n{df_str}\n\n{prompt}\n\nPlease return the modified "
                        f"DataFrame in CSV format without any other response:"}
        ],
        max_tokens=150,
        temperature=0.5
    )

    # Extract the AI's response, which should contain code to modify the DataFrame
    modified_data = response['choices'][0]['message']['content'].strip()

    cleaned_response = modified_data.strip('\"')  # Remove leading and trailing quotes
    cleaned_response = cleaned_response.replace('\\n', '\n')

    # Convert the cleaned response into a pandas DataFrame
    modified_df = pd.read_csv(StringIO(cleaned_response))

    # Return the modified DataFrame
    return modified_df


# Example prompt to modify the asset value for deal_id 3
prompt = "Change share value as 10 for deal id 3"

# Call the function to modify the DataFrame
modified_df = modify_dataframe_with_prompt(df, prompt)

# Show the modified DataFrame
print(modified_df)
