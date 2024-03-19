class Article:

    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title (self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine




#!!!!!!
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name


    def articles(self):
        # a_articles = []

        # for article in Article.all:
        #     if article.author is self:
        #         a_articles.append(article)
        # return a_articles
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        authors_magazine = []
        # for article in self.articles():
        #     if isinstance(article.magazine, Magazine):
        #         authors_magazine.append(article.magazine)
        # return authors_magazine

        them = [article.magazine for article in self.articles() if isinstance(article.magazine, Magazine)]
        return list(set(them))
        


    def add_article(self, magazine, title):
        for article in self.magazines():
            if isinstance(magazine, Magazine) and isinstance(title, Article):
                return None

        new_article = Article(self,magazine, title)
        return new_article

        # new_article = [article for article in self.magazines() if not isinstance(magazine, Magazine) and not isinstance(title, Article)]
        # return new_article


    def topic_areas(self):
        topics = []
        for article in self.articles():
            topics.append(article.magazine.category)
        if topics:
            return topics
        else:
            return None







class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str) and 2<= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
    

    def articles(self):
        # m_articles = []
        # for article in Article.all:
        #     if article.magazine is self:
        #         m_articles.append(article)

        # return m_articles

        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        # authors_of_magazine = []
        # for article in Article.all:
        #     if isinstance(article.author, Author):
        #         authors_of_magazine.append(article.author)

        # return authors_of_magazine
 
        them = [article.author for article in self.articles() if isinstance(article.author, Author)]
        return list(set(them))
        

    def article_titles(self):
        titles = []
        for article in self.articles():
            titles.append(article.title)
        if titles:
            return titles
        else:
            return None


    def contributing_authors(self):

        #!!!!!
        counts = {}

        for article in self.articles():
            if article.author in counts:
                counts[article.author] += 1
            else:
                counts[article.author] = 1
        
        # !!!!!
        better_authors = []
        for author, count in counts.items():
            if count > 2:
                better_authors.append(author)

        if len(better_authors) == 0:
            return None

        return better_authors




                
        # count
        # author

        # author.magazine < 2



