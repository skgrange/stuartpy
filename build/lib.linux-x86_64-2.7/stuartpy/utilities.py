import os

def list_files(d, sort = True):

  # Expand tilde
  d = os.path.expanduser(d)

  files = [os.path.join(d, f) for f in os.listdir(d)]
  
  if sort:
  
    files.sort()
    
  else:
  
    pass
    
  return files
  

import xmltodict
import json

def xml_to_json(file_input, file_export, pretty = True):
  
  # Load document
  document_file = open(file_input, "r")
  text = document_file.read()

  # Parse xml document
  dict_xml = xmltodict.parse(text)
  
  # Create a json character string
  if pretty:
    
    text_json = json.dumps(dict_xml, sort_keys = False, indent = 2, 
      separators = (",", ": "))
      
  else:
    
    text_json = json.dumps(dict_xml, sort_keys = False, separators = (",", ":"))
  
  # Save json file
  output_file = open(file_export, "w")
  output_file.write(text_json)
  output_file.close()
