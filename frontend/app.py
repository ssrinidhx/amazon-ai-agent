import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Amazon Advertising Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

sns.set_style("whitegrid")

@st.cache_data
def load_data():
    sales = pd.read_csv(r"D:\amazon_agent_ai\data\sales_cleaned.csv")
    ads = pd.read_csv(r"D:\amazon_agent_ai\data\ads_cleaned.csv")

    sales["date"] = pd.to_datetime(sales["date"])
    ads["date"] = pd.to_datetime(ads["date"])

    ads["roas"] = ads["attributed_sales"] / ads["ad_spend"]

    return sales, ads

sales, ads = load_data()

st.sidebar.title("Amazon AI Intelligence")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Visualizations", "Agent"]
)

if page == "Home":

    st.title("Amazon Advertising & Sales Intelligence Platform")

    st.markdown(
        "AI-powered analytics platform for understanding **product performance, advertising efficiency, and revenue growth**."
    )

    total_revenue = sales["revenue"].sum()
    total_units = sales["units_sold"].sum()
    total_ad_spend = ads["ad_spend"].sum()
    total_ad_sales = ads["attributed_sales"].sum()

    acos = (total_ad_spend / total_ad_sales) * 100 if total_ad_sales > 0 else 0
    roas = (total_ad_sales / total_ad_spend) if total_ad_spend > 0 else 0

    st.subheader("Business Performance Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Revenue", f"${total_revenue:,.0f}")
    col2.metric("Units Sold", f"{total_units:,}")
    col3.metric("Ad Spend", f"${total_ad_spend:,.0f}")
    col4.metric("Ad Sales", f"${total_ad_sales:,.0f}")
    col5.metric("ROAS", f"{roas:.2f}")

    st.subheader("Revenue vs Advertising Sales Trend")

    revenue = sales.groupby("date")["revenue"].sum()
    ad_sales = ads.groupby("date")["attributed_sales"].sum()

    trend = pd.concat([revenue, ad_sales], axis=1)
    trend.columns = ["Revenue", "Ad Sales"]

    fig, ax = plt.subplots(figsize=(10,5))
    trend.plot(ax=ax)

    ax.set_title("Revenue vs Ad Driven Sales")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    st.subheader("Category Revenue Performance")

    category_sales = (
        sales.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=category_sales.values, y=category_sales.index, ax=ax)

    ax.set_title("Revenue by Category")

    st.pyplot(fig)

    st.subheader("Profit Margin Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        sales["profit_margin_pct"].dropna(),
        bins=20,
        kde=True,
        ax=ax
    )

    ax.set_title("Profit Margin Distribution")

    st.pyplot(fig)

elif page == "Visualizations":

    st.title("Advanced Data Visualizations")

    st.subheader("Top 10 Products by Revenue")

    top_products = (
        sales.groupby("product_title")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax)

    ax.set_title("Top Performing Products")

    st.pyplot(fig)

    st.subheader("Advertising Spend vs Attributed Sales")

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=ads,
        x="ad_spend",
        y="attributed_sales",
        hue="match_type",
        ax=ax
    )

    ax.set_title("Ad Spend vs Ad Sales")

    st.pyplot(fig)

    st.subheader("Keyword Efficiency (ACoS vs ROAS)")

    fig, ax = plt.subplots(figsize=(8,6))

    sns.scatterplot(
        data=ads,
        x="acos",
        y="roas",
        hue="match_type",
        ax=ax
    )

    ax.set_title("Advertising Efficiency Analysis")

    st.pyplot(fig)

    st.subheader("ACoS Distribution")

    fig, ax = plt.subplots()

    sns.histplot(
        ads["acos"],
        bins=30,
        kde=True,
        ax=ax
    )

    ax.set_title("ACoS Distribution")

    st.pyplot(fig)

    st.subheader("Advertising Efficiency Heatmap")

    heatmap_data = ads.pivot_table(
        values="acos",
        index="match_type",
        columns="date",
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(12,5))

    sns.heatmap(
        heatmap_data,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

elif page == "Agent":

    st.title("AI Advertising Intelligence Agent")

    st.write(
        "Ask questions about your Amazon sales and advertising performance."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask a question about your Amazon data")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing data..."):

                try:

                    response = requests.post(
                        "http://127.0.0.1:8000/analyze",
                        json={"query": user_input}
                    )

                    if response.status_code == 200:

                        result = response.json()
                        analysis = result["analysis"]

                        st.markdown(analysis)

                        st.session_state.messages.append(
                            {"role": "assistant", "content": analysis}
                        )

                    else:
                        st.error("API error. Please check FastAPI server.")

                except:
                    st.error("Cannot connect to backend.")