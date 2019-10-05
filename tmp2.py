from bs4 import BeautifulSoup
# The above data can be view in a pretty format by using beautifulsoup's prettify() method.
# For this we will create a bs4 object and use the prettify method
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# This will print data in format like we have seen when we inspected the web page.
# …
# As of now we know that our table is in tag table and class wikitable. 
# So, first we will extract the data in table tag using find method of bs4 object. 
# This method returns a bs4 object
tb = soup.find('table', class_='wikitable')

# This tag has many nested tags but we only need text under title element of the tag a of
# parent tag b (which is the child tag of table). For that we need to find all b tags under 
# the table tag and then find all the a tags under the b tags. For this we will use find_all
# method and iterate over each of the b tag to get the a tag


for link in tb.find_all('b'):
    name = link.find('a')
    print(name) 

# This will extract data under all the a tags
#<a href="/wiki/George_Washington" title="George Washington">George Washington</a>
#<a href="/wiki/John_Adams" title="John Adams">John Adams</a>
#<a href="/wiki/Thomas_Jefferson" title="Thomas Jefferson">Thomas Jefferson</a>
#...
#<a href="/wiki/Donald_Trump" title="Donald Trump">Donald Trump</a>

# The eleemnt title can be extracted from all a tags using the method get_text(). 
# So modifyng the above code snippet


