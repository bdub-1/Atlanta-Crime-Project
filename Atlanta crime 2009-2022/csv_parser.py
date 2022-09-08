# Step 1) import the csv files
def import_csv_lst(dirname):
    
    print('Importing:', os.listdir(dirname), '\n...')
    files = os.listdir(dirname)
    dfs = []
    x = 0
    
    while x < len(files):
        assert files[x].endswith('.csv'), 'Error: all files must be csv'
        file = ('COBRA-Data/' + files[x])
        print('loading:', file)
        df = pd.read_csv(file, low_memory=False)
        x+=1
        dfs.append(df)

    if len(dfs) == len(files):
        print('... \nSuccess')
    else:
        print('... \nerror')
    
    return (dfs, files)



# Step 2) Create a dictionary of {(file_name: column.names)} by passing in the output of step 1 
def csv_and_cols_to_dict(output):
    d = {}
    c = 0
    ls = []
    files = output[1]
    
    for i in output[0]:
        for e in i.columns:
            ls.append(e) 
        d[files[c]] = ls
        c+=1
        ls = []
    return d



# Step 3) Returns max length of a value (column.names) for any key (file_name) in dictionary
def max_dict_len(d):
    max_len = 0
    for k in d:
        if len(d[k]) > max_len:
            max_len = len(d[k])
    return max_len




# Step 4) Adjusts lengths of values (column.names) to allow for data frame creation
def len_adjust(d):
    max_len = max_dict_len(d) #retrieves max len
    for i in d:
        if len(d[i]) < max_len:
            dif = max_len - len(d[i])
            ls = []
            for t in range(dif):
                d[i].append('XXX')
    return d



# Step 5) Convert columns of each dataframe from a list of dataframes into a table (rows=column.names, columns=file_name)
def dfNameToCol_dfColToRow(csv_columnNames_to_rows):
    return len_adjust(csv_and_cols_to_dict(csv_columnNames_to_rows)) # returns adjusted dictionary 



# Step 6) Converts a dictionary to a data frame
def dfsLst_to_rowsOfColumns(csv_columnNames_to_rows):
    return pd.DataFrame.from_dict(dfNameToCol_dfColToRow(csv_columnNames_to_rows))



# Step 7) Tie it all together
def csv_columnNames_to_rows(dirname):    
    return dfsLst_to_rowsOfColumns(import_csv_lst(dirname))