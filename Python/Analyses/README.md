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
python md5_checksum.py [Arg_1] [Arg_2]
```

The Arguments should be **`.txt.`** files. 
You should see something similar to this:
```python
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\Python\Analyses> python .\md5_checksum.py .\ExportPOSStudents.txt .\ExportNutrikidsSkywardCompare.txt
Comparing Files: .\ExportPOSStudents.txt and .\ExportNutrikidsSkywardCompare.txt
Not Matched
```

Both **`[Arg_1]`** and **`[Arg_2]`** should be used as files. 

## How To Compare Two Excel Files Using [excel_diff](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Python/Analyses/excel_diff.py)

## How To Compare Two Excel Files Using [excel_diff_equal_shape.py](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Python/Analyses/excel_diff_equal_shape.py)

## How To Compare Two Excel Files Using [excel_diff_nonequal_shape.py](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Python/Analyses/excel_diff_nonequal_shape.py)
To run the comparison just use the following: 
```python 
python excel_diff_nonequal_shape.py
```
What happens is that the script goes through and looks for a **`v1.xlsx`** and a **`v2.xlsx`** within the directory. 
I have uploaded two test files for such an extent to test the code blocks for you.
Once the script runs you will see something similar to the following:
```
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\Python\Analyses> python .\excel_diff_nonequal_shape.py

Index column: Student

         Last Name  Student ID  Grade Current Date Effective Date   Code
Student
Abe           Fam1           8      9   2020-02-27      2020-02-27      0
Abel          Fam2           2      4   2019-01-01      2026-02-21      1
Ashley        Fam3           3     10   2019-01-05      2019-05-21      2
Gabe          Fam4           1      9   2020-02-27      2020-02-27      0
James         Fam6           5     11   2018-08-02      2018-09-02      0
John          Fam5           4     10   2018-08-01      2018-09-01      2
Jorge         Fam8           7      2   2018-08-04      2018-09-04      1
Juan          Fam7           6      5   2018-08-03      2018-09-03      1

New Rows:     ['Gabe', 'John', 'James', 'Juan', 'Jorge']
Dropped Rows: ['Abe']

Done.
```

