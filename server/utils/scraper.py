from selenium import webdriver
from selenium.webdriver.chrome.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time
import os


def get_filename(title):
    return "".join("_" if c in (" ") else c for c in title).strip().lower()


visited_urls = set()
visited_urls.add("")
visited_urls.add("https://helpcenter.affirm.ca/s/topic/0TO7V00000134SJWAY/about-affirm")
visited_urls.add(
    "https://helpcenter.affirm.ca/s/topic/0TO7V00000134SKWAY/account-&-payments"
)
visited_urls.add(
    "https://helpcenter.affirm.ca/s/topic/0TO7V00000134SMWAY/disputes-&-refunds"
)
visited_urls.add(
    "https://helpcenter.affirm.ca/s/topic/0TO7V00000134SOWAY/security-&-privacy"
)
visited_urls.add("https://helpcenter.affirm.ca/s/topic/0TO7V00000134SLWAY/affirm-loans")
visited_urls.add(
    "https://helpcenter.affirm.ca/s/topic/0TO7V00000134SNWAY/paybright-loans"
)
visited_urls.add(
    "https://helpcenter.affirm.ca/s/topic/0TO7V000001D7NWWA0/shop-pay-installments"
)

driver = webdriver.Firefox()

output_dir = "affirm_support_articles"
os.makedirs(output_dir, exist_ok=True)

try:
    while True:
        time.sleep(2)

        current_url = driver.current_url
        if current_url in visited_urls:
            continue

        title = driver.title
        file_name = get_filename(title)

        try:
            content_div = driver.find_element(
                By.CSS_SELECTOR,
                "div.slds-rich-text-editor__output.selfServiceOutputRichTextWithSmartLinks",
            )
            body = content_div.text
            visited_urls.add(current_url)
        except:
            continue

        file_path = os.path.join(output_dir, f"{file_name}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n")
            f.write(body)

        print(f"✅ Saved: {file_name}.txt")

except KeyboardInterrupt:
    print("Script stopped.")
    driver.quit()
