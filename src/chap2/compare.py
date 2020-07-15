x, y, z = 1, 2, 3
if x < y < z:
    print('true')

if x < z > y:
    print('true2')

a = 'book'
if a is not None:
    print('object exists')

items = ['book', 'note']
if 'book' in items:
    print('there is a book')

count = {'book': 1, 'note': 2}
if 'note' in count:
    print('there is a note')