#define RELAY_PIN 13     // what digital pin we're connected to
int val = 0;

void setup() {
    Serial.begin(9600);
    Serial1.begin(57600);

    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, 0);
    Serial1.println("JQC-3FF Relay test!");
}

void loop() {
    int c = Serial1.read();
    if (c != -1)
    {
        switch(c)
        {
            case '0':
                digitalWrite(RELAY_PIN, 0);
                Serial1.print("Relay Off! Value: ");
                break;
            case '1':
                digitalWrite(RELAY_PIN, 1);
                Serial1.print("Relay On! Value: ");
                break;
        }
        val = digitalRead(RELAY_PIN);
        Serial1.println(val);
    }
}

