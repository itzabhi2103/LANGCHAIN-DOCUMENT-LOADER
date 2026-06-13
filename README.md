# Understanding Document Loaders in LangChain

This repository explores **Document Loaders**, one of the most important components in LangChain for building **Retrieval-Augmented Generation (RAG)** applications. Document loaders help ingest data from various sources and convert it into a standardized format that can be processed by Large Language Models (LLMs).

---

## Table of Contents

* Introduction to RAG
* Standardizing Data with Document Objects
* Common Document Loaders

  * TextLoader
  * PyPDFLoader
  * DirectoryLoader
  * WebBaseLoader
  * CSVLoader
* Advanced Techniques

  * Load vs Lazy Load
  * Custom Document Loaders
* Conclusion

---

## Introduction to RAG

**Retrieval-Augmented Generation (RAG)** is a technique that enhances the capabilities of Large Language Models by connecting them to external knowledge sources.

Instead of relying solely on pre-trained knowledge, RAG allows the model to:

* Retrieve relevant information from external documents.
* Access private or domain-specific data.
* Provide more accurate and up-to-date responses.
* Reduce hallucinations by grounding responses in real data.

---

## Standardizing Data with Document Objects

Document loaders transform raw data from different sources into a standardized **Document** object.

Each Document contains:

### `page_content`

The actual textual content extracted from the source.

```python
document.page_content
```

### `metadata`

Additional contextual information about the document, such as:

* File path
* Source URL
* Page number
* Creation date
* Author information

```python
document.metadata
```

This standardized structure makes it easy to process documents regardless of their original format.

---

## Common Document Loaders

### 1. TextLoader

Used to load plain text files such as:

* Notes
* Logs
* Configuration files
* Source code files

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt")
docs = loader.load()
```

---

### 2. PyPDFLoader

Used to extract text from PDF files.

Key Features:

* Processes PDFs page by page.
* Creates a separate Document object for each page.
* Preserves page-level metadata.

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
docs = loader.load()
```

---

### 3. DirectoryLoader

Used for bulk loading multiple files from a directory.

Key Features:

* Loads files recursively.
* Supports pattern matching.
* Ideal for large document collections.

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader(
    "./data",
    glob="*.pdf"
)

docs = loader.load()
```

---

### 4. WebBaseLoader

Used to load content from web pages.

Key Features:

* Extracts text from static HTML pages.
* Utilizes BeautifulSoup for parsing.
* Useful for web-based knowledge sources.

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
docs = loader.load()
```

---

### 5. CSVLoader

Used to load structured data from CSV files.

Key Features:

* Treats each row as a separate Document.
* Preserves column information.
* Useful for tabular datasets.

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="data.csv")
docs = loader.load()
```

---

## Advanced Techniques

### Load vs Lazy Load

#### `load()`

Loads all documents into memory at once.

Best suited for:

* Small datasets
* Quick prototyping
* Local testing

```python
docs = loader.load()
```

#### `lazy_load()`

Loads documents one at a time using a generator.

Benefits:

* Lower memory consumption
* Better scalability
* Suitable for large datasets

```python
for doc in loader.lazy_load():
    print(doc.page_content)
```

---

### Custom Document Loaders

LangChain allows developers to create custom loaders for unsupported data sources.

This is achieved by extending the `BaseLoader` class.

Benefits:

* Support proprietary file formats.
* Connect to internal databases.
* Integrate with custom APIs.
* Build organization-specific ingestion pipelines.

```python
from langchain_core.document_loaders import BaseLoader

class CustomLoader(BaseLoader):
    def load(self):
        pass
```

---

## Conclusion

Document Loaders are the first step in building effective RAG applications. They provide a unified way to ingest data from multiple sources and convert it into LangChain's standard Document format.

By understanding and utilizing loaders such as:

* TextLoader
* PyPDFLoader
* DirectoryLoader
* WebBaseLoader
* CSVLoader

you can efficiently prepare data for retrieval, embedding, and downstream LLM applications.
