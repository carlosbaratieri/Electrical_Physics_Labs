#include <xc.h>
#include "nxlcd.h"

#pragma config PLLDIV = 5 
#pragma config WDT = OFF
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config DEBUG = OFF
#pragma config MCLRE = ON

#define _XTAL_FREQ 20000000

#define C1 PORTBbits.RB0
#define C2 PORTBbits.RB1
#define C3 PORTBbits.RB2
#define C4 PORTBbits.RB3
#define L0 PORTBbits.RB4
#define L1 PORTBbits.RB5
#define L2 PORTBbits.RB6
#define L3 PORTBbits.RB7

char getKey(void) {
    char k = ' ';

    PORTB = 0b11111110;
    if(!L0) k = 'A';
    else if(!L1) k = 'B';
    else if(!L2) k = 'C';
    else if(!L3) k = 'D';

    PORTB = 0b11111101;
    if(!L0) k = '3';
    else if(!L1) k = '6';
    else if(!L2) k = '9';
    else if(!L3) k = 'E';

    PORTB = 0b11111011;
    if(!L0) k = '2';
    else if(!L1) k = '5';
    else if(!L2) k = '8';
    else if(!L3) k = '0';

    PORTB = 0b11110111;
    if(!L0) k = '1';
    else if(!L1) k = '4';
    else if(!L2) k = '7';
    else if(!L3) k = 'F';

    return(k);
}

unsigned char charToHex(char k) {
    if (k >= '0' && k <= '9')
        return k - '0';
    else if (k >= 'A' && k <= 'F')
        return k - 'A' + 10;
    else
        return 0xFF;
}

void main(void) {
    char tecla = ' ';
    unsigned char posicao = 0xC0;

    OpenXLCD(FOUR_BIT & LINES_5X7);
    WriteCmdXLCD(0x01);
    __delay_ms(2);
    WriteCmdXLCD(0xC0);
    WriteCmdXLCD(0x80);
    putsXLCD("EC45C - 22/09/26");

    TRISB = 0xF0;
    TRISD = 0x00;

    while (1) {
        tecla = getKey();

        if (tecla != ' ') {
            WriteCmdXLCD(posicao);
            putcXLCD(tecla);
            posicao++;
            
            if (posicao > 0xCF) {
                posicao = 0xC0;
            }
            __delay_ms(150);
        }
    }
}
