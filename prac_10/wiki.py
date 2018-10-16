import wikipedia

def search_something():
    search_topic = str(input("What would you like to search? "))
    print("You searched for: " + str(search_topic))
    wikipedia.search(str(search_topic))
    wikipedia.summary(str(search_topic))

search_something()