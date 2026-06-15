from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel
import torch

app = Flask(__name__)
CORS(app, origins="*")

MODEL_PATH = r".\models\English-Igbo_NLLB_FT_model"
BASE_MODEL = "facebook/nllb-200-distilled-600M"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
base_model = AutoModelForSeq2SeqLM.from_pretrained(BASE_MODEL)
model = PeftModel.from_pretrained(base_model, MODEL_PATH)
model.eval()
target_lang_id = tokenizer.convert_tokens_to_ids("ibo_Latn")
print("Model ready! Target lang ID:", target_lang_id)

@app.route("/translate", methods=["POST", "OPTIONS"])
def translate():
    if request.method == "OPTIONS":
        r = jsonify({})
        r.headers["Access-Control-Allow-Origin"] = "*"
        r.headers["Access-Control-Allow-Headers"] = "Content-Type"
        r.headers["Access-Control-Allow-Methods"] = "POST"
        return r
    try:
        data = request.json
        text = data.get("text", "")
        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                forced_bos_token_id=target_lang_id,
                max_length=200
            )
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        resp = jsonify({"translation": translation})
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.headers["Access-Control-Allow-Origin"] = "*"
        return resp, 500

if __name__ == "__main__":
    app.run(port=5002, debug=False)