# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:22:54 2021

@author: takumi
"""
import streamlit as st
from PIL import Image
st.title('私の名前は小林拓未です')
st.write('これから作品を作っていきます')
text = st.text_input('あなたの名前を教えてください')
'あなたの名前は、', text,'です'


option=st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
'あなたが選択したのは',option,'です'

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
    
img=Image.open('14515546903010.jpg')
st.image(img,caption='生活場面',use_column_width=True)



