Xgate ={{0,1}, {1,0}}
Ygate = {{0, -I}, {I, 0}}
Zgate = {{1,0}, {0,-1}}
Pgate[phi_] := {{1, 0}, {0,Exp[I*phi]}}
Hgate = 1/Sqrt[2]*{{1,1}, {1,-1}}
Sgate = Pgate[Pi/2]
Tgate = Pgate[Pi/4]
KroneckerProduct[Xgate, KroneckerProduct[Zgate, Hgate]]

