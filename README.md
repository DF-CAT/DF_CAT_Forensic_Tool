This tool uses open source artifact collecting tools and restruct it to suitable json file for the [DF-CAT web service](http://df-cat.com/).

## Basic usage

1. Download DF_CAT_Tool(aka. CACAT).
2. Collect artifacts.
3. Collected artifacts (json files, called CACAT data) can be used with DF-CAT web service.

## Execute in Python3.10
    pip install -r requirements.txt
then execute `gui_main.py`

## Licenses

[Nirsoft](https://www.nirsoft.net/)  
[Eric Zimmerman's tools](https://ericzimmerman.github.io/#!index.md)

## How to Build?

1. [pip install auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/)
2. Write auto-py-to-exe in your command, like this
![image](https://user-images.githubusercontent.com/99635869/207246439-065c4830-06c0-4d38-9283-bd3ebf779672.png)
3. When the auto-py-to-exe window turns on, put the path of gui_main.py in the Script Location, like this
![image](https://user-images.githubusercontent.com/99635869/207246773-935877da-ba4a-4bf2-898b-6102d8480d87.png)
4. And if you want to create one exe file, if you want to make One File a directory, click One Directory
   Also, if you want to display Console Window, click Console Based or Window Based
![image](https://user-images.githubusercontent.com/99635869/207246974-f143a003-f45e-4dc2-9ef8-c96aa98cf730.png)
5. Next, put the path of favorite.ico in the artifact_parser directory in the icon
![image](https://user-images.githubusercontent.com/99635869/207247630-75da0cc6-3844-4206-a9cb-e881e4bf43fc.png)
6. In Additional Files, press Add Files and download.Add the path of py, json_merge_files.py, main.py, favicon.ico
   and add the path of the artifact_parser directory as Add Folder
![image](https://user-images.githubusercontent.com/99635869/207248230-c2036c46-105d-471d-94bf-94007fc465a5.png)
7. In Advanced, write the name of the exe you want to write in -name and enable -uac-admin
![image](https://user-images.githubusercontent.com/99635869/207248336-ff29406e-64ac-44e6-bd9f-341e56f3098b.png)
![image](https://user-images.githubusercontent.com/99635869/207248383-a4156b6c-d51c-4397-9eb0-c552a70e0bcc.png)
8. Lastly, Click The CONVERT .py TO .EXE to create an exe file
