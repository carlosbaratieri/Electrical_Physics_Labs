// Carlos Gabriel Baratieri
// Leonardo Ruzza

#include <xc.h>

#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config WDT = OFF
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config DEBUG = ON
#pragma config MCLRE = ON

#define _XTAL_FREQ 20000000

#define LED0 LATDbits.LATD0
#define LED1 LATDbits.LATD1

void __interrupt() isr(void) {
    if (PIR1bits.TMR1IF) {
        TMR1H = 0x0B;
        TMR1L = 0xDC;
        LED0 = !LED0;
        PIR1bits.TMR1IF = 0;
    }

    if (PIR2bits.TMR3IF) {
        TMR3H = 0xC2;
        TMR3L = 0xF7;
        LED1 = !LED1;
        PIR2bits.TMR3IF = 0;
    }
}

void main(void) {
    TRISD = 0x00;
    LATD = 0x00;

    LED0 = 1;
    LED1 = 1;

    RCONbits.IPEN = 0;
    INTCONbits.PEIE = 1;
    INTCONbits.GIE = 1;

    T1CON = 0b10110001;
    TMR1H = 0x0B;
    TMR1L = 0xDC;
    PIR1bits.TMR1IF = 0;
    PIE1bits.TMR1IE = 1;

    T3CON = 0b10110001;
    TMR3H = 0xC2;
    TMR3L = 0xF7;
    PIR2bits.TMR3IF = 0;
    PIE2bits.TMR3IE = 1;
    
    while (1) {
    }
}
