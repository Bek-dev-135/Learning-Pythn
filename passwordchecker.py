import requests
import hashlib
import sys



#first build a function to  request data

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char

    res = requests.get(url)

    if res.status_code!=200:
        raise RuntimeError(f'error fetching: {res.status_code} check api atatus')

    return res
# second function check password if it exists in api response

def get_password_leak_count(hashes, hash_to_check):
    hashes= (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):

    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_char, tail= sha1password[:5],sha1password[5:]
    response= request_api_data(first_char)
    return get_password_leak_count(response, tail)


def main(args):
    for passwords in args:
        count=pwned_api_check(passwords)
        if count:
            print(f' this passworsd {passwords} was found {count} times. you should change your password')
        else:
            print(f'Your password {passwords} is safe')
    return 'done'
if __name__=="__main__":
    sys.exit(main(sys.argv[1:]))