from selenium import webdriver

url = 'https://www.agoda.com/ko-kr/search?guid=4b4792af-80c7-4e27-93b6-eddd06ad39e7&asq=2na0Ptfz2JsG5nEElCDFjpufa9Vwpz6XltTHq4n%2B9gPa2cVuPBDNBS66qiAcw9QAkTyUuoGUX9sTJrA5op2abUN46vRtCacOUjrA5TdR6hRh4GzPh7vt556DWCUPlxsGr6QDs48C6hOjLzuYUvlEgOm%2B3QacrQMDUE7JkJAfzu1drXjgTr9Q2g2j2W02PNVC6dTyDhQZpv4KZQO7BroNPQ%3D%3D&city=16901&tick=638043522884&locale=ko-kr&ckuid=8f8c05aa-416f-41f8-9665-a027b9719aeb&prid=0&currency=KRW&correlationId=642865fd-f0d2-4f88-995a-ad1d8a0fa0a3&pageTypeId=1&realLanguageId=9&languageId=9&origin=KR&cid=1439847&tag=6a04b0e6-774d-4722-a28c-c148c5cdc0c6&userId=8f8c05aa-416f-41f8-9665-a027b9719aeb&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=26&currencyCode=KRW&htmlLanguage=ko-kr&cultureInfoName=ko-kr&machineName=hk-pc-2g-acm-web-user-649c4cffb5-gh5xs&trafficGroupId=5&sessionId=ksjzrg4nta4g2aavf124pzgw&trafficSubGroupId=128&aid=103944&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&utm_medium=banner&utm_source=naver&utm_campaign=naverbz&utm_content=nbz2&utm_term=nbz2&browserFamily=Whale&checkIn=2022-11-27&checkOut=2023-01-31&rooms=1&adults=2&children=0&priceCur=KRW&los=65&textToSearch=%EC%A0%9C%EC%A3%BC&travellerType=1&familyMode=off'

driver = webdriver.Chrome("C:\git\chromedriver.exe") # webdriver 실행(크롬 창 생성)
driver.get(url) # url로 접속

name = driver.find_element_by_css_selector("h2.hp__hotel-name").text
price_b = driver.find_elements_by_css_selector("div.bui-price-display__value")


price = []
for i in range(len(price_b)):
    price.append(price_b[i].text)
    
print(name)
print(price)