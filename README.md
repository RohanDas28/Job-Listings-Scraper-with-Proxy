# 🕵️‍♂️ Proxy Scraper Project — Job Listings Scraper with NodeMaven Proxy

## 📌 Overview
This Python project scrapes **job listings** from **Indeed.com** using a **NodeMaven proxy** for anonymity and IP rotation. It rotates **User-Agent headers** to mimic real user behavior and avoid detection.

---

## 🚀 Features
- 🌐 Scrapes real job data: **Job Title, Company, Location**
- 🔐 Uses **authenticated NodeMaven proxy**
- 🎭 Random **User-Agent spoofing**
- 🧠 Handles request failures with retries
- 📊 Exports data to **CSV file**
- 💤 Mimics human behavior with **random delays**

---

## 📦 Requirements
Install dependencies via `pip`:
```bash
pip install requests beautifulsoup4 fake-useragent
```

---

## ⚙️ Configuration
In the script, replace your **NodeMaven credentials** and proxy details:
```python
NODEMAVEN_PROXY = "proxy.nodemaven.net:8000"  # Replace with your proxy
USERNAME = "your_nodemaven_username"          # Replace with your username
PASSWORD = "your_nodemaven_password"          # Replace with your password
```

---

## 🏃‍♂️ Usage
Run the script:
```bash
python proxy_scraper.py
```

After execution, you'll find the scraped data in:
```
job_listings.csv
```

---

## 💸 NodeMaven Discounts & Bonuses

### 🔗 Your Referral Link:
[https://go.nodemaven.com/rohan](https://go.nodemaven.com/rohan)

### 💰 Available Coupons:
- **DAS50** – Get **50% OFF** any plan.  
  ⏳ Valid until **April 30th**, **limited to first 20 users** only!
  
- **DS80** – Get **+80% more data** with any plan purchase.  
  Buy 5GB, receive **9GB** at the same price.  
  🗓️ Valid until **September 2025**


---

## 🛡️ Disclaimer
This tool is for **educational purposes only**. Please ensure compliance with the **Terms of Service** of any website you scrape. Use proxies and scraping responsibly.

---


## 📬 Contact
Created by **Rohan Das**  
Feel free to reach out for help or collaboration ideas!
