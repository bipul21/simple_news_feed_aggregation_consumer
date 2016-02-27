import random
from threading import Thread
from time import sleep

from news_feed.aggregator import NewsFeedAggregator
from news_feed.news_feed import NewsFeed

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
            print  "========= End of News Feed =============="
            sleep(3)


def main():
    print "\n\n"
    print "================================"
    print "This is a simple example of newsfeed aggregator and generator based on certain filter criteria"
    print "There are three different users deepak, bipul and hridyesh who are constantly posting new feed of different types"
    print "Your feed is being and continouly with most recent news feed at the last"
    print  "================================"
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
