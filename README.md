# streamlit-cv-maker
CV maker app using StreamLit and Fast APi

### Folder structure
```
app
|-data
    |- about_me.json
    |- Certifications.csv
    |- Educational-background.csv
    |-Projects.csv
    |-Work-Experience.csv
|- main.py --> Fast API backend
|- frontend.py
|requirements.txt
```

 Recommeded to use and/or create virtual environment (I have used conda)
 ```
 conda create -n cv-maker python=3.10
 comda activate cv-maker
 pip install -r requirements.txt
 ```

### To view Swagger API 
```
#run following
uvicorn, main:app, --reload
```
then go do
<base-URL>/docs

### To view Front-End 
```
# run following
streamlit, run, frontend.py
```

### To run application
```
python app.py
```