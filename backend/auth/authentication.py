from flask import Request
import urllib.request
import jwt

auth_key = urllib.request.urlopen("https://firm-moose-85.clerk.accounts.dev/.well-known/jwks.json").read()

def authenticate(req:Request):
    print(auth_key)
    authorization_header = req.headers.get('Authorization')
    print(authorization_header)
    if authorization_header == None or authorization_header == 'Bearer null':
        return False
    
    data = jwt.decode(authorization_header, auth_key)
    print(data)