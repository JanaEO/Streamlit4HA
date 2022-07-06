#Library Import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu




# Create a horizontal menu
page = option_menu(
    menu_title=None,
    options=["Home","Dataset", "Visualizations", "Regions"],
    orientation="horizontal",
    icons=['house', 'cloud-upload', "graph-up-arrow", 'gear','currency-dollar'],
    )



#First Page
if page == "Home":
    #Title
    st.markdown("## Insurance Charges Variation")
    #Image
    st.image('https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/advisor/wp-content/uploads/2022/04/how_much_is_health_insurance.jpg')
    st.subheader("Jana El Oud")
#Second Page
if page == "Dataset":
    # Display details of page 1
    st.write("This application shows how different factors affect insurance charges in the United States")
    #Data Import
    bytes_data = pd.read_csv('insurance.csv')
    with st.expander("Detailed Data View!"):
        st.markdown("### Detailed Data View")
        st.write(bytes_data)

    st.write("The dataframe shows the insurance charges across different regions of the United States.")
    st.write("The dataframe shows the insurance fees for each client along with his/her demographics such as age, sex, bmi, number of children, smoking status, and region.")
    st.write("This dataset will be used to study how different variables affect the insurance fees set by an insurance company to a client.")

#Third Page: Visualizations
elif page == "Visualizations":
    # Data Import
    bytes_data = pd.read_csv('insurance.csv')

    # create four columns
    st.markdown("#### Number of subscribers in each Region")
    kpi1, kpi2, kpi3,kpi4 = st.columns(4)
    #  KPIs
    #These KPIs show the number of subscribers in each region.
    southwest=bytes_data["region"].value_counts().southwest
    kpi1.metric(
        label="Southwest ",
        value=southwest,
        )
    northeast=bytes_data["region"].value_counts().northeast
    kpi2.metric(
        label="Northeast",
        value=round(northeast),
        )
    northwest=bytes_data["region"].value_counts().northwest
    kpi3.metric(
        label="Northwest ",
        value=northwest,
        )
    southeast=bytes_data["region"].value_counts().southeast
    kpi4.metric(
        label="Southeast ",
        value=southeast,
        )
    #Total revenue generated from each district
    st.markdown("#### Total Insurance Charges in each District $")
    kpi5, kpi6, kpi7,kpi8 = st.columns(4)
        #southwest Dataframe to calculate charges
    southwest_df = bytes_data.loc[(bytes_data['region'] == 'southwest')]
    southwest = southwest_df["charges"].sum()


    kpi5.metric(
        label="Southwest ",
        value=round(southwest),
        )
        #Northeast Dataframe to calculate  charges
    northeast_df = bytes_data.loc[(bytes_data['region'] == 'northeast')]
    northeast = northeast_df["charges"].sum()
    kpi6.metric(
        label="Northeast",
        value=round(northeast),
        )
        #Northwest Dataframe to calculate  charges
    northwest_df = bytes_data.loc[(bytes_data['region'] == 'northwest')]
    northwest = northwest_df["charges"].sum()

    kpi7.metric(
        label="Northwest ",
        value=round(northwest),
        )
        #southeast Dataframe to calculate charges
    southeast_df = bytes_data.loc[(bytes_data['region'] == 'southeast')]
    southeast = southeast_df["charges"].sum()
    kpi8.metric(
        label="Southeast ",
        value=round(southeast),
        )
#Graphs to show how Gender affects Charges
    #Column Divider
    fig_col1, fig_col2 = st.columns(2)

    with fig_col1:
        st.markdown("### Gender Count")
        fig3 = px.histogram(data_frame=bytes_data, x="sex")
        st.write(fig3)
    with fig_col2:
        st.markdown("### Charges by Gender")
        fig2 = px.histogram(data_frame=bytes_data, x="sex", y='charges')
        st.write(fig2)




