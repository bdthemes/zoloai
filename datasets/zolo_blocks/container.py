import re
from nanoid import generate
import pandas as pd
import random
import json

class Container():
  def __init__(self, generated_input):
    self.block_type = "container"
    self.code_all = pd.read_csv (r'zolo_blocks/containers_info.csv')
    self.container_id = generated_input["Container_ID"]
    self.paragraph_list = generated_input["Paragraph_List"]
    self.unique_id_count = self.code_all[self.code_all["container_index"] == self.container_id]["unique_id_count"].values[0]
    self.block_id_count = self.code_all[self.code_all["container_index"] == self.container_id]["block_id_count"].values[0]
    self.paragraph_count = self.code_all[self.code_all["container_index"] == self.container_id]["paragraph_count"].values[0]
    self.html_code =  self.code_all[self.code_all["container_index"] == self.container_id]["boiler_plate_code"].values[0]
    
  # function to generate unique IDs
  def gen_uniqueId(self):
    # generate unique ID
    # identified by [UNIQUE_ID] in the code
    block_type = self.block_type
    unique_ID_char = generate("123456789abcdefghijklmnopqrstuvwxyz",size=8) # 8 character long  only number and alphabet
    unique_ID = f"{block_type}-{unique_ID_char}"
    return unique_ID
    
  def generate_block_id(self) -> "str":
    # example id "8a4130b5-1364-45b6-9dc4-53e1135edc81"
    # total 5 parts
    id_1 = generate("123456789abcdefghijklmnopqrstuvwxyz",size=8)
    id_2 = generate("123456789abcdefghijklmnopqrstuvwxyz",size=4)
    id_3 = generate("123456789abcdefghijklmnopqrstuvwxyz",size=4)
    id_4 = generate("123456789abcdefghijklmnopqrstuvwxyz",size=4)
    id_5 = generate("123456789abcdefghijklmnopqrstuvwxyz",size=12)
    block_id = f"{id_1}-{id_2}-{id_3}-{id_4}-{id_5}"
    return block_id

  def replace_params(self, string, replacements):
    # Regular expression to match custom placeholders
    pattern = r'\[([^\[\]]*)\]'
    return re.sub(pattern, lambda match: replacements.get(match.group(1), match.group(0)), string)

  def gen_replacements(self):
    replacement_dict = {}

    # generate BLOCK_ID
    for loop_count in range(self.block_id_count):
        block_id = self.generate_block_id()
        block_id_name = f"BLOCK_ID_{loop_count}"
        temp_dict = {block_id_name:block_id}
        replacement_dict.update(temp_dict)

    # generate UNIQUE_ID
    for loop_count in range(self.unique_id_count):
        unique_id = self.gen_uniqueId()
        unique_id_name = f"UNIQUE_ID_{loop_count}"
        temp_dict = {unique_id_name:unique_id}
        replacement_dict.update(temp_dict)
    
    # paragraph list
    for loop_count in range(self.paragraph_count):
        try:
            temp_paragraph = self.paragraph_list[loop_count]
        except:
            temp_paragraph = "This is generated paragraph, replace with your own paragraph."
            
        paragraph_id = f"GENERATED_PARAGRAPH_{loop_count+1}"
        temp_dict = {paragraph_id:temp_paragraph}
        replacement_dict.update(temp_dict)

    return replacement_dict

  def get_code(self):
    replacement_dict = self.gen_replacements()
    gen_html = self.replace_params(self.html_code, replacement_dict)

    return gen_html