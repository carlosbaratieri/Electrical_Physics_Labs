% Questao 1
dt = 0.01;
t = -10:dt:10;
x = exp(-t).*(t>=0);
h = exp(-2*t).*(t>=0);
y_conv = conv(x, h, 'same') * dt;

% Questao 2
y_corrigido = conv(x, h, 'same') * dt;

% Questao 3
% Erros de aproximacao numerica devido ao passo de amostragem dt

% Questao 4
dt = 0.0001;

% Questao 5
% A entrada contém um modo que coincide com o modo próprio do sistema

% Questao 6
% O efeito da ressonancia (termo t*exp(-2t))

% Questao 7
u = (t >= 0);
y_degrau = conv(u, h, 'same') * dt;
