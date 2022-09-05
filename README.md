# Start Machine Learning Project
# Software and Account Requirement

1. [GitHub Account]
2. [Heroku Account]
3. [VS Code IDE]
4. [GIT CLI]




Creating Conda environment
```
conda create -p venv python==3.7 -y
```
conda activate venvv\
```
pip install -r requirements.txt
```
To add file to git
```
git add .
```
OR
```
git add <Filename>
```
Note: To  ignore file or folder from git we can write name of file or folder in .gitignore file 
```
to check git status
```
git status
```
to check all versions maintained by git
```
git log
```
to create version/commit all changes  by git
```
git commit -m "message"
```
To send versions/changes to github
```
git push origin main 
```
To check remote URL
```
git remote -v
```
To setup CI/CD pipeline in Heroku we need 3 information

1. HEROKU_EMAIL = ansarisharique.97@gmail.com
2. HEROKU_API_KEY = 30a3a258-2da1-41c7-b4e2-24f32ceb7605
3. HEROKU_APP_NAME =  ml-regression-application

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list Docker Images
```
docker images
```

To Run The image

dock run enable ports -p <port no:port no> enable environment_variable -e PORT=<port_number> image_id
```
docker run -p 5000:5000 -e PORT=5000 d1d5403ff651
```
To check running containers in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>