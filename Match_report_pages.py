import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go 
import glob
import base64
import requests


@st.cache_data
def get_base64_of_bin_file(bin_file):
    response = requests.get(bin_file)
    data = response.content
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)


def chances(df):
    if 'code' in df.columns:
        Finishing = df[df['code'] == 'O4 Finishing']
        Defending = df[df['code'] == 'D4 Defending the Box']
    else:
        Finishing = df[df['Row'] == 'O4 Finishing']
        Defending = df[df['Row'] == 'D4 Defending the Box']
    Finishing = Finishing.reset_index(drop=True)
    Defending = Defending.reset_index(drop=True)
    return Finishing,Defending

def O4_D4(df):
    #O4 & D4-Total Dataframes
    #Attacking Phases Dataframes
    Finishing,Defending=chances(df)
    a_est=Finishing[Finishing['01. Phase'] == 'Established Play']
    a_est = a_est.reset_index(drop=True)
    a_tr=Finishing[Finishing['01. Phase'] == 'Transition']
    a_tr = a_tr.reset_index(drop=True)
    a_sp=pd.DataFrame(columns=Finishing.columns)
    a_sp = a_sp.reset_index(drop=True)
    for i in range(len(Finishing)):
        if (Finishing['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
            a_sp = a_sp.append(Finishing.iloc[i])
    #Defensive Phases Dataframes
    d_est=Defending[Defending['01. Phase'] == 'Established Play']
    d_est = d_est.reset_index(drop=True)
    d_tr=Defending[Defending['01. Phase'] == 'Transition']
    d_tr = d_tr.reset_index(drop=True)
    d_sp=pd.DataFrame(columns=Defending.columns)
    d_sp = d_sp.reset_index(drop=True)
    for i in range(len(Defending)):
        if (Defending['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
            d_sp = d_sp.append(Defending.iloc[i])

    #Page1: 
    #Part 1: Finishing-Defending: Successful-Unsuccessful-Neutral:
    SF=Finishing['04. Rating'].value_counts().get('Successful', 0)
    UF=Finishing['04. Rating'].value_counts().get('Unsuccessful', 0)
    NF=Finishing['04. Rating'].value_counts().get('Neutral', 0)
 
    SD=Defending['04. Rating'].value_counts().get('Successful', 0)
    UD=Defending['04. Rating'].value_counts().get('Unsuccessful', 0)
    ND=Defending['04. Rating'].value_counts().get('Neutral', 0)

    #Part 2: Phases-Ratings
    #a)Finishing
    A_SEp=a_est['04. Rating'].value_counts().get('Successful', 0)
    A_UEp=a_est['04. Rating'].value_counts().get('Unsuccessful', 0)
    A_NEp=a_est['04. Rating'].value_counts().get('Neutral', 0)

    A_ST=a_tr['04. Rating'].value_counts().get('Successful', 0)
    A_UT=a_tr['04. Rating'].value_counts().get('Unsuccessful', 0)
    A_NT=a_tr['04. Rating'].value_counts().get('Neutral', 0)

    A_SSp=a_sp['04. Rating'].value_counts().get('Successful', 0)
    A_USp=a_sp['04. Rating'].value_counts().get('Unsuccessful', 0)
    A_NSp=a_sp['04. Rating'].value_counts().get('Neutral', 0)
    #b)Defending
    D_SEp=d_est['04. Rating'].value_counts().get('Successful', 0)
    D_UEp=d_est['04. Rating'].value_counts().get('Unsuccessful', 0)
    D_NEp=d_est['04. Rating'].value_counts().get('Neutral', 0)

    D_ST=d_tr['04. Rating'].value_counts().get('Successful', 0)
    D_UT=d_tr['04. Rating'].value_counts().get('Unsuccessful', 0)
    D_NT=d_tr['04. Rating'].value_counts().get('Neutral', 0)

    D_SSp=d_sp['04. Rating'].value_counts().get('Successful', 0)
    D_USp=d_sp['04. Rating'].value_counts().get('Unsuccessful', 0)
    D_NSp=d_sp['04. Rating'].value_counts().get('Neutral', 0)
    return SF,UF,NF,SD,UD,ND,A_SEp,A_UEp,A_NEp,A_ST,A_UT,A_NT,A_SSp,A_USp,A_NSp,D_SEp,D_UEp,D_NEp,D_ST,D_UT,D_NT,D_SSp,D_USp,D_NSp

def time_period_O4(df):
    Finishing,Defending=chances(df)
    if 'Time Period' in df.columns:
        #15-Minutes periods:
        Reading = Finishing[Finishing['Time Period'] == '0 - 15 min']
        Reading = Reading.reset_index(drop=True)
        Reacting = Finishing[Finishing['Time Period'] == '16 - 30 min']
        Reacting = Reacting.reset_index(drop=True)
        Acting_1= Finishing[Finishing['Time Period'] == '31 - 45 min']
        Acting_1 = Acting_1.reset_index(drop=True)
        Breathe=Finishing[Finishing['Time Period'] == '46 - 60 min']
        Breathe = Breathe.reset_index(drop=True)
        Refresh=Finishing[Finishing['Time Period'] == '61 - 75 min']
        Refresh = Refresh.reset_index(drop=True)
        Acting_2=Finishing[Finishing['Time Period'] == '76 - 90 min']
        Acting_2 = Acting_2.reset_index(drop=True)

        #0-15:
        Read_ep=Reading[Reading['01. Phase']=='Established Play']
        Read_ep = Read_ep.reset_index(drop=True)
        EP0_15=Read_ep['01. Phase'].value_counts().get('Established Play', 0)
        Read_tr=Reading[Reading['01. Phase']=='Transition']
        Read_tr = Read_tr.reset_index(drop=True)
        TR0_15=Read_tr['01. Phase'].value_counts().get('Transition', 0)
        Read_sp = pd.DataFrame(columns=Reacting.columns)
        Read_sp = Read_sp.reset_index(drop=True)
        SP0_15 = 0

        for i in range(len(Reading)):
            if (Reading['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Read_sp = Read_sp.append(Reading.iloc[i])
                SP0_15 += 1
        #16-30:
        React_ep=Reacting[Reacting['01. Phase']=='Established Play']
        React_ep = React_ep.reset_index(drop=True)
        EP16_30=React_ep['01. Phase'].value_counts().get('Established Play', 0)
        React_tr=Reacting[Reacting['01. Phase']=='Transition']
        React_tr = React_tr.reset_index(drop=True)
        TR16_30=React_tr['01. Phase'].value_counts().get('Transition', 0)
        React_sp = pd.DataFrame(columns=Reacting.columns)
        React_sp = React_sp.reset_index(drop=True)
        SP16_30 = 0

        for i in range(len(Reacting)):
            if (Reacting['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                React_sp = React_sp.append(Reacting.iloc[i])
                SP16_30 += 1
        #31-45:
        Act1_ep=Acting_1[Acting_1['01. Phase']=='Established Play']
        Act1_ep = Act1_ep.reset_index(drop=True)
        EP31_45=Act1_ep['01. Phase'].value_counts().get('Established Play', 0)
        Act1_tr=Acting_1[Acting_1['01. Phase']=='Transition']
        Act1_tr = Act1_tr.reset_index(drop=True)
        TR31_45=Act1_tr['01. Phase'].value_counts().get('Transition', 0)
        Act1_sp = pd.DataFrame(columns=Acting_1.columns)
        Act1_sp = Act1_sp.reset_index(drop=True)
        SP31_45 = 0

        for i in range(len(Acting_1)):
            if (Acting_1['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Act1_sp = Act1_sp.append(Acting_1.iloc[i])
                SP31_45 += 1
        #46-60:
        Br_ep=Breathe[Breathe['01. Phase']=='Established Play']
        Br_ep = Br_ep.reset_index(drop=True)
        EP46_60=Br_ep['01. Phase'].value_counts().get('Established Play', 0)
        Br_tr=Breathe[Breathe['01. Phase']=='Transition']
        Br_tr = Br_tr.reset_index(drop=True)
        TR46_60=Br_ep['01. Phase'].value_counts().get('Transition', 0)
        Br_sp = pd.DataFrame(columns=Breathe.columns)
        Br_sp = Br_sp.reset_index(drop=True)
        SP46_60 = 0

        for i in range(len(Breathe)):
            if (Breathe['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Br_sp = Br_sp.append(Breathe.iloc[i])
                SP46_60 += 1
        #61-75:
        Re_ep=Refresh[Refresh['01. Phase']=='Established Play']
        Re_ep = Re_ep.reset_index(drop=True)
        EP61_75=Re_ep['01. Phase'].value_counts().get('Established Play', 0)
        Re_tr=Refresh[Refresh['01. Phase']=='Transition']
        Re_tr = Re_tr.reset_index(drop=True)
        TR61_75=Re_ep['01. Phase'].value_counts().get('Transition', 0)
        Re_sp = pd.DataFrame(columns=Refresh.columns)
        Re_sp = Re_sp.reset_index(drop=True)
        SP61_75 = 0

        for i in range(len(Refresh)):
            if (Refresh['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Re_sp = Re_sp.append(Refresh.iloc[i])
                SP61_75 += 1
        #76-90:
        Act2_ep=Acting_2[Acting_2['01. Phase']=='Established Play']
        Act2_ep = Act2_ep.reset_index(drop=True)
        EP76_90=Act2_ep['01. Phase'].value_counts().get('Established Play', 0)
        Act2_tr=Acting_2[Acting_2['01. Phase']=='Transition']
        Act2_tr = Act2_tr.reset_index(drop=True)
        TR76_90=Act2_tr['01. Phase'].value_counts().get('Transition', 0)
        Act2_sp = pd.DataFrame(columns=Acting_2.columns)
        Act2_sp = Act2_sp.reset_index(drop=True)
        SP76_90 = 0

        for i in range(len(Acting_2)):
            if (Acting_2['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Act2_sp = Act2_sp.append(Acting_2.iloc[i])
                SP76_90 += 1
        #Page2:
        SEP0_15=Read_ep['04. Rating'].value_counts().get('Successful', 0)
        STR0_15=Read_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP0_15=Read_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP16_30=React_ep['04. Rating'].value_counts().get('Successful', 0)
        STR16_30=React_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP16_30=React_sp['04. Rating'].value_counts().get('Successful', 0)
        
        SEP31_45=Act1_ep['04. Rating'].value_counts().get('Successful', 0)
        STR31_45=Act1_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP31_45=Act1_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP46_60=Br_ep['04. Rating'].value_counts().get('Successful', 0)
        STR46_60=Br_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP46_60=Br_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP61_75=Re_ep['04. Rating'].value_counts().get('Successful', 0)
        STR61_75=Re_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP61_75=Re_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP76_90=Act2_ep['04. Rating'].value_counts().get('Successful', 0)
        STR76_90=Act2_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP76_90=Act2_sp['04. Rating'].value_counts().get('Successful', 0)

        return (EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,
                SP16_30,EP31_45,TR31_45,SP31_45,EP46_60,TR46_60,SP46_60,
                EP61_75,TR61_75,SP61_75,EP76_90,TR76_90,
                SP76_90,SEP0_15,
                STR0_15,SSP0_15,SEP16_30,STR16_30,SSP16_30,
                SEP31_45,STR31_45,SSP31_45,SEP46_60,STR46_60,SSP46_60,SEP61_75,
                STR61_75,SSP61_75,SEP76_90,STR76_90,SSP76_90)
    else:
        return None
    
def time_period_D4(df):
    Finishing,Defending=chances(df)
    if 'Time Period' in df.columns:
        #15-Minutes periods:
        DReading = Defending[Defending['Time Period'] == '0 - 15 min']
        DReading = DReading.reset_index(drop=True)
        DReacting = Defending[Defending['Time Period'] == '16 - 30 min']
        DReacting = DReacting.reset_index(drop=True)
        DActing_1= Defending[Defending['Time Period'] == '31 - 45 min']
        DActing_1 = DActing_1.reset_index(drop=True)
        DBreathe=Defending[Defending['Time Period'] == '46 - 60 min']
        DBreathe = DBreathe.reset_index(drop=True)
        DRefresh=Defending[Defending['Time Period'] == '61 - 75 min']
        DRefresh = DRefresh.reset_index(drop=True)
        DActing_2=Defending[Defending['Time Period'] == '76 - 90 min']
        DActing_2 = DActing_2.reset_index(drop=True)

        #0-15:
        Read_ep=DReading[DReading['01. Phase']=='Established Play']
        Read_ep = Read_ep.reset_index(drop=True)
        DEP0_15=Read_ep['01. Phase'].value_counts().get('Established Play', 0)
        Read_tr=DReading[DReading['01. Phase']=='Transition']
        Read_tr = Read_tr.reset_index(drop=True)
        DTR0_15=Read_tr['01. Phase'].value_counts().get('Transition', 0)
        Read_sp = pd.DataFrame(columns=DReacting.columns)
        Read_sp = Read_sp.reset_index(drop=True)
        DSP0_15 = 0

        for i in range(len(DReading)):
            if (DReading['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Read_sp = Read_sp.append(DReading.iloc[i])
                DSP0_15 += 1
        #16-30:
        React_ep=DReacting[DReacting['01. Phase']=='Established Play']
        React_ep = React_ep.reset_index(drop=True)
        DEP16_30=React_ep['01. Phase'].value_counts().get('Established Play', 0)
        React_tr=DReacting[DReacting['01. Phase']=='Transition']
        React_tr = React_tr.reset_index(drop=True)
        DTR16_30=React_tr['01. Phase'].value_counts().get('Transition', 0)
        React_sp = pd.DataFrame(columns=DReacting.columns)
        React_sp = React_sp.reset_index(drop=True)
        DSP16_30 = 0

        for i in range(len(DReacting)):
            if (DReacting['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                React_sp = React_sp.append(DReacting.iloc[i])
                DSP16_30 += 1
        #31-45:
        Act1_ep=DActing_1[DActing_1['01. Phase']=='Established Play']
        Act1_ep = Act1_ep.reset_index(drop=True)
        DEP31_45=Act1_ep['01. Phase'].value_counts().get('Established Play', 0)
        Act1_tr=DActing_1[DActing_1['01. Phase']=='Transition']
        Act1_tr = Act1_tr.reset_index(drop=True)
        DTR31_45=Act1_tr['01. Phase'].value_counts().get('Transition', 0)
        Act1_sp = pd.DataFrame(columns=DActing_1.columns)
        Act1_sp = Act1_sp.reset_index(drop=True)
        DSP31_45 = 0

        for i in range(len(DActing_1)):
            if (DActing_1['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Act1_sp = Act1_sp.append(DActing_1.iloc[i])
                DSP31_45 += 1
        #46-60:
        Br_ep=DBreathe[DBreathe['01. Phase']=='Established Play']
        Br_ep = Br_ep.reset_index(drop=True)
        DEP46_60=Br_ep['01. Phase'].value_counts().get('Established Play', 0)
        Br_tr=DBreathe[DBreathe['01. Phase']=='Transition']
        Br_tr = Br_tr.reset_index(drop=True)
        DTR46_60=Br_ep['01. Phase'].value_counts().get('Transition', 0)
        Br_sp = pd.DataFrame(columns=DBreathe.columns)
        Br_sp = Br_sp.reset_index(drop=True)
        DSP46_60 = 0

        for i in range(len(DBreathe)):
            if (DBreathe['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Br_sp = Br_sp.append(DBreathe.iloc[i])
                DSP46_60 += 1
        #61-75:
        Re_ep=DRefresh[DRefresh['01. Phase']=='Established Play']
        Re_ep = Re_ep.reset_index(drop=True)
        DEP61_75=Re_ep['01. Phase'].value_counts().get('Established Play', 0)
        Re_tr=DRefresh[DRefresh['01. Phase']=='Transition']
        Re_tr = Re_tr.reset_index(drop=True)
        DTR61_75=Re_ep['01. Phase'].value_counts().get('Transition', 0)
        Re_sp = pd.DataFrame(columns=DRefresh.columns)
        Re_sp = Re_sp.reset_index(drop=True)
        DSP61_75 = 0

        for i in range(len(DRefresh)):
            if (DRefresh['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Re_sp = Re_sp.append(DRefresh.iloc[i])
                DSP61_75 += 1
        #76-90:
        Act2_ep=DActing_2[DActing_2['01. Phase']=='Established Play']
        Act2_ep = Act2_ep.reset_index(drop=True)
        DEP76_90=Act2_ep['01. Phase'].value_counts().get('Established Play', 0)
        Act2_tr=DActing_2[DActing_2['01. Phase']=='Transition']
        Act2_tr = Act2_tr.reset_index(drop=True)
        DTR76_90=Act2_tr['01. Phase'].value_counts().get('Transition', 0)
        Act2_sp = pd.DataFrame(columns=DActing_2.columns)
        Act2_sp = Act2_sp.reset_index(drop=True)
        DSP76_90 = 0

        for i in range(len(DActing_2)):
            if (DActing_2['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Act2_sp = Act2_sp.append(DActing_2.iloc[i])
                DSP76_90 += 1
        #Page2:
        DSEP0_15=Read_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR0_15=Read_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP0_15=Read_sp['04. Rating'].value_counts().get('Successful', 0)

        DSEP16_30=React_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR16_30=React_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP16_30=React_sp['04. Rating'].value_counts().get('Successful', 0)
        
        DSEP31_45=Act1_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR31_45=Act1_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP31_45=Act1_sp['04. Rating'].value_counts().get('Successful', 0)

        DSEP46_60=Br_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR46_60=Br_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP46_60=Br_sp['04. Rating'].value_counts().get('Successful', 0)

        DSEP61_75=Re_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR61_75=Re_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP61_75=Re_sp['04. Rating'].value_counts().get('Successful', 0)

        DSEP76_90=Act2_ep['04. Rating'].value_counts().get('Successful', 0)
        DSTR76_90=Act2_tr['04. Rating'].value_counts().get('Successful', 0)
        DSSP76_90=Act2_sp['04. Rating'].value_counts().get('Successful', 0)
        
        return (DEP0_15,DTR0_15,DSP0_15,DEP16_30,DTR16_30,
                DSP16_30,DEP31_45,DTR31_45,DSP31_45,DEP46_60,DTR46_60,DSP46_60,
                DEP61_75,DTR61_75,DSP61_75,DEP76_90,DTR76_90,
                DSP76_90,DSEP0_15,
                DSTR0_15,DSSP0_15,DSEP16_30,DSTR16_30,DSSP16_30,
                DSEP31_45,DSTR31_45,DSSP31_45,DSEP46_60,DSTR46_60,DSSP46_60,DSEP61_75,
                DSTR61_75,DSSP61_75,DSEP76_90,DSTR76_90,DSSP76_90)
    else:
        return None
    



def max_values(df):
    SF,UF,NF,SD,UD,ND,A_SEp,A_UEp,A_NEp,A_ST,A_UT,A_NT,A_SSp,A_USp,A_NSp,D_SEp,D_UEp,D_NEp,D_ST,D_UT,D_NT,D_SSp,D_USp,D_NSp=O4_D4(df)
    max_O4_D4=max(SF,UF,NF,SD,UD,ND)
    a=A_SEp+A_UEp+A_NEp
    b=A_ST+A_UT+A_NT
    c=A_SSp+A_USp+A_NSp
    d=D_SEp+D_UEp+D_NEp
    e=D_ST+D_UT+D_NT
    f=D_SSp+D_USp+D_NSp
    max_O4_phases=max(a,b,c,d,e,f)
    return max_O4_D4,max_O4_phases


def overview_page(df):
    st.subheader("Match Details")
    st.write("Information about the game and pics")
    st.write("Sunday 14/05/2023 19:00")
    set_png_as_page_bg("https://www.sgclark.com/blog/wp-content/uploads/europe_soccer_danish_fc_nordsjaelland_home-2048x1152.png")
    

def statistics_page(df):
    st.subheader("Finishing & Defending")
    st.write("This is the statistics page.")

    SF,UF,NF,SD,UD,ND,A_SEp,A_UEp,A_NEp,A_ST,A_UT,A_NT,A_SSp,A_USp,A_NSp,D_SEp,D_UEp,D_NEp,D_ST,D_UT,D_NT,D_SSp,D_USp,D_NSp=O4_D4(df)
    max1,max2=max_values(df)

    # Create two columns for the charts
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display the first chart in the first column
    with col1:
        categories1 = ['Succesful', 'Unsuccessful', 'Neutral']
        values1 = [SF, UF, NF]

        # Plotting the bar chart
        fig, ax = plt.subplots(figsize=(8, 6.25))
        ylim = (0, max1)
        ax.bar(categories1, values1, color=['green','red','grey'], linewidth=2, edgecolor='black')
        ax.set_ylim(ylim)

        for i in range(len(categories1) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max1], linestyle='dotted', color='gray')

        # Adding the line connecting the top points of the bars
        #ax.plot(categories, values, marker='o', linestyle='-', color='red')

        # Setting labels and title
        ax.set_xlabel('Ratings',labelpad=25)
        ax.set_ylabel('Values')
        ax.set_title('Total finishing chances')

        # Displaying the chart using Streamlit
        st.pyplot(fig)

    # Display the second chart in the second column
    with col2:
        #2nd chart
        categories2 = ['Succesful', 'Unsuccessful', 'Neutral']
        values2 = [SD, UD, ND]

        # Plotting the bar chart
        fig2, ax = plt.subplots(figsize=(8, 6))
        ylim = (0, max1)
        ax.bar(categories2, values2, color=['green','red','grey'], linewidth=2, edgecolor='black')
        ax.set_ylim(ylim)

        for i in range(len(categories2) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max1], linestyle='dotted', color='gray')

        # Adding the line connecting the top points of the bars
        #ax.plot(categories2, values2, marker='o', linestyle='-', color='red')

        # Setting labels and title
        ax.set_xlabel('Ratings',labelpad=25)
        ax.set_title('Total Defending occasions')

        # Displaying the chart using Streamlit
        st.pyplot(fig2)
    with col3:
        # Data for three phases and three categories
        Ratings = ['Successful', 'Neutral', 'Unsuccessful']
        categories = ['Established play', 'Tranistion', 'Set pieces']
        values = np.array([[A_SEp, A_ST, A_SSp], [A_NEp, A_NT, A_NSp], [A_UEp, A_UT, A_USp]])

        # Define custom colors for the bars
        colors = ['green', 'grey', 'red']

        # Create a stacked bar chart
        fig3, ax = plt.subplots(figsize=(8, 6.25))
        ylim = (0, max2)
        # Iterate over phases and create stacked bars with custom colors, thicker line width, and outer line color
        bottom = np.zeros(len(categories))
        for i, rating in enumerate(Ratings):
            ax.bar(categories, values[i], bottom=bottom, label=rating, color=colors[i], linewidth=2, edgecolor='black')
            # Add phase names and values as text annotations inside the bars
            for j, val in enumerate(values[i]):
                if val != 0:  # Exclude displaying value if it is 0
                    ax.text(j, bottom[j] + val / 2, f'{rating}: {val}', ha='center', va='center', color='white')
            bottom += values[i]
        for i in range(len(categories1) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max2], linestyle='dotted', color='gray')
        
        ax.set_ylim(ylim)

        # Set the chart title and labels
        ax.set_title('Finishing by phases')
        ax.set_xlabel('Phases', labelpad=25)
        ax.set_ylabel('Values')

        # Add a legend
        ax.legend()

        # Display the chart in Streamlit
        st.pyplot(fig3)

    with col4:
        # Data for three phases and three categories
        Ratings = ['Successful', 'Neutral', 'Unsuccessful']
        Phases = ['Established play', 'Tranistion', 'Set pieces']
        values = np.array([[D_SEp, D_ST, D_SSp], [D_NEp, D_NT, D_NSp], [D_UEp, D_UT, D_USp]])

        # Define custom colors for the bars
        colors = ['green', 'grey', 'red']

        # Create a stacked bar chart
        fig4, ax = plt.subplots(figsize=(8, 6))
        ylim = (0, max2)
        # Iterate over phases and create stacked bars with custom colors, thicker line width, and outer line color
        bottom = np.zeros(len(Phases))
        for i, rating in enumerate(Ratings):
            ax.bar(Phases, values[i], bottom=bottom, label=rating, color=colors[i], linewidth=2, edgecolor='black')
            # Add phase names and values as text annotations inside the bars
            for j, val in enumerate(values[i]):
                if val != 0:  # Exclude displaying value if it is 0
                    ax.text(j, bottom[j] + val / 2, f'{rating}: {val}', ha='center', va='center', color='white')
            bottom += values[i]
        for i in range(len(Phases) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max2], linestyle='dotted', color='gray')
        
        ax.set_ylim(ylim)

        # Set the chart title and labels
        ax.set_title('Defending by phases')
        ax.set_xlabel('Phases', labelpad=25)

        # Add a legend
        ax.legend()

        # Display the chart in Streamlit
        st.pyplot(fig4)
    set_png_as_page_bg("https://tactical-times.com/wp-content/uploads/2021/07/Untitled.png")


    

def visualization_page(df):
    st.subheader("Quarters")
    st.write("This is the visualization page.")
    EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,SP16_30,EP31_45,TR31_45,SP31_45,EP46_60,TR46_60,SP46_60,EP61_75,TR61_75,SP61_75,EP76_90,TR76_90,SP76_90,SEP0_15,STR0_15,SSP0_15,SEP16_30,STR16_30,SSP16_30,SEP31_45,STR31_45,SSP31_45,SEP46_60,STR46_60,SSP46_60,SEP61_75,STR61_75,SSP61_75,SEP76_90,STR76_90,SSP76_90=time_period_O4(df)
    DEP0_15,DTR0_15,DSP0_15,DEP16_30,DTR16_30,DSP16_30,DEP31_45,DTR31_45,DSP31_45,DEP46_60,DTR46_60,DSP46_60,DEP61_75,DTR61_75,DSP61_75,DEP76_90,DTR76_90,DSP76_90,DSEP0_15,DSTR0_15,DSSP0_15,DSEP16_30,DSTR16_30,DSSP16_30,DSEP31_45,DSTR31_45,DSSP31_45,DSEP46_60,DSTR46_60,DSSP46_60,DSEP61_75,DSTR61_75,DSSP61_75,DSEP76_90,DSTR76_90,DSSP76_90=time_period_D4(df)
    ep_table,tr_table,sp_table,final,jtable=avg_calculations()
    d_ep_table,d_tr_table,d_sp_table,d_final,d_jtable=def_avg_calculations()
    maxbar=max(EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,SP16_30,EP31_45,
               TR31_45,SP31_45,EP46_60,TR46_60,SP46_60,EP61_75,TR61_75,
               SP61_75,EP76_90,TR76_90,SP76_90,SEP0_15,STR0_15,SSP0_15,
               SEP16_30,STR16_30,SSP16_30,SEP31_45,STR31_45,SSP31_45,SEP46_60,
               STR46_60,SSP46_60,SEP61_75,STR61_75,SSP61_75,SEP76_90,STR76_90,SSP76_90,
               DEP0_15,DTR0_15,DSP0_15,DEP16_30,DTR16_30,DSP16_30,DEP31_45,DTR31_45,
               DSP31_45,DEP46_60,DTR46_60,DSP46_60,DEP61_75,DTR61_75,DSP61_75,DEP76_90,
               DTR76_90,DSP76_90,DSEP0_15,DSTR0_15,DSSP0_15,DSEP16_30,DSTR16_30,DSSP16_30,
               DSEP31_45,DSTR31_45,DSSP31_45,DSEP46_60,DSTR46_60,DSSP46_60,DSEP61_75,
               DSTR61_75,DSSP61_75,DSEP76_90,DSTR76_90,DSSP76_90)
    set_png_as_page_bg("https://tactical-times.com/wp-content/uploads/2021/07/Untitled.png")

    array = jtable.values
    d_array=d_jtable.values

    print(array)
    
    col1, col2 = st.columns(2)
    with col1:
        if 'Time Period' in df.columns:
            # Define the time periods
            time_periods = ['0-15', '16-30', '31-45', '46-60', '61-75', '76-90']

            # Define the situations
            situations = ['Established Play', 'Transition', 'Set Piece']

            # Sample data for situation counts
            situation_counts1 = np.array([[EP0_15, TR0_15, SP0_15],
                                        [EP16_30, TR16_30, SP16_30],
                                        [EP31_45, TR31_45, SP31_45],
                                        [EP46_60, TR46_60, SP46_60],
                                        [EP61_75, TR61_75, SP61_75],
                                        [EP76_90, TR76_90, SP76_90]])
            
            print(situation_counts1)

            # Set up the chart
            fig, ax = plt.subplots()
            ylim = (0, maxbar)

            # Calculate the width for each bar
            bar_width = 0.2

            # Set the positions of the bars on the x-axis
            bar_positions = np.arange(len(time_periods))

            colors = ['blue', 'yellow', 'purple']

            # Create a bar for each situation
            for i, situation in enumerate(situations):
                # Set the x-position for the bars of each situation
                situation_positions = [pos + i * bar_width for pos in bar_positions]

                # Get the counts for the current situation
                counts = situation_counts1[:, i]

                # Create the bar for the situation
                bar = ax.bar(situation_positions, counts, bar_width, label=situation, color=colors[i], linewidth=2, edgecolor='black')

            # Add average lines
            for i in range(len(time_periods)):
                for j in range(len(situations)):
                    value = array[i, j]
                    bar_position = bar_positions[i] + j * bar_width  # x-coordinate of the bar

                    # Calculate the starting and ending positions of the line
                    start = bar_position - bar_width / 2  # Starting position of the line
                    end = bar_position + bar_width / 2    # Ending position of the line

                    ax.plot([start, end], [value] * 2, color='red', linestyle='-')

            c = max(EP0_15, EP16_30, EP31_45, EP46_60, EP61_75, EP76_90,DEP0_15,DEP16_30,DEP31_45,DEP46_60,DEP61_75,DEP76_90)
            for i in range(len(time_periods) - 1):
                line_x = i + 0.75  # x-coordinate of the line (adjust as needed)

                # Plotting the dotted line
                ax.plot([line_x, line_x], [0, c], linestyle='dotted', color='gray')

                
            ax.set_ylim(ylim)
            # Set labels and title
            ax.set_xlabel('Time Periods')
            ax.set_ylabel('Count')
            ax.set_title('15-Minutes O4 from phases')

            # Set the x-axis ticks and labels
            ax.set_xticks(bar_positions)
            ax.set_xticklabels(time_periods)
            

            # Add a legend
            ax.legend()

            # Remove the extra whitespace from the figure
            plt.tight_layout()

            # Convert the Matplotlib figure to a Streamlit figure
            st.pyplot(fig)
        else: 
            print("15 Minutes intervals do not exist")
            st.write("15 Minutes intervals do not exist")
    with col2:
        if 'Time Period' in df.columns:
            # Define the time periods
            time_periods = ['0-15', '16-30', '31-45', '46-60', '61-75', '76-90']

            # Define the situations
            situations = ['Established Play', 'Transition', 'Set Piece']

            # Sample data for situation counts
            situation_counts2 = np.array([[DEP0_15, DTR0_15, DSP0_15],
                                        [DEP16_30, DTR16_30, DSP16_30],
                                        [DEP31_45, DTR31_45, DSP31_45],
                                        [DEP46_60, DTR46_60, DSP46_60],
                                        [DEP61_75, DTR61_75, DSP61_75],
                                        [DEP76_90, DTR76_90, DSP76_90]])

            # Set up the chart
            fig, ax = plt.subplots()
            ylim = (0, maxbar)

            # Calculate the width for each bar
            bar_width = 0.2

            # Set the positions of the bars on the x-axis
            bar_positions = np.arange(len(time_periods))

            colors = ['blue', 'yellow', 'purple']

            # Create a bar for each situation
            for i, situation in enumerate(situations):
                # Set the x-position for the bars of each situation
                situation_positions = [pos + i * bar_width for pos in bar_positions]

                # Get the counts for the current situation
                counts = situation_counts2[:, i]

                # Create the bar for the situation
                bar = ax.bar(situation_positions, counts, bar_width, label=situation, color=colors[i], linewidth=2, edgecolor='black')

            # Add average lines
            for i in range(len(time_periods)):
                for j in range(len(situations)):
                    value = d_array[i, j]
                    bar_position = bar_positions[i] + j * bar_width  # x-coordinate of the bar

                    # Calculate the starting and ending positions of the line
                    start = bar_position - bar_width / 2  # Starting position of the line
                    end = bar_position + bar_width / 2    # Ending position of the line

                    ax.plot([start, end], [value] * 2, color='red', linestyle='-')

            c=max(EP0_15, EP16_30, EP31_45, EP46_60, EP61_75, EP76_90, DEP0_15,DEP16_30,DEP31_45,DEP46_60,DEP61_75,DEP76_90)
            for i in range(len(time_periods) - 1):
                    line_x = i + 0.75  # x-coordinate of the line (adjust as needed)

                    # Plotting the dotted line
                    ax.plot([line_x, line_x], [0, c], linestyle='dotted', color='gray')

                
            ax.set_ylim(ylim)
            # Set labels and title
            ax.set_xlabel('Time Periods')
            ax.set_ylabel('Count')
            ax.set_title('15-Minutes D4 from phases')

            # Set the x-axis ticks and labels
            ax.set_xticks(bar_positions)
            ax.set_xticklabels(time_periods)

            # Add a legend
            ax.legend()

            # Remove the extra whitespace from the figure
            plt.tight_layout()

            # Convert the Matplotlib figure to a Streamlit figure
            st.pyplot(fig)
        else: 
            print("15 Minutes intervals do not exist")
            st.write("15 Minutes intervals do not exist")

def avg_calculations():
    folder_path = 'https://raw.githubusercontent.com/Vangelis19/Streamlit/main/Superliga%202022-2023/'
    csv_files = ['01_OB-FCN','02_BIF-FCN','03_FCN-LBK',
                '04_FCN-VFF','05_AAB-FCN','06_FCN-SIF',
                '07_FCN-FCK','08_AGF-FCN','09_FCN-FCM',
                '10_ACH-FCN','11_FCN-RFC','12_FCK-FCN',
                '13_FCN-AGF','14_RFC-FCN','15_FCN-ACH',
                '16_FCM-FCN','17_FCN-AAB','18_LBK-FCN',
                '19_FCN-OB','20_SIF-FCN','21_VFF-FCN',
                '22_FCN-BIF','23_FCK-FCN','24_FCN-BIF',
                '25_RFC-FCN','26_VFF-FCN','27_FCN-AGF',
                '28_FCN-FCK','29_AGF-FCN','30_FCN-RFC',
                '31_BIF-FCN','32_FCN-VFF'
                ]

    # Iterate over each CSV file and read it into a DataFrame
    files=[]
    dataframes = []
    for i in range (len(csv_files)):
        item=folder_path+csv_files[i]+'.csv'
        files.append(item)
    us_ep = []
    s_ep = []
    n_ep = []
    us_tr = []
    s_tr = []
    n_tr = []
    us_sp = []
    s_sp = []
    n_sp = []
    total_ep=[]
    total_tr=[]
    total_sp=[]
    tp1=[]
    tp2=[]
    tp3=[]
    tp4=[]
    tp5=[]
    tp6=[]
    tp_tr1=[]
    tp_tr2=[]
    tp_tr3=[]
    tp_tr4=[]
    tp_tr5=[]
    tp_tr6=[]

    tp_sp1=[]
    tp_sp2=[]
    tp_sp3=[]
    tp_sp4=[]
    tp_sp5=[]
    tp_sp6=[]

    a_t1=[]
    a_t2=[]
    a_t3=[]
    a_t4=[]
    a_t5=[]
    a_t6=[]

    


    for file in files:
        df = pd.read_csv(file)
        required_columns = ['00. Start Phase', '02. Situation Type','03. Outcomes','04. Rating','01. Phase']
        if all(column in df.columns for column in required_columns):
            if 'code' in df:
                filtered_df = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Unsuccessful')]
                filtered_df1 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Successful')]
                filtered_df2 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Neutral')]
                tr_df = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Unsuccessful')]
                tr_df1 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Successful')]
                tr_df2 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Neutral')]
                sp_df = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Unsuccessful')]
                sp_df1 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Successful')]
                sp_df2 = df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Neutral')]
                total1=filtered_df['04. Rating'].str.count('Unsuccessful').sum()+filtered_df1['04. Rating'].str.count('Successful').sum()+filtered_df2['04. Rating'].str.count('Neutral').sum()
                total2=tr_df['04. Rating'].str.count('Unsuccessful').sum()+tr_df1['04. Rating'].str.count('Successful').sum()+tr_df2['04. Rating'].str.count('Neutral').sum()
                total3=sp_df['04. Rating'].str.count('Unsuccessful').sum()+sp_df1['04. Rating'].str.count('Successful').sum()+sp_df2['04. Rating'].str.count('Neutral').sum()
                if 'Time Period' in df:
                    time_15=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='0 - 15 min')]
                    time_30=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='16 - 30 min')]
                    time_45=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='31 - 45 min')]
                    time_60=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='46 - 60 min')]
                    time_75=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='61 - 75 min')]
                    time_90=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='76 - 90 min')]

                    time_15_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='0 - 15 min')]
                    time_30_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='16 - 30 min')]
                    time_45_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='31 - 45 min')]
                    time_60_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='46 - 60 min')]
                    time_75_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='61 - 75 min')]
                    time_90_tr=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='76 - 90 min')]

                    time_15_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='0 - 15 min')]
                    time_30_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='16 - 30 min')]
                    time_45_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='31 - 45 min')]
                    time_60_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='46 - 60 min')]
                    time_75_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='61 - 75 min')]
                    time_90_sp=df.loc[(df['code'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='76 - 90 min')]
                else:
                    time_15=0
                    time_30=0
                    time_45=0
                    time_60=0
                    time_75=0
                    time_90=0

                    time_15_tr=0
                    time_30_tr=0
                    time_45_tr=0
                    time_60_tr=0
                    time_75_tr=0
                    time_90_tr=0

                    time_15_sp=0
                    time_30_sp=0
                    time_45_sp=0
                    time_60_sp=0
                    time_75_sp=0
                    time_90_sp=0
            else:
                filtered_df = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Unsuccessful')]
                filtered_df1 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Successful')]
                filtered_df2 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Neutral')]
                tr_df = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Unsuccessful')]
                tr_df1 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Successful')]
                tr_df2 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Neutral')]
                sp_df = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Unsuccessful')]
                sp_df1 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Successful')]
                sp_df2 = df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Neutral')]
                total1=filtered_df['04. Rating'].str.count('Unsuccessful').sum()+filtered_df1['04. Rating'].str.count('Successful').sum()+filtered_df2['04. Rating'].str.count('Neutral').sum()
                total2=tr_df['04. Rating'].str.count('Unsuccessful').sum()+tr_df1['04. Rating'].str.count('Successful').sum()+tr_df2['04. Rating'].str.count('Neutral').sum()
                total3=sp_df['04. Rating'].str.count('Unsuccessful').sum()+sp_df1['04. Rating'].str.count('Successful').sum()+sp_df2['04. Rating'].str.count('Neutral').sum()
                if 'Time Period' in df:
                    time_15=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='0 - 15 min')]
                    time_30=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='16 - 30 min')]
                    time_45=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='31 - 45 min')]
                    time_60=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='46 - 60 min')]
                    time_75=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='61 - 75 min')]
                    time_90=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='76 - 90 min')]

                    time_15_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='0 - 15 min')]
                    time_30_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='16 - 30 min')]
                    time_45_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='31 - 45 min')]
                    time_60_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='46 - 60 min')]
                    time_75_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='61 - 75 min')]
                    time_90_tr=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='76 - 90 min')]

                    time_15_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='0 - 15 min')]
                    time_30_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='16 - 30 min')]
                    time_45_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='31 - 45 min')]
                    time_60_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='46 - 60 min')]
                    time_75_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='61 - 75 min')]
                    time_90_sp=df.loc[(df['Row'] == 'O4 Finishing') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='76 - 90 min')]
                else:
                    time_15=0
                    time_30=0
                    time_45=0
                    time_60=0
                    time_75=0
                    time_90=0

                    time_15_tr=0
                    time_30_tr=0
                    time_45_tr=0
                    time_60_tr=0
                    time_75_tr=0
                    time_90_tr=0

                    time_15_sp=0
                    time_30_sp=0
                    time_45_sp=0
                    time_60_sp=0
                    time_75_sp=0
                    time_90_sp=0
            us_ep.append(filtered_df['04. Rating'].str.count('Unsuccessful').sum())
            s_ep.append(filtered_df1['04. Rating'].str.count('Successful').sum())
            n_ep.append(filtered_df2['04. Rating'].str.count('Neutral').sum())
            us_tr.append(tr_df['04. Rating'].str.count('Unsuccessful').sum())
            s_tr.append(tr_df1['04. Rating'].str.count('Successful').sum())
            n_tr.append(tr_df2['04. Rating'].str.count('Neutral').sum())
            us_sp.append(sp_df['04. Rating'].str.count('Unsuccessful').sum())
            s_sp.append(sp_df1['04. Rating'].str.count('Successful').sum())
            n_sp.append(sp_df2['04. Rating'].str.count('Neutral').sum())
            total_ep.append(total1)
            total_tr.append(total2)
            total_sp.append(total3)
            if 'Time Period' in df:
                tp1.append(time_15['Time Period'].str.count('0 - 15 min').sum())
                tp2.append(time_30['Time Period'].str.count('16 - 30 min').sum())
                tp3.append(time_45['Time Period'].str.count('31 - 45 min').sum())
                tp4.append(time_60['Time Period'].str.count('46 - 60 min').sum())
                tp5.append(time_75['Time Period'].str.count('61 - 75 min').sum())
                tp6.append(time_90['Time Period'].str.count('76 - 90 min').sum())

                tp_tr1.append(time_15_tr['Time Period'].str.count('0 - 15 min').sum())
                tp_tr2.append(time_30_tr['Time Period'].str.count('16 - 30 min').sum())
                tp_tr3.append(time_45_tr['Time Period'].str.count('31 - 45 min').sum())
                tp_tr4.append(time_60_tr['Time Period'].str.count('46 - 60 min').sum())
                tp_tr5.append(time_75_tr['Time Period'].str.count('61 - 75 min').sum())
                tp_tr6.append(time_90_tr['Time Period'].str.count('76 - 90 min').sum())

                tp_sp1.append(time_15_sp['Time Period'].str.count('0 - 15 min').sum())
                tp_sp2.append(time_30_sp['Time Period'].str.count('16 - 30 min').sum())
                tp_sp3.append(time_45_sp['Time Period'].str.count('31 - 45 min').sum())
                tp_sp4.append(time_60_sp['Time Period'].str.count('46 - 60 min').sum())
                tp_sp5.append(time_75_sp['Time Period'].str.count('61 - 75 min').sum())
                tp_sp6.append(time_90_sp['Time Period'].str.count('76 - 90 min').sum())
            else:
                tp1.append(0)
                tp2.append(0)
                tp3.append(0)
                tp4.append(0)
                tp5.append(0)
                tp6.append(0)

                time_15_tr=0
                time_30_tr=0
                time_45_tr=0
                time_60_tr=0
                time_75_tr=0
                time_90_tr=0

                time_15_sp=0
                time_30_sp=0
                time_45_sp=0
                time_60_sp=0
                time_75_sp=0
                time_90_sp=0
            
        else:
            us_ep.append(0)
            s_ep.append(0)
            n_ep.append(0)
            us_tr.append(0)
            s_tr.append(0)
            n_tr.append(0)
            us_sp.append(0)
            s_sp.append(0)
            n_sp.append(0)
            total_ep.append(0)
            total_tr.append(0)
            total_sp.append(0)
            tp1.append(0)
            tp2.append(0)
            tp3.append(0)
            tp4.append(0)
            tp5.append(0)
            tp6.append(0)
            time_15_tr=0
            time_30_tr=0
            time_45_tr=0
            time_60_tr=0
            time_75_tr=0
            time_90_tr=0

            time_15_sp=0
            time_30_sp=0
            time_45_sp=0
            time_60_sp=0
            time_75_sp=0
            time_90_sp=0
    denominator=len(files)
    att_ep_avg_1=sum(tp1)/denominator
    att_ep_avg_2=sum(tp2)/denominator
    att_ep_avg_3=sum(tp3)/denominator
    att_ep_avg_4=sum(tp4)/denominator
    att_ep_avg_5=sum(tp5)/denominator
    att_ep_avg_6=sum(tp6)/denominator
    print(att_ep_avg_1)
    print(att_ep_avg_2)
    print(att_ep_avg_3)
    print(att_ep_avg_4)
    print(att_ep_avg_5)
    print(att_ep_avg_6)

    att_tr_avg_1=sum(tp_tr1)/denominator
    att_tr_avg_2=sum(tp_tr2)/denominator
    att_tr_avg_3=sum(tp_tr3)/denominator
    att_tr_avg_4=sum(tp_tr4)/denominator
    att_tr_avg_5=sum(tp_tr5)/denominator
    att_tr_avg_6=sum(tp_tr6)/denominator

    att_sp_avg_1=sum(tp_sp1)/denominator
    att_sp_avg_2=sum(tp_sp2)/denominator
    att_sp_avg_3=sum(tp_sp3)/denominator
    att_sp_avg_4=sum(tp_sp4)/denominator
    att_sp_avg_5=sum(tp_sp5)/denominator
    att_sp_avg_6=sum(tp_sp6)/denominator

    ep_table=[]
    
    ep_table.append(att_ep_avg_1)
    ep_table.append(att_ep_avg_2)
    ep_table.append(att_ep_avg_3)
    ep_table.append(att_ep_avg_4)
    ep_table.append(att_ep_avg_5)
    ep_table.append(att_ep_avg_6)
    print(ep_table)
    
    tr_table=[]
    tr_table.append(att_tr_avg_1)
    tr_table.append(att_tr_avg_2)
    tr_table.append(att_tr_avg_3)
    tr_table.append(att_tr_avg_4)
    tr_table.append(att_tr_avg_5)
    tr_table.append(att_tr_avg_6)
    print(tr_table)

    sp_table=[]
    sp_table.append(att_sp_avg_1)
    sp_table.append(att_sp_avg_2)
    sp_table.append(att_sp_avg_3)
    sp_table.append(att_sp_avg_4)
    sp_table.append(att_sp_avg_5)
    sp_table.append(att_sp_avg_6)
    print(sp_table)
    
    epO4=pd.DataFrame({'Unsuccessful':us_ep,'Successful':s_ep,'Neutral':n_ep,'Total':total_ep})
    spO4=pd.DataFrame({'Unsuccessful':us_sp,'Successful':s_sp,'Neutral':n_sp,'Total':total_sp})
    trO4=pd.DataFrame({'Unsuccessful':us_tr,'Successful':s_tr,'Neutral':n_tr,'Total':total_tr})

    final = pd.concat([epO4, trO4, spO4], axis=1, keys=['Established Play', 'Transition', 'Set Pieces'], )
    final.index.name = 'Matchday'
    final.index += 1

    conc = {'ep': ep_table, 'tr': tr_table, 'sp': sp_table}
    jtable = pd.DataFrame(conc)
    for i in range(1, 6):
        jtable.iloc[i] = [ep_table[i], tr_table[i], sp_table[i]]

    return ep_table,tr_table,sp_table,final,jtable

