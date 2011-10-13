#!/usr/bin/env ruby

require 'erb'
require 'rexml/document'

if ARGV.length < 2
	puts "sitemap_merger.rb takes at least two arguments. The two (or more) sitemap.xml files you want to merge"
	exit(1)
end

urls = []

ARGV.each do |sitemap_file|
	
	begin
		xml = File.read(sitemap_file)
		sitemap = REXML::Document.new(xml)

		sitemap.elements.each('urlset/url') do |url|
			urls.push(url)	
		end
	rescue Exception => ex
		puts "#{sitemap_file} does not exist!"
		exit(1)
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
