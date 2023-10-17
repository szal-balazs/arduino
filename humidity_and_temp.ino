#include <DHT.h>

#define DHTPIN 13

#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float tempC = dht.readTemperature();
  Serial.println(String(humidity)+','+String(tempC));
  Serial.flush();
  delay(2000);
}