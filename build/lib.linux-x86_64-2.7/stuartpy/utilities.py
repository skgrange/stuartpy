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


