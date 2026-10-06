import unittest
from unittest.mock import Mock, patch
from src.reddit.reddit import Reddit

class RedditTests(unittest.TestCase):
    @patch("src.reddit.reddit.requests.get")
    def test_feed_parsing_with_current_dependencies(self, get):
        xml = b'<feed><entry><title>Sample post</title><category term="python"/><content>&lt;h1&gt;Hello&lt;/h1&gt;</content><link href="https://example.com/post"/></entry></feed>'
        get.side_effect = [Mock(content=xml), Mock(json=lambda: {"data": {"title": "Python"}}), Mock(json=lambda: {"photos": {"results": [{"urls": {"small": "https://example.com/image"}}]}})]
        articles = Reddit("example", "test-feed").query_all_saved_content()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["title"], "Sample post")
        self.assertEqual(articles[0]["content"].strip(), "# Hello")
        self.assertEqual(articles[0]["url"], "https://example.com/post")
