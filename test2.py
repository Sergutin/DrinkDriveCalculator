drinks = {
    'pub': [
        {'text': 'Pints of lager, 3% (568ml)',
        'alcohol': 1.3},
        {'text': 'Pints of lager, 4.5% (568ml)',
        'alcohol': 2.05},
        {'text': 'Bottles of lager, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Pints of stout, 4.2% (568ml)',
        'alcohol': 2.05},
        {'text': 'Pints of cider, 4.5% (568ml)',
        'alcohol': 2.05},
        {'text': 'Bottles of cider, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Bottles of alcopop, 4% (330ml)',
        'alcohol': 1.2},
        {'text': 'Glasses of white wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of white wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of red wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of red wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of sparkling wine, 11.5% (125ml)',
        'alcohol': 1},
        {'text': 'Measures of spirits, 40% (35.5ml)',
        'alcohol': 1}
    ],
    'home': [
        {'text': 'Cans of lager, 4.5% (500ml)',
        'alcohol': 1.8},
        {'text': 'Bottles of lager, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Cans of stout, 4.2% (500ml)',
        'alcohol': 1.8},
        {'text': 'Cans of cider, 4.5% (500ml)',
        'alcohol': 1.8},
        {'text': 'Bottles of cider, 4.5% (330ml)',
        'alcohol': 1},
        {'text': 'Bottles of alcopop, 4% (330ml)',
        'alcohol': 1.2},
        {'text': 'Glasses of white wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of white wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of red wine, 12.5% (150ml)',
        'alcohol': 1.5},
        {'text': 'Bottles of red wine, 12.5% (750ml)',
        'alcohol': 7.5},
        {'text': 'Glasses of sparkling wine, 11.5% (125ml)',
        'alcohol': 1},
        {'text': 'Measures of spirits, 40% (35.5ml)',
        'alcohol': 1}
    ]
}

# for index, item in enumerate(drinks['pub']):
#     print(f'{index + 1}: {item}')

for index, items in enumerate(drinks['pub']):
    print(f'{index + 1}: {items.get("text")}')