import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def O4_D4(df):
    #O4 & D4-Total Dataframes
    Finishing = df[df['code'] == 'O4 Finishing']
    Finishing = Finishing.reset_index(drop=True)
    Defending = df[df['code'] == 'D4 Defending the Box']
    Defending = Defending.reset_index(drop=True)

    #Attacking Phases Dataframes
    a_est=Finishing[Finishing['01. Phase'] == 'Established Play']
    a_est = a_est.reset_index(drop=True)
    a_tr=Finishing[Finishing['01. Phase'] == 'Transition']
    a_tr = a_tr.reset_index(drop=True)
    a_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Finishing)):
        if Finishing['01. Phase'][i]=='Throw In' or Finishing['01. Phase'][i]=='Lateral Free Kick' or Finishing['01. Phase'][i]=='Corner Kick' or Finishing['01. Phase'][i]=='Free Kick' or Finishing['01. Phase'][i]=='Penalty' or Finishing['01. Phase'][i]=='Direct Free Kick':
            a_sp = pd.concat([a_sp, Finishing.iloc[i]])
    a_sp = a_sp.reset_index(drop=True)
    #Defensive Phases Dataframes
    d_est=Defending[Defending['01. Phase'] == 'Established Play']
    d_est = d_est.reset_index(drop=True)
    d_tr=Defending[Defending['01. Phase'] == 'Transition']
    d_tr = d_tr.reset_index(drop=True)
    d_sp=pd.DataFrame(columns=Defending.columns)
    for i in range(len(Defending)):
        if Defending['01. Phase'][i]=='Throw In' or Defending['01. Phase'][i]=='Lateral Free Kick' or Defending['01. Phase'][i]=='Corner Kick' or Defending['01. Phase'][i]=='Free Kick' or Defending['01. Phase'][i]=='Penalty' or Defending['01. Phase'][i]=='Direct Free Kick':
           d_sp = pd.concat([d_sp, Defending.iloc[i]])
    d_sp = d_sp.reset_index(drop=True)

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
    #15-Minutes periods:
    Finishing = df[df['code'] == 'O4 Finishing']
    Finishing = Finishing.reset_index(drop=True)
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
    Read_tr=Reading[Reading['01. Phase']=='Transition']
    Read_tr = Read_tr.reset_index(drop=True)
    Read_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Reading)):
        if Reading['01. Phase'][i]=='Throw In' or Reading['01. Phase'][i]=='Lateral Free Kick' or Reading['01. Phase'][i]=='Corner Kick' or Reading['01. Phase'][i]=='Free Kick' or Reading['01. Phase'][i]=='Penalty' or Reading['01. Phase'][i]=='Direct Free Kick':
           Read_sp = pd.concat([Read_sp, Reading.iloc[i]])
    Read_sp = Read_sp.reset_index(drop=True)
    #16-30:
    React_ep=Reacting[Reacting['01. Phase']=='Established Play']
    React_ep = React_ep.reset_index(drop=True)
    React_tr=Reacting[Reacting['01. Phase']=='Transition']
    React_tr = React_tr.reset_index(drop=True)
    React_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Reacting)):
        if Reacting['01. Phase'][i]=='Throw In' or Reacting['01. Phase'][i]=='Lateral Free Kick' or Reacting['01. Phase'][i]=='Corner Kick' or Reacting['01. Phase'][i]=='Free Kick' or Reacting['01. Phase'][i]=='Penalty' or Reacting['01. Phase'][i]=='Direct Free Kick':
           React_sp = pd.concat([React_sp, Reacting.iloc[i]])
    React_sp = React_sp.reset_index(drop=True)
    #31-45:
    Act1_ep=Acting_1[Acting_1['01. Phase']=='Established Play']
    Act1_ep = Act1_ep.reset_index(drop=True)
    Act1_tr=Acting_1[Acting_1['01. Phase']=='Transition']
    Act1_tr = Act1_tr.reset_index(drop=True)
    Act1_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Acting_1)):
        if Acting_1['01. Phase'][i]=='Throw In' or Acting_1['01. Phase'][i]=='Lateral Free Kick' or Acting_1['01. Phase'][i]=='Corner Kick' or Acting_1['01. Phase'][i]=='Free Kick' or Acting_1['01. Phase'][i]=='Penalty' or Acting_1['01. Phase'][i]=='Direct Free Kick':
           Act1_sp = pd.concat([Act1_sp, Acting_1.iloc[i]])
    Act1_sp = Act1_sp.reset_index(drop=True)
    #45+:
    Trp1_ep=Trap_1[Trap_1['01. Phase']=='Established Play']
    Trp1_ep = Trp1_ep.reset_index(drop=True)
    Trp1_tr=Trap_1[Trap_1['01. Phase']=='Transition']
    Trp1_tr = Trp1_tr.reset_index(drop=True)
    Trp1_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Trap_1)):
        if Trap_1['01. Phase'][i]=='Throw In' or Trap_1['01. Phase'][i]=='Lateral Free Kick' or Trap_1['01. Phase'][i]=='Corner Kick' or Trap_1['01. Phase'][i]=='Free Kick' or Trap_1['01. Phase'][i]=='Penalty' or Trap_1['01. Phase'][i]=='Direct Free Kick':
           Trp1_sp = pd.concat([Trp1_sp, Trap_1.iloc[i]])
    Trp1_sp = Trp1_sp.reset_index(drop=True)
    #46-60:
    Br_ep=Breathe[Breathe['01. Phase']=='Established Play']
    Br_ep = Br_ep.reset_index(drop=True)
    Br_tr=Breathe[Breathe['01. Phase']=='Transition']
    Br_tr = Br_tr.reset_index(drop=True)
    Br_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Breathe)):
        if Breathe['01. Phase'][i]=='Throw In' or Breathe['01. Phase'][i]=='Lateral Free Kick' or Breathe['01. Phase'][i]=='Corner Kick' or Breathe['01. Phase'][i]=='Free Kick' or Breathe['01. Phase'][i]=='Penalty' or Breathe['01. Phase'][i]=='Direct Free Kick':
           Br_sp = pd.concat([Br_sp, Breathe.iloc[i]])
    Br_sp = Br_sp.reset_index(drop=True)
    #61-75:
    Re_ep=Refresh[Refresh['01. Phase']=='Established Play']
    Re_ep = Re_ep.reset_index(drop=True)
    Re_tr=Refresh[Refresh['01. Phase']=='Transition']
    Re_tr = Re_tr.reset_index(drop=True)
    Re_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Refresh)):
        if Refresh['01. Phase'][i]=='Throw In' or Refresh['01. Phase'][i]=='Lateral Free Kick' or Refresh['01. Phase'][i]=='Corner Kick' or Refresh['01. Phase'][i]=='Free Kick' or Refresh['01. Phase'][i]=='Penalty' or Refresh['01. Phase'][i]=='Direct Free Kick':
           Re_sp = pd.concat([Re_sp, Refresh.iloc[i]])
    Re_sp = Re_sp.reset_index(drop=True)
    #76-90:
    Act2_ep=Acting_2[Acting_2['01. Phase']=='Established Play']
    Act2_ep = Act2_ep.reset_index(drop=True)
    Act2_tr=Acting_2[Acting_2['01. Phase']=='Transition']
    Act2_tr = Act2_tr.reset_index(drop=True)
    Act2_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Acting_2)):
        if Acting_2['01. Phase'][i]=='Throw In' or Acting_2['01. Phase'][i]=='Lateral Free Kick' or Acting_2['01. Phase'][i]=='Corner Kick' or Acting_2['01. Phase'][i]=='Free Kick' or Acting_2['01. Phase'][i]=='Penalty' or Acting_2['01. Phase'][i]=='Direct Free Kick':
           Act2_sp = pd.concat([Act2_sp, Acting_2.iloc[i]])
    Act2_sp = Act2_sp.reset_index(drop=True)
    #90+:
    Trp2_ep=Trap_2[Trap_2['01. Phase']=='Established Play']
    Trp2_ep = Trp2_ep.reset_index(drop=True)
    Trp2_tr=Trap_2[Trap_2['01. Phase']=='Transition']
    Trp2_tr = Trp2_tr.reset_index(drop=True)
    Trp2_sp=pd.DataFrame(columns=Finishing.columns)
    for i in range(len(Trap_2)):
        if Trap_2['01. Phase'][i]=='Throw In' or Trap_2['01. Phase'][i]=='Lateral Free Kick' or Trap_2['01. Phase'][i]=='Corner Kick' or Trap_2['01. Phase'][i]=='Free Kick' or Trap_2['01. Phase'][i]=='Penalty' or Trap_2['01. Phase'][i]=='Direct Free Kick':
           Trp2_sp = pd.concat([Trp2_sp, Trap_2.iloc[i]])
    Trp2_sp = Trp2_sp.reset_index(drop=True)
    #Page2:
    EP0_15=Read_ep['04. Rating'].value_counts().get('Successful', 0)
    TR0_15=Read_tr['04. Rating'].value_counts().get('Successful', 0)
    SP0_15=Read_sp['04. Rating'].value_counts().get('Successful', 0)

    EP16_30=React_ep['04. Rating'].value_counts().get('Successful', 0)
    TR16_30=React_tr['04. Rating'].value_counts().get('Successful', 0)
    SP16_30=React_sp['04. Rating'].value_counts().get('Successful', 0)

    EP31_45=Act1_ep['04. Rating'].value_counts().get('Successful', 0)
    TR31_45=Act1_tr['04. Rating'].value_counts().get('Successful', 0)
    SP31_45=Act1_sp['04. Rating'].value_counts().get('Successful', 0)

    EP45_=Trp1_ep['04. Rating'].value_counts().get('Successful', 0)
    TR45_=Trp1_tr['04. Rating'].value_counts().get('Successful', 0)
    SP45_=Trp1_sp['04. Rating'].value_counts().get('Successful', 0)

    EP46_60=Br_ep['04. Rating'].value_counts().get('Successful', 0)
    TR46_60=Br_tr['04. Rating'].value_counts().get('Successful', 0)
    SP46_60=Br_sp['04. Rating'].value_counts().get('Successful', 0)

    EP61_75=Re_ep['04. Rating'].value_counts().get('Successful', 0)
    TR61_75=Re_tr['04. Rating'].value_counts().get('Successful', 0)
    SP61_75=Re_sp['04. Rating'].value_counts().get('Successful', 0)

    EP76_90=Act2_ep['04. Rating'].value_counts().get('Successful', 0)
    TR76_90=Act2_tr['04. Rating'].value_counts().get('Successful', 0)
    SP76_90=Act2_sp['04. Rating'].value_counts().get('Successful', 0)

    EP90_=Trp2_ep['04. Rating'].value_counts().get('Successful', 0)
    TR90_=Trp2_tr['04. Rating'].value_counts().get('Successful', 0)
    SP90_=Trp2_sp['04. Rating'].value_counts().get('Successful', 0)

    return (EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,SP16_30,EP31_45,TR31_45,SP31_45,EP45_,TR45_,SP45_,EP46_60,TR46_60,SP46_60,EP61_75,TR61_75,
            SP61_75,EP76_90,TR76_90,SP76_90,EP90_,TR90_,SP90_)


    

