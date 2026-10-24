#include <xc.h>
#include "nxlcd.h"

#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config WDT = OFF
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config DEBUG = OFF
#pragma config MCLRE = ON
#define _XTAL_FREQ 20000000

void __interrupt(high_priority) HighISR(void) {
    if (INTCONbits.INT0IF) {
        WriteCmdXLCD(0x01);
        __delay_ms(2);
        WriteCmdXLCD(0x80); 
        putsXLCD("Interrupcao   P1");
        
        WriteCmdXLCD(0xC0); 
        putsXLCD("AGUARDAR 3s");
        __delay_ms(3000);
        
        if(!INTCON3bits.INT1IF){
            WriteCmdXLCD(0x01);
            __delay_ms(2);
            WriteCmdXLCD(0x83);
            putsXLCD("29/09/2026");
        }else{
            WriteCmdXLCD(0x8F); 
            putsXLCD("0");
            WriteCmdXLCD(0xC9);
            putsXLCD("5");
        }
    
        INTCONbits.INT0IF = 0;
    }
}

void __interrupt(low_priority) LowISR(void) {
    if (INTCON3bits.INT1IF) {
        WriteCmdXLCD(0x01);
        __delay_ms(2);
        WriteCmdXLCD(0x80);
        putsXLCD("Interrupcao   P0");
        
        WriteCmdXLCD(0xC0); 
        putsXLCD("AGUARDAR 5s");
        
        __delay_ms(5000);
        
        WriteCmdXLCD(0x01);
        __delay_ms(2);
        WriteCmdXLCD(0x83);
        putsXLCD("29/09/2026");
        
        INTCON3bits.INT1IF = 0;
    }
}

void main(void) {
    unsigned char segundos = 0;

    TRISD = 0;
    TRISE = 0;
    
    TRISBbits.TRISB0 = 1;
    TRISBbits.TRISB1 = 1;

    RCONbits.IPEN = 1;
    INTCONbits.GIEH = 1;      
    INTCONbits.GIEL = 1;      
    
    INTCONbits.INT0IE = 1;  
    INTCONbits.INT0IF = 0;

    INTCON3bits.INT1IE = 1;    
    INTCON3bits.INT1IF = 0;
    INTCON3bits.INT1IP = 0;     
    
    OpenXLCD(FOUR_BIT & LINES_5X7);
    WriteCmdXLCD(0x01);
    __delay_ms(2);
    
    WriteCmdXLCD(0x83);
    putsXLCD("29/09/2026");

    while(1) {
        WriteCmdXLCD(0xC2);
        putsXLCD("SEGUNDOS: ");
        
        putcXLCD((segundos / 10) + '0');
        putcXLCD((segundos % 10) + '0');
        
        segundos++;
        __delay_ms(1000);
        
        if (segundos >= 60) {
            segundos = 0;
        }
    }
}
