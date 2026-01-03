import pymupdf
import argparse

# 3. Usage
parser = argparse.ArgumentParser(description="Input and Output file names")
parser.add_argument("in_filename", help="Path to the input file")
parser.add_argument("out_filename", help="Path to the output file")
args = parser.parse_args()

doc = pymupdf.open(args.in_filename) # open a document
out = open(args.out_filename, "wb") # create a text output
for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()
