import os
import sys
import django
import random
from faker import Faker
from datetime import timedelta, date
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_BookStore.settings")  # Update with your project name
django.setup()
from e_BookStore.models import Book,Category
fake = Faker()

# Get all categories from the database
categories = list(Category.objects.all())

if not categories:
    print("⚠️ No categories found! Add some categories first.")
else:
    # Generate 20 fake books
    for _ in range(60):
        book = Book.objects.create(
            title=fake.sentence(nb_words=3),  # Random book title
            author=fake.name(),  # Random author name
            description=fake.paragraph(nb_sentences=2),  # Random description
            price=random.randint(10, 100),  # Random price between $10 and $100
            stock=random.randint(1, 50),  # Random stock quantity
            category=random.choice(categories),  # Assign a random existing category
            cover_image="H:/DJANGO/e_BookStore/e_BookStore/static/images/sample.jpg",  # Replace with an actual path or URL
            published_date=fake.date()
            )
        print(f"✅ Added: {book.title} by {book.author}")

print("🎉 20 fake books added successfully!")
