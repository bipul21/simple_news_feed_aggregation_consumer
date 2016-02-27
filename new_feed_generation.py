import random
from threading import Thread
from time import sleep
from news_feed.aggregator import NewsFeedAggregator
from news_feed.config import categories
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
            news_feed_aggregator.push(new_feed)
            sleep(random.randint(2, 5))


class UserFeedGenerator(Thread):
    user_categories = []

    def __init__(self, categories):
        super(UserFeedGenerator, self).__init__()
        self.user_categories = categories

    def run(self):
        while True:
            global news_feed_aggregator
            feeds = news_feed_aggregator.get_news_feed(self.user_categories)
            print "========== Print Feed Generated ==========="
            for index, feed in enumerate(feeds):
                print "Feed no: %d" % (index + 1)
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
    print "Select Categories for which you want the feed"
    print "Press number to select 0  to to be done"
    selected_categories = []
    while True:
        for index, category in enumerate(categories):
            print "%d %s" % (index+1, category)
        selected_index = int(raw_input())

        if selected_index==0:
            break

        selected_category = categories[selected_index-1]
        selected_categories.append(selected_category)
        print "==========  Selected Categories ==========="
        for category in selected_categories:
            print category
        print "Enter 0 to exit"
        print "==========================================="

    user1 = User("Deepak")
    user2 = User("Bipul")
    user3 = User("Hridyesh")
    user1.start()
    user2.start()
    user3.start()
    feed_generator = UserFeedGenerator(selected_categories)
    feed_generator.run()


if __name__ == "__main__":
    main()
