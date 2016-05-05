from setuptools import setup

setup(name = 'stuartpy',
      version = '0.1.3',
      description = 'Things',
      url = 'http://github.com/skgrange',
      author = 'Stuart K. Grange',
      author_email = '',
      license = 'MIT',
      packages = ['stuartpy'],
      install_requires = ["xmltodict"],
      scripts = ["bin/restart_network_connection", "bin/dropbox_sync", 
        "bin/pretty_xml", "bin/xml_json", "bin/lights_out", "bin/pdf_drop_first_page",
        "bin/dropbox_start"],
      zip_safe = False)

