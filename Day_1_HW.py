#In-class Exercise 2:
#Write a function using regular expressions to find the domain name in the given email addresses (and return None for the invalid email addresses)
#HINT: Use '|' for either or

my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com",
             "yourfavoriteband@g6.org", "@codingtemple.com"]

# You can also use the $ at the end of your compile expression -- this stops the search

#Expected output:
#jordanw@codingtemple.orgcom
#pocohontas1776@gmail.com
#None
#yourfavoriteband@g6.org
#None

pattern = re.compile(r'[a-zA-Z]+[0-9]*[\W][a-zA-Z]+[0-9]*[\W]{1}[a-zA-z]+')
for email in my_emails:
    found = pattern.match(email)
    if found:
        start,stop = found.span()
        print(email[start:stop])
    else:
        print(found)
