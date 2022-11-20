import streamlit as st
from streamlit_option_menu import option_menu


sb = st.sidebar



menu = option_menu(None, ["Jupe", "Robe"],orientation="horizontal",
                            menu_icon="cast", default_index=0)

if menu == "Jupe":
   type_jupe = sb.radio("Choisir le type de la jupe"
            ,('Demi cloche', 'Cloche', 'Double cloche'))
   tour_taille = sb.slider('Tour de taille', 60, 180, 80)

   if type_jupe == "Demi cloche" : 
      h_cloche = (tour_taille/3)-1
   elif type_jupe == "Cloche":
      h_cloche = ((tour_taille/3)-1)/2
   else :
      h_cloche = ((tour_taille/3)-1)/4
   
   
   sb.image("../pictures/jupe.webp", use_column_width=True)
   st.write("L'hauteur de la cloche doit être : ",round(h_cloche,2))
else :
   sb.image("../pictures/robe.webp")
   st.write("En cours ...")

