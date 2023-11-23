from data import read_file
from data import data_info
from data import clean
from features import build_features
from models import train_model
from models import predict_model
from visualization import visualize
from features import correlation
from features import balance_data

def main():
    
    visualize.main()
    build_features.main()
    train_model.main()
    correlation.main()
    #balance_data.main()

    

main()
