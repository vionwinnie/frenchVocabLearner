import os 


dirpath = os.path.dirname(os.path.abspath(__file__))

#dirpath = os.path.dirname(__file__) or '.'

#dirpath = os.path.dirname( __file__ )
print(dirpath)

dir_above_path = os.path.join(dirpath, '..')
print(dir_above_path)

abs_dir_above_path = os.path.abspath(dir_above_path)
print(abs_dir_above_path)
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..'))

