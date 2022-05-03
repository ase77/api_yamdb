from csv import DictReader

from django.core.management import BaseCommand

from review.models import Genre, Category, Title


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from genre.csv"

    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('genre data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading genre data")

        for row in DictReader(open('./static/data/genre.csv', encoding="utf8")):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            genre.save()

        if Category.objects.exists():
            print('category data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading category data")

        for row in DictReader(open('./static/data/category.csv', encoding="utf8")):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        if Title.objects.exists():
            print('title data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading titles data")

        for row in DictReader(open('./static/data/titles.csv', encoding="utf8")):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                # category=row['category']
            )
            title.save()
