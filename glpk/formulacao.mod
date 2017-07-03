set V;
/* itens */

set E dimen 2;

param c;

param n;

param w{v in V};
/* peso dos itens */

param p{v in V};
/* valor de cada item */

var x{v in V} >= 0 binary;
/* presença de um item na mochila nesta solução */



maximize cost: sum{v in V} p[v] * x[v];

s.t. capacity: sum{v in V} w[v] * x[v] <= c;
s.t. conflict{(i,j) in E}: x[i] + x[j] <= 1;

end;
