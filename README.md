# langchain_tutorial_250609
Set up a local AI agent using python, langchain &amp; ollama.

## Requirements

```
langchain
langchain-ollama
langchain-chroma
pandas
```

## Set up Ollama

Download & install:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download models:
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

Usefule commands:

```python
# Display all models currently instlled
ollama list
```

---
