import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰")
st.title("Personal Expense Tracker 💰")

# Initialize session state for expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(
        columns=['Date', 'Category', 'Amount', 'Description']
    )

# Input form
with st.form("expense_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        date = st.date_input("Date", datetime.now())
        amount = st.number_input("Amount", min_value=0.0, step=1.0)
    
    with col2:
        category = st.selectbox(
            "Category",
            ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]
        )
        description = st.text_input("Description")
    
    submit = st.form_submit_button("Add Expense")
    
    if submit:
        new_expense = pd.DataFrame({
            'Date': [date],
            'Category': [category],
            'Amount': [amount],
            'Description': [description]
        })
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
        st.success("Expense added!")

# Display expenses
if not st.session_state.expenses.empty:
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)
    
    # Show total expenses
    total = st.session_state.expenses['Amount'].sum()
    st.metric("Total Expenses", f"Rs. {total:,.2f}")
    
    # Category-wise analysis
    st.subheader("Category-wise Expenses")
    category_total = st.session_state.expenses.groupby('Category')['Amount'].sum()
    st.bar_chart(category_total) 