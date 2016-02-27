import random
from threading import Thread
from time import gmtime, strftime,sleep

categories = ["music", "movies", "games", "photography", "career", "ai"]
news_feed_text = ["Pune is beautiful", "I want to work at mindtickle", "Lorum Ipsum Dotum", "Harry Potter",
                  "Flipkart Red Shoes", "Being fashionable"]


class NewsFeed:
    body = None
    category = None
    score = 0
    ts = None
    user = None

    def __repr__(self):
        return "\nUser: %s\nBody : %s \nCategory : %s \nScore: %s\nts: %s\n" % (
        self.user, self.body, self.category, self.score, self.ts)

    def __init__(self, name):
        self.user = name
        self.category = random.choice(categories)
        self.body = random.choice(news_feed_text)
        self.score = random.randint(0, 10)
        self.ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())


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

        return sorted(ret_news_feed_list, key=lambda x: x.ts)


news_feed_aggregator = NewsFeedAggregator()


class User(Thread):
    name = None

    def __init__(self, name):
        super(User, self).__init__()
        self.name = name

    def run(self):
        while True:
            global news_feed_aggregator
            new_feed = NewsFeed(self.name)
            # print new_feed
            news_feed_aggregator.push(new_feed)
            sleep(random.randint(2, 5))


class UserFeedGenerator(Thread):
    user_categories = ["games", "ai", "photography"]

    def run(self):
        while True:
            global news_feed_aggregator
            feeds = news_feed_aggregator.get_news_feed(self.user_categories)
            print "========== Print Feed Generated ==========="
            for feed in feeds:
                print feed
            sleep(3)


def main():
    user1 = User("deepak")
    user2 = User("bipul")
    user3 = User("hridyesh")
    user1.start()
    user2.start()
    user3.start()
    feed_generator = UserFeedGenerator()
    feed_generator.run()
    # user4.start()
    # user5.start()


if __name__ == "__main__":
    main()
