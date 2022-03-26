import streamlit as st
from slugify import slugify
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image

st.title('The Source Church QR Code Generator App')

url = st.sidebar.text_input("URL", value="", placeholder="Paste URL Here")
source = slugify(st.sidebar.text_input("Source", value="", placeholder="Ex: Email Campaing"))
medium = slugify(st.sidebar.text_input("Medium", value="qr-code", placeholder="Default is QR-Code"))
name = slugify(st.sidebar.text_input("Name", value="", placeholder="Give this campaing a name"))

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
st.image(image)