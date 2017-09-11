# A simple example of performing line-by-line time profiling in python 

## Install the profiler 
The line profiler is from https://github.com/rkern/line_profiler.git.
```
pip install line_profiler
```
Note that it will install a binary command ''kernprof'' and a python library module ''line_profiler''.

## Run and convert the original python file
```
kernprof -l example.py 
```
Note that @profile decorator is used to define the functions we want to perform profiling in the python script. 


## Get the profiled results
```
python -m line_profiler example.py.lprof
```
