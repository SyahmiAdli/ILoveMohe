import streamlit as st
import pandas as pd
import numpy as np



df=pd.read_csv("StudentsPerformance.csv")


st.write("""
         # STUDENTS PERFORMANCE AND SCORE IN THE EXAMINATION
         """)
st.text('Database Source: https://www.kaggle.com/spscientist/students-performance-in-exams')

st.write("")
st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html).')

show = st.checkbox('Click here to see the references')
st.write("")
st.write("")
if show:
### --- Sidebar layout
    st.write(
       """Credits to:  
          - Ts. Dr. Yong Poh Yu  (Trainer)
          - Dr. Tan Yan Bin      (Trainer)
          - Shreyas Gangopadhyay (Reference)"""
    )
###########################################################################################################
dataset = st.sidebar.selectbox("Search for Comparison Factor",
                               ("Select to Choose",
                                "Average Score",
                                "Gender",
                                "Race/Ethnics",
                                 "Meals Type",
                                 "Preparation Courses",
                                        "Parents Educational Background")
                               )

dataset1 = st.sidebar.selectbox("Choose To See The Observations",
                               ("Select to Choose",
                                "Min and Max Score",
                                "Top Performance",
                                "Lower Performance")
                                )
##########################################################################################################
if dataset== 'Gender':
    A=pd.DataFrame(df['gender'].value_counts().reset_index())
    A.columns=['Gender', 'Count']
    A
    st.text('Mean:')
    A1= df.groupby(['gender']).mean()
    A1
    st.text('Median:')
    A2= df.groupby(['gender']).median()
    A2
    st.text('In general, female students perform better than the male students')
############################################################################################################
elif dataset== 'Race/Ethnics':
    B=pd.DataFrame(df['race/ethnicity'].value_counts().reset_index())
    B.columns=["Race/Ethnicity", "Count"]
    B
    st.text('Mean:')
    B1= df.groupby(['race/ethnicity']).mean()
    B1
    st.text('Median:')
    B2= df.groupby(['race/ethnicity']).median()
    B2
    st.text('Students from group E performed better than students in other groups')

############################################################################################################
elif dataset== 'Meals Type':
    C=pd.DataFrame(df['lunch'].value_counts().reset_index())
    C.columns=["Meals Type", "Count"]
    C
    st.text('Mean:')
    C1= df.groupby(['lunch']).mean()
    C1
    st.text('Median:')
    C2= df.groupby(['lunch']).median()
    C2
    st.text('Students with standard lunch performed better than those who got free/reduced lunch')
#############################################################################################################
elif dataset== 'Preparation Courses':
    D=pd.DataFrame(df['test preparation course'].value_counts().reset_index())
    D.columns=["Preparation Courses", "Count"]
    D
    st.text('Mean:')
    D1= df.groupby(['test preparation course']).mean()
    D1
    st.text('Median:')
    D2= df.groupby(['test preparation course']).median()
    D2
    st.text('Those whom completing the preparation courses more likely to perform better than those whom without preparation courses')
#############################################################################################################
elif dataset== 'Parents Educational Background':
    E=pd.DataFrame(df['parental level of education'].value_counts().reset_index())
    E.columns=["Parents Educational Background", "Count"]
    E
    st.text('Mean:')
    E1= df.groupby(['parental level of education']).mean()
    E1
    st.text('Median:')
    E2= df.groupby(['parental level of education']).median()
    E2
    st.text('Student whom parents that have masters degree scored better compared to others')
#############################################################################################################
elif dataset== 'Average Score':
    df
    df['Average score'] = (df['math score']+df['reading score']+df['writing score'])/3
    df['Average score']
    df.head()
###############################################################################################################
else:
    st.title("THANK YOU FOR VISITING!")
    #st.subheader("Your recommendation is highly appreciated.")
###############################################################################################################
if dataset1== 'Min and Max Score':
    st.text('Maximum score for Math is')
    F1= df['math score'].max()
    F1
    st.text('Maximum score for Reading is')
    F2= df['reading score'].max()
    F2
    st.text('Maximum score for Writing is')
    F3= df['writing score'].max()
    F3
    
    st.text('Minimum score for Math is')
    F1a= df['math score'].min()
    F1a
    st.text('Minimum score for Reading is')
    F2a= df['reading score'].min()
    F2a
    st.text('Minimum score for Writing is')
    F3a= df['writing score'].min()
    F3a
###############################################################################################################
elif dataset1== 'Top Performance':
    st.text('Perfect Score Achieved  By Students:')
    G1= df[(df['math score'] == 100) & (df['reading score']==100) & (df['writing score']==100)]
    G1
    st.text('Top Scored Students:')
    G2= df[(df['math score'] > 82) & (df['reading score'] > 82) & (df['writing score'] > 82)]
    G2
###############################################################################################################
elif dataset1== 'Lower Performance':
    st.text('Lowest Scored Students:')
    H1= df[(df['math score'] == 0) & (df['reading score']==17) & (df['writing score']==10)]
    H1
    st.text('Failed:')
    H2= df[(df['math score'] < 41) & (df['reading score'] < 41) & (df['writing score'] < 41)]
    H2        
