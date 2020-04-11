
# Readme

## 1 Introduction

The objective of Model is that from the scanned version
of any paper, a handwritten text recognition is followed to capture the
data written. Since, the accuracy rate of the state-of- the-
art hand written character reorganization is not still up to the acceptable level,
we propose to apply an error correction mechanism to reduce the errors. The
solution does not oppose the age-old convention and affordable as it is mostly
a software solution with a minimum hardware requirement.

## 2 Requirements and dependencies

### 2.1 Hardware and OS

- Display resolution of minimum 1024x
- Ubuntu 14.04 LTS
- An internet connection

### 2.2 Software dependencies

2.2.1 Linux packages

- pip
- scipy

2.2.2 Python packages

- reportlab
- qdarkstyle
- requests
- sklearn

## 3 Test on Dataset

- Place the Test Dataset in Directory containing main.py
- Create an empty folder for result text files
- In case input file is 'input' and output file is 'output'. Run the model as : 

python main.py input output 

### Output on Buffalo Dataset

The [Buffalo Dataset](https://drive.google.com/drive/folders/1cm1fv4TMy-kGcvXK6AFjuAWkBDBDuv7A) contains 70 Handwritten Documents and the folder 'output' contians 70 analysed text files



