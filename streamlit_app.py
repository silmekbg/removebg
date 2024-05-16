import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
from rembg import remove
from io import BytesIO

st.set_page_config(page_title="Éditeur d'images", layout="wide")
st.write("# Éditeur d'images")
st.write("Uploadez une image pour la retoucher, l'optimiser et la personnaliser")

# Sidebar
st.sidebar.write("## Uploader")
st.sidebar.link_button("Go to gallery", "https://unsplash.com/fr/s/photos/animals?license=free")
image_upload = st.sidebar.file_uploader("Choisissez une image", type=['png', 'jpg', 'jpeg'])

col1, col2 = st.columns(2)

def convert_image(image):
    buf = BytesIO()
    image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

def fix_image(image):
    image = Image.open(image)
    col1.write("Image originale")
    col1.image(image)
    fixed = remove(image)
    col2.write("Image détourée")
    col2.image(fixed)

    st.sidebar.download_button("Télécharger l'image", convert_image(fixed), 'removebg.png', 'image/png')

    # Édition et retouche d'images
    st.sidebar.write("## Édition d'images")
    brightness = st.sidebar.slider("Luminosité", 0.0, 2.0, 1.0)
    contrast = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
    sharpness = st.sidebar.slider("Netteté", 0.0, 2.0, 1.0)
    edited_image = ImageEnhance.Brightness(fixed).enhance(brightness)
    edited_image = ImageEnhance.Contrast(edited_image).enhance(contrast)
    edited_image = ImageEnhance.Sharpness(edited_image).enhance(sharpness)
    col2.write("Image retouchée")
    col2.image(edited_image)

    # Optimisation des images
    st.sidebar.write("## Optimisation d'images")
    quality = st.sidebar.slider("Qualité JPEG", 0, 100, 100)
    optimized_image = edited_image.convert('RGB')
    buf = BytesIO()
    optimized_image.save(buf, format='JPEG', quality=quality)
    byte_im = buf.getvalue()
    st.sidebar.download_button("Télécharger l'image optimisée", byte_im, 'optimized.jpg', 'image/jpeg')

    # Fonctionnalités pour l'e-commerce
    st.sidebar.write("## Personnalisation pour l'e-commerce")
    add_logo = st.sidebar.file_uploader("Ajouter un logo", type=['png', 'jpg', 'jpeg'])
    if add_logo is not None:
        logo = Image.open(add_logo)
        edited_image.paste(logo, (10, 10), mask=logo)
        col2.write("Image avec logo")
        col2.image(edited_image)

# Upload une image par défaut
if image_upload is not None:
    fix_image(image_upload)
else:
    fix_image("./kuş.jpg")
