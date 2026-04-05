from tools.data_loader import ads
from tools.date_filter import filter_by_date


def keyword_performance_evaluator(question=None):

    filtered_ads = filter_by_date(ads, question)

    wasteful = filtered_ads[
        (filtered_ads["acos"] > 0.5) &
        (filtered_ads["attributed_sales"] > 0)
    ]

    wasteful_keywords = (
        wasteful
        .groupby("keyword")
        .agg({
            "ad_spend": "sum",
            "attributed_sales": "sum",
            "acos": "mean"
        })
        .reset_index()
    )

    wasteful_keywords = wasteful_keywords.sort_values(
        by="acos",
        ascending=False
    )

    result = wasteful_keywords.head(10)

    return result.to_dict(orient="records")