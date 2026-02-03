from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product
from decimal import Decimal
from django.core.files.base import ContentFile
from PIL import Image, ImageDraw
import io


class Command(BaseCommand):
    help = 'Populate database with sample data including products with images'

    def generate_product_image(self, product_name, color):
        """Generate a simple placeholder image for a product"""
        # Create image
        img = Image.new('RGB', (400, 400), color=color)
        draw = ImageDraw.Draw(img)
        
        # Add text to image
        text = product_name[:20]  # Limit text length
        bbox = draw.textbbox((0, 0), text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = ((400 - text_width) // 2, (400 - text_height) // 2)
        draw.text(position, text, fill='white')
        
        # Save to BytesIO
        img_io = io.BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        return ContentFile(img_io.read(), name=f'{product_name.lower().replace(" ", "_")}.png')

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with sample data and images...')

        # Create sample categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Garden', 'slug': 'home-garden'},
            {'name': 'Sports', 'slug': 'sports'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Define color schemes for each category
        category_colors = {
            'electronics': '#FF6B6B',
            'clothing': '#4ECDC4',
            'books': '#FFE66D',
            'home-garden': '#95E1D3',
            'sports': '#FF8B94',
        }

        # Create sample products with more variety
        products_data = [
            # Electronics
            {
                'category': 'electronics',
                'name': 'Wireless Headphones',
                'description': 'Premium wireless headphones with noise cancellation and 30-hour battery life.',
                'price': Decimal('149.99'),
                'stock': 50
            },
            {
                'category': 'electronics',
                'name': 'Smartphone Pro',
                'description': 'Latest smartphone with advanced camera and 5G connectivity.',
                'price': Decimal('799.99'),
                'stock': 30
            },
            {
                'category': 'electronics',
                'name': 'Gaming Laptop',
                'description': 'High-performance gaming laptop with RTX 3080 and 16GB RAM.',
                'price': Decimal('1299.99'),
                'stock': 20
            },
            {
                'category': 'electronics',
                'name': 'Tablet Device',
                'description': '10-inch tablet with touchscreen and stylus support.',
                'price': Decimal('399.99'),
                'stock': 25
            },
            {
                'category': 'electronics',
                'name': 'USB-C Charger',
                'description': 'Fast charging USB-C charger compatible with all devices.',
                'price': Decimal('29.99'),
                'stock': 150
            },
            # Clothing
            {
                'category': 'clothing',
                'name': 'Cotton T-Shirt',
                'description': 'Comfortable 100% cotton t-shirt in various colors.',
                'price': Decimal('19.99'),
                'stock': 100
            },
            {
                'category': 'clothing',
                'name': 'Denim Jeans',
                'description': 'Classic fit denim jeans with premium quality fabric.',
                'price': Decimal('49.99'),
                'stock': 75
            },
            {
                'category': 'clothing',
                'name': 'Winter Jacket',
                'description': 'Warm winter jacket with waterproof material.',
                'price': Decimal('89.99'),
                'stock': 40
            },
            {
                'category': 'clothing',
                'name': 'Summer Dress',
                'description': 'Light and breathable summer dress perfect for hot days.',
                'price': Decimal('39.99'),
                'stock': 60
            },
            {
                'category': 'clothing',
                'name': 'Casual Sneakers',
                'description': 'Comfortable casual sneakers for everyday wear.',
                'price': Decimal('59.99'),
                'stock': 85
            },
            # Books
            {
                'category': 'books',
                'name': 'Python Programming Guide',
                'description': 'Comprehensive guide to Python programming for beginners and experts.',
                'price': Decimal('34.99'),
                'stock': 60
            },
            {
                'category': 'books',
                'name': 'Mystery Novel',
                'description': 'Bestselling mystery novel with unexpected twists.',
                'price': Decimal('14.99'),
                'stock': 80
            },
            {
                'category': 'books',
                'name': 'Web Development Masterclass',
                'description': 'Learn HTML, CSS, JavaScript and modern frameworks.',
                'price': Decimal('44.99'),
                'stock': 50
            },
            {
                'category': 'books',
                'name': 'Science Fiction Adventure',
                'description': 'Epic sci-fi adventure across galaxies.',
                'price': Decimal('16.99'),
                'stock': 70
            },
            {
                'category': 'books',
                'name': 'Data Science Handbook',
                'description': 'Complete guide to data science and machine learning.',
                'price': Decimal('54.99'),
                'stock': 40
            },
            # Home & Garden
            {
                'category': 'home-garden',
                'name': 'Coffee Maker',
                'description': 'Automatic coffee maker with programmable timer.',
                'price': Decimal('79.99'),
                'stock': 45
            },
            {
                'category': 'home-garden',
                'name': 'Garden Tool Set',
                'description': 'Complete 10-piece garden tool set with carrying case.',
                'price': Decimal('59.99'),
                'stock': 35
            },
            {
                'category': 'home-garden',
                'name': 'Indoor Plant Pot',
                'description': 'Decorative ceramic pot perfect for indoor plants.',
                'price': Decimal('24.99'),
                'stock': 120
            },
            {
                'category': 'home-garden',
                'name': 'Kitchen Blender',
                'description': 'High-power blender for smoothies and soups.',
                'price': Decimal('99.99'),
                'stock': 30
            },
            {
                'category': 'home-garden',
                'name': 'LED Desk Lamp',
                'description': 'Adjustable LED desk lamp with touch control.',
                'price': Decimal('35.99'),
                'stock': 80
            },
            # Sports
            {
                'category': 'sports',
                'name': 'Yoga Mat',
                'description': 'Non-slip yoga mat with extra cushioning.',
                'price': Decimal('24.99'),
                'stock': 90
            },
            {
                'category': 'sports',
                'name': 'Running Shoes',
                'description': 'Lightweight running shoes with advanced cushioning technology.',
                'price': Decimal('89.99'),
                'stock': 55
            },
            {
                'category': 'sports',
                'name': 'Dumbbells Set',
                'description': '20kg dumbbell set with stand for home gym.',
                'price': Decimal('79.99'),
                'stock': 40
            },
            {
                'category': 'sports',
                'name': 'Resistance Bands',
                'description': 'Set of 5 resistance bands for strength training.',
                'price': Decimal('19.99'),
                'stock': 100
            },
            {
                'category': 'sports',
                'name': 'Water Bottle',
                'description': 'Insulated water bottle keeps drinks cold for 24 hours.',
                'price': Decimal('29.99'),
                'stock': 150
            },
        ]

        for prod_data in products_data:
            category_slug = prod_data['category']
            category = categories[category_slug]
            
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                category=category,
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'stock': prod_data['stock']
                }
            )
            
            # Add image if product was just created
            if created:
                try:
                    color_hex = category_colors[category_slug]
                    # Convert hex to RGB tuple
                    color_rgb = tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                    image = self.generate_product_image(prod_data['name'], color_rgb)
                    product.image = image
                    product.save()
                    self.stdout.write(f'Created product with image: {product.name}')
                except Exception as e:
                    self.stdout.write(f'Created product (image error): {product.name} - {str(e)}')
            else:
                self.stdout.write(f'Product already exists: {product.name}')

        # Create a test user if it doesn't exist
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(
                username='testuser',
                email='test@example.com',
                password='testpass123'
            )
            self.stdout.write('Created test user (username: testuser, password: testpass123)')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with 25 products and images!'))
        self.stdout.write(self.style.SUCCESS('Test credentials - Username: testuser, Password: testpass123'))

