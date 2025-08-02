from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from flask_cors import CORS
import os
from dotenv import load_dotenv
 

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True) #flask ile sunucu arasında iletişimi sağlar.

#Flask app.route komutu ile belirtilen URL isteği geldiğinde ilgili dosyayı istemciye gönderir. js ve html dosyalarını manuel yazmak gerekir.

@app.route("/")
def serve_form():
    return send_from_directory(".", "form.html")
    
@app.route("/api.js")
def serve_js():
    return send_from_directory(".", "api.js")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/generateActivity", methods=["POST"]) #kullanıcıdan veri alma
def generateActivity():
    data = request.json #tarayıcıdan gelen json verisini alır
    prompt = f"{data['age']} yaşlarında bir {data['gender']} çocuğu için {data['number']} kişilik {data['place']} da {data['hobby']} gibi hobileri içeren basit ama etkili bir aktivite, etkinlik, oluştur. Yaralanma ya da yanlış davranış sergilemesine neden olabilecek etkinlikleri içermesin. Öğretici olsun."

    try: #api ile modele promptu gönderme işlemi yapılır
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"Activity": response.choices[0].message.content}) #yanıt döndürme
    except Exception as e:
        return jsonify({"error": str(e)}), 500 #hata yakalama

if __name__ == "__main__":
    app.run(debug=True, port=5000) #flask sunucusunu başlatır

