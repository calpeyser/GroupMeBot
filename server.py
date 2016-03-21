import webapp2
from google.appengine.ext.webapp import template
from generate_post import generate_post, get_authors

class MainPage(webapp2.RequestHandler):
    def get(self):
        corpus = open("groupme_stats/temp.csv", "rb")
        self.response.write(template.render("index.html", {"authors": get_authors(corpus)}))
        corpus.close()

    def post(self):
        corpus = open("groupme_stats/temp.csv", "rb")
        authors = get_authors(corpus)
        corpus.close()

        if self.request.get("author"):
            author = self.request.get("author")
            corpus = open("groupme_stats/temp.csv", "rb")
            post = generate_post(author, corpus)
            self.response.write(template.render("index.html", {"post": post, "authors": authors}))
        else:
            self.response.write(template.render("index.html", {"authors": authors}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)