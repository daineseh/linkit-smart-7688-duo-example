#include <Servo.h>

Servo myservo; // Create a Servo object for servo motor.
int pos = 0;
int pulse = 700;

void setup()
{
    Serial1.begin(57600);
        
    myservo.attach(3, 700, 2300);
    myservo.write(90);
    delay(3000);
}

void loop()
{
    String str = "";
    while (Serial1.available())
    {
        str = Serial1.readString();
        Serial1.println(str);
        
        if (str == "0")
            myservo.detach();
        else if (str == "1")
            myservo.attach(3, 700, 2300);
        else
            pulse = str.toInt();
    }
    myservo.writeMicroseconds(pulse);
}

