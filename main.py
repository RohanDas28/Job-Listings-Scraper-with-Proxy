import requests
from bs4 import BeautifulSoup
import random
import time
import csv
from fake_useragent import UserAgent

# ======================
# CONFIGURATION
# ======================
TARGET_URL = "https://www.indeed.com/jobs?q=python+developer&l="  # Target website
OUTPUT_FILE = "job_listings.csv"
SCRAPE_COUNT = 20  # Number of job listings to scrape

# ======================
# NODEMAVEN PROXY CONFIG
# ======================
NODEMAVEN_PROXY = "proxy.nodemaven.net:8000"  # Replace with actual IP/Port
USERNAME = "your_nodemaven_username"  # Replace with your NodeMaven username
PASSWORD = "your_nodemaven_password"  # Replace with your NodeMaven password

proxy_with_auth = f"http://{USERNAME}:{PASSWORD}@{NODEMAVEN_PROXY}"
proxies = {
    "http": proxy_with_auth,
    "https": proxy_with_auth
}

# ======================
# STEP 1: Rotate User Agents
# ======================
def get_random_headers():
    ua = UserAgent()
    return {"User-Agent": ua.random}

# ======================
# STEP 2: Scrape Jobs with NodeMaven Proxy
# ======================
def scrape_jobs():
    print("[INFO] Starting scraping jobs with NodeMaven proxy...")
    job_data = []
    scraped = 0

    while scraped < SCRAPE_COUNT:
        headers = get_random_headers()

        try:
            print(f"[INFO] Requesting page using NodeMaven proxy...")
            response = requests.get(TARGET_URL, headers=headers, proxies=proxies, timeout=10)

            if response.status_code != 200:
                print(f"[WARN] Bad response: {response.status_code}")
                time.sleep(2)
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            job_cards = soup.select(".job_seen_beacon")

            for job in job_cards:
                if scraped >= SCRAPE_COUNT:
                    break

                title_tag = job.find("h2", class_="jobTitle")
                company_tag = job.find("span", class_="companyName")
                location_tag = job.find("div", class_="companyLocation")

                title = title_tag.text.strip() if title_tag else "N/A"
                company = company_tag.text.strip() if company_tag else "N/A"
                location = location_tag.text.strip() if location_tag else "N/A"

                print(f"[DATA] {title} | {company} | {location}")
                job_data.append({"Title": title, "Company": company, "Location": location})
                scraped += 1

            time.sleep(random.uniform(1, 3))  # Random delay to mimic human behavior

        except Exception as e:
            print(f"[ERROR] {e}. Retrying...")
            time.sleep(3)
            continue

    return job_data

# ======================
# STEP 3: Save to CSV
# ======================
def save_to_csv(data, filename):
    print(f"[INFO] Saving data to {filename}...")
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Location"])
        writer.writeheader()
        writer.writerows(data)
    print("[INFO] Data saved successfully.")

# ======================
# MAIN
# ======================
if __name__ == "__main__":
    job_listings = scrape_jobs()
    save_to_csv(job_listings, OUTPUT_FILE)
