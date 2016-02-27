from .config import categories


class NewsFeedAggregator():
    news_feed_map = {}

    def __init__(self):
        for category in categories:
            self.news_feed_map[category] = []

    def push(self, new_feed):
        category = new_feed.category
        self.news_feed_map.get(category).append(new_feed)

    def get_news_feed(self, categories):
        ret_news_feed_list = []
        for category in categories:
            category_queue = self.news_feed_map.get(category)
            news_feeds = category_queue
            ret_news_feed_list += news_feeds
        return sorted(ret_news_feed_list, key=lambda x: x.ts,reverse=True)[:6]
