# E-Commerce Platform

A full-featured e-commerce web application built with Django that provides a complete online shopping experience with product management, shopping cart, order processing, and transaction handling.

## Features

- **User Authentication**: Registration, login, and user profile management
- **Product Catalog**: Browse products by categories with detailed product pages
- **Shopping Cart**: Add, update, and remove items from cart
- **Order Management**: Place orders and track order history
- **Product Reviews**: Rate and review products
- **Transaction Processing**: Complete payment and transaction tracking
- **Admin Panel**: Django admin interface for managing products, orders, and users

## Technologies Used

- **Backend**: Django 6.0.1
- **Database**: SQLite
- **API**: Django REST Framework 3.16.1
- **Image Processing**: Pillow 12.1.0
- **Frontend**: HTML, CSS, JavaScript

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd ecommerce
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
      ```bash
      venv\Scripts\activate
      ```
   - macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**

   ```bash
   cd ecommerce
   pip install -r requirements.txt
   ```

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Populate sample data (optional)**

   ```bash
   python manage.py populate_data
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
ecommerce/
├── ecommerce/              # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── store/                 # Main store application
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── urls.py            # Store URL patterns
│   ├── admin.py           # Admin configurations
│   ├── management/        # Custom management commands
│   ├── static/            # CSS and JavaScript files
│   └── templates/         # HTML templates
│       ├── base.html      # Base template
│       ├── auth/          # Authentication templates
│       └── store/         # Store-specific templates
├── media/                 # User-uploaded files
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Models

- **UserProfile**: Extended user information (phone, address)
- **Category**: Product categories
- **Product**: Product information (name, price, stock, images)
- **Review**: Product reviews and ratings
- **Cart**: Shopping cart items
- **Order**: Customer orders
- **OrderItem**: Individual items in an order
- **Transaction**: Payment transactions

## Usage

### For Customers

1. **Browse Products**: View all available products on the homepage
2. **Product Details**: Click on a product to see detailed information
3. **Add to Cart**: Add products to your shopping cart
4. **Checkout**: Complete your purchase through the checkout process
5. **Order History**: View your past orders and their status
6. **Leave Reviews**: Rate and review products you've purchased

### For Administrators

1. Access the admin panel at `/admin/`
2. Manage products, categories, orders, and users
3. Update order statuses
4. Review transactions
5. Moderate product reviews

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Database Backups

```bash
python manage.py dumpdata > backup.json
```

### Loading Data

```bash
python manage.py loaddata backup.json
```

## Security Notes

⚠️ **Important**: Before deploying to production:

1. Change the `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production-grade database (PostgreSQL, MySQL)
5. Configure proper static file serving
6. Set up HTTPS
7. Implement secure payment processing

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.
