import requests
import fake_useragent
from bs4 import BeautifulSoup


session = requests.Session()

user = fake_useragent.UserAgent().random


header = {
    'user-agent':user

}

url = 'https://www.codewars.com/users/sign_in'

data = {
    'user[email]': 'pasakuksin9@gmail.com',
    'user[password]': 'bandana123@'

}

respounce = session.post(url,data=data, headers=header).text


profile_info = 'https://www.codewars.com/users/Nintai-ryoku'



coockies_dict = [
    {'domain':key.domain, 'name':key.name,'path':key.path,'value':key.value}
    for key in session.cookies
]


session2=requests.Session()
for coockies in coockies_dict:
    session2.cookies.set(**coockies)

profile_responce = session2.get(profile_info, headers=header).text

print(profile_responce)