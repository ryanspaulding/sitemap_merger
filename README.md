# Sitemap Merger
A simple Ruby script that takes N number of sitemap.xml files (http://www.sitemaps.org/) and merges them to create a single file. I wrote it so I could merge my fairly static sitemap.xml file with the one generated every time I wrote a blog post.


### Running out of cron on your web server
Run it once a day (or more) to make sure that your sitemap.xml file is always up-to-date:

1 8 * * * ~/bin/sitemap_merger.rb sitemap.xml ~/public_html/blog/sitemap.xml > ~/public_html/sitemap.xml

### Issues?
Feel free to send me pull requests or email me :)
