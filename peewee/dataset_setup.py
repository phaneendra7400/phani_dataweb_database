import dataset

db = dataset.connect('sqlite:///bike_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Jawa' },
        { "description": 'RoyalEnfiled' },
        { "description": 'Ducati' },
        { "description": 'BMW' },
        { "description": 'Triumph' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()