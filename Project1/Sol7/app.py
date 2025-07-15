import io
import base64
import os

from flask import Flask, render_template, url_for
from flask import request
from gtts import gTTS

# app = Flask(__name__)
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

SUPPORTED_LANGUAGES = ['ko', 'en', 'ja', 'es']

@app.route('/', methods=["GET", "POST"])
def home() -> str:
    # POST 요청
    if request.method == "POST":
        text = request.form.get('input_text')
        # text = "" 비어 있는 값 테스트를 위함.
        if not text or not text.strip():
            return render_template('index.html', error="텍스트를 입력해주세요.")
        lang = request.form.get('lang')
        
        if lang not in SUPPORTED_LANGUAGES:
            return render_template('index.html', error="지원하지 않는 언어입니다.")

        mp3_fp = io.BytesIO()
        try:            
            tts = gTTS(text=text, lang=lang, tld="com", slow=True)
            tts.write_to_fp(mp3_fp)
            static_dir = os.path.join(os.path.dirname(__file__), 'static')
            os.makedirs(static_dir, exist_ok=True)
            output_path = os.path.join(static_dir, 'output.mp3')
            tts.save(output_path)
            mp3_fp.seek(0)
            audio_b64 = base64.b64encode(mp3_fp.read()).decode('utf-8')
            return render_template('index.html', audio=audio_b64, download_url=url_for('static', filename='output.mp3'))
        except Exception as e:
            print("TTS 변환 오류:", e)
            return render_template("index.html", error="음성 변환 중 오류가 발생했습니다.")
    # GET 요청
    else:
        return render_template('index.html')    
    
if __name__ == "__main__":
    app.run(port=8080)