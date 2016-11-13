# CSAOV_ml
The tools for "A Simple Machine Language" which is introduced in "Computer Science"

# l++
l++ is a translater used to transfer the "self-made assembly language" into "A Simple Machine Language". For the grammar of "self-made assembly language", I believe you can readily get it after checking the file of "b_src.txt" and "c_src.txt".

usage:
~~~
python3 l++.py c_src.txt ans.txt
~~~

# Simulator

If you just want running a source file of Machine Language, run
~~~
python3 run.py b.txt
~~~
It won't be stop until execute `C000` or `0000`.

## Pre Execute

Maybe there are some value of registor or memory are needed to be initialized before running source file, you can wrting an initialized script, then indicate init script by options "--pre_file".
~~~
python3 run.py source/ch6_4.txt --pre_file source/ch6_4.pre.txt
~~~

## Single Step Mode

Single Step Mode can be used for debugging. Append `--debug` in command line.

~~~
python3 run.py source/ch6_4.txt --pre_file source/ch6_4.pre.txt --debug
~~~