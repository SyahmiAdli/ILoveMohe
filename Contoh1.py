import streamlit as st
import pandas as pd
##########################################################################################
#PC Components List
#memory_size=(1, 2, 4, 6, 8, 10, 11, 12, 16, 24)

nvidia=pd.read_csv("Nvidia Graphics Cards.csv")
nvidia=nvidia.sort_values('Released Year')

st.write("""
         # NVIDIA GRAPHICS CARD FINDER
         """)
st.text('Database Source: https://www.techpowerup.com/gpu-specs/')
##########################################################################################    

memory = st.sidebar.slider('Select Lowest Memory Size (in Gb):', 1,24,1)
    
gpu=st.sidebar.slider('Select lowest GPU Clock (in MHz):', 675,2321,675)
    
    
memory_c=st.sidebar.slider('Select Lowest Memory Clock (in MHz)', 900,2248, 900)
    
    
shaders=st.sidebar.slider('Select Lowest Shaders:', 192,10496,192)

#########################################################################################

nvidia = nvidia[nvidia['Memory (Gb)'] >= memory] 

nvidia = nvidia[nvidia['GPU clock (MHz)'] >= gpu] 

nvidia = nvidia[nvidia['Memory clock (MHz)'] >= memory_c] 

nvidia = nvidia[nvidia['Shaders'] >= shaders] 


########################################################################################
if len(nvidia.index)==0:
    st.subheader('No Graphics Cards Found')
else:
    st.table(nvidia)






