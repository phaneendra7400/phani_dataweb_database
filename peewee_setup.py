from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('peewee_bike_list.db')

class Item(Model):
    description = CharField()

    class Meta:
        database = db

def add_items_to_db():
    global db
    items = [
        { "description": 'Jawa' },
        { "description": 'RoyalEnfiled' },
        { "description": 'Ducati' },
        { "description": 'BMW' },
        { "description": 'Triumph' }
        ]
    for item in items:
        Item.create(description=item['description'])

if __name__ == "__main__":
    db.connect()
    db.create_tables([Item])
    add_items_to_db()