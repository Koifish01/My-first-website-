import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

optionsez= ["Option 1","Option 2","Option 3"]

st.set_page_config(page_title="Website1",page_icon =":musical_note:",layout = "wide")

with st.sidebar :
    the_selected_main_bar = option_menu(
    menu_title= None,
    options=["Home","Contents","Local Heritage","References"],
    icons=["house-fill","book-fill","book-fill","sticky"],
    orientation="hehe",
    
        styles={
            "container": {"padding": "0!important","background-color":"#228CB9"},
            "icon":{"color":"#D6F002","font-size": "24px"},
            "nav-link": {"font-size": "21px","text-align":"center","margin":"5px",}
        }, 
)

def lottie_loadurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json() 
####################################  IMAGE SECTION !!!!
lottie_coding = lottie_loadurl("https://lottie.host/0ffaf8de-8f5e-406d-93ad-27a60744a513/SXc4XS7gGN.json")
#Image_random = Image.open("images\istockphoto-918259136-612x612.jpg")
#Image_petra = Image.open("Petra101.jpg")
Image_cat = Image.open("cat101.jpg")
Image_huh = Image.open("gasp101.jpg")
Image_quotes1 = Image.open("platoque101.jpg")
Image_UN1 = Image.open ("Unzzzs.jpg")
Image_UN = Image.open("thisUN.jpg")
Image_Rom = Image.open("roman101.jpg")
Image_Pyrami = Image.open("pyrami101.jpg")
Image_Wall = Image.open("thewall101.jpg")
Image_Strait = Image.open("malaccstra.jpg")
Image_Travel1 = Image.open("mantravel.jpg")
Image_Malacca = Image.open("melacca.jpg")
Image_George = Image.open("Gt101.jpg")
Image_Cat1 = Image.open("cat2101.jpg")
Image_quote2 = Image.open("platoque102.jpg")
Image_Taj = Image.open("Tajteuer.jpg")
Image_machu101 = Image.open("machu.jpg")
###############################
if the_selected_main_bar == "Home":  
    selected_sub = option_menu(
            menu_title=None,
            options=["Home", "Why Learn", "Our Wish", "About"],
            icons=["house-fill", "book-fill", "collection-play-fill", "sticky-fill"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#002F6C"},
                "icon": {"color": "#FFFFFF", "font-size": "24px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin": "5px",}
            },
        )
else:
        selected_sub = None 
if selected_sub == "Why Learn":
    right_coll0, left_coll0 = st.columns(2)
    the_selected_main_bar = False
    with right_coll0:
        st.title("One Never Get Bored When One Is Never Stop Learning")
        st.image(Image_quotes1, width=230,)
        st.subheader("Learning Is Everywhere Can It Doesn't Matter Your Age At All!!")
    with left_coll0:
        st.title("Learning Doesn't care about Your Age")
        st.image(Image_quote2, width=200)
elif selected_sub == "Our Wish":
    the_selected_main_bar = False
    st.subheader("Please Note That Knowledge Can Be Obtain Anywhere and Knowledge Didn't Even Choose An Age At All!!")
elif selected_sub == "About":
    the_selected_main_bar = False 
    st.title("About This Website")
    st.subheader("This is Part of My Project at UMTeenz lead by my Amazing Teacher!")
    st.subheader("It is Part of Promoting People To Be More Curious and Broadly Thinking And Beyond")
    st.write("Bye")
if the_selected_main_bar == "Home":
    st.title("Welcome!:sunglasses::sunglasses::sunglasses:")
    left_coll1, right_coll1 = st.columns(2)
    #with left_coll1:
     #   st.caption("Credit To")
      #  st.image(Image_UN1,width=110)
       # with right_coll1:
        #    st.caption("This one too!")
         #   st.image(Image_UN,width=160)
    left_coll, right_coll = st.columns(2)
    with left_coll:
        st.subheader("Wanna Get Knowledgable???")
        st.image(Image_Cat1,width=320)
        


