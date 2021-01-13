import pandas as pd


class BatchDataProcessing:

    def process_csv(self, path, data_column, sentiment_column, encoding=None, columns=None):

        if path == None:
            raise Exception("keyword 'path' cannot be none")
        
        if data_column == None:
            raise Exception("keyword 'data_column' cannot be none")
        
        if sentiment_column == None:
            raise Exception("keyword 'sentiment_column' cannot be none")
        
        # TODO: Add validation for columns=None

        self.encoding = encoding
        self.file_path = path
        self.col_data = data_column
        self.col_sentiment = sentiment_column

        try:

            df = pd.read_csv(self.file_path, encoding=encoding, names=columns)
            print(df.head())

            for i in range(len(df)):
                sentiment = None
                headline = None
                for col in df.columns:
                    if col == self.col_data:
                        headline = df.loc[i, col]
                    elif col == self.col_sentiment:
                        sentiment = df.loc[i, col]

                print("Sentiment:", sentiment, ", Headline: ", headline)
                if i == 10:
                    break

        except Exception as ex:
            x = 1


if __name__ == '__main__':
    processor = BatchDataProcessing()
    processor.process_csv(path='data/all-data.csv',
                          encoding="ISO-8859-1", sentiment_column="Sentiment", data_column="News Headline", columns=["Sentiment", "News Headline"])
