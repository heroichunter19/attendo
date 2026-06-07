import streamlit as sl
from sourcefld.uifolder.style_layout import style_layout_other ,style_layout
from sourcefld.compofile.header import header_dashboard
def teacher_in():
    
    style_layout_other()
    style_layout()
    

    if 'teacher_login_type' not in sl.session_state or sl.session_state.teacher_login_type=="login":
        teacher_login()
    elif sl.session_state.teacher_login_type=="register":
        teacher_register()


def teacher_login():
    
    cA,cB=sl.columns(2,vertical_alignment='center', gap='large')
    with cA:
        header_dashboard()
    with cB:
        if sl.button("Home", type='secondary', key='loginbackbtn'):
            sl.session_state['login_type'] = None
            sl.rerun()
            
    
    
    sl.header('Login using password', text_alignment='center')
    sl.space()
    sl.space()

    teacher_username = sl.text_input("Enter Username", placeholder='enter your username')
   
    teacher_password = sl.text_input("Enter Password", type='password', placeholder='enter password')
   
    
    sl.divider()

    btnc1, btnc2 = sl.columns(2)
    with btnc1:
        sl.button('Login', icon=':material/passkey:', width='stretch')
    with btnc2:
        if sl.button('Register',type='primary', icon=':material/passkey:', width='stretch'):
            sl.session_state.teacher_login_type='register'
        
    


    




def teacher_register():
    
    cA,cB=sl.columns(2,vertical_alignment='center', gap='large')
    with cA:
        header_dashboard()
    with cB:
        if sl.button("Home", type='secondary', key='loginbackbtn'):
            sl.session_state['login_type'] = None
            sl.rerun()

            
    sl.header('Register your teacher profile')
    sl.space()
    sl.space()

    teacher_username = sl.text_input("Enter Username", placeholder='enter your username')
    teacher_name =sl.text_input("Enter Name",placeholder="Adam John")
    teacher_password = sl.text_input("Enter Password", type='password', placeholder='enter password')
    password_confirm = sl.text_input("Confirm Your Password", type='password',placeholder='confirm your password')
    
    sl.divider()

    btnc1, btnc2 = sl.columns(2)
    with btnc1:
        sl.button('Register Now', icon=':material/passkey:', width='stretch')
    with btnc2:
        if sl.button('Login',type='primary', icon=':material/passkey:', width='stretch'):
            sl.session_state.teacher_login_type = 'login'
        
   