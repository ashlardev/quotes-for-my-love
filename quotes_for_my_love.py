import yagmail
import json
import random
import wikipedia

# open the quotes file and load them into the variable d
with open('quotes.json') as f:
    d = json.load(f)
    
# Generate the random quote from the json list.
quote = random.choice(d)

# Generate the associated wikipedia page about the author.
q = wikipedia.page(quote['quoteAuthor'])


def send_quote():
    yag = yagmail.SMTP('not_today_you_wont', 'your_password_here_if_you_are_crazy') # use keyring please!!!
    # The contents variable will recognize HTML even in string form, read the docs you savage. https://github.com/kootenpv/yagmail
    contents = [
        "<H3><I>" + quote['quoteText'] + "</I></H3>" + ' - ' + quote['quoteAuthor'],
        "<p>",
        q.summary,
        "</p><br>",
        q.url
        ]
               
    yag.send('you_know_exactly_what_to_put_here@email.com', 'Your Subject', contents)



send_quote()
