from market import db

class item(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=30), nullable=False, unique=True)
    price=db.Column(db.Integer(), nullable=False)
    barcode=db.Column(db.String(length=11), nullable=False, unique=True)
    description=db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'item {self.name}'