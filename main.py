import streamlit as st
import streamlit_authenticator as stauth

COOKIE_EXPIRY_DAYS = 30

def main():
    authenticator = stauth.Authenticate(
        {'usernames': {'teste': {'name': 'testando', 'password': 'blablabla'}}},
        'random_cookie_name',
        'random_signature_key',

         COOKIE_EXPIRY_DAYS,
    )

if __name__ == '__main__':
    main()