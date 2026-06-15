# 🇳🇬 English-Igbo Neural Machine Translation

A fine-tuned neural machine translation model and Flask web application for translating between **English and Igbo**, built on Meta's [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) (No Language Left Behind) model with PEFT/LoRA adapters.

---

## 📌 Overview

Igbo is a low-resource African language spoken by over 45 million people, primarily in southeastern Nigeria. This project fine-tunes a state-of-the-art multilingual translation model specifically for English ↔ Igbo translation and packages it into a fully offline Flask web application.

### Key Features

- **Fine-tuned NLLB-200** model with PEFT/LoRA adapters for efficient translation
- **Fully offline** — no internet connection required after setup
- **Flask web app** with a clean, styled interface
- **Flashcards & Quiz** tabs for language learning
- Lightweight adapter weights (~7MB) on top of the base model

---

## 🗂️ Project Structure

```
Igbo-model/
├── app.py                        # Root Flask entry point
├── PROMPT.md                     # Model training prompt reference
├── model instructions.txt        # Setup and usage notes
└── lla-llm-igbo/
    ├── app.py                    # Main Flask application
    ├── index.html                # Landing page
    ├── Dockerfile                # Docker deployment config
    ├── requirements.txt          # Python dependencies
    ├── README.md                 # Sub-module notes
    └── models/
        └── English-Igbo_NLLB_FT_model/
            ├── adapter_model.safetensors   # Fine-tuned LoRA weights
            ├── adapter_config.json         # PEFT adapter configuration
            ├── tokenizer.json              # Tokenizer (NLLB-200)
            ├── tokenizer_config.json       # Tokenizer settings
            ├── sentencepiece.bpe.model     # SentencePiece BPE model
            ├── special_tokens_map.json     # Special token mappings
            └── generation_config.json      # Inference generation config
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.9 or higher
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Madu39627/Igbo-model.git
cd Igbo-model
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r lla-llm-igbo/requirements.txt
```

### 4. Download the base NLLB model

The fine-tuned adapter weights are included in this repo. You also need the base NLLB-200 model from Hugging Face (downloaded automatically on first run):

```
facebook/nllb-200-distilled-600M
```

> ⚠️ First run will download ~2.4GB. Ensure you have a stable internet connection and enough disk space.

---

## 🚀 Running the App

```bash
cd lla-llm-igbo
python app.py
```

Then open your browser and go to:

```
http://localhost:5002
```

---

## 🖥️ App Features

| Tab | Description |
|-----|-------------|
| **Home** | Overview and introduction |
| **Translate** | English → Igbo and Igbo → English translation |
| **Flashcards** | Vocabulary flashcards for learning common words |
| **Quiz** | Test your English-Igbo knowledge |

---

## 🧠 Model Details

| Property | Value |
|----------|-------|
| Base model | `facebook/nllb-200-distilled-600M` |
| Fine-tuning method | PEFT / LoRA |
| Adapter size | ~6.8 MB |
| Source language | English (`eng_Latn`) |
| Target language | Igbo (`ibo_Latn`) |
| Framework | Hugging Face Transformers + PEFT |

### Loading the model manually

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel

BASE_MODEL = "facebook/nllb-200-distilled-600M"
ADAPTER_PATH = "lla-llm-igbo/models/English-Igbo_NLLB_FT_model"

tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
base_model = AutoModelForSeq2SeqLM.from_pretrained(BASE_MODEL)
model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)

inputs = tokenizer("Good morning", return_tensors="pt", src_lang="eng_Latn")
outputs = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["ibo_Latn"])
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🐳 Docker (Optional)

```bash
cd lla-llm-igbo
docker build -t igbo-translator .
docker run -p 5002:5002 igbo-translator
```

---

## 📦 Dependencies

Key packages used:

```
flask
transformers==4.41.0
peft
torch
sentencepiece
```

See `lla-llm-igbo/requirements.txt` for the full list.

---

## 🌍 Why Igbo?

Igbo is one of Nigeria's three major languages but remains severely underrepresented in NLP research and technology. Most translation tools perform poorly on Igbo due to limited training data. This project is part of a broader effort to build better language technology for African languages, alongside a parallel [English-Hausa](https://github.com/Madu39627) translation project.

---

## 🙏 Acknowledgements

- [Meta AI — NLLB-200](https://ai.meta.com/research/no-language-left-behind/) for the base multilingual model
- [Hugging Face](https://huggingface.co/) for the Transformers and PEFT libraries
- The open-source Igbo NLP community for training data contributions

---

## 📄 License

This project is for educational and research purposes. The base NLLB-200 model is released under the [CC-BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/) by Meta AI.
