from img2table.document import image
from img2table.document import PDF
from img2table.ocr import TesseractOCR
from PIL import Image


pdf = PDF(src="test.pdf")

ocr = TesseractOCR(lang="eng")

pdf_tables = pdf.extract_tables(ocr=ocr)

for key in pdf_tables.keys():
    print(key, ":", pdf_tables[key])

#print("Extracted content:", pdf_tables[1][2].content.values())

pdf.to_xlsx('tables.xlsx', ocr=ocr)
    
print('Success')
