import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Add the custom CSS styles
st.markdown('<link href="https://github.com/Vangelis19/Streamlit/styles.css" rel="stylesheet">', unsafe_allow_html=True)
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
    print(NF)

    SD=Defending['04. Rating'].value_counts().get('Successful', 0)
    UD=Defending['04. Rating'].value_counts().get('Unsuccessful', 0)
    ND=Defending['04. Rating'].value_counts().get('Neutral', 0)
    print(ND)
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

def time_period(df):
    Finishing,Defending=chances(df)
    if 'Time Period' in df.columns:
        #15-Minutes periods:
        Reading = Finishing[Finishing['Time Period'] == '0 - 15 min']
        Reading = Reading.reset_index(drop=True)
        Reacting = Finishing[Finishing['Time Period'] == '16 - 30 min']
        Reacting = Reacting.reset_index(drop=True)
        Acting_1= Finishing[Finishing['Time Period'] == '31 - 45 min']
        Acting_1 = Acting_1.reset_index(drop=True)
        Trap_1=Finishing[Finishing['Time Period'] == '45+ min']
        Trap_1 = Trap_1.reset_index(drop=True)
        Breathe=Finishing[Finishing['Time Period'] == '46 - 60 min']
        Breathe = Breathe.reset_index(drop=True)
        Refresh=Finishing[Finishing['Time Period'] == '61 - 75 min']
        Refresh = Refresh.reset_index(drop=True)
        Acting_2=Finishing[Finishing['Time Period'] == '76 - 90 min']
        Acting_2 = Acting_2.reset_index(drop=True)
        Trap_2=Finishing[Finishing['Time Period'] == '90+ min']
        Trap_2 = Trap_2.reset_index(drop=True)
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
        #45+:
        Trp1_ep=Trap_1[Trap_1['01. Phase']=='Established Play']
        Trp1_ep = Trp1_ep.reset_index(drop=True)
        EP45_=Trp1_ep['01. Phase'].value_counts().get('Established Play', 0)
        Trp1_tr=Trap_1[Trap_1['01. Phase']=='Transition']
        Trp1_tr = Trp1_tr.reset_index(drop=True)
        TR45_=Trp1_ep['01. Phase'].value_counts().get('Transition', 0)
        Trp1_sp = pd.DataFrame(columns=Trap_1.columns)
        Trp1_sp = Trp1_sp.reset_index(drop=True)
        SP45_ = 0

        for i in range(len(Trap_1)):
            if (Trap_1['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Trp1_sp = Trp1_sp.append(Trap_1.iloc[i])
                SP45_ += 1
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
        #90+:
        Trp2_ep=Trap_2[Trap_2['01. Phase']=='Established Play']
        Trp2_ep = Trp2_ep.reset_index(drop=True)
        EP90_=Trp2_ep['01. Phase'].value_counts().get('Established Play', 0)
        Trp2_tr=Trap_2[Trap_2['01. Phase']=='Transition']
        Trp2_tr = Trp2_tr.reset_index(drop=True)
        TR90_=Trp2_ep['01. Phase'].value_counts().get('Transition', 0)
        Trp2_sp = pd.DataFrame(columns=Trap_2.columns)
        Trp2_sp = Trp2_sp.reset_index(drop=True)
        SP90_ = 0

        for i in range(len(Trap_2)):
            if (Trap_2['01. Phase'][i] in ['Throw In', 'Lateral Free Kick', 'Corner Kick', 'Free Kick', 'Penalty', 'Direct Free Kick']):
                Trp2_sp = Trp2_sp.append(Trap_2.iloc[i])
                SP90_ += 1
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

        SEP45_=Trp1_ep['04. Rating'].value_counts().get('Successful', 0)
        STR45_=Trp1_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP45_=Trp1_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP46_60=Br_ep['04. Rating'].value_counts().get('Successful', 0)
        STR46_60=Br_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP46_60=Br_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP61_75=Re_ep['04. Rating'].value_counts().get('Successful', 0)
        STR61_75=Re_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP61_75=Re_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP76_90=Act2_ep['04. Rating'].value_counts().get('Successful', 0)
        STR76_90=Act2_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP76_90=Act2_sp['04. Rating'].value_counts().get('Successful', 0)

        SEP90_=Trp2_ep['04. Rating'].value_counts().get('Successful', 0)
        STR90_=Trp2_tr['04. Rating'].value_counts().get('Successful', 0)
        SSP90_=Trp2_sp['04. Rating'].value_counts().get('Successful', 0)

        return (EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,
                SP16_30,EP31_45,TR31_45,SP31_45,EP45_,
                TR45_,SP45_,EP46_60,TR46_60,SP46_60,
                EP61_75,TR61_75,SP61_75,EP76_90,TR76_90,
                SP76_90,EP90_,TR90_,SP90_,SEP0_15,
                STR0_15,SSP0_15,SEP16_30,STR16_30,SSP16_30,
                SEP31_45,STR31_45,SSP31_45,SEP45_,STR45_,
                SSP45_,SEP46_60,STR46_60,SSP46_60,SEP61_75,
                STR61_75,SSP61_75,SEP76_90,STR76_90,SSP76_90,
                SEP90_,STR90_,SSP90_)
    else:
        return None
    


    

def overview_page(df):
    st.subheader("Match Details")
    st.write("Information about the game and pics")
    st.write("Sunday 14/05/2023 19:00")
    

def statistics_page(df):
    st.subheader("Finishing & Defending")
    st.write("This is the statistics page.")

    SF,UF,NF,SD,UD,ND,A_SEp,A_UEp,A_NEp,A_ST,A_UT,A_NT,A_SSp,A_USp,A_NSp,D_SEp,D_UEp,D_NEp,D_ST,D_UT,D_NT,D_SSp,D_USp,D_NSp=O4_D4(df)
    print('succesful ep:',A_SEp)
    print('neutra tr:',A_NT)
    print('unsuccesful sp:',A_USp)

    # Create two columns for the charts
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display the first chart in the first column
    with col1:
        categories1 = ['Succesful', 'Unsuccessful', 'Neutral']
        values1 = [SF, UF, NF]

        # Plotting the bar chart
        fig, ax = plt.subplots(figsize=(8, 6.25))
        ax.bar(categories1, values1, color='green', linewidth=2, edgecolor='black')

        for i in range(len(categories1) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max(values1)], linestyle='dotted', color='gray')

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
        ax.bar(categories2, values2, color='red', linewidth=2, edgecolor='black')

        for i in range(len(categories2) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, max(values2)], linestyle='dotted', color='gray')

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
        colors = ['green', 'red', 'grey']

        # Create a stacked bar chart
        fig3, ax = plt.subplots(figsize=(8, 6.25))

        # Iterate over phases and create stacked bars with custom colors, thicker line width, and outer line color
        bottom = np.zeros(len(categories))
        for i, rating in enumerate(Ratings):
            ax.bar(categories, values[i], bottom=bottom, label=rating, color=colors[i], linewidth=2, edgecolor='black')
            # Add phase names and values as text annotations inside the bars
            for j, val in enumerate(values[i]):
                if val != 0:  # Exclude displaying value if it is 0
                    ax.text(j, bottom[j] + val / 2, f'{rating}: {val}', ha='center', va='center', color='white')
            bottom += values[i]
        a=A_SEp+A_NEp+A_UEp
        for i in range(len(categories1) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, a], linestyle='dotted', color='gray')

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
        colors = ['green', 'red', 'grey']

        # Create a stacked bar chart
        fig4, ax = plt.subplots(figsize=(8, 6))

        # Iterate over phases and create stacked bars with custom colors, thicker line width, and outer line color
        bottom = np.zeros(len(Phases))
        for i, rating in enumerate(Ratings):
            ax.bar(Phases, values[i], bottom=bottom, label=rating, color=colors[i], linewidth=2, edgecolor='black')
            # Add phase names and values as text annotations inside the bars
            for j, val in enumerate(values[i]):
                if val != 0:  # Exclude displaying value if it is 0
                    ax.text(j, bottom[j] + val / 2, f'{rating}: {val}', ha='center', va='center', color='white')
            bottom += values[i]
        b=D_SEp+D_NEp+D_UEp
        for i in range(len(Phases) - 1):
            line_x = i + 0.5  # x-coordinate of the line (adjust as needed)

            # Plotting the dotted line
            ax.plot([line_x, line_x], [0, b], linestyle='dotted', color='gray')

        # Set the chart title and labels
        ax.set_title('Defending by phases')
        ax.set_xlabel('Phases', labelpad=25)

        # Add a legend
        ax.legend()

        # Display the chart in Streamlit
        st.pyplot(fig4)


    

