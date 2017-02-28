from setuptools import setup

setup(name = "stuartpy",
      version = "0.1.8",
      description = "Things to do things",
      url = "http://github.com/skgrange",
      author = "Stuart K. Grange",
      author_email = "",
      license = "MIT",
      packages = ["stuartpy"],
      install_requires = ["xmltodict"],
      scripts = ["bin/restart_network_connection", "bin/dropbox_sync", 
        "bin/pretty_xml", "bin/xml_to_json", "bin/lights_out", 
        "bin/pdf_drop_first_page", "bin/dropbox_start", "bin/pretty_json"],
      zip_safe = False)
