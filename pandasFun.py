import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast

# df.replace('\xa0','', regex=True) # This rids key values of unicode space value

df = pd.read_excel('work_log.xlsx')
df = df.dropna(how='all').reset_index(drop=True)

## Find the indices of the empty rows
# def is_empty(row):
#     return all(pd.isna(cell) for cell in row)
# empty_row_indices = df.apply(is_empty, axis=1)

## Filter out the empty rows and overwrite the DataFrame
# df = df[~empty_row_indices]

df['Total Time'] = None
df['Avg., Std.'] = None
timecol = df['Span (minutes)']
for i in range(len(timecol)):
    try:
        span_list = timecol[i].split(',')
        num_array = [int(num.strip()) for num in span_list]
    except Exception as e:
        print(e, "@ row " + i)
    else:
        total = np.sum(num_array)
        df.loc[i ,'Total Time'] = str(total//60) + "H:" + str(total%60) + "M"
        mean_span = int(np.mean(num_array))
        std_span = int(np.std(num_array))
        df.loc[i, 'Avg., Std.'] = str(mean_span)+", "+str(std_span)


df.to_excel('work_log.xlsx', index=False)

# df = df.drop('Avg. Attention Span', axis=1) # This would remove the entire column
                                              # created by mistake

# for lst in df['Breaks']:
#     num_array = [int(num.strip()) for num in lst.split(',')]
#     print(num_array)