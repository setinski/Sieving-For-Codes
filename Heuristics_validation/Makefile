CXX = g++
CXXFLAGS = -march=native -O3 -funroll-loops -std=c++14
BINDIR = ./bin
LENGTH ?= 256

sieveisdlib: sieveisdlib.o
	@$(CXX) -shared $(CXXFLAGS) $(BINDIR)/sieveisdlib.o -o $(BINDIR)/$@-$(LENGTH).so
	@rm -f $(BINDIR)/$@.o
	@echo "Compilation finished."

sieveisdlib.o: sieveisdlib.cpp
	@mkdir -p $(BINDIR)
	@$(CXX) -fPIC $(CXXFLAGS) -Dmaxn=$(LENGTH) -c sieveisdlib.cpp -o $(BINDIR)/$@

.PHONY: clean

clean:
	rm -rf $(BINDIR)


