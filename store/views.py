from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from django.db import transaction as db_transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import uuid
from .models import (
    Category,
    Product,
    Review, 
    Cart,
    Order,
    OrderItem,
    Transaction
)



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        login(request, user)
        return redirect('product_list')

    return render(request, 'auth/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'auth/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    selected_category = None

    # Filter by category if provided
    category_id = request.GET.get('category')
    if category_id:
        try:
            selected_category = Category.objects.get(id=category_id)
            products = products.filter(category=selected_category)
        except Category.DoesNotExist:
            pass

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'store/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    reviews = product.reviews.all()
    average_rating = reviews.aggregate(avg=Avg('rating'))['avg']

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
    }
    return render(request, 'store/product_detail.html', context)


@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # prevent duplicate review
        if Review.objects.filter(product=product, user=request.user).exists():
            messages.error(request, 'You already reviewed this product.')
            return redirect('product_detail', pk=pk)

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )
        messages.success(request, 'Review added successfully!')
        return redirect('product_detail', pk=pk)
    
    return redirect('product_detail', pk=pk)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, 'Product added to cart!')
    return redirect('cart_view')


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total_price = 0
    for item in cart_items:
        total_price += item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/cart.html', context)


@login_required
def update_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_view')


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()

    messages.success(request, 'Item removed from cart.')
    return redirect('cart_view')


@login_required
def checkout(request):
    """
    Checkout view: Converts user's cart into an order,
    creates OrderItems and a Transaction (Pending status),
    then clears the cart.
    """
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('product_list')

    # Calculate total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        # Use atomic transaction to prevent partial saves
        with db_transaction.atomic():
            # 1️⃣ Create Order
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                status='Pending'
            )

            # 2️⃣ Create OrderItems
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )

            # 3️⃣ Create Transaction (Pending by default)
            transaction_id = str(uuid.uuid4())  # Unique transaction ID
            Transaction.objects.create(
                user=request.user,
                order=order,
                transaction_id=transaction_id,
                status='Pending'
            )

            # 4️⃣ Clear Cart
            cart_items.delete()

        messages.success(request, 'Order placed successfully! Your transaction is pending.')
        return redirect('transaction_list')

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'store/checkout.html', context)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'orders': orders
    }
    return render(request, 'store/order_history.html', context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = order.items.all()

    context = {
        'order': order,
        'items': items
    }
    return render(request, 'store/order_detail.html', context)



@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/transactions.html', {'transactions': transactions})


@login_required
def transaction_detail(request, tx_id):
    transaction = get_object_or_404(
        Transaction,
        transaction_id=tx_id,
        user=request.user
    )
    return render(request, 'store/transaction_detail.html', {'transaction': transaction})


@login_required
def cancel_transaction(request, tx_id):
    transaction = get_object_or_404(
        Transaction,
        transaction_id=tx_id,
        user=request.user
    )

    if transaction.status == 'Pending':
        transaction.status = 'Cancelled'
        transaction.save()
        messages.success(request, 'Transaction cancelled')

    return redirect('transaction_list')
