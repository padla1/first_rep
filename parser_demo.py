import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random

header ={'user-agent':user}

link = 'https://browser-info.ru/'
responce=requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')

#Check js
check_js = block.find('div', id='javascript_check')
#print(check_js)
result_js = check_js.find_all('span')[1].text
print(f'Java script:{result_js}')

#Check language
#check_language = block.find_all_next('div', id='browser_lang')
#print(check_language)
#result_language = check_language.find_all('span')[0].text
#print(result_language)

#Check flash
check_flash = block.find('div', id ='flash_version')

status_flash = check_flash.find_all( 'span')[1].text
result_flash = f'flash:{status_flash}'
print(result_flash)



#Check user agent

check_user_agent = block.find('div',id='user_agent').text

result_user_agent = (f'status user agent:{check_user_agent}')
print(result_user_agent)