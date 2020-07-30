from collections import Counter

from bs4 import BeautifulSoup
import requests
import re


COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    r = requests.get(url)
    r_data = r.content
    soup = BeautifulSoup(r_data, "html.parser")
    target = soup.find("div", attrs=TARGET_DIV)
    target = str(target)
    domains = re.findall(r'height:24px;"/></td><td>(.*..*)</td><td>', target)
    return domains




def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    email_counter = Counter()

    filtered_emails = [email.split("@")[1] for email in emails if email.split("@")[1] not in common_domains]
    for domain in filtered_emails:
        email_counter[domain] += 1
    return email_counter.most_common()