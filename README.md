## Andrii Kovalov Cool Scripts

Create Docker image for the project
```
docker build -t ${PWD##*/}-image .
```
Run project`s Docker container
```
docker run -d -p 9000:9000 -v ${PWD}:/usr/src/app --name ${PWD##*/}-container ${PWD##*/}-image
```