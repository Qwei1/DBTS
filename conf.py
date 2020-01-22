# encoding:utf-8
class conf(object):

    def __init__(self):

        # Dataset Parameters
        self.dataset_name = "ft"  # short name of datasets ["ft":"filmtrust","db":"douban","ca":"ciao"]
        
        self.k_fold_num = 5
        self.rating_path = "../data/%s_ratings.txt"
        self.trust_path = '../data/%s_trust.txt'
        self.random_state = 0
        self.size = 0.8

        # Model Parameter
        self.alfha = 0.1
        self.beta = 0.1
        self.theta = 0.1
        self.gamma = 0.1
        
        # Recommender Parameters
        self.K = 20
        self.N = 20
