%males
male(som).
male(anil).
male(harish).
male(maganlal).
male(narsih).
male(ayush).
male(harsh).

%females
female(arti).
female(padmaben).
female(bhanubhen).
female(darshana).
female(bhavi).

%parents
parent(anil , som).
parent(anil , harsh).
parent(arti , som).
parent(arti , harsh).
parent(maganlal, anil).
parent(maganlal, harish ).
parent(maganlal, darshana).
parent(narsih , arti).
parent(harish , ayush).
parent(harish , bhavi).

father(X , Y) :- parent(X, Y), male(X).
mother(X , Y) :- parent(X, Y), female(X).
grandfather(X,Y) :- parent(Z,Y),parent(X,Z), male(X).
grandmother(X,Y) :- parent(Z,Y),parent(X,Z), female(X).
sibling(X,Y) :- parent(Z,Y),parent(Z,X),X\=Y.
uncle(X,Y) :- parent(Z,Y), sibling(X,Z), male(X).
aunt(X,Y) :- parent(Z,Y), sibling(X,Z), female(X).
cousin(X,Y) :- parent(Z,Y),parent(W,X),sibling(Z,W).