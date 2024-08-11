import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

optionsez= ["Option 1","Option 2","Option 3"]

st.set_page_config(page_title="Website1",page_icon =":musical_note:",layout = "wide")

with st.sidebar :
    the_selected_menu = option_menu(
    menu_title= None,
    options=["Home","My Music","What Platform","Notes"],
    icons=["house-fill","file-music-fill","collection-play-fill","sticky"],
    orientation="hehe",
    
        styles={
            "container": {"padding": "0!important","background-color":"#228CB9"},
            "icon":{"color":"#D6F002","font-size": "35px"},
            "nav-link": {"font-size": "20px","text-align":"center","margin":"5px",}
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
    st.subheader(":musical_note: My Music Player List!!! :musical_note:")
    st.container()
    st.subheader("Welcome!:sunglasses::sunglasses::sunglasses:")
    st.subheader("This is part of my project!")
    st.write("This website contain my music list in 2018 and what platform i use :musical_note:")
    st.write(":desktop_computer: now")
elif the_selected_menu == "My Music":
    st.title("My Types of Genre:musical_note:")
    left_collum2,right_collum2= st.columns(2)
    with left_collum2:
        
        if st.checkbox("Poppy pop"):
            st.subheader("Artists I listen to!: ")
            st.write("Michael Jackson is a must??: ")
            st.write("idk Taylor Swift maybe: ")
            st.write("Steve Lacy is random name lol: ")
            st.write ("is scary to put in here")
        
    with right_collum2:
        if st.checkbox("Jazzy Jazz"):
            st.subheader("Artists I listen to!")
            st.write("Frank Sinatraa cuz cant argue about it: ")
            st.write("Chet Baker some dude : ")
            st.write("Dinah Washington idk is the best maybe???: ")
            st.write("Tatiana Eva-Marie i dont wanna talk about it: ")

elif the_selected_menu == "What Platform":
    st.container()
    left_collum1,middle_collum1,right_collum1 = st.columns(3)
    with left_collum1:
        if st.checkbox("My Soft Skills :>"):
            st.subheader("List of My Soft Skills")
            st.write("i can walk for 10 minutes without sweating :)")
            st.write("i can have the thinking ")
    with middle_collum1:
        st.subheader("What Platform I Use In Order To listen to Those People")  
        st.title(":arrow_left:""           "" " " " " "":arrow_right:")
    with right_collum1:
        if st.checkbox("My Hard Skills List"):
            st.subheader("List of my hard skills")
            st.write("I can run")
            st.write("That's it")


elif the_selected_menu == "Notes":
    st.container()
    left_collum,middle_collum,right_collum = st.columns(3)
    with left_collum:
        st.title("Notes")
        st.write("Eat the earth stuff")
    with middle_collum:
        st.title("Stuff")
        st.write("Youtube Stuff")
        st.write("[YouTube >](https://www.youtube.com/#!)")
        if st.checkbox("Show More Stuff"):
            st.subheader("More Stuff")
            st.write("YouTube Stuff")
        st_lottie(lottie_coding,height=200, width=300, speed=0.1, loop=True)
    with right_collum:
        st.title("Time")
        st.write("Whenever when you feel you have time")
        
        


    




######################
with st.container():
    st.write("---")
    st.caption("Developed by Rafiq!:brain: all right reserved ehehe ")
    


if st.button("CLICK TO EXPLODE!"):
    st.write("You're fine!")
    



