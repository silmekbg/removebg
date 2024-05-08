# Un script python pour streamlit qui utilise rembg 

import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO


st.set_page_config(page_title="RemoveBG", layout="wide")
st.write("# Remove BG")
st.write("Uploadez une image pour retirer le fond et le rendre transparent")

# Sidebar
st.sidebar.write("## Uploader")
st.sidebar.link_button("Go to gallery", "https://unsplash.com/fr/s/photos/animals?license=free")
image_upload = st.sidebar.file_uploader("Choissisez une image", type=['png', 'jpg', 'jpeg'])




col1, col2 = st.columns(2)


def convert_image(image):
    buf = BytesIO()
    image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

def fix_image(image):
    image = Image.open(image)   
    col1.write("Image original")
    col1.image(image)
    fixed = remove(image)
    col2.write("Image détourée")
    col2.image(fixed)

    st.sidebar.download_button("Télécharger l'image", convert_image(fixed), 'removebg.png', 'image/png')


# Upload une image par défaut
if image_upload is not None:
    fix_image(image_upload)
else:
    fix_image("./kuş.jpg")


