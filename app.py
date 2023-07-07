import os
import requests
import openai


def main():
    """
    The main function of the program. This function reads a file, sends its content to OpenAI's GPT-35-TURBO API to generate an explanation, and writes the explanation to a README.md file. The README.md file will have a project description, instructions on how to install the dependencies and how to execute the code, how to contribute, and any references to external sources of information if available.
    """

    openai.api_type = "azure"
    openai.api_version = "2023-05-15" 
    openai.api_base = os.getenv("OPENAI_API_BASE") 
    openai.api_key = os.getenv("OPENAI_API_KEY")


    # Get the filename from the environment variables
    filename = os.environ['FILENAME']

    # Read the content of the file
    with open(filename, 'r') as file:
        code = file.read()

    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k", 
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a GitHub Actions automation bot that upon exectution, will create a README.md file with the explanation of the code in this repository."},
            {"role": "user", "content": "Explain this code with as much detail as possible and, using GitHub Markdown, create a nice and easy to understand README.md file to be included in the project repository. The file always must have a project description, instructions on how to install the dependencies and how to execute the code, how to contribute, and any references to external sources of information if available The code is as follows: \n\n" + code},
        ]
    )

    explanation = response['choices'][0]['message']['content']

    # Write the explanation to the README.md file
    with open('README.md', 'w') as file:
        file.write(explanation)


if __name__ == '__main__':
    main()

