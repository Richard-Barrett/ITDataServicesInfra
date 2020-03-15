# Secrets
Here you can use Python Scripts to make a secrets file for you to use throughout the cluster. 
Part of the Initial Install Script prompts you for this information. 

- **[Using Python to Make a JSON File](https://realpython.com/python-json/)**

You can make the **secrets.json** by using the following script:

- **[`python secrets_json_maker.py`](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Python/Secrets/secrets_json_maker.py)**

Once you run the script check the wrking directory for a s**`secrets.json`** template that you can use throughout the repository. 

**Before Script is Ran:**
```bash
.
├── README.md
└── secrets_json_maker.py
```

**Output:**
```bash
 jessicarey@Jessicas-MacBook-Pro  ~/Git/ITDataServicesInfra/Python/Secrets   master  python secrets_json_maker.py
JSON will be STD.OUT to secrets.json
Please check the current working directory for the file.
{
    "user": {
        "password": "password",
        "name": "yourname"
    }
}
```

**After Script is Ran:**
```bash
.
├── README.md
├── secrets.json
└── secrets_json_maker.py
```
