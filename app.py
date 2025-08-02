from flask import Flask

app = Flask(__name__)  # ये आपका ऐप ऑब्जेक्ट है

@app.route("/")
def home():
    return "Hello, World!"

# इस लाइन की ज़रूरत लोकल रन के लिए होती है, डिप्लॉय के लिए नहीं
if __name__ == "__main__":
    app.run(debug=True)
