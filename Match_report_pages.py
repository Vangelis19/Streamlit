import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def analysis(df):
    #O4 & D4-Total Dataframe
    Finishing = df[df['code'] == 'O4 Finishing']
    Defending = df[df['code'] == 'D4 Defending the Box']

    #1st and 2nd half O4 & D4 Dataframe
    FH_finishing = Finishing[Finishing['Half'] == '1st Half']
    SH_finishing= Finishing[Finishing['Half'] == '2nd Half']
    FH_defending = Defending[Defending['Half'] == '1st Half']
    SH_defending= Defending[Defending['Half'] == '2nd Half']

    #O4 & D4 Total values
    FT = Finishing['code'].value_counts().get('O4 Finishing', 0)
    DT = Defending['code'].value_counts()['D4 Defending the Box']

    #1st & 2nd O4 & D4
    FFH=Finishing['Half'].value_counts().get('1st Half', 0)
    FSH=Finishing['Half'].value_counts().get('2nd Half', 0)
    DFH=Defending['Half'].value_counts()['1st Half']
    DSH=Defending['Half'].value_counts().get('2nd Half', 0)

    #Events O4
    normal_att = Finishing[Finishing['01. Phase'] == 'Established Play']
    trans_att = Finishing[Finishing['01. Phase'] == 'Transition']
    set_att1 = Finishing[Finishing['01. Phase'] == 'Corner Kick']
    set_att2 = Finishing[Finishing['01. Phase'] == 'Lateral Free Kick']
    set_att3 = Finishing[Finishing['01. Phase'] == 'Throw In']
    set_att=pd.concat([set_att1,set_att2,set_att3])


    #Events D4
    normal_def = Defending[Defending['01. Phase'] == 'Established Play']
    trans_def = Defending[Defending['01. Phase'] == 'Transition']
    set_def1 = Defending[Defending['01. Phase'] == 'Corner Kick']
    set_def2 = Defending[Defending['01. Phase'] == 'Lateral Free Kick']
    set_def3 = Defending[Defending['01. Phase'] == 'Throw In']
    set_def4 = Defending[Defending['01. Phase'] == 'Direct Free Kick']
    set_def=pd.concat([set_def1,set_def2,set_def3, set_def4])
    
    #counting occurence of events (attacking transition and established play for O4 & D4)
    Attacking_transition=Finishing['01. Phase'].value_counts().get('Transition', 0)
    Established_play_A=Finishing['01. Phase'].value_counts().get('Established Play', 0)
    Defending_transition=Defending['01. Phase'].value_counts()['Transition']
    Established_play_D=Defending['01. Phase'].value_counts().get('Established Play', 0)

    #counters for finishing & defending and calculation of the set pieces for O4 & D4
    Finishing_times=len(Finishing)
    Set_piece_att=Finishing_times-Attacking_transition-Established_play_A
    Defending_times=len(Defending)
    Set_piece_def=Defending_times-Defending_transition-Established_play_D

    #stats and calculations for successful/unsuccessful D4
    Successful_defending=Defending['04. Rating'].value_counts().get('Successful', 0)
    
    """#stats and calculations for successful/unsuccessful O4
    Successful_finishing=Finishing['04. Rating'].value_counts()['Successful']
    Unsuccessful_finishing=Finishing['04. Rating'].value_counts()['Unsuccessful']
    Neutral_result_O=Finishing['04. Rating'].value_counts()['Neutral']"""

    # Stats and calculations for successful/unsuccessful O4
    Successful_finishing = normal_att['04. Rating'].value_counts().get('Successful', 0)
    # Stats and calculations for successful/unsuccessful O4
    Successful_finishing1 = trans_att['04. Rating'].value_counts().get('Successful', 0)
    # Stats and calculations for successful/unsuccessful O4
    Successful_trdef = trans_def['04. Rating'].value_counts().get('Successful', 0)

    
    """#time period stats finishing-defending
    Finish_0_15=Finishing['Time Period'].value_counts()['0 - 15 min']
    Finish_16_30=Finishing['Time Period'].value_counts()['16 - 30 min']
    Finish_31_45=Finishing['Time Period'].value_counts()['31 - 45 min']
    Finish_45only=Finishing['Time Period'].value_counts()['31 - 45 min']
    Finish_46_60=Finishing['Time Period'].value_counts()['46 - 60 min']
    Finish_61_75=Finishing['Time Period'].value_counts()['61 - 75 min']
    Finish_76_90=Finishing['Time Period'].value_counts()['76 - 90 min']

    Defend_0_15=Defending['Time Period'].value_counts()['0 - 15 min']
    Defend_16_30=Defending['Time Period'].value_counts()['16 - 30 min']
    Defend_31_45=Defending['Time Period'].value_counts()['31 - 45 min']
    Defend_45only=Finishing['Time Period'].value_counts()['31 - 45 min']
    Defend_46_60=Defending['Time Period'].value_counts()['46 - 60 min']
    Defend_61_75=Defending['Time Period'].value_counts()['61 - 75 min']
    Defend_76_90=Defending['Time Period'].value_counts()['76 - 90 min']"""

    #EPO4Succ=normal_att['04. Rating'].value_counts()['Successful']
    TrO4Succ=trans_att['04. Rating'].value_counts().get('Successful', 0)
    #SPO4Succ=set_att['04. Rating'].value_counts()['Successful']
    EPD4Succ=normal_def['04. Rating'].value_counts().get('Successful', 0)
    #TrD4Succ=trans_def['04. Rating'].value_counts()['Successful']
    SPD4Succ=set_def['04. Rating'].value_counts().get('Successful', 0)
    EPO4=Finishing['01. Phase'].value_counts().get('Established Play', 0)
    TrO4=Finishing['01. Phase'].value_counts().get('Transition', 0)
    SPO4=set_att['01. Phase'].value_counts().get('Throw In', 0)
    EPD4=Defending['01. Phase'].value_counts().get('Established Play', 0)
    TrD4=Defending['01. Phase'].value_counts().get('Transition', 0)
    SPD4=set_def['01. Phase'].value_counts().get('Throw In', 0)

    return FFH,FSH,FT,DFH,DSH,DT

