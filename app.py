import os
import openai


def main():
    """
    The main function of the program. This function reads a file, sends its content to OpenAI's GPT-35-TURBO API to generate an explanation, and writes the explanation to a README.md file. The README.md file will have a project description, instructions on how to install the dependencies and how to execute the code, how to contribute, and any references to external sources of information if available.
    """

    openai.api_type = "azure"
    openai.api_version = "2023-05-15" 
    openai.api_base = os.getenv("OPENAI_API_BASE") 
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Get a directory name from the environment variables. If the variable is not set, use the current directory
    directory = os.environ.get('DIRECTORY', '.')
    print('Directory: ' + directory)
    
    # List all python files in the directory, including subdirectories, but excluding hidden files, virtual environments and the ai-readme directory
    files = []
    for root, directories, filenames in os.walk(directory):
        if  'ai-readme' not in root:
            for filename in filenames:
                if filename.endswith('.py') and not filename.startswith('.') and not 'venv' in root:
                    files.append(os.path.join(root, filename))

    print('Files: ' + str(files))

    for filename in files:

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

        # Create a docs directory if it doesn't exist
        if not os.path.exists('docs'):
            os.mkdir('docs')

        # Write the explanation to a file in the docs directory. The filename is the same as the original file but with a .md extension
        with open('docs/' + filename.split('/')[-1].split('.')[0] + '.md', 'w') as file:
            file.write(explanation)

    # Read all *.md files in the docs directory
    files = []
    for root, directories, filenames in os.walk('docs'):
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(os.path.join(root, filename))

    # Combine all *.md files into a single variable
    readme = ''
    for filename in files:
        with open(filename, 'r') as file:
            readme += file.read() + '\n\n'

    # Call OpenAI's GPT-35-TURBO API to generate a README.md file that is the summary of all the *.md files in the docs directory and invite the reader to contribute to the project
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k", 
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a GitHub Actions automation bot that upon exectution, will create a README.md file with the explanation of the code in this repository."},
            {"role": "user", "content": "Sumarize the content in the docs folder, using GitHub Markdown, create a nice and easy to understand README.md file to be included in the project repository.  The documentation is as follows: \n\n" + readme},
        ]
    )
    explanation = response['choices'][0]['message']['content']

    # Write the explanation to a README.md file
    with open('README.md', 'w') as file:
        file.write(explanation)

if __name__ == '__main__':
    main()

