import os
import glob
import pandas as pd


DATASET_FOLDER = "../../datasets/"
COMBINED_FILENAME = "house_listings_all.csv"


os.chdir(DATASET_FOLDER)

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv(DATASET_FOLDER + COMBINED_FILENAME, index=False, encoding='utf-8-sig')