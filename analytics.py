# ==========================================
# Analytics Module
# ==========================================

def calculate_summary(filtered_df):

    income = filtered_df[filtered_df["Amount"] > 0]

    expenses = filtered_df[filtered_df["Amount"] < 0]

    savings = (
        income["Amount"].sum() +
        expenses["Amount"].sum()
    )

    expenses = expenses.copy()

    expenses["Amount"] = expenses["Amount"].abs()

    category_spending = (
        expenses
        .groupby("Category")["Amount"]
        .sum()
    )

    return (
        income,
        expenses,
        savings,
        category_spending
    )