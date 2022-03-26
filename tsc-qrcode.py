import streamlit as st
from slugify import slugify
import png
import pyqrcode
from pyqrcode import QRCode
from PIL import Image

st.title('The Source Church QR Code Generator App')

url = st.sidebar.text_input("URL", value="", placeholder="Paste URL Here")
source = slugify(st.sidebar.text_input("Source", value="", placeholder="Ex: Flyer, Door Hanger, Email Campaing"))
medium = slugify(st.sidebar.text_input("Medium", value="QR Code", placeholder="Where is this URL going to be used?"))
name = slugify(st.sidebar.text_input("Name", value="", placeholder="What is this Campaing Promoting?"))

track = st.sidebar.checkbox('Track this URL')
qr_size = st.sidebar.slider('QR Code Size', min_value = 6, max_value = 12, value = 6)

if track:
     full_url = url + "?utm_source=" + source + "&utm_medium=" + medium + "&utm_campaign=" + name
     st.text("Campaing URL:")
     st.write(full_url)
else:
    full_url = url
    st.text("Campaing URL:")
    st.write(full_url)


# Generate QR code
qr = pyqrcode.create(full_url)

qr.png('tsc_qr.png', scale = qr_size)

image = Image.open('tsc_qr.png')
 
st.text("QR Code:")
st.image(image,caption="Right Click and then Save Image As...")