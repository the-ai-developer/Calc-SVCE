import streamlit as st
from PIL import Image
st.set_page_config(page_title="SVCE Marks Calculator",page_icon=":tada:",layout="wide")
def DispMarks(FinMarks,Sub,Marks,Low):
    if FinMarks >= Low:
        return "&#128074;",f" You Are Safe!",f"Your {Sub} Internal Marks:",f"{FinMarks}/{Marks}"
    else:
        return "&#129310;",f" Better Luck Next Time!",f"Your {Sub} Internal Marks:",f"{FinMarks}/{Marks}"

def Calc_LAB():
    Sub = st.text_input(label="Enter Laboratory Name:")
    mark1 = int(st.number_input(label="Enter FAT 1 Lab Mark:"))
    mark2 = int(st.number_input(label="Enter FAT 2 Lab Mark:"))
    mark3 = int(st.number_input(label="Enter FAT 3 Lab Mark:"))
    Model = int(st.number_input(label="Enter Model Examination Mark:"))
    btn = st.button(label="Calculate Marks")
    FinMarks = round(((mark1+mark2+mark3)/3)*0.8+(Model*0.2), 2)
    if btn:
            Emoji, Res, Stat, Mrks = DispMarks(FinMarks,Sub,60,27)
            st.markdown("""
                      <div style="display: flex; justify-content: center; flex-direction:column; align-items: center; margin-left:10px;">
                          <p><h2>{} {}</h2> </p>
                          <h2 style="align-items:centre; margin-top:-10px; margin-left:10%;">{}</h2>
                          <div style="height:18%; width:42%; margin-top:-2px; border:5px solid  #5479A4; font-color:#5479A4; border-radius:5px; background: darkblue; justify-content: center; ">
                          <h1 style="margin-left:10px;">{}</h1>
                      </div>
                      </div>
                  """.format(Emoji, Res, Stat, Mrks), unsafe_allow_html=True)

def Calc_FAT():
    Sub = st.text_input(label="Enter Subject Name:")
    mark1 = int(st.number_input(label="Enter FAT 1 Mark:"))
    mark2 = int(st.number_input(label="Enter FAT 2 Mark:"))
    mark3 = int(st.number_input(label="Enter FAT 3 Mark:"))
    Assign1 = int(st.number_input(label="Enter Assignment 1 Mark:"))
    Assign2 = int(st.number_input(label="Enter Assignment 2 Mark:"))
    Assign3 = int(st.number_input(label="Enter Assignment 3 Mark:"))
    btn = st.button(label="Calculate Marks")
    FinMarks = round((((mark1 + mark2 + mark3) * 0.7 + (Assign1 + Assign2 + Assign3) * 0.3) / 3) * 0.8, 2)
    if btn:
            Emoji, Res, Stat, Mrks = DispMarks(FinMarks,Sub,40,23)
            st.markdown("""
                      <div style="display: flex; justify-content: center; flex-direction:column; align-items: center; margin-left:10px;">
                          <p><h2>{} {}</h2> </p>
                          <h2 style="align-items:centre; margin-top:-10px; margin-left:10%;">{}</h2>
                          <div style="height:18%; width:42%; margin-top:-2px; border:5px solid  #5479A4; font-color:#5479A4; border-radius:5px; background: darkblue; justify-content: center; ">
                          <h1 style="margin-left:10px;">{}</h1>
                      </div>
                      </div>
                  """.format(Emoji, Res, Stat, Mrks), unsafe_allow_html=True)

with st.container():
  left_col, Right_col = st.columns(2)
  with left_col:
        st.subheader("SVCE Internal Marks Calculation Portal :wave:")
        img=Image.open("Image/Logo.png")
        st.image(img)
        option = st.selectbox("Select What To Calculate", ["Select One!","FAT Internals", "LAB Internals"],index=0)
        if option=="FAT Internals" :
            Calc_FAT()
        if option=="LAB Internals":
            Calc_LAB()
        else:
            pass

#print(f"{mark1} {mark2} {mark3} {Assign1} {Assign2} {Assign3}")
