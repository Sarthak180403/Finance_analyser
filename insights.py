# ==========================================
# Financial Insights Module
# ==========================================

import streamlit as st

def show_insights(category_spending, expenses, income, filtered_df, savings):

    # need to check for the expense data availability
    if not category_spending.empty:

        highest_category = category_spending.idxmax()
        highest_amount = category_spending.max()

        st.subheader("Financial Insights")

        st.info(
            f"Highest spending category: **{highest_category}** "
            f"(₹{highest_amount:,.2f})"
        )

        # adding the average spending insight
        average_expense = expenses["Amount"].mean()
        st.info(f"Average expense : ₹{average_expense:,.2f}")

        # adding the largest expense
        largest_expense = expenses["Amount"].max()
        st.info(f"Largest expense : ₹{largest_expense:,.2f}")

        # adding the total transactions
        total_transactions = len(filtered_df)
        st.info(f"Total transactions : {total_transactions}")

        # adding the total categories to the dashboard
        total_categories = filtered_df["Category"].nunique()
        st.info(f"Categories used : {total_categories}")

        # adding total savings percentage
        if income["Amount"].sum() > 0:

            savings_rate = (
                savings / income["Amount"].sum()
            ) * 100

            st.info(
                f"Savings rate : {savings_rate:.1f}%"
            )

            # percentage contribution
            highest_percentage = (
                highest_amount / category_spending.sum()
            ) * 100

            st.success(
                f"{highest_category} accounts for {highest_percentage:.1f}% of your total spending"
            )

    else:
        st.warning("No expense data available to generate financial insights.")