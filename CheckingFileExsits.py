import time
from pathlib import Path



get_pdf_file_name = 'Biomechanical Evaluation of Movement in Sport and Exercise_ The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science) ( PDFDrive ).pdf'
print(len('D:/InterestBasedDownload/Biomechanical Evaluation of Movement in Sport and Exercise_ The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science) ( PDFDrive ).pdf'))
print(len('D:/InterestBasedDownload/' + get_pdf_file_name))

while True:
    file_path = Path( 'D:/InterestBasedDownload/' + get_pdf_file_name)
    print('file_path = ', file_path.is_file())
    if file_path.is_file():
        break
    else:
        time.sleep(5)

# D:\InterestBasedDownload\Biomechanical Evaluation of Movement in Sport and Exercise The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science)( PDFDrive ).pdf
# D:\InterestBasedDownload\Biomechanical Evaluation of Movement in Sport and Exercise_ The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science) ( PDFDrive ).pdf

# D:\InterestBasedDownload\Biomechanical Evaluation of Movement in Sport and Exercise_ The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science) ( PDFDrive )
# D:\InterestBasedDownload\Biomechanical Evaluation of Movement in Sport and Exercise_ The British Association of Sport and Exercise Sciences Guide (BASES Sport and Exercise Science) ( PDFDrive )




