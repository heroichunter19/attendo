import streamlit as sl
from sourcefld.compofile.header import home_header
from sourcefld.uifolder.style_layout import style_layout , style_layout_main , style_layout_other

def  home_screenload():

    
    


    home_header() 
    style_layout_main()
    

    style_layout()


    col1, col2 = sl.columns(2, gap="large")

    with col1:
        sl.header("Student")
        sl.image("https://i.ibb.co.com/zT0dRnrC/pixabay-stunning-illustrations-removebg-preview.png",width=120)
        if sl.button('Student Login', type="primary"):
            sl.session_state['login_type'] = 'student'    
            sl.rerun()


    with col2:
        


        sl.header("Teacher")
        sl.image("https://i.ibb.co.com/zVkqYPjj/3d-Cute-Cartoon-Male-Teacher-Character-PNG-Images-PSD-Free-Download-Pikbest-removebg-preview.png",width=120)

        if sl.button('Teacher Login', type="primary"):
            sl.session_state['login_type'] = 'teacher'
            sl.rerun()
        