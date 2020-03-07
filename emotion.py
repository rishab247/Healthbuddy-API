# emotion range is calulated through 7 questions and reaction scores against the questions.
def emotion(n):
    if 46<=n<=56:
        return "happiness"
    elif 35<=n<=46:
        return "neutral"
    elif 24<=n<=35:
        return "sadness"
    elif 14<=n<=24:
        return "anger"
    