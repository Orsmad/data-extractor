from models.params import HtmlExtractionParams

extraction_configs = [
        {
            'params': HtmlExtractionParams(
                post_num_pattern=r'<div class="pagination">.*?(\d+)\s+posts.*?</div>',
                content_regex=r'<div class="content">.*?(?=<div id=|$)',
                datetime_regex=r'<time[^>]*datetime=[\'"]([^\'"]+)[\'"][^>]*>.*?<\/time>',
                title_regex=r'<h3[^>]*>\s*<a[^>]*>(.*?)</a>\s*</h3>',
                author_regex=r'by\s+<strong><a[^>]*class="(?:username|username-coloured)"[^>]*>(.*?)</a></strong>'
            ),
            'url': "http://www.phpbb.com/community/viewtopic.php?f=46&t=2159437",
            'output_file': './output/phbb.json'
        },
        {
            'params': HtmlExtractionParams(
                post_num_pattern=r'<a[^>]*class="b-post__count[^>]*">#(\d+)</a>',
                content_regex=r'<div class="js-post__content-text restore h-wordwrap"[^>]*itemprop="text"[^>]*>.*?(?=<div class="h-flex-spacer h-margin-top-16"|<div class="post-signature restore"|$)',
                datetime_regex=r'<div class="b-post__timestamp">.*?<time[^>]*datetime=[\'"]([^\'"]+)[\'"][^>]*>.*?<\/time>.*?<\/div>',
                title_regex=r'<h2[^>]*class="b-post__title js-post-title b-post__hide-when-deleted"[^>]*itemprop="headline"[^>]*>(.*?)</h2>',
                author_regex=r'<div class="b-userinfo__details"[^>]*>.*?<a[^>]*href="https://forum\.vbulletin\.com/member/\d+-[^"]+"[^>]*>.*?<span[^>]*itemprop="name"[^>]*>(.*?)</span>.*?</a>.*?</div>'
            ),
            'url': "https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login",
            'output_file': './output/vbulletin.json'
        }
    ]