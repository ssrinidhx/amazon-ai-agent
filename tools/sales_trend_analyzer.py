from tools.data_loader import sales
from tools.date_filter import filter_by_date


def sales_trend_analyzer(question=None):

    filtered_sales = filter_by_date(sales, question)

    product_sales = (
        filtered_sales
        .groupby(["asin", "product_title", "category", "sub_category"])
        .agg({
            "units_sold": "sum",
            "revenue": "sum",
            "profit_margin_pct": "mean"
        })
        .reset_index()
    )

    product_sales = product_sales.sort_values(
        by="revenue", ascending=False
    )

    result = product_sales.head(10)

    return result.to_dict(orient="records")