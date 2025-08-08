from flask import Flask, render_template, request

app = Flask(__name__)

# Simple fraud detection function
def is_suspicious(text):
    suspicious_keywords = [
        'urgent', 'verify', 'click here', 'blocked', 
        'lottery', 'account update', 'kyc', 'otp', 'paytm', 'bank'
    ]
    found = [word for word in suspicious_keywords if word in text.lower()]
    
    if found:
        return f"⚠️ Suspicious:  {found}"
    else:
        return "✅ Looks Safe"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        message = request.form['message']
        result = is_suspicious(message)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
