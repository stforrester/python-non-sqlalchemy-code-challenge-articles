class Article:

    all = [] # single-source of truth

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.__class__.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 50 and not hasattr(self, "title"):
            self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "name"):
            self._name = value

    def articles(self): # demonstrates one-to-many
        return [article for article in Article.all if article.author == self]

    def magazines(self): # demonstrates many-to-many
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass