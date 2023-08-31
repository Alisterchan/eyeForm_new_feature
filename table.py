from js import sex, age, y1, y2, records, report , language_type

import re


def _y_m(age):
    m = re.match('(\d+)歲(\d+)', age)
    if int(m.group(1)) > 9:
        space01=''
    else :
        space01='&nbsp'
    if int(m.group(2)) > 9:
        space02=''
    else :
        space02='&nbsp'
    if language_type== 0 :
        return f'&nbsp{space01}{m.group(1)}歲{space02}{m.group(2)}個月'
    elif language_type== 2:
        return f'&nbsp{space01}{m.group(1)}岁{space02}{m.group(2)}个月'
    else:
        return f'&nbsp{space01}{m.group(1)}y{space02}{m.group(2)}m'
    
#print(language_type)
table = {}
table['Age　'] = [f'{_y_m(age)}']
if y1 == 19.5 :
    table['OD'] = [f'<20']
elif y1== 30.5 :
    table['OD'] = [f'>30']
else :
    table['OD'] = [f'{y1:.2f}']

if y2 == 19.5 :
    table['OS'] = [f'<20']
elif y2 == 30.5 :
    table['OS'] = [f'>30']
else :
    table['OS'] = [f'{y2:.2f}']

import json
records = json.loads(records)
od, os = (18, 24) if report == '軸長' else (15, 21)
for record in records:
    if record[od] or record[os]:
        table['Age　'].insert(0, f'{_y_m(record[11])}')
        if record[od] == 19.5 :
            table['OD'].insert(0, f'<20')
        elif record[od] == 30.5 :
            table['OD'].insert(0, f'>30')
        else :
            table['OD'].insert(0, f'{record[od]:.2f}')

        if record[os] == 19.5 :
            table['OS'].insert(0, f'<20')
        elif record[os] == 30.5 :
            table['OS'].insert(0, f'>30')
        else :
            table['OS'].insert(0, f'{record[os]:.2f}')
        
import pandas as pd
df = pd.DataFrame(table)
"""
if report == '軸長':
    new_column_names = {'OD': 'OD(mm)　', 'OS': 'OS(mm)　'}
elif language_type == 0 or language_type == 2:
    new_column_names = {'OD': 'OD(度)　', 'OS': 'OS(度)　'}
else :
    new_column_names = {'OD': 'OD(degrees)　', 'OS': 'OS(degrees)　'}
df.rename(columns=new_column_names, inplace=True)
"""
df = df.T
"""
if language_type == 0 :
    new_index_names  = {'Age　': '年齡　'}
    df.rename(index=new_index_names, inplace=True)
    df.columns = df.loc['年齡　']
    df = df.drop(index='年齡　')
elif  language_type == 2:
    new_index_names  = {'Age　': '年龄　'}
    df.rename(index=new_index_names, inplace=True)
    df.columns = df.loc['年龄　']
    df = df.drop(index='年龄　')
else:
    df.columns = df.loc['Age　']
    df = df.drop(index='Age　')
"""
df.columns = df.loc['Age　']
df = df.drop(index='Age　')
"""
styled_df = df.style.set_properties(**{
'background-color': 'white', 
'color': 'black',
'text-align': 'center',
'border': 'solid',
'border-width': '2px',
'padding': '2px'
})
"""
#display(styled_df, target='table')

display(df, target='table')