import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Website1",page_icon =":desktop_computer:",layout = "wide")

the_selected_menu = option_menu(
    menu_title= None,
    options=["Home","Education","Skills","Notes"],
    icons=["house","book","trophy","sticky"],
    orientation="horizontal",
        styles={
            "container": {"padding": "0!important","background-color":"#228CB9"},
            "icon":{"color":"#D6F002","font-size": "25px"},
            "nav-link": {"font-size": "25px","text-align":"center","margin":"5px",}
        }, 
)



        

def lottie_loadurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json() 

lottie_coding = lottie_loadurl("https://lottie.host/0ffaf8de-8f5e-406d-93ad-27a60744a513/SXc4XS7gGN.json")
#Image_random = Image.open("images\istockphoto-918259136-612x612.jpg")

if the_selected_menu == "Home":
    st.container()
    st.title("Welcome to my first website!!!")
    st.subheader("Welcome!:smile:")
    st.write("You can put anything in here :fish::fish::fish:")
    st.write(":desktop_computer: now")
   
elif the_selected_menu == "Education":
    st.container()
    st.title("List of Education Background")
    st.subheader("What I Learned!")
    st.write("---")
    st.write("Bachelor in Computer Science(Software Enginerring)")
    st.write("Master in Gender Study :>")
elif the_selected_menu == "Skills":
    st.title("List of Skills")
    st.subheader("What I Master it ")  
    st.write("i can run 100km/h in 2 minutes")
    st.write("I Didn't cry when i lose all of my codes :)")
    st.write(":fish::fish::fish:")


elif the_selected_menu == "Notes":
    st.container()
    left_collum,right_collum,middle_collum = st.columns(3)
    with left_collum:
        st.title("Notes")
        st.write("[YouTube >](https://www.youtube.com/#!)")
        st.write("Eat the earth stuff")
    with right_collum:
        st.title("Stuff")
        st.write("Youtube Stuff")
        st_lottie(lottie_coding,height=200, width=300, speed=0.5, loop=True)
    with middle_collum:
        st.title("Time")
        st.write("Whenever when you feel you have time")

with st.container():
    st.write("---")
    st.write("Developed by Rafiq!:brain:")
    st.write("all right reserved ehehe")
