import streamlit as sl
from sourcefld.sceens.home import home_screenload
from sourcefld.sceens.teacher import teacher_in
from sourcefld.sceens.student import student_in
def main():
    if 'login_type' not in sl.session_state:
        sl.session_state['login_type'] = None

    match sl.session_state['login_type']:
        case 'teacher':
            teacher_in()
        case 'student':
            student_in()
        case None:
            home_screenload()            

main()
