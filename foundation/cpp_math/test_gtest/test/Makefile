CXX = g++
CXXFLAGS = -g  -lgtest -lgtest_main -lpthread
INCS = -I./ -I../../src/

OBJS = ../../src/Addition.o Addition_Test.o ../../src/Multiply.o Multiply_Test.o

testAll:	$(OBJS)
			$(CXX) $(CXXFLAGS) $(INCS) -o testAll Main_TestAll.cpp $(OBJS)

.cpp.o: 	$(CXX) $(CXXFLAGS) -c $< $@ $(INCS)

clean: rm testAll *.o testAll.xml
	
