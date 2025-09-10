from flask import Flask, render_template, request, send_file
from scraper import scrape_website
from report_generator import generate_report
from email_sender import send_email
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_data():
    keyword = request.form.get("keyword") or "General"
    url = request.form.get("url")

    if not url:
        return "❌ Please provide a URL"

    # Scrape website
    data = scrape_website(url, keyword)

    if not data:
        data = ["No results found."]

    # Generate PDF
    pdf_file = generate_report(data, keyword)

    return render_template('result.html', data=data, pdf_file=pdf_file)

@app.route('/download/<filename>')
def download_report(filename):
    filepath = os.path.join("reports", filename)
    return send_file(filepath, as_attachment=True)

@app.route('/email/<filename>', methods=['POST'])
def email_report(filename):
    recipient = request.form.get("email")
    filepath = os.path.join("reports", filename)
    send_email(recipient, filepath)
    return f"📧 Report emailed to {recipient}"

if __name__ == "__main__":
    app.run(debug=True)
