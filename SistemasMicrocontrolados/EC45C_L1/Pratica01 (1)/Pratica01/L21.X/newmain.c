#include <xc.h>
// Configurações
#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config WDT = OFF
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config DEBUG = OFF
#pragma config MCLRE = ON

#define _XTAL_FREQ 20000000

void incremento();
void decremento();

void main(void){
    TRISB = 0b00000111; // portas de entrada
    TRISD = 0; // portas de saída
    LATD = 15;
    while(1) {
        if (PORTBbits.RB0 == 0) {
            if(LATD >= 15){
                LATD = 15;
            }else{
                incremento();
            }
        }
        if (PORTBbits.RB1 == 0) {
            if(LATD <= 0){
                LATD = 0;
            }else{
                decremento();
            }
        }
        if (PORTBbits.RB2 == 0) {
            LATD = 15;
        }
    }
}
void incremento(){
    LATD++;
    __delay_ms(300);
}
void decremento(){
    LATD--;
    __delay_ms(300);
}