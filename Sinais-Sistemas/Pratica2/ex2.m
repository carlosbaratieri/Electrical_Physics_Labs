% Questao 1
% p(t) = e^(2t) -> Derivada: 2*e^(2t)
syms t;
p = exp(2*t);
dp = diff(p, t);

% Questao 2
% m(t) = sin(t) -> Derivada: cos(t)
m = sin(t);
dm = diff(m, t);

% Questao 3
% q(t) = t^3 + 3t^2 + 1 -> Derivada: 3t^2 + 6t
q = t^3 + 3*t^2 + 1;
dq = diff(q, t);

% Questao 4
% r(t) = t*u(t) -> Derivada: u(t) (Heaviside)
syms t real;
r = t * heaviside(t);
dr = diff(r, t);

% Questao 5
% int(e^(2t), t, -1, 1) = (1/2)*(e^2 - e^(-2))
val5 = int(exp(2*t), t, -1, 1);

% Questao 6
% int(sin(t), t, -pi, pi) = 0
val6 = int(sin(t), t, -pi, pi);

% Questao 7
% int(t^3 + 3t^2 + 1, t, -1, 1) = 4
val7 = int(t^3 + 3*t^2 + 1, t, -1, 1);

% Questao 8
% Integrador com entrada u(t) -> r(t) = t*u(t)
syms t;
u = heaviside(t);
saida_integrador = int(u, 0, t);
