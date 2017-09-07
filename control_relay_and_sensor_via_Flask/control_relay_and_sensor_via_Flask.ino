#include "DHT.h"

#define DHTPIN 3     // what digital pin we're connected to
#define RELAY_PIN  14

// Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial1.begin(57600);
    dht.begin();
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, 0);
}

void loop() {
    while(Serial1.available())
    {
        // Wait a few seconds between measurements.
        delay(2100);
        String msg = "";
        String s = Serial1.readString();
        //if(s == "sensor\0" || s == "sensor\r")
        if(s == "sensor\0")
        {
            // Reading temperature or humidity takes about 250 milliseconds!
            // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
            float h = dht.readHumidity();
            // Read temperature as Celsius (the default)
            float t = dht.readTemperature();

            // Check if any reads failed and exit early (to try again).
            if (isnan(h) || isnan(t)) {
                msg += "Failed to read from the sensor!";
            }
            else
            {
                // Compute heat index in Celsius (isFahreheit = false)
                float hic = dht.computeHeatIndex(t, h, false);
    
                msg += "Humidity: ";
                msg += h;
                msg += "% ";
                msg += "Temperature: ";
                msg += t;
                msg += "*C ";
                msg += "Heat index: ";
                msg += hic;
                msg += "*C ";
            }
        }
        //else if(s == "relay0\0" || s == "relay0\r")
        else if(s == "relay0\0")
        {
            digitalWrite(RELAY_PIN, 0);
            msg += "Turned off the relay.";
        }
        //else if(s == "relay1\0" || s == "relay1\r")
        else if(s == "relay1\0")
        {
            digitalWrite(RELAY_PIN, 1);
            msg += "Turned on the relay.";
        }
        Serial1.println(msg);
    }
}

