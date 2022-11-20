import streamlit as st
from streamlit_option_menu import option_menu


sb = st.sidebar



menu = option_menu(None, ["Jupe", "Robe"],orientation="horizontal",
                            menu_icon="cast", default_index=0)

if menu == "Jupe":
   type_jupe = st.radio("Choisir le type de la jupe"
            ,('Demi cloche', 'Cloche', 'Double cloche'))
   tour_taille = st.slider('Tour de taille', 60, 180, 80)

   if type_jupe == "Demi cloche" : 
      h_cloche = (tour_taille/3)-1
   elif type_jupe == "Cloche":
      h_cloche = ((tour_taille/3)-1)/2
   else :
      h_cloche = ((tour_taille/3)-1)/4
   
   st.write("L'hauteur de la cloche doit être : ",round(h_cloche,2))
   st.image("https://www.cdiscount.com/pdt2/8/8/6/1/300x300/mp59284886/rw/jupe-courte-femmes-mini-plissee-style-coreen-pou.jpg", use_column_width=True)
else :
   st.image("https://www.maison123.ch/dw/image/v2/AAWW_PRD/on/demandware.static/-/Sites-UPAP-master/default/dw0ec481b3/653619782_6.jpg?sw=1000&sh=1180&strip=false")
   st.write("En cours ...")

