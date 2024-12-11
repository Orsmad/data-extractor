class HtmlExtractionParams:
    def __init__(
        self, post_num_pattern, content_regex, datetime_regex, title_regex, author_regex
    ):
        self.post_num_pattern = post_num_pattern
        self.content_regex = content_regex
        self.datetime_regex = datetime_regex
        self.title_regex = title_regex
        self.author_regex = author_regex
