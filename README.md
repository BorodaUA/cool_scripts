## Andrii Kovalov Cool Scripts
### How to run project's Docker container:
1. Clone [this](https://github.com/BorodaUA/cool_scripts) repository
2. Create Docker image for the project
```
docker build -t ${PWD##*/}-image .
```
3. Run project's Docker container
```
docker run -d -p 9000:9000 -v ${PWD}:/usr/src/app --name ${PWD##*/}-container ${PWD##*/}-image
```
### How to run project's tests:
1. Run project's tests command
```
docker exec -it ${PWD##*/}-container /bin/sh -c "pytest"
```
2. Create project's coverage report
```
docker exec -it ${PWD##*/}-container /bin/sh -c "pytest --cov-config=.coveragerc --cov"
```
3. Create project's coverage html details
```
docker exec -it ${PWD##*/}-container /bin/sh -c "coverage html"
```
![coverage-example](/README/coverage.jpg?raw=true)  
4. Open coverage html report in [./htmlcov/index.html](./htmlcov/index.html)
## How to run individual scripts:
1. Run command for task_1 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_1_chess_board/task_1.py"
```
2. Run command for task_2 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_2_envelope_analysis/task_2.py"
```
3. Run command for task_3 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_3_triangles_sorting/task_3.py"
```
4. Run command for task_4 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_4_file_parser/task_4.py"
```
5. Run command for task_5 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_5_numbers_convertor/task_5.py"
```
6. Run command for task_6 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_6_lucky_tickets/task_6.py"
```
7. Run command for task_7 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_7_number_sequence/task_7.py"
```
8. Run command for task_8 initial help:
```
docker exec -it ${PWD##*/}-container /bin/sh -c "python task_8_fibo_range/task_8.py"
```