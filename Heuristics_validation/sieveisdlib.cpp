#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <bitset>
#include <assert.h>
#include <time.h>
#include <unistd.h>

using namespace std;

#define max_n maxn   // Hardcode maximal code length as a compilation parameter maxn

typedef bitset<max_n> binvec;   
typedef vector<binvec> binmat;

size_t n, c;        // The length n and codimension c of the code.
binmat H;           // The parity check of the code


// Redefining it for abusing builtins
inline int64_t popcnt(binvec& t)
{
    int64_t ham = 0;
    uint64_t * t_ = (uint64_t *) &t;

    for (int j = 0; j < maxn/64; j+=1)
    {
        ham +=__builtin_popcountll(t_[j]);
    }
    return ham;
}

inline int64_t AND_popcnt(const binvec& t, const binvec&  e)
{
    int64_t ham = 0;
    uint64_t * t_ = (uint64_t *) &t;
    uint64_t * e_ = (uint64_t *) &e;

    for (int j = 0; j < maxn/64; j+=1)
    {
        ham +=__builtin_popcountll(t_[j] & e_[j]);
    }
return ham;
}


inline int64_t XOR_popcnt(const binvec& t, const binvec&  e)
{
    int64_t ham = 0;
    uint64_t * t_ = (uint64_t *) &t;
    uint64_t * e_ = (uint64_t *) &e;

    for (int j = 0; j < maxn/64; j+=1)
    {
        ham +=__builtin_popcountll(t_[j] ^ e_[j]);
    }
return ham;
}


inline bool parity_check(const binvec& t, const binvec& h)
{
    return !(AND_popcnt(t, h) % 2);
}

inline binvec sample(uint64_t w)
{
    binvec v;
    v.reset();
    for (int i = 0; i < w;)
    {
        uint64_t p = rand() % n;
        if (v[p]) continue;
        v.set(p);
        i++;
    }
    assert(popcnt(v) == w);
    return v;
}
unordered_set<binvec> L;
// Initialize a list with H random vectors of weight w
void initialize_list(uint64_t w, uint64_t N)
{
    L.clear();
    while (L.size() < N)
    {
        L.insert(sample(w));
    }
}

// Sieve through list L for weigth w  with parity constraint H[s], until we get N elements
void sieve_step(uint64_t w, uint64_t N, uint64_t s, long int*stats)
{
    stats[0] = s + 1;
    
    unordered_set<binvec> R, L0;
    long int tried = 0;
    long int found = 0;
    stats[1] = L.size();
    
    // First split the list according to parity
    for (auto i = L.begin(); i != L.end();) {
        if (!parity_check(*i, H[s])) {i++; continue;}
        L0.emplace(*i);
        i = L.erase(i);
    }


    // Then sieve pairs of parity 1
    for (auto i = L0.begin(); i != L0.end(); ++i) {
        for (auto j = L0.begin(); j != i; ++j) {
            tried++;
            if (XOR_popcnt(*i, *j) != w) continue;
            found++;
            R.emplace(*i ^ *j);
        }
    }


    // Then sieve pairs of parity 1
    for (auto i = L.begin(); i != L.end(); ++i) {
        for (auto j = L.begin(); j != i; ++j) {
            tried++;
            if (XOR_popcnt(*i, *j) != w) continue;
            found++;
            R.emplace(*i ^ *j);
        }
    }

    long int unique_found = R.size();
    long int to_remove = R.size() - N;

    if (to_remove < 0) to_remove = 0;
    auto x = R.begin();
    for (int i = 0; i < to_remove; ++i)
    {
        x = R.erase(x);
    }

    // assert all parities of the new list
    for (auto i = R.begin(); i != R.end(); ++i) {
        assert(parity_check(*i, H[s]));
    }

    R.swap(L);
    R.clear();
    long int collision = found - unique_found;

    stats[2] = tried;
    stats[3] = found;
    stats[4] = unique_found;
    stats[5] = collision;
    stats[6] = to_remove;
}




extern "C" 
{
    void _setup(/*input*/ size_t c_, size_t n_, char* H_, long seed=0)
    {
        c = c_;
        n = n_;
        assert(n <= max_n);
        if (seed==0) seed = time(NULL)+99997*getpid()+123*clock();
        srand(seed);

        H.clear();
        binvec v;
        size_t i = 0;
        for (size_t j = 0; j < c; ++j)
        {
            v.reset();
            for (size_t k = 0; k < n; ++k)
            {
                v[k] = H_[i];
                i++;
            }
            H.push_back(v);
        }
    }
    void _initialize_list(long int w, long int N)
    {
        initialize_list(w, N);
    }
    void _sieve_step(long int w, long int N, int i, long int* stats)
    {
        sieve_step(w, N, i, stats);
    }
}
