import random
from time import strftime, gmtime

from .config import categories, news_feed_text


class NewsFeed:
    body = None
    category = None
    score = 0
    ts = None
    user = None

    def __repr__(self):
        return "User: %s\nBody : %s \nCategory : %s \nScore: %s\nts: %s\n" % (
            self.user, self.body, self.category, self.score, self.ts)

    def __init__(self, name):
        self.user = name
        self.category = random.choice(categories)
        self.body = random.choice(news_feed_text)
        self.score = random.randint(0, 10)
        self.ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())