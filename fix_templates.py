import os

templates = {
    'store/templates/auth/login.html': {
        'old': "{% extends 'base.html' %} {% block title %}Login - E-Commerce Store{% endblock\n%} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Login - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/auth/signup.html': {
        'old': "{% extends 'base.html' %} {% block title %}Sign Up - E-Commerce Store{% endblock\n%} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Sign Up - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/product_list.html': {
        'old': "{% extends 'base.html' %} {% block title %}Products - E-Commerce Store{% \nendblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Products - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/product_detail.html': {
        'old': "{% extends 'base.html' %} {% block title %}{{ product.name }} - E-Commerce\nStore{% endblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}{{ product.name }} - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/cart.html': {
        'old': "{% extends 'base.html' %} {% block title %}Shopping Cart - E-Commerce Store{% \nendblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Shopping Cart - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/checkout.html': {
        'old': "{% extends 'base.html' %} {% block title %}Checkout - E-Commerce Store{% \nendblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Checkout - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/order_history.html': {
        'old': "{% extends 'base.html' %} {% block title %}Order History - E-Commerce Store{% \nendblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Order History - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/order_detail.html': {
        'old': "{% extends 'base.html' %} {% block title %}Order #{{ order.id }} - E-Commerce\nStore{% endblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Order #{{ order.id }} - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/transactions.html': {
        'old': "{% extends 'base.html' %} {% block title %}Transactions - E-Commerce Store{% \nendblock %} {% block content %}",
        'new': "{% extends 'base.html' %}\n{% block title %}Transactions - E-Commerce Store{% endblock %}\n{% block content %}"
    },
    'store/templates/store/transaction_detail.html': {
        'old': "{% extends 'base.html' %} {% block title %}Transaction {{\ntransaction.transaction_id }} - E-Commerce Store{% endblock %} {% block content\n%}",
        'new': "{% extends 'base.html' %}\n{% block title %}Transaction {{ transaction.transaction_id }} - E-Commerce Store{% endblock %}\n{% block content %}"
    }
}

for filepath, patterns in templates.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if patterns['old'] in content:
            content = content.replace(patterns['old'], patterns['new'])
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed {filepath}")
        else:
            print(f"✗ Pattern not found in {filepath}")
    else:
        print(f"✗ File not found: {filepath}")

print("\nAll templates fixed!")
