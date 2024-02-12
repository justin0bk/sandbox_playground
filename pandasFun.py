import numpy as np
import pandas as pd
import ast

df = pd.read_excel("work_log.xlsx")

# df.replace('\xa0','', regex=True) # This rids key values of unicode space value

df['Total Time'] = None
df['Avg., Std.'] = None
timecol = df['Time Span (minutes)']
for i in range(len(timecol)):
    try:
        num_array = [int(num.strip()) for num in timecol[i].split(',')]
    except Exception as e:
        print(e, "@ row " + i)
    else:
        total = np.sum(num_array)
        df.loc[i ,'Total Time'] = str(total//60) + "H:" + str(total%60) + "M"
        mean_span = int(np.mean(num_array))
        std_span = int(np.std(num_array))
        df.loc[i, 'Avg., Std.'] = str(mean_span)+", "+str(std_span)

# df = df.drop('Avg. Attention Span', axis=1) # This would remove the entire column
                                              # created by mistake

for lst in df['Breaks']:
    num_array = [int(num.strip()) for num in lst.split(',')]
    print(num_array)