"""
This code demonstrates the application of the collection and formation stage of the Data Ingestion Pipeline for RAG apps with a Python code sample. You can also view or fork the code from the Curriculum GitHub repository.
"""

'''Install requirements
pip3 install pymupdf pandas tabulate
'''


"""Script to identify and format tables in a PDF file using PyMuPDF."""


import os
import pymupdf  # import package PyMuPDF


# get the path of the script
script_path = os.path.dirname(os.path.abspath(__file__))


# construct the path to the PDF file
pdf_path = os.path.join(script_path, "Sales_Report.pdf")


# open the pdf file
pdf = pymupdf.open(pdf_path)


# get the first page
page = pdf[0]


# get the tables in the page
tables = page.find_tables()


# get the first table
table = tables[0]


# convert the table to pandas dataframe
df = table.to_pandas()


# format the dataframe to markdown
markdown_table = df.to_markdown()


# print the markdown table
print(markdown_table)

# Run the file `python collection_and_formatting.py`
