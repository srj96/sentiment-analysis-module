import sys
import os 
import json
'''Input text data at the command line prompt and execute the .py pressing
CTRL + Z, CTRL + D (twice)
'''
if __name__ == "__main__":
    
    text = sys.stdin.read()
    
    text_dict = dict()
    
    text_dict['body'] = text

    with open(os.getcwd() + "\\" + "text_data.txt", 'w') as data_file:
        
        json.dump(text_dict,data_file)
        

# print(text_dict) 
