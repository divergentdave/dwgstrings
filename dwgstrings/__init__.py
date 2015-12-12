import dxfgrabber
import os
import os.path
import shutil
import subprocess
import tempfile

from . import teigha_file_converter

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
        converter_location = teigha_file_converter.find_teigha()
        try:
            subprocess.check_call([converter_location,
                                   input_directory, temp_directory,
                                   'ACAD2010', 'DXF',
                                   '0',  # recurse
                                   '1',  # audit dwg files
                                   input_basename])
            if os.path.exists(output_path):
                return dxfgrabber.readfile(output_path)
            else:
                raise Exception("Conversion failed, %s was not found" %
                                output_path)
        finally:
            shutil.rmtree(temp_directory)
    else:
        raise Exception("Unsupported filetype: %s" % extension)


def dump_text(path):
    drawing = parse(path)
    print "Dumping text entities"
    for entity in drawing.entities:
        if entity.dxftype == "TEXT":
            print entity.text
        elif entity.dxftype == "MTEXT":
            print entity.plain_text()
        elif entity.dxftype == "INSERT":
            for attrib in entity.attribs:
                print attrib.text
