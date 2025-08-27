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
            st.rerun()

def confirm_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning("Senhas não confere")

    elif 'consulta_nome()':
            st.warning('Nome de usuario já ecxistem. ')
    else:
        'add_registro()'
        st.success('Registro Efetuado com Sucesso')

def register_user_form():
    with st.form(key='formulario', clear_on_submit=True):
        nome = st.text_input('Nome', key='nome')
        username = st.text_input('Usuário', key='user')
        password = st.text_input('Senha', key='pswrd', type='password')
        confirm_password = st.text_input('Confirme a Senha', key='confirm_paswrd', type='confirm_pswrd')
        submit = st.form_submit_button(
            'Registrar', on_click=confirm_msg,

        )

        clicou_fazer_login = st.button('Fazer Login')
        if clicou_fazer_login:
            st.session_state['user_register'] = False
            st.rerun()


if __name__ == '__main__':
    main()