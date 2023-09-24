import paralleldots as pd

class Api:
    def __init__(self):
        pd.set_api_key('gNxalXJdncA2AKla8rceUhYKYuXqag6F63XKuiGSuGs')

    def sentiment_analysis(self,text):
        response=pd.sentiment(text)     #function to check the sentiment
        return response