#Graphs to show how Charges are affected by Smoking status and BMI
    #Column Divider
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### Charges VS Smoking")
        bd = px.data.tips()
        fig = px.box(bytes_data,x="charges", y="smoker")
        st.write(fig)
    with fig_col2:
        st.markdown("### Charges VS BMI")
        fig7 = px.scatter(bytes_data, x = 'bmi', y ='charges' ,color ='smoker')
        st.plotly_chart(fig7)



    fig_col1, fig_col2 = st.columns(2)
    # Creating an Age category Column to categorize age


        # create a list of our conditions
    conditions = [
            (bytes_data['age'] >= 18) & (bytes_data['age'] < 36),
            (bytes_data['age'] >= 36) & (bytes_data['age'] <= 55),
            (bytes_data['age'] > 55)
            ]

            # create a list of the values we want to assign for each condition
    values = ['youth', 'adults', 'seniors']

        # create a new column and use np.select to assign values to it using our lists as arguments
    bytes_data['age_category'] = np.select(conditions, values)


    tips = px.data.tips()
    with fig_col1:
        fig = px.histogram(bytes_data, x="age_category", y="charges",
                   hover_data=bytes_data.columns)
        st.markdown("#### Age Categories")

        st.write(fig)

    with fig_col2:
        st.markdown("#### Charges By Age Category")
        bd = px.data.tips()
        fig = px.box(bytes_data,x="age_category", y="charges")
        st.write(fig)
#correlation
    st.markdown("#### Correlation Between Variables")
    correlation = bytes_data[['age', 'bmi', 'children', 'charges']].corr()
    y=px.imshow(correlation,text_auto=True, color_continuous_scale='blues')
    st.write(y)

#Fourth Page: KPIs
elif page == "Regions":
    # Display details of page 2
    bytes_data = pd.read_csv('insurance.csv')
    # top-level filters
    st.markdown("#### Select the Region")
    region_filter = st.selectbox("", pd.unique(bytes_data["region"]))


    # dataframe filter
    bytes_data = bytes_data[bytes_data["region"] == region_filter]
    average_age=bytes_data["age"].mean()
    # create four columns
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    # KPIs that shows average age, average number of kids, average bmi, and average charges
    kpi1.metric(
        label="Average Age ",
        value=round(average_age,2),
        )
    average_number_of_kids=bytes_data['children'].mean()
    kpi2.metric(
        label="Kids Count ",
        value=round(average_number_of_kids),
        )
    average_charges=bytes_data['charges'].mean()
    kpi3.metric(
        label="Average Charges ",
        value=round(average_charges,2),
        )
    average_bmi=bytes_data['bmi'].mean()
    kpi4.metric(
        label="Average BMI ",
        value=round(average_bmi,2),
        )


        # create two columns for charts
    fig_col1, fig_col2 = st.columns(2)
#Histogram that shows children count
    with fig_col1:
        st.markdown("#### Number of Children")

        figd = px.histogram(data_frame=bytes_data, x="children")
        st.write(figd)
#Histogram that shows total charges by the number of children
    with fig_col2:
        st.markdown("#### Charges by Children")
        fig2 = px.histogram(data_frame=bytes_data, x="children", y='charges')
        st.write(fig2)
    fig_col3, fig_col4 = st.columns(2)

    with fig_col3:
#Histogram that shows charges by smoking status
        st.markdown("#### Charges By Smoking Status")
        fig2 = px.histogram(data_frame=bytes_data, x="smoker", y='charges')
        st.write(fig2)
#Histogram that shows charges by gender
    with fig_col4:
        st.markdown("#### Charges By Gender")
        fig4 = px.density_heatmap(
        data_frame=bytes_data, y="charges", x="sex",color_continuous_scale='blues')

        st.write(fig4)


#Scatterplot
    st.subheader('Scatterplot analysis')
    selected_x_var = st.selectbox('What do you want the x variable to be?', ['age','sex','bmi','children','smoker','region','charges'])
    selected_y_var = st.selectbox('What about the y?', ['age','sex','bmi','children','smoker','region','charges'])
    fig = px.scatter(bytes_data, x = bytes_data[selected_x_var], y = bytes_data[selected_y_var])
    st.plotly_chart(fig)
    st.write("Refer to the above scatter plot for different visualizations of client demographics and charges!")
