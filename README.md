# GitHub Actions Automation Bot

This is a Python script that uses OpenAI's GPT-3 language model to generate an explanation of the code in a file and writes it to a README.md file. The script is intended to be used as a GitHub Actions workflow, which will automatically execute the script whenever a new commit is pushed to the repository.

## Dependencies

The script requires the following dependencies:

- `requests`
- `openai`

You can install them by running:

```
pip install requests openai
```

## How to Use

To use this script, you need to create a GitHub Actions workflow that executes the script. Here's an example workflow:

```yaml
name: Generate README

on:
  push:
    branches:
      - main

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Install dependencies
        run: pip install requests openai

      - name: Generate README
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          FILENAME: code.py
        run: python generate_readme.py

      - name: Commit changes
        uses: EndBug/add-and-commit@v7
        with:
          author_name: GitHub Actions
          author_email: actions@github.com
          message: Add README.md
```

In this example, the workflow is triggered whenever a new commit is pushed to the `main` branch. It checks out the code, installs the dependencies, and executes the `generate_readme.py` script. The script requires two environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `FILENAME`: The name of the file containing the code you want to explain.

The script reads the content of the file, sends it to OpenAI's GPT-3 language model, and writes the generated explanation to a `README.md` file.

## How to Contribute

If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.

## References

- [OpenAI API documentation](https://beta.openai.com/docs/api-reference/introduction)
- [GitHub Actions documentation](https://docs.github.com/en/actions)