def def_avg_calculations():
    folder_path = 'https://raw.githubusercontent.com/Vangelis19/Streamlit/main/Superliga%202022-2023/'
    csv_files = ['01_OB-FCN','02_BIF-FCN','03_FCN-LBK',
                '04_FCN-VFF','05_AAB-FCN','06_FCN-SIF',
                '07_FCN-FCK','08_AGF-FCN','09_FCN-FCM',
                '10_ACH-FCN','11_FCN-RFC','12_FCK-FCN',
                '13_FCN-AGF','14_RFC-FCN','15_FCN-ACH',
                '16_FCM-FCN','17_FCN-AAB','18_LBK-FCN',
                '19_FCN-OB','20_SIF-FCN','21_VFF-FCN',
                '22_FCN-BIF','23_FCK-FCN','24_FCN-BIF',
                '25_RFC-FCN','26_VFF-FCN','27_FCN-AGF',
                '28_FCN-FCK','29_AGF-FCN','30_FCN-RFC',
                '31_BIF-FCN','32_FCN-VFF'
                ]

    # Iterate over each CSV file and read it into a DataFrame
    d_files=[]
    dataframes = []
    for i in range (len(csv_files)):
        item=folder_path+csv_files[i]+'.csv'
        d_files.append(item)
    d_us_ep = []
    d_s_ep = []
    d_n_ep = []
    d_us_tr = []
    d_s_tr = []
    d_n_tr = []
    d_us_sp = []
    d_s_sp = []
    d_n_sp = []
    d_total_ep=[]
    d_total_tr=[]
    d_total_sp=[]
    d_tp1=[]
    d_tp2=[]
    d_tp3=[]
    d_tp4=[]
    d_tp5=[]
    d_tp6=[]
    d_tp_tr1=[]
    d_tp_tr2=[]
    d_tp_tr3=[]
    d_tp_tr4=[]
    d_tp_tr5=[]
    d_tp_tr6=[]

    d_tp_sp1=[]
    d_tp_sp2=[]
    d_tp_sp3=[]
    d_tp_sp4=[]
    d_tp_sp5=[]
    d_tp_sp6=[]

    d_t1=[]
    d_t2=[]
    d_t3=[]
    d_t4=[]
    d_t5=[]
    d_t6=[]

    


    for file in d_files:
        df = pd.read_csv(file)
        required_columns = ['00. Start Phase', '02. Situation Type','03. Outcomes','04. Rating','01. Phase']
        if all(column in df.columns for column in required_columns):
            if 'code' in df:
                d_filtered_df = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Unsuccessful')]
                d_filtered_df1 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Successful')]
                d_filtered_df2 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Neutral')]
                d_tr_df = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Unsuccessful')]
                d_tr_df1 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Successful')]
                d_tr_df2 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Neutral')]
                d_sp_df = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Unsuccessful')]
                d_sp_df1 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Successful')]
                d_sp_df2 = df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Neutral')]
                d_total1=d_filtered_df['04. Rating'].str.count('Unsuccessful').sum()+d_filtered_df1['04. Rating'].str.count('Successful').sum()+d_filtered_df2['04. Rating'].str.count('Neutral').sum()
                d_total2=d_tr_df['04. Rating'].str.count('Unsuccessful').sum()+d_tr_df1['04. Rating'].str.count('Successful').sum()+d_tr_df2['04. Rating'].str.count('Neutral').sum()
                d_total3=d_sp_df['04. Rating'].str.count('Unsuccessful').sum()+d_sp_df1['04. Rating'].str.count('Successful').sum()+d_sp_df2['04. Rating'].str.count('Neutral').sum()
                if 'Time Period' in df:
                    d_time_15=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='0 - 15 min')]
                    d_time_30=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='16 - 30 min')]
                    d_time_45=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='31 - 45 min')]
                    d_time_60=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='46 - 60 min')]
                    d_time_75=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='61 - 75 min')]
                    d_time_90=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='76 - 90 min')]

                    d_time_15_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='0 - 15 min')]
                    d_time_30_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='16 - 30 min')]
                    d_time_45_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='31 - 45 min')]
                    d_time_60_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='46 - 60 min')]
                    d_time_75_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='61 - 75 min')]
                    d_time_90_tr=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='76 - 90 min')]

                    d_time_15_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='0 - 15 min')]
                    d_time_30_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='16 - 30 min')]
                    d_time_45_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='31 - 45 min')]
                    d_time_60_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='46 - 60 min')]
                    d_time_75_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='61 - 75 min')]
                    d_time_90_sp=df.loc[(df['code'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='76 - 90 min')]
                else:
                    d_time_15=0
                    d_time_30=0
                    d_time_45=0
                    d_time_60=0
                    d_time_75=0
                    d_time_90=0

                    d_time_15_tr=0
                    d_time_30_tr=0
                    d_time_45_tr=0
                    d_time_60_tr=0
                    d_time_75_tr=0
                    d_time_90_tr=0

                    d_time_15_sp=0
                    d_time_30_sp=0
                    d_time_45_sp=0
                    d_time_60_sp=0
                    d_time_75_sp=0
                    d_time_90_sp=0
            else:
                d_filtered_df = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Unsuccessful')]
                d_filtered_df1 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Successful')]
                d_filtered_df2 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['04. Rating'] == 'Neutral')]
                d_tr_df = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Unsuccessful')]
                d_tr_df1 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Successful')]
                d_tr_df2 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['04. Rating'] == 'Neutral')]
                d_sp_df = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Unsuccessful')]
                d_sp_df1 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Successful')]
                d_sp_df2 = df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['04. Rating'] == 'Neutral')]
                d_total1=d_filtered_df['04. Rating'].str.count('Unsuccessful').sum()+d_filtered_df1['04. Rating'].str.count('Successful').sum()+d_filtered_df2['04. Rating'].str.count('Neutral').sum()
                d_total2=d_tr_df['04. Rating'].str.count('Unsuccessful').sum()+d_tr_df1['04. Rating'].str.count('Successful').sum()+d_tr_df2['04. Rating'].str.count('Neutral').sum()
                d_total3=d_sp_df['04. Rating'].str.count('Unsuccessful').sum()+d_sp_df1['04. Rating'].str.count('Successful').sum()+d_sp_df2['04. Rating'].str.count('Neutral').sum()
                if 'Time Period' in df:
                    d_time_15=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='0 - 15 min')]
                    d_time_30=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='16 - 30 min')]
                    d_time_45=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='31 - 45 min')]
                    d_time_60=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='46 - 60 min')]
                    d_time_75=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='61 - 75 min')]
                    d_time_90=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Established Play') & (df['Time Period']=='76 - 90 min')]

                    d_time_15_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='0 - 15 min')]
                    d_time_30_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='16 - 30 min')]
                    d_time_45_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='31 - 45 min')]
                    d_time_60_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='46 - 60 min')]
                    d_time_75_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='61 - 75 min')]
                    d_time_90_tr=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'] == 'Transition') & (df['Time Period']=='76 - 90 min')]

                    d_time_15_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='0 - 15 min')]
                    d_time_30_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='16 - 30 min')]
                    d_time_45_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='31 - 45 min')]
                    d_time_60_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='46 - 60 min')]
                    d_time_75_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='61 - 75 min')]
                    d_time_90_sp=df.loc[(df['Row'] == 'D4 Defending the Box') & (df['01. Phase'].isin(['Corner Kick', 'Direct Free Kick','Lateral Free Kick','Throw In'])) & (df['Time Period']=='76 - 90 min')]
                else:
                    d_time_15=0
                    d_time_30=0
                    d_time_45=0
                    d_time_60=0
                    d_time_75=0
                    d_time_90=0

                    d_time_15_tr=0
                    d_time_30_tr=0
                    d_time_45_tr=0
                    d_time_60_tr=0
                    d_time_75_tr=0
                    d_time_90_tr=0

                    d_time_15_sp=0
                    d_time_30_sp=0
                    d_time_45_sp=0
                    d_time_60_sp=0
                    d_time_75_sp=0
                    d_time_90_sp=0
            d_us_ep.append(d_filtered_df['04. Rating'].str.count('Unsuccessful').sum())
            d_s_ep.append(d_filtered_df1['04. Rating'].str.count('Successful').sum())
            d_n_ep.append(d_filtered_df2['04. Rating'].str.count('Neutral').sum())
            d_us_tr.append(d_tr_df['04. Rating'].str.count('Unsuccessful').sum())
            d_s_tr.append(d_tr_df1['04. Rating'].str.count('Successful').sum())
            d_n_tr.append(d_tr_df2['04. Rating'].str.count('Neutral').sum())
            d_us_sp.append(d_sp_df['04. Rating'].str.count('Unsuccessful').sum())
            d_s_sp.append(d_sp_df1['04. Rating'].str.count('Successful').sum())
            d_n_sp.append(d_sp_df2['04. Rating'].str.count('Neutral').sum())
            d_total_ep.append(d_total1)
            d_total_tr.append(d_total2)
            d_total_sp.append(d_total3)
            if 'Time Period' in df:
                d_tp1.append(d_time_15['Time Period'].str.count('0 - 15 min').sum())
                d_tp2.append(d_time_30['Time Period'].str.count('16 - 30 min').sum())
                d_tp3.append(d_time_45['Time Period'].str.count('31 - 45 min').sum())
                d_tp4.append(d_time_60['Time Period'].str.count('46 - 60 min').sum())
                d_tp5.append(d_time_75['Time Period'].str.count('61 - 75 min').sum())
                d_tp6.append(d_time_90['Time Period'].str.count('76 - 90 min').sum())

                d_tp_tr1.append(d_time_15_tr['Time Period'].str.count('0 - 15 min').sum())
                d_tp_tr2.append(d_time_30_tr['Time Period'].str.count('16 - 30 min').sum())
                d_tp_tr3.append(d_time_45_tr['Time Period'].str.count('31 - 45 min').sum())
                d_tp_tr4.append(d_time_60_tr['Time Period'].str.count('46 - 60 min').sum())
                d_tp_tr5.append(d_time_75_tr['Time Period'].str.count('61 - 75 min').sum())
                d_tp_tr6.append(d_time_90_tr['Time Period'].str.count('76 - 90 min').sum())

                d_tp_sp1.append(d_time_15_sp['Time Period'].str.count('0 - 15 min').sum())
                d_tp_sp2.append(d_time_30_sp['Time Period'].str.count('16 - 30 min').sum())
                d_tp_sp3.append(d_time_45_sp['Time Period'].str.count('31 - 45 min').sum())
                d_tp_sp4.append(d_time_60_sp['Time Period'].str.count('46 - 60 min').sum())
                d_tp_sp5.append(d_time_75_sp['Time Period'].str.count('61 - 75 min').sum())
                d_tp_sp6.append(d_time_90_sp['Time Period'].str.count('76 - 90 min').sum())
            else:
                d_tp1.append(0)
                d_tp2.append(0)
                d_tp3.append(0)
                d_tp4.append(0)
                d_tp5.append(0)
                d_tp6.append(0)

                d_time_15_tr=0
                d_time_30_tr=0
                d_time_45_tr=0
                d_time_60_tr=0
                d_time_75_tr=0
                d_time_90_tr=0

                d_time_15_sp=0
                d_time_30_sp=0
                d_time_45_sp=0
                d_time_60_sp=0
                d_time_75_sp=0
                d_time_90_sp=0
            
        else:
            d_us_ep.append(0)
            d_s_ep.append(0)
            d_n_ep.append(0)
            d_us_tr.append(0)
            d_s_tr.append(0)
            d_n_tr.append(0)
            d_us_sp.append(0)
            d_s_sp.append(0)
            d_n_sp.append(0)
            d_total_ep.append(0)
            d_total_tr.append(0)
            d_total_sp.append(0)
            d_tp1.append(0)
            d_tp2.append(0)
            d_tp3.append(0)
            d_tp4.append(0)
            d_tp5.append(0)
            d_tp6.append(0)
            d_time_15_tr=0
            d_time_30_tr=0
            d_time_45_tr=0
            d_time_60_tr=0
            d_time_75_tr=0
            d_time_90_tr=0

            d_time_15_sp=0
            d_time_30_sp=0
            d_time_45_sp=0
            d_time_60_sp=0
            d_time_75_sp=0
            d_time_90_sp=0
    denominator=len(d_files)
    d_ep_avg_1=sum(d_tp1)/denominator
    d_ep_avg_2=sum(d_tp2)/denominator
    d_ep_avg_3=sum(d_tp3)/denominator
    d_ep_avg_4=sum(d_tp4)/denominator
    d_ep_avg_5=sum(d_tp5)/denominator
    d_ep_avg_6=sum(d_tp6)/denominator
    print(d_ep_avg_1)
    print(d_ep_avg_2)
    print(d_ep_avg_3)
    print(d_ep_avg_4)
    print(d_ep_avg_5)
    print(d_ep_avg_6)

    d_tr_avg_1=sum(d_tp_tr1)/denominator
    d_tr_avg_2=sum(d_tp_tr2)/denominator
    d_tr_avg_3=sum(d_tp_tr3)/denominator
    d_tr_avg_4=sum(d_tp_tr4)/denominator
    d_tr_avg_5=sum(d_tp_tr5)/denominator
    d_tr_avg_6=sum(d_tp_tr6)/denominator

    d_sp_avg_1=sum(d_tp_sp1)/denominator
    d_sp_avg_2=sum(d_tp_sp2)/denominator
    d_sp_avg_3=sum(d_tp_sp3)/denominator
    d_sp_avg_4=sum(d_tp_sp4)/denominator
    d_sp_avg_5=sum(d_tp_sp5)/denominator
    d_sp_avg_6=sum(d_tp_sp6)/denominator

    d_ep_table=[]
    
    d_ep_table.append(d_ep_avg_1)
    d_ep_table.append(d_ep_avg_2)
    d_ep_table.append(d_ep_avg_3)
    d_ep_table.append(d_ep_avg_4)
    d_ep_table.append(d_ep_avg_5)
    d_ep_table.append(d_ep_avg_6)
    print(d_ep_table)
    
    d_tr_table=[]
    d_tr_table.append(d_tr_avg_1)
    d_tr_table.append(d_tr_avg_2)
    d_tr_table.append(d_tr_avg_3)
    d_tr_table.append(d_tr_avg_4)
    d_tr_table.append(d_tr_avg_5)
    d_tr_table.append(d_tr_avg_6)
    print(d_tr_table)

    d_sp_table=[]
    d_sp_table.append(d_sp_avg_1)
    d_sp_table.append(d_sp_avg_2)
    d_sp_table.append(d_sp_avg_3)
    d_sp_table.append(d_sp_avg_4)
    d_sp_table.append(d_sp_avg_5)
    d_sp_table.append(d_sp_avg_6)
    print(d_sp_table)
    
    d_epO4=pd.DataFrame({'Unsuccessful':d_us_ep,'Successful':d_s_ep,'Neutral':d_n_ep,'Total':d_total_ep})
    d_spO4=pd.DataFrame({'Unsuccessful':d_us_sp,'Successful':d_s_sp,'Neutral':d_n_sp,'Total':d_total_sp})
    d_trO4=pd.DataFrame({'Unsuccessful':d_us_tr,'Successful':d_s_tr,'Neutral':d_n_tr,'Total':d_total_tr})

    d_final = pd.concat([d_epO4, d_trO4, d_spO4], axis=1, keys=['Established Play', 'Transition', 'Set Pieces'], )
    d_final.index.name = 'Matchday'
    d_final.index += 1

    conc = {'ep': d_ep_table, 'tr': d_tr_table, 'sp': d_sp_table}
    d_jtable = pd.DataFrame(conc)
    for i in range(1, 6):
        d_jtable.iloc[i] = [d_ep_table[i], d_tr_table[i], d_sp_table[i]]

    return d_ep_table,d_tr_table,d_sp_table,d_final,d_jtable

def table_page():
    ep_table,tr_table,sp_table,final,jtable=avg_calculations()
    set_png_as_page_bg("https://tactical-times.com/wp-content/uploads/2021/07/Untitled.png")
    st.write(final)
def main():
    st.title("Automated Report")
    # Upload a CSV file
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    set_png_as_page_bg("https://www.sgclark.com/blog/wp-content/uploads/europe_soccer_danish_fc_nordsjaelland_home-2048x1152.png")

    if csv_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Create a page navigation sidebar
        page = st.sidebar.selectbox("Select a page", ("Match Details", "Finishing & Defending", "15-Minutes O4 & D4 from phases", "O4 Table"))

        # Display the selected page
        if page == "Match Details":
            overview_page(df)
        elif page == "Finishing & Defending":
            statistics_page(df)
        elif page == "15-Minutes O4 & D4 from phases":
            visualization_page(df)
        elif page == "O4 Table":
            table_page()


if __name__ == "__main__":
    main()










