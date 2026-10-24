 #include <xc.h>

#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config DEBUG = ON

#define _XTAL_FREQ 20000000

void delay(void) {
 __delay_ms(200);
 }

 void main(void) {
 unsigned char disp7s[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F};
 unsigned int valor = 0;
 unsigned int milhar, centena, dezena, unidade;
 TRISA = 0;
 TRISD = 0;
 TRISE = 0;
 TRISB = 0b00000011;

 while (1) {
 if (PORTBbits.RB0 == 0) {
 if (valor <= 4997) {
 valor += 5;
 } else {
 valor = 4999;
 }
 // delay();
 }

if (PORTBbits.RB1 == 0) {
 if (valor >= 2) {
 valor -= 2;
 } else {
 valor = 0;
 }
 // delay();
 }

 milhar = valor / 1000;
 centena = (valor / 100) % 10;
dezena = (valor / 10) % 10;
 unidade = valor % 10;

LATEbits.LATE2 = 1;
 LATEbits.LATE0 = 0;
 LATAbits.LATA2 = 0;
 LATAbits.LATA5 = 0;

 LATD = disp7s[unidade];
 delay();

 LATEbits.LATE2 = 0;
 LATEbits.LATE0 = 1;
 LATAbits.LATA2 = 0;
 LATAbits.LATA5 = 0;

 LATD = disp7s[dezena];
 delay();

 LATEbits.LATE2 = 0;
 LATEbits.LATE0 = 0;
 LATAbits.LATA2 = 1;
 LATAbits.LATA5 = 0;

 LATD = disp7s[centena];
 delay();
 LATEbits.LATE2 = 0;
 LATEbits.LATE0 = 0;
 LATAbits.LATA2 = 0;
 LATAbits.LATA5 = 1;

 LATD = disp7s[milhar];
 delay();
 }
 }