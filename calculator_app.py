import streamlit as st
st.title("Calculator App using Streamlit")
x=st.number_input("enter number1")
y=st.number_input("enter number2") 
st.write("operation") 
op=st.radio("select",("add","sub","mul","div")) 
def  calculat():
    if(op=="add"):
        st.write(x+y)
    elif(op=="sub"):
        st.write(x-y)
    elif(op=="mul"):
        st.write(x*y)
    else:
        st.write(x/y)   
if(st.button("calculate")): 
    calculat()   