def anal(df):
    #O4 & D4-Total Dataframe
    Finishing = df[df['code'] == 'O4 Finishing']
    Defending = df[df['code'] == 'D4 Defending the Box']

    #1st and 2nd half O4 & D4 Dataframe
    FH_finishing = Finishing[Finishing['Half'] == '1st Half']
    SH_finishing= Finishing[Finishing['Half'] == '2nd Half']
    FH_defending = Defending[Defending['Half'] == '1st Half']
    SH_defending= Defending[Defending['Half'] == '2nd Half']

    #O4 & D4 Total values
    FT = Finishing['code'].value_counts().get('O4 Finishing', 0)
    DT = Defending['code'].value_counts()['D4 Defending the Box']

    #1st & 2nd O4 & D4
    FFH=Finishing['Half'].value_counts().get('1st Half', 0)
    FSH=Finishing['Half'].value_counts().get('2nd Half', 0)
    DFH=Defending['Half'].value_counts()['1st Half']
    DSH=Defending['Half'].value_counts().get('2nd Half', 0)

    #Events O4
    normal_att = Finishing[Finishing['01. Phase'] == 'Established Play']
    trans_att = Finishing[Finishing['01. Phase'] == 'Transition']
    set_att1 = Finishing[Finishing['01. Phase'] == 'Corner Kick']
    set_att2 = Finishing[Finishing['01. Phase'] == 'Lateral Free Kick']
    set_att3 = Finishing[Finishing['01. Phase'] == 'Throw In']
    set_att=pd.concat([set_att1,set_att2,set_att3])


    #Events D4
    normal_def = Defending[Defending['01. Phase'] == 'Established Play']
    trans_def = Defending[Defending['01. Phase'] == 'Transition']
    set_def1 = Defending[Defending['01. Phase'] == 'Corner Kick']
    set_def2 = Defending[Defending['01. Phase'] == 'Lateral Free Kick']
    set_def3 = Defending[Defending['01. Phase'] == 'Throw In']
    set_def4 = Defending[Defending['01. Phase'] == 'Direct Free Kick']
    set_def=pd.concat([set_def1,set_def2,set_def3, set_def4])
    
    #counting occurence of events (attacking transition and established play for O4 & D4)
    Attacking_transition=Finishing['01. Phase'].value_counts().get('Transition', 0)
    Established_play_A=Finishing['01. Phase'].value_counts().get('Established Play', 0)
    Defending_transition=Defending['01. Phase'].value_counts()['Transition']
    Established_play_D=Defending['01. Phase'].value_counts().get('Established Play', 0)

    #counters for finishing & defending and calculation of the set pieces for O4 & D4
    Finishing_times=len(Finishing)
    Set_piece_att=Finishing_times-Attacking_transition-Established_play_A
    Defending_times=len(Defending)
    Set_piece_def=Defending_times-Defending_transition-Established_play_D

    #stats and calculations for successful/unsuccessful D4
    Successful_defending=Defending['04. Rating'].value_counts().get('Successful', 0)
    # Stats and calculations for successful/unsuccessful O4
    Successful_finishing = normal_att['04. Rating'].value_counts().get('Successful', 0)
    # Stats and calculations for successful/unsuccessful O4
    Successful_finishing1 = trans_att['04. Rating'].value_counts().get('Successful', 0)
    # Stats and calculations for successful/unsuccessful O4
    Successful_trdef = trans_def['04. Rating'].value_counts().get('Successful', 0)
    #EPO4Succ=normal_att['04. Rating'].value_counts()['Successful']
    TrO4Succ=trans_att['04. Rating'].value_counts().get('Successful', 0)
    #SPO4Succ=set_att['04. Rating'].value_counts()['Successful']
    EPD4Succ=normal_def['04. Rating'].value_counts().get('Successful', 0)
    #TrD4Succ=trans_def['04. Rating'].value_counts()['Successful']
    SPD4Succ=set_def['04. Rating'].value_counts().get('Successful', 0)
    EPO4=Finishing['01. Phase'].value_counts().get('Established Play', 0)
    TrO4=Finishing['01. Phase'].value_counts().get('Transition', 0)
    SPO4=set_att['01. Phase'].value_counts().get('Throw In', 0)
    EPD4=Defending['01. Phase'].value_counts().get('Established Play', 0)
    TrD4=Defending['01. Phase'].value_counts().get('Transition', 0)
    SPD4=set_def['01. Phase'].value_counts().get('Throw In', 0)
    return EPO4,TrO4,SPO4,EPD4,TrD4,SPD4,Successful_finishing,TrO4Succ,Successful_finishing1,EPD4Succ,Successful_trdef,SPD4Succ

