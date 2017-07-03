set V;
/* itens */

set E;

param c;

param n;

param w{v in V};
/* peso dos itens */

param p{v in V};
/* valor de cada item */

var x{v in V} >= 0;
/* presença de um item na mochila nesta solução */



maximize cost: sum{v in V} p[v] * x[v];

s.t. capacity: sum{v in V} w[v] * x[v] <= c;

end;
