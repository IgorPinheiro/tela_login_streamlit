import streamlit as st
import streamlit_authenticator as stauth

COOKIE_EXPIRY_DAYS = 30

def main():
    authenticator = stauth.Authenticate(
        {'usernames': {'teste': {'name': 'testando', 'password': '12345'}}},
        'random_cookie_name',
        'random_signature_key',

         COOKIE_EXPIRY_DAYS,
    )


    if 'user_register' not in st.session_state:
        st.session_state['user_register'] = False
    
    if st.session_state['user_register'] == False:
        login_form(authenticator=authenticator)
    else:
        register_user_form()


st.title('Sejam bem Vindo ao DashBoad da Engenharia')
def login_form(authenticator):
    name, authentication_status, username = authenticator.login("login")
   
    if authentication_status:
        authenticator.logout('Logout', main)
        st.title('Bem Vindo')
        st.write(f'Bem vindo: *{name}!')


    if authentication_status == False:
        st.error('Usuário/senha incorreto')
        

    if authentication_status == None:
        st.warning('Sejam bem Vindo ao DashBoad da Engenharia')
        user_register = st.button('Registrar')

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
        confirm_password = st.text_input('Confirme a Senha', key='confirm_pswrd', type='password')
        submit = st.form_submit_button(
            'Registrar', on_click=confirm_msg,

        )

    clicou_fazer_login = st.button('Fazer Login')
    if clicou_fazer_login:
        st.session_state['user_register'] = False
        st.rerun()


if __name__ == '__main__':
    main()