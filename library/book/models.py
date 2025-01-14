from django.db import models


class Book(models.Model):
    """
        This class represents a Book. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param year_of_publication: Year the book was published
        type year_of_publication: int
        param date_of_issue: Date when the book was issued
        type date_of_issue: date
    """
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    year_of_publication = models.PositiveIntegerField(null=True, blank=True, verbose_name="Рік публікації")
    date_of_issue = models.DateField(null=True, blank=True, verbose_name="Дата видачі")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return f"'id': {self.id}, 'name': '{self.name}', 'description': '{self.description}', 'count': {self.count}, 'authors': {[author.id for author in self.authors.all()]}, 'year_of_publication': {self.year_of_publication}, 'date_of_issue': {self.date_of_issue}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id) else None

    @staticmethod
    def delete_by_id(book_id):
        if Book.get_by_id(book_id) is None:
            return False
        Book.objects.get(id=book_id).delete()
        return True

    @staticmethod
    def create(name, description, count=10, year_of_publication=None, date_of_issue=None, authors=None):
        if len(name) > 128:
            return None
        book = Book()
        book.name = name
        book.description = description
        book.count = count
        book.year_of_publication = year_of_publication
        book.date_of_issue = date_of_issue
        book.save()
        if authors:
            book.add_authors(authors)
        return book

    def update(self, name=None, description=None, count=None, year_of_publication=None, date_of_issue=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if year_of_publication is not None:
            self.year_of_publication = year_of_publication
        if date_of_issue is not None:
            self.date_of_issue = date_of_issue
        self.save()

    def add_authors(self, authors):
        if authors:
            for author in authors:
                self.authors.add(author)
        self.save()

    def remove_authors(self, authors):
        if authors:
            for author in authors:
                self.authors.remove(author)
        self.save()

    @staticmethod
    def get_all():
        return list(Book.objects.all())