def overview_page(df):
    st.subheader("Match Details")
    st.write("AGF vs FCN")
    st.write("Sunday 14/05/2023 19:00")
    image = Image.open("C:/Users/vangj/Desktop/1.png")

    # Display the image on the Streamlit report
    st.image(image, caption='Your Image', use_column_width=True)

def statistics_page(df):
    st.subheader("Finishing & Defending")
    st.write("This is the statistics page.")

    FFH,FSH,FT,DFH,DSH,DT=analysis(df)
    
    # Data for the chart
    categories = ['1st Half', '2nd Half', 'Total']
    values_positive = [FFH,FSH,FT]
    values_negative = [-DFH, -DSH, -DT]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create the bars for positive values
    ax.barh(categories, values_positive, color='green', label='Finishing')

    # Create the bars for negative values
    ax.barh(categories, values_negative, color='red', label='Defending')

    # Set the labels and title
    ax.set_xlabel('Value')
    ax.set_ylabel('Category')
    ax.set_title('Stacked Horizontal Double-Sided Bar Chart')

    # Set x-axis limits to include both positive and negative values
    min_value = min(min(values_positive), min(values_negative))
    max_value = max(max(values_positive), max(values_negative))
    ax.set_xlim(min_value - 3, max_value + 3)

    # Modify x-axis ticks and labels to include negative values
    ticks = np.arange(min_value - 3, max_value + 3, 5)
    ax.set_xticks(ticks)
    ax.set_xticklabels([abs(tick) if tick < 0 else tick for tick in ticks])

    # Add a grid
    ax.grid(True, axis='x', linestyle='--', alpha=1)

    # Add a legend
    ax.legend()

    # Display the chart
    st.pyplot(fig)
    print(df)
    

def visualization_page(df):
    st.subheader("Finishing efficiency")
    st.write("This is the visualization page.")
    
    EPO4,TrO4,SPO4,EPD4,TrD4,SPD4,Successful_finishing,TrO4Succ,Successful_finishing1,EPD4Succ,Successful_trdef,SPD4Succ=anal(df)

    # Data for the chart
    categories = ['Est. Play', 'Transition', 'Set Piece']
    values_fcn = [EPO4, TrO4, SPO4]
    values_opp = [-EPD4, -TrD4, -SPD4]
    O4succ=[Successful_finishing,TrO4Succ,Successful_finishing1]
    D4succ=[-EPD4Succ,-Successful_trdef,-SPD4Succ]

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 6))

    # Positive values
    ax.bar(np.arange(len(categories)), values_fcn, color='green', label='Values_fcn')

    # Negative values
    ax.bar(np.arange(len(categories)), values_opp, color='red', label='Values_opp')

    # Positive stacked bar (starting from 0)
    ax.bar(np.arange(len(categories)), O4succ, bottom=0, color='blue', label='O4succ')

    # Negative stacked bar (starting from 0)
    ax.bar(np.arange(len(categories)), D4succ, bottom=0, color='orange', label='D4succ')

    # Axis labels and title
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Double-Sided Bar Chart')

    # Set x-axis limits to include both positive and negative values
    min_value = min(min(values_fcn), min(values_opp))
    max_value = max(max(values_fcn), max(values_opp))
    ax.set_ylim(min_value - 2, max_value + 2)

    # Modify x-axis ticks and labels
    ax.set_xticks(np.arange(len(categories)))
    ax.set_xticklabels(categories)

    # Modify y-axis ticks and labels to include negative values
    ticks = np.arange(min_value - 2, max_value + 2, 5)
    ax.set_yticks(ticks)
    ax.set_yticklabels([abs(tick) if tick < 0 else tick for tick in ticks])

    # Add a vertical zero axis
    ax.axhline(0, color='black', linewidth=0.5)

    # Add a grid
    ax.grid(True, axis='y', linestyle='--', alpha=1)

    # Legend
    ax.legend()

    # Display the chart using Streamlit
    st.pyplot(fig)


def fourth_page(df):
    st.subheader("15 Minutes periods")
    st.write("This is the visualization page.")
    column = st.selectbox("Select a column for bar chart", df.columns)
    st.bar_chart(df[column])

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
            visualization_page(df)
        elif page == "2022/2023 Finishing table":
            visualization_page(df)

if __name__ == "__main__":
    main()










