import os
import requests
import subprocess
import openai


def main():

    openai.api_type = "azure"
    openai.api_version = "2023-05-15" 
    openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value.
    openai.api_key = os.getenv("OPENAI_API_KEY")


    #get current directory
    #current_dir = os.getcwd()

    # Get the filename from the environment variables
    filename = os.environ['FILENAME']

    # Read the content of the file
    with open(filename, 'r') as file:
        code = file.read()

    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a GitHub Actions automation bot that upon exectution, will create a README.md file with the explanation of the code in this repository."},
            {"role": "user", "content": "Explain this code with as much detail as possible and, using GitHub Markdown, create a nice and easy to understand README.md file to be included in the project repository. The file always must have a project description, instructions on how to install the dependencies and how to execute the code, how to contribute, and any references to external sources of information if available The code is as follows: \n\n" + code},
        ]
    )

    print(response)

    explanation = response['choices'][0]['message']['content']

    print(explanation)


    # Write the explanation to the README.md file
    with open('README.md', 'w') as file:
        file.write(explanation)

#    # Configure git
#    subprocess.run(['git', 'config', '--global', 'user.email', os.environ['GIT_EMAIL']])
#    subprocess.run(['git', 'config', '--global', 'user.name', os.environ['GIT_USERNAME']])
#
#    # Add the README.md file to the git staging area
#    subprocess.run(['git', 'add', 'README.md'])
#
#    # Commit the changes
#    subprocess.run(['git', 'commit', '-m', 'Add explanation to README.md'])
#
#    # Push the changes to the repository
#    subprocess.run(['git', 'push', 'origin', 'HEAD'])

if __name__ == '__main__':
    main()

