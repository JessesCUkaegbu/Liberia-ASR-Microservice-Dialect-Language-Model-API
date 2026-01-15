from flask import Flask, request, jsonify, render_template_string
from faster_whisper import WhisperModel
import os

app = Flask(__name__)

print("Loading ASR model...")
model = WhisperModel("base", device="cpu", compute_type="int8")
print("Model loaded successfully!")

UPLOAD_FOLDER = "/tmp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Web Upload Page
# -----------------------------
HTML_PAGE = """
<!doctype html>
<title>ASR Upload</title>
<h2>Upload Audio for Transcription</h2>
<form action="/transcribe" method="post" enctype="multipart/form-data">
  <input type="file" name="audio_file" accept=".wav,.mp3" required>
  <br><br>
  <button type="submit">Transcribe</button>
</form>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PAGE)


# -----------------------------
# Transcription API
# -----------------------------
@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio_file" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio = request.files["audio_file"]

    if audio.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    path = os.path.join(UPLOAD_FOLDER, audio.filename)
    audio.save(path)

    # Safety check
    if os.path.getsize(path) < 1000:
        return jsonify({"error": "Invalid or empty audio file"}), 400

    try:
        segments, info = model.transcribe(path)
        text = " ".join([seg.text for seg in segments])

        os.remove(path)

        return jsonify({
            "language": info.language,
            "transcription": text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