def overview_page(df):
    st.subheader("Match Details")
    st.write("AGF vs FCN")
    st.write("Sunday 14/05/2023 19:00")
    image = Image.open("C:/Users/vangj/Desktop/fcn.png")

    # Display the image on the Streamlit report
    st.image(image, caption='Your Image', use_column_width=True)

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
    EP0_15,TR0_15,SP0_15,EP16_30,TR16_30,SP16_30,EP31_45,TR31_45,SP31_45,EP45_,TR45_,SP45_,EP46_60,TR46_60,SP46_60,EP61_75,TR61_75,SP61_75,EP76_90,TR76_90,SP76_90,EP90_,TR90_,SP90_=time_period(df)
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

    # Create a bar for each situation
    for i, situation in enumerate(situations):
        # Set the x-position for the bars of each situation
        situation_positions = [pos + i * bar_width for pos in bar_positions]

        # Get the counts for the current situation
        counts = situation_counts[:, i]

        # Create the bar for the situation
        bar = ax.bar(situation_positions, counts, bar_width, label=situation)

        # Connect the top points of bars for each situation with lines
        x_coords = [rect.get_x() + rect.get_width() / 2 for rect in bar]
        y_coords = [rect.get_height() for rect in bar]
        color = bar[0].get_facecolor()  # Get the color of the bars
        ax.plot(x_coords, y_coords, marker='o', color=color)

    # Set labels and title
    ax.set_xlabel('Time Periods')
    ax.set_ylabel('Count')
    ax.set_title('Situations by Time Period')

    # Set the x-axis ticks and labels
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(time_periods)

    # Add a legend
    ax.legend()

    # Remove the extra whitespace from the figure
    plt.tight_layout()

    # Convert the Matplotlib figure to a Streamlit figure
    st.pyplot(fig)

    


def fourth_page(df):
    st.subheader("15 Minutes periods")
    st.write("This is the visualization page.")
    FFH,FSH,FT,DFH,DSH,DT=O4_D4(df)


    

def fifth_page(df):
    st.subheader("2022/2023 Finishing table")
    st.write("This is the visualization page.")
    column = st.selectbox("Select a column for bar chart", df.columns)
    st.bar_chart(df[column])
    

def main():
    st.title("Automated Report")
    # Upload a CSV file
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if csv_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Create a page navigation sidebar
        page = st.sidebar.selectbox("Select a page", ("Match Details", "Finishing & Defending", "Finishing efficiency","15 Minutes periods","2022/2023 Finishing table"))

        # Display the selected page
        if page == "Match Details":
            overview_page(df)
        elif page == "Finishing & Defending":
            statistics_page(df)
        elif page == "Finishing efficiency":
            visualization_page(df)
        elif page == "15 Minutes periods":
            fourth_page(df)
        elif page == "2022/2023 Finishing table":
            visualization_page(df)

if __name__ == "__main__":
    main()










