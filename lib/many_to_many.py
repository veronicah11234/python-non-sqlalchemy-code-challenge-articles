class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return [article.magazine for article in self._articles]

    def topic_areas(self):
        return [article.magazine.category for article in self._articles]

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas_are_unique(self):
        return len(set(self.topic_areas())) == len(self.topic_areas())



class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long")

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return [article.author for article in self._articles]

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        return [author for author, count in authors.items() if count > 2]

    def add_article(self, article):
        self._articles.append(article)

class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._title =title
        self._author = None
        self._magazine = None
        self.author = author
        self.magazine = magazine
        self.all.append(self)


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    
    def __repr__(self):
        return f"Article(author={self.author.name}, magazine={self.magazine.name}, title={self.title})"

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be of type Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = new_magazine

    def validate_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        return title
