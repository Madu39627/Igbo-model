# LinguAfrika English-Igbo Translation Server

A standalone Flask REST API server serving a fine-tuned NLLB (No Language Left Behind) model for English to Igbo translation. The model is a PEFT/LoRA adapter hosted on Hugging Face at `drakensberg85/English-Igbo_NLLB_FT_model`.

## Prerequisites

- Python 3.10+
- Docker (optional)
- Git

## Model Download

Download the model weights into `./models/English-Igbo_NLLB_FT_model/`:

```bash
huggingface-cli download drakensberg85/English-Igbo_NLLB_FT_model --local-dir ./models/English-Igbo_NLLB_FT_model/
```

## Running Locally (Python)

```bash
pip install -r requirements.txt
python app.py
```

Server starts at `http://localhost:5002`.

## Running with Docker

```bash
docker build -t lla-igbo .
docker run -p 5002:5002 lla-igbo
```

## API Reference

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "model": "drakensberg85/English-Igbo_NLLB_FT_model",
  "device": "cuda"
}
```

### POST /translate

Translate a single text.

**Request:**
```json
{
  "text": "Hello world",
  "source_lang": "eng_Latn",
  "target_lang": "ibo_Latn"
}
```

**Response:**
```json
{
  "translation": "Ndewo ụwa"
}
```

**curl example:**
```bash
curl -X POST http://localhost:5002/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "source_lang": "eng_Latn", "target_lang": "ibo_Latn"}'
```

### POST /translate/batch

Translate multiple texts.

**Request:**
```json
{
  "texts": ["Hello", "Goodbye"],
  "source_lang": "eng_Latn",
  "target_lang": "ibo_Latn"
}
```

**Response:**
```json
{
  "translations": ["Ndewo", "Ka ọ dị"]
}
```

**curl example:**
```bash
curl -X POST http://localhost:5002/translate/batch \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Hello", "Goodbye"], "source_lang": "eng_Latn", "target_lang": "ibo_Latn"}'
```

### GET /languages

Get supported language codes.

**Response:**
```json
{
  "source_language": "English",
  "source_lang_code": "eng_Latn",
  "target_language": "Igbo",
  "target_lang_code": "ibo_Latn"
}
```

## Language Codes

| Language | Code |
|----------|------|
| English | eng_Latn |
| Igbo | ibo_Latn |

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| PORT | 5002 | Server port |
| HOST | 0.0.0.0 | Server host |
| DEBUG | false | Enable debug mode |

## Error Responses

| HTTP Code | Description | Example |
|-----------|-------------|---------|
| 400 | Bad Request - Missing or invalid input | `{"error": "Missing 'text' in request body"}` |
| 500 | Internal Server Error - Translation failed | `{"error": "Translation error details"}` |