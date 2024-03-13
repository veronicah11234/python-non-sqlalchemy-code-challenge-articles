class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
         if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
         self._name = name
         self._articles = []

    @property
    def name(self):
        return self._name


    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    magazine_list= []
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self.name = name
        self.category = category
        self._articles = []
        Magazine.magazines_list.append(self)

    @property
    def articles(self):
        return self._articles


    def contributors(self):
        return list(set(article.author for article in self._articles))


    def article_titles(self):
                return [article.title for article in self._articles]
    

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author_name = article.author.name
            authors_count[author_name] = authors_count.get(author_name, 0) + 1

        return [author for author, count in authors_count.items() if count > 2]
    
    @classmethod
    def top_publisher(cls):
        if not cls.magazines_list:
            return None
        return max(cls.magazines_list, key=lambda mag: len(mag.articles()))


class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
        