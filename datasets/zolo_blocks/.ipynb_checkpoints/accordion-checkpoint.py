import re
from nanoid import generate
import pandas as pd
import random
import json

class Accordion():
  def __init__(self, generated_input):
    self.block_type = "accordion"
    self.code_all = pd.read_csv (r'zolo_blocks/accordion_info.csv')
    self.start_code = self.code_all["accordion_code_start"].values[0]
    self.end_code = self.code_all["accordion_end"].values[0]
    self.child_code = self.code_all["accordion_child"].values[0]
    
    self.child_number = generated_input["Accordion_Child_Number"]
    self.child_titles = generated_input["Accordion_Titles"]
    self.child_contents = generated_input["Accordion_Contents"]
    
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
    unique_ID_replacement_dict = self.gen_unique_id()
    accordion_code = self.replace_params(self.start_code, unique_ID_replacement_dict)
    
    # Generate Childs
    for child_number in range(self.child_number):
        # Gen unique ID
        replacement_dict = self.gen_unique_id()
        
        # Gen titles
        try:
            title = self.child_titles[child_number]
        except:
            title = f"Generated_Title_For_Child_{child_number+1}"
        temp_dict = {"Accordion_Title":title}
        replacement_dict.update(temp_dict)

        # Generate contents
        try:
            contents = self.child_contents[child_number]
        except:
            contents = f"Generated_Contents_For_Child_{child_number+1}"
        temp_dict = {"Accordion_Content":contents}
        replacement_dict.update(temp_dict)
        
        child_code = self.replace_params(self.child_code, replacement_dict)
        
        accordion_code = accordion_code + child_code
    
    # Add the end code
    accordion_code = accordion_code + self.end_code
        
    return accordion_code