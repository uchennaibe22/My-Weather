from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    message = None

    print("✅ Flask route hit!")  

    if request.method == "POST":
        city = request.form.get("city")
        print("📍 City entered:", city)  

        api_key = "dac0bfa034b6ca0be5f9e1f6ad92c5e2"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        print("🌐 Requesting:", url)

        try:
            response = requests.get(url)
            print("🔢 Status Code:", response.status_code)
            data = response.json()
            print("🧾 Data received:", data)

            if response.status_code == 200 and "main" in data:
                weather = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "desc": data["weather"][0]["description"].title()
                }
                print("✅ Parsed weather:", weather)
            else:
                message = "City not found or invalid response."
                print("⚠️ Error:", message)
        except Exception as e:
            message = f"Error: {e}"
            print("🚨 Exception:", message)

    return render_template("index.html", weather=weather, message=message)


if __name__ == "__main__":
    app.run(debug=True)


