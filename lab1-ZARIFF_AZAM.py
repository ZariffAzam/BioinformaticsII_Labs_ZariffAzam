import streamlit as st

# you may put all your functions at HERE

st.title('Lab 1 - ZARIFF AZAM')

protein_id = st.text_input('Enter Uniprot ID')
retrieve = st.button('Retrieve')

if retrieve:
    if protein_id!="":
    	# your function calls and execution of processes at HERE
    else:
        st.warning('Please enter Uniprot ID')