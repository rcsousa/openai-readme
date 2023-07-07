# Syslog-ng Indexer

This code is a Python script that creates a FAISS index from a log file. The FAISS index is a similarity search index that allows for fast and efficient similarity searches. The script reads the content from a log file, splits it into chunks of 1000 characters, and creates a FAISS index with a dimensionality compatible with OpenAI embeddings. The script also includes commented code that initializes a Kafka consumer and creates a FAISS index if there is a message in the topic.

## Dependencies

This script requires the following dependencies:

- `langchain` (https://github.com/LangChain/langchain)
- `numpy` (https://numpy.org/)
- `faiss` (https://github.com/facebookresearch/faiss)
- `kafka-python` (https://github.com/dpkp/kafka-python)

You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```

## How to Execute the Code

To execute the code, run the following command:

```
python main.py
```

This will create a FAISS index from the `Linux_2k.log` file and save it to a local file named `faiss_syslog_index_file`.

## How to Contribute

If you want to contribute to this project, you can fork the repository and submit a pull request with your changes. Please make sure to follow the PEP 8 style guide (https://www.python.org/dev/peps/pep-0008/) and include tests for your changes.

## References

- LangChain. (n.d.). LangChain. GitHub. https://github.com/LangChain/langchain
- NumPy. (2021). NumPy. https://numpy.org/
- Facebook Research. (n.d.). faiss. GitHub. https://github.com/facebookresearch/faiss
- Kafka-Python. (n.d.). dpkp/kafka-python. GitHub. https://github.com/dpkp/kafka-python