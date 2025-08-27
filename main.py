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


    if 'user_register' not in st.session_state:
        st.session_state['user_register'] = False
    
    if st.session_state['user_register'] = False:
        login_form(authenticator=authenticator)



def login_form(authenticator):
    name, authentication_status, username = authenticator.login('Login')
    if authentication_status:
        authenticator.logout('Logout', main)
        st.write(f'Bem Vindo {name.title()}')


    if authentication_status == False:
        st.error('Usuário/senha incorreto')

    if authentication_status == None:
        st.success('Sejam bem Vindo ao Dash Boad da Engenharia')
        user_register = st._bottom('Registrar')

        if user_register:
            st.session_state['user_register'] = True
            st.rerun



if __name__ == '__main__':
    main()