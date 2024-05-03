import re
from nanoid import generate
import pandas as pd
import random
import json

class Advance_Heading():
  def __init__(self, generated_input):
    self.block_type = "advanced-heading"
    self.code_all = pd.read_csv(r'zolo_blocks/advanced_heading_info.csv')
    
    # Extract Link
    try:
        self.main_heading_url = generated_input["Heading_URL"]
        self.advanced_heading_code = self.code_all["advanced_heading_code_link"].values[0]
        self.main_link = True
    except:
        self.advanced_heading_code = self.code_all["advanced_heading_code_no_link"].values[0]
        self.main_link = False
    
    # Extract Heading
    try:
        self.main_heading = generated_input["Main_Heading"]
    except:
        self.main_heading = "This is generated heading. Input your own."
    
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
    # Add unique id
    replacement_dict = self.gen_unique_id()
    
    # Add heading 
    temp_dict = {"Main_Heading":self.main_heading}
    replacement_dict.update(temp_dict)
    
    if self.main_link:
        # Add url
        temp_dict = {"MAIN_LINK":self.main_heading_url}
        replacement_dict.update(temp_dict)
    
    advanced_heading_code = self.replace_params(self.advanced_heading_code, replacement_dict)
    
    return advanced_heading_code