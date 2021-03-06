# ioc-parser
IOC Parser is a tool to extract indicators of compromise from security reports in PDF format. A good collection of APT related reports with many IOCs can be found here: [APTNotes](https://github.com/kbandla/APTnotes).

## Usage
**iocp [-h] [-p INI] [-i FORMAT] [-o FORMAT] [-d] [-l LIB] [-s SORT] [-t TARGET_DIR] FILE**
* *FILE* File/directory path to report(s)
* *-p INI* Pattern file
* *-i FORMAT* Input format (pdf/txt/html)
* *-o FORMAT* Output format (csv/json/yara)
* *-d* Deduplicate matches
* *-l LIB* Parsing library
* *-s SORT* Sort documents based on keywords specified in pattern file
* *-t TARGET_DIR* Target directory to sort documents to


## Installation
**pip install ioc_parser**

## Requirements
One of the following PDF parsing libraries:
* [PyPDF2](https://github.com/mstamy2/PyPDF2) - *pip install pypdf2*
* [pdfminer](https://github.com/euske/pdfminer) - *pip install pdfminer*

For HTML parsing support:
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) - *pip install beautifulsoup4*

For HTTP(S) support:
* [requests](http://docs.python-requests.org/en/latest/) - *pip install requests*
