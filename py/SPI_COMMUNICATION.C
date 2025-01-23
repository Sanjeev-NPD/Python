#include "msp.h" // Include the MSPM0 header file

// Define pin connections
#define CS_PIN     P1_0 // Example CS pin
#define RD_PIN     P1_1 // Example RD pin
#define WR_PIN     P1_2 // Example WR pin
#define DATA_PIN   P1_6 // Example SPI MOSI pin

// Function prototypes
void SPI_Init(void);
void TM1622_Write(uint8_t data);
uint8_t TM1622_Read(void);
void TM1622_Send_Command(uint8_t command);

void GPIO_Init(void) {
    // Configure CS, RD, and WR as GPIO outputs
    P1DIR |= (1 << CS_PIN) | (1 << RD_PIN) | (1 << WR_PIN);
    P1OUT |= (1 << CS_PIN); // Set CS high (inactive)
    P1OUT |= (1 << RD_PIN); // Set RD high (inactive)
    P1OUT |= (1 << WR_PIN); // Set WR high (inactive)
}

void SPI_Init(void) {
    // Configure SPI peripheral
    EUSCI_B0->CTLW0 = EUSCI_B_CTLW0_SWRST; // Put eUSCI state machine in reset
    EUSCI_B0->CTLW0 |= EUSCI_B_CTLW0_MSTR | // Master mode
                       EUSCI_B_CTLW0_MSB  | // MSB first
                       EUSCI_B_CTLW0_SYNC | // Synchronous mode
                       EUSCI_B_CTLW0_CKPL;  // Clock polarity high
    EUSCI_B0->BRW = 0x02; // Set clock divider (adjust as necessary)
    EUSCI_B0->CTLW0 &= ~EUSCI_B_CTLW0_SWRST; // Release eUSCI state machine
    P1SEL0 |= (1 << DATA_PIN) | (1 << SCLK_PIN); // Configure SPI pins
}

void TM1622_Write(uint8_t data) {
    P1OUT &= ~(1 << CS_PIN); // Set CS low
    P1OUT &= ~(1 << WR_PIN); // Set WR low
    while (!(EUSCI_B0->IFG & EUSCI_B_IFG_TXIFG)); // Wait for TX buffer
    EUSCI_B0->TXBUF = data; // Send data
    while (!(EUSCI_B0->IFG & EUSCI_B_IFG_RXIFG)); // Wait for RX buffer
    (void)EUSCI_B0->RXBUF; // Clear RX buffer
    P1OUT |= (1 << WR_PIN); // Set WR high
    P1OUT |= (1 << CS_PIN); // Set CS high
}

uint8_t TM1622_Read(void) {
    uint8_t receivedData = 0;
    P1OUT &= ~(1 << CS_PIN); // Set CS low
    P1OUT &= ~(1 << RD_PIN); // Set RD low
    while (!(EUSCI_B0->IFG & EUSCI_B_IFG_TXIFG)); // Wait for TX buffer
    EUSCI_B0->TXBUF = 0xFF; // Send dummy data
    while (!(EUSCI_B0->IFG & EUSCI_B_IFG_RXIFG)); // Wait for RX buffer
    receivedData = EUSCI_B0->RXBUF; // Read received data
    P1OUT |= (1 << RD_PIN); // Set RD high
    P1OUT |= (1 << CS_PIN); // Set CS high
    return receivedData;
}

void TM1622_Send_Command(uint8_t command) {
    TM1622_Write(command); // Send command
}

int main(void) {
    WDTCTL = WDTPW | WDTHOLD; // Stop watchdog timer

    GPIO_Init(); // Initialize GPIO pins
    SPI_Init();  // Initialize SPI peripheral

    // Example: Send a command to the TM1622
    TM1622_Send_Command(0x80); // Example command (adjust based on TM1622 datasheet)

    while (1) {
        // Main loop
    }
}



// Function to construct and send a WRITE command
void TM1622_Write_Command(uint8_t address, uint8_t data) {
    uint16_t frame = 0;

    // Construct the frame: TYPE CODE (101) + COMMAND CODE (A5-A0, D0-D3)
    frame |= (0b101 << 13);         // Set TYPE CODE (101) in bits [15:13]
    frame |= ((address & 0x3F) << 4); // Set ADDRESS bits (A5-A0) in bits [12:6]
    frame |= (data & 0x0F);         // Set DATA bits (D3-D0) in bits [3:0]

    // Send the frame MSB-first
    TM1622_Write((frame >> 8) & 0xFF); // Send the higher 8 bits
    TM1622_Write(frame & 0xFF);       // Send the lower 8 bits
}

// Function to construct and send a READ command
void TM1622_Read_Command(uint8_t address) {
    uint16_t frame = 0;

    // Construct the frame: TYPE CODE (110) + COMMAND CODE (A5-A0, D0-D3)
    frame |= (0b110 << 13);         // Set TYPE CODE (110) in bits [15:13]
    frame |= ((address & 0x3F) << 4); // Set ADDRESS bits (A5-A0) in bits [12:6]

    // Send the frame MSB-first
    TM1622_Write((frame >> 8) & 0xFF); // Send the higher 8 bits
    TM1622_Write(frame & 0xFF);       // Send the lower 8 bits
}



Continuously Updating an LCD with New Data

int main(void) {
    WDTCTL = WDTPW | WDTHOLD; // Stop watchdog timer

    GPIO_Init(); // Initialize GPIO pins
    SPI_Init();  // Initialize SPI peripheral

    uint8_t address = 0x00; // Starting address for LCD update
    uint8_t data = 0x0;     // Initial data value

    while (1) {
        // Example: Write data to LCD
        TM1622_Write_Command(address, data);

        // Increment data for demonstration
        data++;
        if (data > 0x0F) {
            data = 0x00; // Reset data to 0 after reaching max value
        }

        // Move to next address
        address++;
        if (address > 0x3F) {
            address = 0x00; // Reset address to 0 after reaching max address
        }

        // Delay for a visible update (adjust delay as necessary)
        for (volatile uint32_t i = 0; i < 100000; i++);
    }
}


Read Data and Display Results

int main(void) {
    WDTCTL = WDTPW | WDTHOLD; // Stop watchdog timer

    GPIO_Init(); // Initialize GPIO pins
    SPI_Init();  // Initialize SPI peripheral

    uint8_t address = 0x00; // Address to read data from
    uint8_t receivedData = 0;

    while (1) {
        // Example: Read data from the TM1622
        TM1622_Read_Command(address);

        // Simulate receiving data after the READ command
        receivedData = TM1622_Read();

        // Process received data (e.g., debug output, further processing)
        // For example: Toggle an LED or update a variable

        // Increment address for demonstration
        address++;
        if (address > 0x3F) {
            address = 0x00; // Reset address to 0 after reaching max address
        }

        // Delay to avoid excessive SPI reads (adjust delay as necessary)
        for (volatile uint32_t i = 0; i < 100000; i++);
    }
}

