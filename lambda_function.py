import pandas as pd


def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Dear my beloved wife,')
    print('   it is another day, BB, now is 5:39pm, the wallpaper have completed 50%')
    print('I miss you, bb')
