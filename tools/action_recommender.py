from tools.data_loader import ads
from tools.date_filter import filter_by_date


def action_recommender(question=None):

    filtered_ads = filter_by_date(ads, question)

    recommendations = []

    high_acos = filtered_ads[filtered_ads["acos"] > 0.6]

    for _, row in high_acos.head(5).iterrows():

        recommendations.append({
            "keyword": row["keyword"],
            "recommendation": "Consider pausing or lowering bid due to high ACoS"
        })

    profitable = filtered_ads[filtered_ads["roas"] > 4]

    for _, row in profitable.head(5).iterrows():

        recommendations.append({
            "keyword": row["keyword"],
            "recommendation": "Increase bid or allocate more budget due to high ROAS"
        })

    return recommendations