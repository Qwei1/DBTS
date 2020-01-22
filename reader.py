# get resource df
def getResource(dataSetName,rating_path,trust_path):
    df_rating = 0
    df_trust = 0
    if('FilmTrust' == dataSetName):
        header_rating = ['user_id', 'item_id','rating']
        header_trust = ['user_u', 'user_v','trust_value']
        df_rating = pd.read_csv(rating_path, sep=' ',header = None, names=header_rating,low_memory=False)
        df_trust = pd.read_csv(trust_path sep=' ', names=header_trust,low_memory=False)
    elif('Ciao' == dataSetName):
        header_rating = ['user_id', 'item_id', 'genre_id','review_id','rating', 'timestamp']
        header_trust = ['user_u', 'user_v','trust_value']
        df_rating = pd.read_csv(rating_path, sep=',', names=header_rating)
        df_trust = pd.read_csv(trust_path, sep=',', names=header_trust)
        df_rating = pd.DataFrame(df_rating,columns=['user_id', 'item_id','rating'])
    elif('Douban' == dataSetName):
        header_rating = ['user_id','userURL','item_id',"bookName",'bookURL','authorAndProvider','rating','bookReadTime','readType','bookTags','bookComment']
        header_trust = ['user_u', 'trustorName','trustorURL','user_v','trusteerName','trusteerURL','trust_value']
        df_rating = pd.read_csv(rating_path, sep=',' ,header = None, names=header_rating,error_bad_lines=False)
        df_rating = pd.DataFrame(df_rating,columns=['user_id', 'item_id','rating'])[1:]
        
        df_trust= pd.read_csv('/Users/qwei/Desktop/user-user.csv', sep=',', names=header_trust, error_bad_lines=False)
        df_trust = pd.DataFrame(df_trust,columns=['user_u', 'user_v','trust_value'])[1:]
    print('Number of users = ' + str(len(set(df_rating['user_id']))) + ' | Number of items = ' + str(len(set(df_rating['item_id']))))
    return df_rating, df_trust
