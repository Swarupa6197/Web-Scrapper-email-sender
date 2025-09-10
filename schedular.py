import schedule
import time
import scraper
import report_generator
import email_sender

URL = "https://news.ycombinator.com/"
KEYWORD = "AI"
EMAIL = "receiver@example.com"

def job():
    data = scraper.scrape_website(URL, KEYWORD)
    pdf = report_generator.generate_report(data, KEYWORD)
    email_sender.send_email(EMAIL, f"reports/{pdf}")
    print("Report generated & emailed!")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
