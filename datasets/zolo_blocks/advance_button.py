import re
from nanoid import generate
import pandas as pd
import random
import json

class Advance_Button():
  def __init__(self, generated_input):
    self.block_type = "advanced-button"
    self.code_all = pd.read_csv (r'zolo_blocks/advanced_button_info.csv')
    self.advanced_button_code = self.code_all["advanced_button_code"].values[0]
    
    try:
        self.button_name = generated_input["Button_Name"]
    except:
        self.button_name = "Advanced Button"
    
    try:
        self.button_url = generated_input["Button_URL"]
    except:
        self.button_url = "enter_your_url_here"
    
  # function to generate unique IDs
  def gen_uniqueId(self):
    # generate unique ID
    # identified by [UNIQUE_ID] in the code
    block_type = self.block_type
    unique_ID_char = generate("123456789abcdefghijklmnopqrstuvwxyz",size=8) # 8 character long  only number and alphabet
    unique_ID = f"{block_type}-{unique_ID_char}"
    return unique_ID

  def replace_params(self, string, replacements):
    # Regular expression to match custom placeholders
    pattern = r'\[([^\[\]]*)\]'
    return re.sub(pattern, lambda match: replacements.get(match.group(1), match.group(0)), string)

  def gen_unique_id(self):
    replacement_dict = {}
    # generate UNIQUE_ID
    unique_id = self.gen_uniqueId()
    unique_id_name = f"UNIQUE_ID_0"
    temp_dict = {unique_id_name:unique_id}
    replacement_dict.update(temp_dict)
    return replacement_dict

  def get_code(self):
    # Generate accordion start code
    replacement_dict = self.gen_unique_id()
    
    # Add button name
    temp_dict = {"Button_Name":self.button_name}
    replacement_dict.update(temp_dict)
    
    # Add URL
    temp_dict = {"URL_Here":self.button_url}
    replacement_dict.update(temp_dict)
    
    advanced_button_code = self.replace_params(self.advanced_button_code, replacement_dict)
    
    return advanced_button_code