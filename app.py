import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from categorization import categorize
from data_preprocessing import load_data

from insights import show_insights
from analytics import calculate_summary

st.title(" Personal Finance Analyzer")
st.write("Upload your bank statement to analyze your income, expenses and spending patterns.")
# uploading the csv file for the project 
uploaded_file = st.file_uploader(
    "Upload your bank statement CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df=load_data(uploaded_file)


    
    # Categorize transactions
    df["Category"] = df["Description"].apply(categorize)

    # helps to create drop down to select a Particular category 
    selected_category=st.selectbox("Select category :",["ALL"]+sorted(df["Category"].unique().tolist()))
    
    if selected_category=="ALL":
        filtered_df=df
    else:
        filtered_df = df[df["Category"] == selected_category]
    # the below code is the UI code of filter selector 
    st.subheader(" Date filter:")
    Col1 ,Col2 =st.columns(2)
    with Col1:
        start_date=st.date_input("Start date: ", filtered_df["Date"].min())
    with Col2:
        end_date = st.date_input(
        "End Date",
        filtered_df["Date"].max()
    )
        # for case if we put future dates first 
    if start_date > end_date:
        st.error(" Start date cannot be after End date.")
        st.stop()

    # filter transaction between the start date and end date 
    filtered_df = filtered_df[
    (filtered_df["Date"] >= pd.Timestamp(start_date)) &
    (filtered_df["Date"] <= pd.Timestamp(end_date))
]
    #for case if we dont add date 
    if filtered_df.empty:
        st.warning("No transactions found for the selected date range.")
        st.stop()
    # Summary
    income = filtered_df[filtered_df["Amount"] > 0]
    expenses = filtered_df[filtered_df["Amount"] < 0]

    st.subheader(" Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Income",
            f"₹{income['Amount'].sum():,.2f}"
        )

    with col2:
        st.metric(
            "Expenses",
            f"₹{abs(expenses['Amount'].sum()):,.2f}"
        )

    with col3:
        savings = income["Amount"].sum() + expenses["Amount"].sum()

        st.metric(
            "Net Savings",
            f"₹{savings:,.2f}"
        )

    # Expense Chart
    income, expenses,savings,category_spending=calculate_summary(filtered_df)
    
    left, right = st.columns(2)

    with left:

        st.subheader(" Spending by Category")

        st.bar_chart(category_spending)

    with right:

        fig, ax = plt.subplots(figsize=(5, 5))

        category_spending.plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

        ax.set_ylabel("")

        st.subheader(" Spending Distribution")

        st.pyplot(fig)

        # adding financial insights to the dashboard 


        #st.subheader("Financial Insights")
        #adding the highest spend category using the idxmax

        # need to check for the expense data availability 
        show_insights(category_spending,expenses,income,filtered_df,savings)
    # Transaction Table
    st.subheader(" Your Data")

    st.dataframe(filtered_df)