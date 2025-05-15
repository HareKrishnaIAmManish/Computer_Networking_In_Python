import zipfile
def list_files_in_zip(filename):
    with zipfile.ZipFile(filename) as myzip:
        for zipinfo in myzip.infolist():
            yield zipinfo.filename
for filename in list_files_in_zip("JEEM Full Syllabus Tests-20250503T081030Z-001.zip"):
    print(filename)
    