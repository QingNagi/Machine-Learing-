import numpy as np
import pandas as pd
head= '''
<html>
    <head>
        <style>
                .data
        </style>
    </head>
    <body>
'''
boot = '''
    </body>
</html>
'''
data = pd.DataFrame({'one': [100, 99, 88], 'Two':[99, 98, 1000]})
with open('show.html', 'w') as f:
    f.write(head)
    f.write(data.to_html(col_space=20, classes='data'))
f.write(boot)