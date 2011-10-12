#!/usr/bin/env ruby

require 'erb'
require 'rexml/document'

if ARGV.length != 2
	puts "sitemap_merger.rb takes two arguments. The two sitemap.xml files you want to merge"
	exit(1)
end

urls = []

ARGV.each do |sitemap_file|
	xml = File.read(sitemap_file)
	sitemap = REXML::Document.new(xml)

	sitemap.elements.each('urlset/url') do |url|
		urls.push(url)	
	end
end


static_sitemap = ERB.new <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
                      http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
 <% urls.each do |url| %>
	<%= url %>
 <% end %>
</urlset>
EOF

puts static_sitemap.result
