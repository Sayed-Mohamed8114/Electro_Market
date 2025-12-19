from market import app, db
from market.modules import User ,Item

# to make the data base as a first time
'''
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
'''

# now to add some dummy data 
'''
with app.app_context():
    # Example: create dummy items
    item1 = Item(
        name="Laptop",
        price=500,
        barcode="123456789012",
        description="A high-end laptop",
        owner=None  # no owner yet
    )

    item2 = Item(
        name="Phone",
        price=300,
        barcode="987654321098",
        description="A smartphone",
        owner=None
    )

    # Add all to session
    db.session.add(item1)
    db.session.add(item2)

    # Commit to save in the database
    db.session.commit()

    print("Dummy data added successfully!")
'''

# add more dummy data to the project 
# add_dummy_items.py
'''

from market import app, db
from market.modules import Item  # make sure Item model is correct

# List of dummy items
dummy_items = [
    {"name": "Headphones", "price": 100, "barcode": "100000000003", "description": "Noise-cancelling headphones"},
    {"name": "Keyboard", "price": 50, "barcode": "100000000004", "description": "Mechanical keyboard"},
    {"name": "Mouse", "price": 40, "barcode": "100000000005", "description": "Wireless mouse"},
    {"name": "Monitor", "price": 200, "barcode": "100000000006", "description": "24-inch LED monitor"},
    {"name": "Tablet", "price": 300, "barcode": "100000000007", "description": "10-inch tablet"},
    {"name": "Smartwatch", "price": 150, "barcode": "100000000008", "description": "Smartwatch with heart rate monitor"},
    {"name": "Camera", "price": 600, "barcode": "100000000009", "description": "Digital DSLR camera"},
    {"name": "Printer", "price": 120, "barcode": "100000000010", "description": "Wireless color printer"}
]

with app.app_context():
    seller=User.query.first()
    for item_data in dummy_items:
        item = Item(
            name=item_data["name"],
            price=item_data["price"],
            barcode=item_data["barcode"],
            description=item_data["description"],
            owner=None ,
            creator=seller.id
        )
        db.session.add(item)

    db.session.commit()
    print("8 dummy items added successfully!")
'''