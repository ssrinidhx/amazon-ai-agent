import pandas as pd
from tools.data_loader import sales_new, ads_new
from tools.date_filter import filter_by_date


def spend_revenue_analyzer(question=None):

    filtered_sales = filter_by_date(sales_new, question)
    filtered_ads = filter_by_date(ads_new, question)

    sales_summary = (
        filtered_sales
        .groupby(["asin", "product_title"])
        .agg({
            "revenue": "sum",
            "units_sold": "sum"
        })
        .reset_index()
    )

    ads_summary = (
        filtered_ads
        .groupby("asin")
        .agg({
            "ad_spend": "sum",
            "attributed_sales": "sum"
        })
        .reset_index()
    )

    combined = pd.merge(
        sales_summary,
        ads_summary,
        on="asin",
        how="left"
    )

    combined.fillna(0, inplace=True)

    combined["ad_contribution_pct"] = (
        combined["attributed_sales"] /
        combined["revenue"].replace(0, 1)
    ) * 100

    combined["ad_contribution_pct"] = combined["ad_contribution_pct"].round(2)

    combined = combined.sort_values(
        by="ad_contribution_pct",
        ascending=False
    )

    return combined.head(5).to_dict(orient="records")