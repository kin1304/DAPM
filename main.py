import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

student_label = ["id", "Toán", "Văn", "Anh", "Lí", "Hóa", "Sinh", "Sử", "Địa", "GDCD","KHTN"]

student_37 = pd.read_csv('dataset/students_37.csv', header=None)
student_37.columns = student_label

student_37['Toán'].plot.hist(bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
img = Image.open('histogram.png')
st.image(img, caption="Ảnh trực quan điểm toán")




