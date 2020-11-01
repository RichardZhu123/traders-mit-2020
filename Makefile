CXXFLAGS = -std=gnu++17 -Wall -pthread -lrt

# check if DEBUG=1 is set on the command line
ifeq ($(DEBUG),1)
  CXXFLAGS := $(CXXFLAGS) -O0 -g
else
  CXXFLAGS := $(CXXFLAGS) -O3 -march=native -flto
endif

CXX = g++

mybot: competitor.o
	$(CXX) -o mybot kirin.o competitor.o $(CXXFLAGS)

competitor.o: competitor.cpp
	$(CXX) competitor.cpp $(CXXFLAGS) -c

# for bot testing purposes, edit these
mybot_rich: competitor_rich.o
	$(CXX) -o mybot_rich kirin.o competitor_rich.o $(CXXFLAGS)

competitor_rich.o: competitor_rich.cpp
	$(CXX) competitor_rich.cpp $(CXXFLAGS) -c

# for bot testing purposes, edit these
mybot_varun: competitor_varun.o
	$(CXX) -o mybot_varun kirin.o competitor_varun.o $(CXXFLAGS)

competitor_varun.o: competitor_varun.cpp
	$(CXX) competitor_varun.cpp $(CXXFLAGS) -c


clean:
	rm -f competitor.o mybot
