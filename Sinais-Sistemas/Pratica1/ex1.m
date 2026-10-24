t = -10:0.01:10;
p = sin(3*t);
f = exp(-t);
m = t.*exp(-t);
q = exp(-t).*cos(t);

figure;
subplot(4,1,1); plot(t, p); grid on; title('p(t) = sin(3t)');
subplot(4,1,2); plot(t, f); grid on; title('f(t) = e^{-t}');
subplot(4,1,3); plot(t, m); grid on; title('m(t) = te^{-t}');
subplot(4,1,4); plot(t, q); grid on; title('q(t) = e^{-t}cos(t)');
xlabel('t');
