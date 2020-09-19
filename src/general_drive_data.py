import pandas as pd
from tqdm import tqdm
import random
from itertools import combinations
from src.preprocessing import create_train_df, remove_misc, remove_stop_words
from src.common import create_final_data
from src.common.Common import hard_drive_types, ssd_types

def generate_pos_hard_drive_data():
    pos_df = []
    drives = ['{} GB'.format(x) for x in range(1, 3193)] + ['{} TB'.format(x) for x in range(1, 101)]
    for drive in drives:
        # For hard drives
        pos_df.append([remove_stop_words('{} {}'.format(drive, random.choice(hard_drive_types))),
                       remove_stop_words('{} {}'.format(drive, random.choice(hard_drive_types))),
                       1])
        
        # For SSDs
        pos_df.append([remove_stop_words('{} {}'.format(drive, random.choice(ssd_types))),
                       remove_stop_words('{} {}'.format(drive, random.choice(ssd_types))),
                       1])
    
    return pd.DataFrame(pos_df, columns=['title_one', 'title_two', 'label'])

def generate_neg_hard_drive_data():
    neg_df = []
    drives = ['{} GB'.format(x) for x in range(8, 1001, 8)] + ['{} TB'.format(x) for x in range(1, 20)]
    
    for drive in drives:
        new_drive = drive
        
        while new_drive == drive:
            new_drive = random.choice(drives)
        
        orig_variations = []
        new_variations = []
        
        # For hard drive
        for x in hard_drive_types:
            orig_variations.append('{} {}'.format(drive, x))
            new_variations.append('{} {}'.format(new_drive, x))
        
        # For ssd
        for x in ssd_types:
            orig_variations.append('{} {}'.format(drive, x))
            new_variations.append('{} {}'.format(new_drive, x))
        
        for old in orig_variations:
            for new in new_variations:
                neg_df.append([remove_stop_words(old), remove_stop_words(new), 0])
        
        
    return pd.DataFrame(neg_df, columns=['title_one', 'title_two', 'label'])

def create_final_drive_data():
    # Generate the data
    pos_df = generate_pos_hard_drive_data()
    neg_df = generate_neg_hard_drive_data()

    # Concatenate the data and save it
    final_df = create_final_data(pos_df, neg_df)
    final_df.to_csv('data/train/more_drive_data.csv')
