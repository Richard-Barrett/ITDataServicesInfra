## Analyses with Python 
This place will be used to run categorical, comparative, and statistical analyses from a python perspective. 
The main goal is to unify infrastructure under python and any system interactions via systems scripts such as Bash, Powershell, and Z-Shell scripts.

## Excel Diff
The overall excel_diff.py will provide a template in python to create a diff between two excel files. 
You will be able to specify the overall data structures that you wish to highlight. 

![Excel Diff Python Script](https://www.lucidchart.com/publicSegments/view/3d780142-665e-43ca-8d70-6ca42f875a9d/image.jpeg)

## How To Compare Two Files with md5 Checksum
To compare two text files to see if they match you can run the following:
```python 
python md5_checksum.py [Arg_1] [Ard_2]
```

The Arguments should be **`.txt.`** files. 
You should see something similar to this:
```python
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\Python\Analyses> python .\md5_checksum.py .\ExportPOSStudents.txt .\ExportNutrikidsSkywardCompare.txt
Comparing Files: .\ExportPOSStudents.txt and .\ExportNutrikidsSkywardCompare.txt
Not Matched
```

Both **`[Arg_1]`** and **`[Arg_2]`** should be used as files. 


