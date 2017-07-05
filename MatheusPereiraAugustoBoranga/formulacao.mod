set V;
/* set dos itens */

set E dimen 2;
/* set das restricoes (arestas) */

param c;
/* da capacidade da mochila */

param n;
/* numero de itens */

param w{v in V};
/* peso dos itens */

param p{v in V};
/* valor de cada item */

var x{v in V} >= 0 binary;
/* presença de um item na mochila em uma solução (binária) */


maximize cost: sum{v in V} p[v] * x[v];
/* função de maximização */

s.t. capacity: sum{v in V} w[v] * x[v] <= c;
/* restricoes de capacidade */

s.t. conflict{(i,j) in E}: x[i] + x[j] <= 1;
/* restricoes de conflito */

end;
