import streamlit as st
import streamlit_authenticator as stauth
from streamlit.components.v1 import html
from dependencies import consulta_nome, consulta_geral, add_registro, cria_tabela
from time import sleep

st.set_page_config(layout="wide", page_title='Engenharia', page_icon="style\\image.png")

COOKIE_EXPIRY_DAYS = 30

def main():

    try:
        consulta_geral()
    except:
        cria_tabela()
    db_query = consulta_geral()
    registro = {'usernames': {}}
    for data in db_query:
        registro['usernames'][data[1]] = {'name': data[0], 'password': data[2]}


    authenticator = stauth.Authenticate(
        registro,
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
        authenticator.logout('Logout', 'main')
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
        sleep(3)

    elif consulta_nome(st.session_state.user):
            st.warning('Nome de usuario já ecxistem. ')
            sleep(3)
    else:
        add_registro(st.session_state.nome, st.session_state.user, hashed_password[0])
        st.success('Registro Efetuado com Sucesso')
        sleep(3)

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