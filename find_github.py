import argparse
import json
import sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def find_github_link(article_title):
    info_dict = {}
    info_dict['Acticle_title'] = article_title
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    
    driver.get("https://paperswithcode.com/")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(f"{article_title}")
    search_box.submit()
    current_url = driver.current_url
    driver.get(current_url)
    sub_tags = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]").find_elements(By.XPATH, "./*")
    if len(sub_tags) > 0:
        info_dict['status'] = "OK"
        code_url = sub_tags[0].find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/a[2]").get_attribute("href")
        driver.get(code_url)
        list_code_link = driver.find_element("id", "implementations-short-list").find_elements(By.XPATH, "./*")
        if len(list_code_link) > 0:
            lst_github = []
            top_code_link = list_code_link if len(list_code_link) < 5 else list_code_link[:5]
            for code_link in top_code_link:
                github_url = code_link.find_element(By.CLASS_NAME, "code-table-link").get_attribute("href")
                lst_github.append(github_url)
            info_dict['Github'] = lst_github
        else:
            info_dict['Github'] = "No code"
    else:
        info_dict['status'] = "Paper not found"
    driver.quit()
    return info_dict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Paper title", required=True)
    args = parser.parse_args()
    
    article_name = args.name
    github_link = find_github_link(article_name)

    if github_link['status'] == 'OK':
        print(f"Found paper: \n{json.dumps(github_link, indent = 4)}")
    else:
        print(f"{json.dumps(github_link, indent = 4)}")

if __name__ == "__main__":
    main()
