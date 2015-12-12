#!/usr/bin/env python
import dxfgrabber
import os
import os.path
import shutil
import subprocess
import sys
import tempfile

CONVERTER_LOCATION = os.path.join(os.environ['PROGRAMFILES'], "ODA", "Teigha Viewer 4.00.1", "TeighaFileConverter.exe")

def parse(path):
  _, extension = os.path.splitext(path)
  extension = extension.lower()
  if extension == '.dxf':
    return dxfgrabber.readfile(path)
  elif extension == '.dwg':
    input_directory, input_basename = os.path.split(os.path.abspath(path))
    output_basename = os.path.splitext(input_basename)[0] + '.dxf'
    temp_directory = tempfile.mkdtemp()
    output_path = os.path.join(temp_directory, output_basename)
    try:
      subprocess.check_call([CONVERTER_LOCATION,
                             input_directory, temp_directory,
                             'ACAD2010', 'DXF',
                             '0', # recurse
                             '1', #audit dwg files
                             input_basename])
      if os.path.exists(output_path):
        return dxfgrabber.readfile(output_path)
      else:
        raise Exception("Conversion failed, %s was not found" % output_path)
    finally:
      shutil.rmtree(temp_directory)
  else:
    raise Exception("Unsupported filetype: %s" % extension)

def main():
  if len(sys.argv) != 2:
    print "Usage: %s file.dwg or %s file.dxf" % (sys.argv[0], sys.argv[0])
    sys.exit(1)

  drawing = parse(sys.argv[1])

  print "Dumping text entities"
  for entity in drawing.entities:
    if entity.dxftype == "TEXT":
      print entity.text
    elif entity.dxftype == "MTEXT":
      print entity.plain_text()
    elif entity.dxftype == "INSERT":
      for attrib in entity.attribs:
        print attrib.text

if __name__ == '__main__':
  main()
