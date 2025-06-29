# 🧠 AI-Powered Contact Form (Flask + TextBlob)

A smart contact form backend built with Flask that uses AI-powered sentiment analysis to filter out spam or abusive messages before accepting them.

---

## 🚀 How to Run

## 1. Clone or download the project
bash terminal
cd ai_contact_form
## 2. Install dependencies
pip install -r requirements.txt
python -m textblob.download_corpora
## 3. Run the Flask app
python app.py
## 4. Open in your browser
Visit: http://127.0.0.1:5000

## 🧩 Features

🧠 Spam filtering using sentiment polarity (via TextBlob)
✅ Accepts only genuine, non-spam messages
📄 Clean UI using Bootstrap
🔄 AJAX-based form submission (no page reload)
🛠️ Ready for database/email integration

## 🛠️ Tech Stack
Backend: Python, Flask
AI Module: TextBlob Sentiment Analyzer
Frontend: HTML, Bootstrap 5, Vanilla JS (AJAX)
Tools: Postman (for API testing), cURL (optional)

## 💡 Future Additions (Optional)
CAPTCHA validation
Email notifications on valid submissions
Database integration (MongoDB / SQLite)
Admin panel to view submissions