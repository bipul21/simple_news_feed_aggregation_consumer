from .config import categories


class NewsFeedAggregator():
    news_feed_map = {}
    threshold = 5
    maximum_bucket = 10
    page_size = 10

    def __init__(self):
        for category in categories:
            self.news_feed_map[category] = []

    def push(self, new_feed):
        category = new_feed.category
        score = new_feed.score
        if score <= self.threshold:
            print "Ignoring Post because size %d <= 5 by %s in category %s"%(score,new_feed.user,new_feed.category)
            return
        self.news_feed_map.get(category).append(new_feed)

    def get_news_feed(self, categories, count=page_size):
        ret_news_feed_list = []
        for category in categories:
            category_queue = self.news_feed_map.get(category)
            news_feeds = category_queue[-self.maximum_bucket:]
            ret_news_feed_list += news_feeds
        return sorted(ret_news_feed_list, key=lambda x: x.ts, reverse=True)[:count]