def visualization_page(df):
    st.subheader("Quarters")
    st.write("This is the visualization page.")
    column = time_period(df)
    if 'Time Period' in df.columns:
        EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,SP16_30,EP31_45,TR31_45,SP31_45,EP45_,TR45_,SP45_,EP46_60,TR46_60,SP46_60,EP61_75,TR61_75,SP61_75,EP76_90,TR76_90,SP76_90,EP90_,TR90_,SP90_,SEP0_15,STR0_15,SSP0_15,SEP16_30,STR16_30,SSP16_30,SEP31_45,STR31_45,SSP31_45,SEP45_,STR45_,SSP45_,SEP46_60,STR46_60,SSP46_60,SEP61_75,STR61_75,SSP61_75,SEP76_90,STR76_90,SSP76_90,SEP90_,STR90_,SSP90_=time_period(df)
        # Define the time periods
        time_periods = ['0-15', '16-30', '31-45', '45+', '46-60', '61-75', '76-90', '90+']

        # Define the situations
        situations = ['Established Play', 'Transition', 'Set Piece']

        # Sample data for situation counts
        situation_counts = np.array([[EP0_15, TR0_15, SP0_15],
                                    [EP16_30, TR16_30, SP16_30],
                                    [EP31_45, TR31_45, SP31_45],
                                    [EP45_, TR45_, SP45_],
                                    [EP46_60, TR46_60, SP46_60],
                                    [EP61_75, TR61_75, SP61_75],
                                    [EP76_90, TR76_90, SP76_90],
                                    [EP90_, TR90_, SP90_]])

        # Set up the chart
        fig, ax = plt.subplots()

        # Calculate the width for each bar
        bar_width = 0.2

        # Set the positions of the bars on the x-axis
        bar_positions = np.arange(len(time_periods))

        colors = ['purple', 'black', 'red']

        # Create a bar for each situation
        for i, situation in enumerate(situations):
            # Set the x-position for the bars of each situation
            situation_positions = [pos + i * bar_width for pos in bar_positions]

            # Get the counts for the current situation
            counts = situation_counts[:, i]

            # Create the bar for the situation
            bar = ax.bar(situation_positions, counts, bar_width, label=situation, color=colors[i], linewidth=2, edgecolor='black')
        c=max(EP0_15,EP16_30,EP31_45,EP46_60,EP61_75,EP76_90)
        for i in range(len(time_periods) - 1):
                line_x = i + 0.75  # x-coordinate of the line (adjust as needed)

                # Plotting the dotted line
                ax.plot([line_x, line_x], [0, c], linestyle='dotted', color='gray')

            

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


    

def main():
    st.title("Automated Report")
    # Upload a CSV file
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Create a page navigation sidebar
        page = st.sidebar.selectbox("Select a page", ("Match Details", "Finishing & Defending", "15-Minutes O4 from phases"))

        # Display the selected page
        if page == "Match Details":
            overview_page(df)
        elif page == "Finishing & Defending":
            statistics_page(df)
        elif page == "15-Minutes O4 from phases":
            visualization_page(df)


if __name__ == "__main__":
    main()










