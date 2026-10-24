% Ex - (1-2) a)
clear;
syms y(t);

edo = [diff(y,2) + 5*diff(y,1) + 6*y == cos(2*t)];
dy = diff(y,1);
cond = [y(0) == 1, dy(0) == 0];
ySol = dsolve(edo, cond);

% converta para um vetor de valores numericos e visualize as funcoes utilizando o comando plot.
dt = 0.01;
tn = 0:dt:10;
yn = subs(ySol, tn);
yn = double(yn);

figure;
plot(tn, yn);

% ------------------------------------------------------------------------%
% Ex - (1-2) b)
edo = [diff(y,1) - 6*y == 1 + exp(-2*t)];
cond = [y(0) == 2];
ySol = dsolve(edo, cond);

% converta para um vetor de valores numericos e visualize as funcoes utilizando o comando plot.
dt = 0.01;
tn = 0:dt:10;
yn = subs(ySol, tn);
yn = double(yn);

figure;
plot(tn, yn);

% ------------------------------------------------------------------------%
% Ex - (1-2) c)
edo = [diff(y,2) + 4*diff(y,1) + 3*y == 2*exp(-t)];
dy = diff(y,1);
cond = [y(0) == 0, dy(0) == 2];
ySol = dsolve(edo, cond);

% converta para um vetor de valores numericos e visualize as funcoes utilizando o comando plot.
dt = 0.01;
tn = 0:dt:10;
yn = subs(ySol, tn);
yn = double(yn);

figure;
plot(tn, yn);

% ------------------------------------------------------------------------%
% Ex 3
% massa de m = 1kg, coeficiente elastica da mola k = 0.5 e coeficiente do amortecedor b = 0.2
m = 1;
b = 0.2;
k = 0.5;

% my''(t) + by'(t) + ky(t) = x(t)
edo = [m*diff(y,2) + b*diff(y,1) + k*y == 1];
dy = diff(y,1);

% Dada uma equacao diferencial, determine sua resposta ao degrau unitario yu(t) considerando condicoes iniciais nulas;
cond = [y(0) == 0, dy(0) == 0]; 

yu = dsolve(edo, cond);
h = diff(yu, t);
