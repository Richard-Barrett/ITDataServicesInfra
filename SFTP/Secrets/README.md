## Secrets
Everything in this directory will be hidden. 
You will not be able to commit anything in here. 
However, you can store txt files and/or what ever is needed in regards to SFTP operations within your overall infrastructure. 
You can make the **`secrets.json`** and the **`files.json`** by using the following scripts:

- **[`python sftp_files_json_maker.py`](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/SFTP/Secrets/sftp_files_json_maker.py)**
- **[`python sftp_secrets_json_maker.py`](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/SFTP/Secrets/sftp_secrets_json_maker.py)**

When you run the above scripts you will see two files populate within the current directory:

**Before Scripts are Ran:**
```bash
.
├── README.md
├── sftp_files_json_maker.py
└── sftp_secrets_json_maker.py
```

**Output:**
```bash
 jessicarey@Jessicas-MacBook-Pro  ~/Git/ITDataServicesInfra/SFTP/Secrets   master  python sftp_files_json_maker.py
JSON will be STD.OUT to files.json
Please check the current working directory for the file.
{
    "get_files": {
        "file_5": "<absolute_path>",
        "file_4": "<absolute_path>",
        "file_1": "<absolute_path>",
        "file_3": "<absolute_path>",
        "file_2": "<absolute_path>"
    },
    "put_files": {
        "file_5": "<absolute_path>",
        "file_4": "<absolute_path>",
        "file_1": "<absolute_path>",
        "file_3": "<absolute_path>",
        "file_2": "<absolute_path>"
    }
}
 jessicarey@Jessicas-MacBook-Pro  ~/Git/ITDataServicesInfra/SFTP/Secrets   master  python sftp_secrets_json_maker.py
JSON will be STD.OUT to secrets.json
Please check the current working directory for the file.
{
    "sftp_credential": {
        "username": "<username>",
        "host": "<hostname>",
        "password": "password",
        "port_num": "<port>",
        "key_file": "<direct_path>"
    }
}
```

**After Scripts are Ran:**
```bash
.
├── README.md
├── files.json
├── secrets.json
├── sftp_files_json_maker.py
└── sftp_secrets_json_maker.py
```
