XGate = {{0, 1}, {1, 0}}
YGate = {{0, -I}, {I, 0}}
ZGate = {{1, 0}, {0, -1}}
PGate[phi_] := {{1, 0}, {0, Exp[I * phi]}}
HGate = 1 / Sqrt[2] * {{1, 1}, {1, -1}}
SGate = PGate[Pi / 2]
TGate = PGate[Pi / 4]
CnotGate = {{1, 0, 0, 0}, {0, 0, 0, 1}, {0, 0, 1, 0}, {0, 1, 0, 0}}
KroneckerProduct[XGate, KroneckerProduct[ZGate, HGate]]

