A sample project illustrating how to perform unit testing with GoogleTest and CMake

##Building

~~~
mkdir build
cd build
cmake ..
make
~~~

##Running

~~~
cd build && make test
~~~

or

~~~
build/test/testfoo/testfoo
~~~

credit to [this blog post](http://kaizou.org/2014/11/gtest-cmake/) for a detailed explaination of how it works.

~~~
install gtest

 1180  ./testAll --gtest_output="xml:./testAll.xml"
 1182  cat testAll.xml 
 1189  history|tail -n 40 >>README 
~~~
