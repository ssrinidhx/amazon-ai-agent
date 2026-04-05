from datetime import timedelta

def filter_by_date(df, question):

    question = question.lower()

    if "last week" in question:
        last_date = df["date"].max()
        start = last_date - timedelta(days=7)
        return df[df["date"] >= start]

    if "last month" in question:
        last_date = df["date"].max()
        start = last_date - timedelta(days=30)
        return df[df["date"] >= start]

    if "today" in question:
        today = df["date"].max()
        return df[df["date"] == today]

    return df