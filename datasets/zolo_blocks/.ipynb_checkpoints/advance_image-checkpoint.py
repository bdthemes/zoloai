import re
from nanoid import generate
import pandas as pd
import random
import json

class Advance_Image():
  def __init__(self, generated_input):
    self.block_type = "advanced-image"
    self.mask_list = ["None", "abstract", "abstract-brush-1", "abstract-brush-2", "aesthetic-blob", "amorphous-blob", "brush", "comment", "container", "hand-drawn-blob",
                     "hexagon", "hexagon-blob", "irregular-blob", "minimal-round", "octagon", "organic-blob", "oval-blob", "pattern", "popup-1", "popup-2", "popup-3",
                     "round-brush", "round-design", "squar-pattern", "testimonial", "triangle-blob"]
    
    self.mask_name = ["None", "Abstract", "Abstract Brush 1", "Abstract Brush 2", "Aesthetic Blob", "Amorphous Blob", "Brush", "Comment", "Container", "Hand Drawn Blob", "Hexagon",
                     "Hexagon Blob", "Irregular Blob", "Minimal Round", "Octagon", "Organic Blob", "Oval Blob", "Pattern", "Popup 1", "Popup 2", "Popup 3", "Round Brush", 
                     "Round Design", "Square Pattern", "Testimonial", "Triangle Blob"]
    
    self.code_all = pd.read_csv(r'zolo_blocks/advanced_image_info.csv')
    
    # Extract image source type
    try:
        self.image_source = generated_input["Image_Source"].upper()
        if self.image_source == "LINK":
            self.image_link = generated_input["IMAGE_LINK"]
            
        if self.image_source not in ["UPLOAD", "LINK"]:
            self.image_source = "UPLOAD"
    except:
        self.image_source = "UPLOAD"
        
    # Extract layout type
    try:
        self.layout = generated_input["Layout"]
        self.layout_overlay = False
        if type(self.layout).__name__ == "dict":
            self.layout_overlay = True
        else:
            self.layout = "Normal"
    except:
        self.layout = "Normal"
    
    # Image ZOLO block code
    if self.image_source == "UPLOAD":
        if self.layout == "Normal":
            self.advanced_image_code = self.code_all["UPLOAD_Normal"]
        else:
            self.advanced_image_code = self.code_all["UPLOAD_Overlay"]
    else: # from link
        if self.layout == "Normal":
            self.advanced_image_code = self.code_all["LINK_Normal"]
        else:
            self.advanced_image_code = self.code_all["LINK_Overlay"]
        
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
    
    # Add image link
    if self.image_source == "LINK":
        IMAGE_LINK = self.image_link
        temp_dict = {"LINK":IMAGE_LINK}
        replacement_dict.update(temp_dict)
    
    # Add heading if overlay
    if self.layout_overlay:
        HEADING = self.layout["HEADING"]
        temp_dict = {"HEADING":HEADING}
        replacement_dict.update(temp_dict)
        
        DESCRIPTION = self.layout["DESCRIPTION"]
        temp_dict = {"DESCRIPTION":DESCRIPTION}
        replacement_dict.update(temp_dict)
    advanced_image_code = self.replace_params(self.advanced_image_code.values[0], replacement_dict)
    
    return advanced_image_code