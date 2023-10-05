CXX = g++
CXXFLAGS = -march=native -O3 -funroll-loops -std=c++14
BINDIR = ./bin
LENGTH ?= 256

$(BINDIR)/sieveisdlib-$(LENGTH).so: $(BINDIR)/sieveisdlib-$(LENGTH).o
	$(CXX) -shared $(CXXFLAGS) $(BINDIR)/sieveisdlib-$(LENGTH).o -o $(BINDIR)/sieveisdlib-$(LENGTH).so
	@rm -f $(BINDIR)/sieveisdlib-$(LENGTH).o

$(BINDIR)/sieveisdlib-$(LENGTH).o: sieveisdlib.cpp
	@mkdir -p $(BINDIR)
	$(CXX) -fPIC $(CXXFLAGS) -Dmaxn=$(LENGTH) -c sieveisdlib.cpp -o $(BINDIR)/sieveisdlib-$(LENGTH).o

.PHONY: clean

clean:
	rm -rf $(BINDIR)


