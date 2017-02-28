# Load packages
import socket
import datetime

# Define a tester
def test_internet_connection(server = "www.google.com"):
  
  # Get date
  date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  date = str(date)
  
  try:
    
    host = socket.gethostbyname(server)
    s = socket.create_connection((host, 80), 2)
    print date + ", online"
    return True
    
  except:
    
    print date + ", offline"
    pass
    return False