elif the_selected_main_bar == "Contents":
    st.title("Wonders of The World")
    left_collum2,middle_collum2,right_collum2= st.columns(3)
    with left_collum2:
        st.subheader("Location 1")
        if st.checkbox(""):
            st.subheader("Petra, Jordan") #photo to put (3)
            st.image(Image_petra,width=150)
            st.write("The city of Petra, capital of the Nabataean Arabs, is one of the most famous archaeological sites in the world, it is Located 240 km south of the capital Amman and 120 km north of the red sea town of Aqaba")

        st.subheader("Location 4")
        if st.checkbox("                                 "):
            st.subheader("The Great Wall Of China")
            st.image(Image_Wall,width=160)
            st.write("The Great Wall of China was built over centuries by China’s emperors to protect their territory. Today, it stretches for thousands of miles along China’s historic northern border.")
    with middle_collum2:
        st.subheader("Location 2")
        if st.checkbox(" "):
            st.subheader("Roman Colosseum ") #photo to put (3)
            st.image(Image_Rom,width=150)
            st.write("Colosseum, giant amphitheater built in Rome under the Flavian emperors as with other amphitheatres, the emperor Vespasian intended the Colosseum to be an entertainment venue, hosting gladiator fights, animal hunts  "   " ")
        st.subheader("Location 5")
        if st.checkbox("    "):
            st.subheader("Taj Mahal")
            st.image(Image_Taj,width=160)
            st.write ("The Taj Mahal is located on the right bank of the Yamuna River in a vast Mughal garden that encompasses nearly 17 hectares. It was built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal ")

        
    with right_collum2:
        st.subheader ("Location 3")
        if st.checkbox("   "):
            st.subheader("Great Pyramid of Giza")
            st.image(Image_Pyrami,width=150)
            st.write("The Giza Pyramids, built to endure an eternity, have done just that. The monumental tombs are relics of Egypt's Old Kingdom era and were constructed some 4,500 years ago.")
        st.subheader("Location 6 ")
        if st.checkbox("                "):
            st.subheader("Machu Picchu")
            st.image(Image_machu101,width=155)
            st.write("Machu Picchu, site of ancient Inca ruins located about 80 km northwest of Cuzco, Peru, in the Cordillera de Vilcabamba of the Andes Mountains. Built without the use of mortar, metal tools, or the wheel, Machu Picchu is an engineering marvel")
            
  
elif  the_selected_main_bar == "Local Heritage":
    st.container()
    st.title("UNESCO certified World Heritage Sites in Malaysia")
    left_collum1,middle_collum1,right_collum1 = st.columns(3)
    with left_collum1:
        st.subheader("Location 1")
        if st.checkbox(" "):
            st.subheader("Melaka City")
            st.image(Image_Malacca,)
            st.write(" Melaka City is located in the state of Melaka, about 125 kilometres away from Kuala Lumpur. The city is often swamped by numerous tourists of different races and nationalities. For centuries, notable historical sites like St. Paul’s Church, Christ Church, and Stadthuys remain as the must-visit tourist spots in the city")

    with middle_collum1:
        st.subheader("Buckle up! We Go To These Places Now ")
        st.image(Image_Travel1,width=230)  
        st.title(":arrow_left:" " " "            "" " " " " "":arrow_right:")
    with right_collum1:
        st.subheader("Location 2")
        if st.checkbox("  "):
            st.subheader("George Town")
            st.image(Image_George)
            st.write("The town was founded as Fort Cornwallis in 1786 by Captain Francis Light of the British East India Company and flourished as a port of call for shipping on the India-China run. It became for a time the capital and commercial centre of the Straits Settlements. A restored Fort Cornwallis, St. George’s Church")


elif  the_selected_main_bar == "References":
    st.container()
    left_collum,middle_collum = st.columns(2)
    with left_collum:
        st.title("Further Reading")
        st.write("Youtube Stuff")
        st.write("[YouTube >](https://www.youtube.com/#!)")
        tab1,tab2 = st.tabs(["Link1","Link2"])
        # Tab 1 Hehe
        tab1.write("https://education.nationalgeographic.org/resource/great-wall-china/")# Link TO Those
        tab1.write("https://www.tandfonline.com/doi/full/10.1080/10382046.2021.2001983#abstract")
        tab1.write("https://www.britannica.com/topic/Taj-Mahal")
        tab1.write("https://whc.unesco.org/en/list/252/")
        # TAB 2 hehe
        tab2.write("https://www.britannica.com/place/George-Town-Malaysia")
        tab2.write("https://www.malaysia.travel/explore/the-historical-city-of-melaka")
        tab2.write("https://www.nationalgeographic.com/travel/article/secrets")
        tab2.write("https://www.britannica.com/topic/Taj-Mahal")
        tab2.write("https://whc.unesco.org/en/list/252/")
    with middle_collum:
        st.write("Hope You Learn Something While Visiting This Website")
        st_lottie(lottie_coding,height=200, width=300, speed=0.1, loop=True)

        if st.checkbox("Show More Stuff"):
            st.subheader("More Stuff")
            st.write("YouTube Stuff")
        
        


    




######################
with st.container():
    st.write("---")
    st.caption("Developed by Rafiq!:brain: all right reserved ehehe ")
    # Insert containers separated into tabs:

the_button = st.button("CLICK TO EXPLODE!")
if the_button:
    st.write("What do you think when you see this button????")
    st.image(Image_huh)
    st.write("You're fine!")
    st.balloons()
    st.button("Go Back") == the_button
    the_button is False
    


    


