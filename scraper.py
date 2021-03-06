# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# the two lines below with import moves to libraries

# # import the libraries
import scraperwiki
import lxml.html
#
print("hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
# # show html code from webpage
print(html)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("a")
print(root.cssselect("a"))
listofmatches=root.cssselect("a")

record={}
for match in listofmatches:
  record["link"]=lxml.html.tostring(match)
  scraperwiki.sqlite.save(
    unique_keys=['link'],
    data=record)
  print(match)
  print(lxml.html.tostring(match))
# # Write out to the sqlite database using scraperwiki library

# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
