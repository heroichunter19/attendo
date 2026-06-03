import streamlit as sl
from sourcefld.compofile.header import home_header
from sourcefld.uifolder.style_layout import style_layout , style_layout_main , style_layout_other

def  home_screenload():

    
    


    home_header() 
    style_layout_main()
    

    style_layout()


    col1, col2 = sl.columns(2)

    with col1:

        if sl.button('Teacher'):
            sl.session_state['login_type'] = 'teacher'
            sl.rerun()

    with col2:
        if sl.button('Student'):
            sl.session_state['login_type'] = 'student'    
            sl.rerun()