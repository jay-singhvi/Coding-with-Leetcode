"""
    1683. Invalid Tweets
    https://leetcode.com/problems/invalid-tweets/
"""

import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    bool_invalid_tweet_status = tweets["content"].str.len() > 15  # True or False
    return tweets.loc[
        bool_invalid_tweet_status, ["tweet_id"]
    ]  # dataframe.loc[True, Columns]


# Alternate / shorter solution
import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets["content"].str.len() > 15, ["tweet_id"]]
