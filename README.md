# GitHub Actions AI README.md Generator

This is a Python script that uses Azure OpenAI's GPT-3.5-turbo language model to generate an explanation of the code in a file and writes it to a README.md file. The script is intended to be used as a GitHub Actions workflow, triggered by a push to a repository.

## Dependencies

The script requires the dependencies in requirements.txt:

```text
aiohttp==3.8.4
aiosignal==1.3.1
async-timeout==4.0.2
attrs==23.1.0
certifi==2023.5.7
charset-normalizer==3.2.0
frozenlist==1.3.3
idna==3.4
multidict==6.0.4
openai==0.27.8
requests==2.31.0
tqdm==4.65.0
urllib3==2.0.3
yarl==1.9.2
```


## How to Use

To use this script, you need to create a GitHub Actions workflow that executes the script. Here's an example workflow:

```yaml
name: Explain Code and Update README

on:
  push:
    branches:
      - <<replace with your branch name (ie. main, master)>>

jobs:
  explain_code:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Checkout action
        uses: actions/checkout@v3
        with:
          repository: rcsousa/openai-readme
          path: ai-readme

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.10.6

      - name: Install dependencies
        run: pip install -r ai-readme/requirements.txt
        
      - name: Run script
        id: run_script
        run: |
          python ai-readme/app.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_API_BASE: ${{ secrets.OPENAI_API_BASE }}
          GIT_EMAIL: ${{ secrets.GIT_EMAIL }}
          GIT_USERNAME: ${{ secrets.GIT_USERNAME }}
          DIRECTORT: <<replace with the folder of your code (ie . for the /)>>

      - name: Create /docs files
        run: |
          git config --global user.name ${{ secrets.GIT_USERNAME }}
          git config --global user.email ${{ secrets.GIT_EMAIL }}
          git add docs/*.md
          git add README.md
          git commit -m "Updating AI Generated Documentation"
          git push

```

This workflow will use Azure OpenAI Model gpt-3.5-turbo to explain the code on the file you defined in the FILENAME environment variable whenever there's a push to the `main` branch. It will install the required dependencies, set the necessary environment variables, and run the script. Finally, it will commit the changes to the repository.

# GitHub Secrets

To make the GitHub Actions workflow to work correctly, you must have an API Key and API endpoint for Azure OpenAI Services or OpenAI, as well as the e-mail and username of a user with read/write permission in the repository you want to generate the README.md. 

Create a GitHub Secret (Settings > Secrets and variables > New repository secret) for:
- GIT_EMAIL
- GIT_USERNAME
- OPENAI_API_BASE
- OPENAI_API_KEY

## How to Contribute

If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.

## References

- [OpenAI API documentation](https://beta.openai.com/docs/api-reference/introduction)
- [GitHub Actions documentation](https://docs.github.com/en/actions)