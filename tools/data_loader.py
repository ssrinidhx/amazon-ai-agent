import pandas as pd

sales = pd.read_csv(r"D:\amazon_agent_ai\data\sales_cleaned.csv")
ads = pd.read_csv(r"D:\amazon_agent_ai\data\ads_cleaned.csv")
sales_new = pd.read_csv(r"D:\amazon_agent_ai\data\new_sales_data.csv")
ads_new = pd.read_csv(r"D:\amazon_agent_ai\data\new_keyword_ad_data.csv")

sales["date"] = pd.to_datetime(sales["date"])
ads["date"] = pd.to_datetime(ads["date"])