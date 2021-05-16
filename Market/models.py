from Market import db

class user(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    uName = db.Column(db.String(length=30),nullable=False,unique=True)
    email_add = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    budget = db.Column(db.Integer(),nullable=False,default=15000)
    items = db.relationship('item',backref='owned_by',lazy=True)

class item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=100), nullable=False,unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))
    def __repr__(self):
        return f'item {self.name}'