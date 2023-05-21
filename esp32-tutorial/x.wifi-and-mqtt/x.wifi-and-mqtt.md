# WiFi and MQTT
## Setting up WiFi
1. Open `src/main.cpp` and add the following include statement to the top: `#include <WiFi.h>`.
2. To be able to connect to a wifi network we need add the following lines to the setup() function:
```cpp
WiFi.mode(WIFI_STA);
WiFi.begin("ssid", "password");

Serial.println("establishing wifi connection: ");

while (WiFi.status() != WL_CONNECTED) {
  Serial.print('.');
  delay(1000);
}

Serial.println(WiFi.localIP());
```

<details>
  <summary>Spoiler</summary>

```cpp
#include <Arduino.h>
#include <WiFi.h>

void setup() {
  Serial.begin(9600);

  WiFi.mode(WIFI_STA);
  WiFi.begin("ssid", "password");

  Serial.println("establishing wifi connection: ");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }

  Serial.println(WiFi.localIP());
}

void loop() {
  Serial.println("This is a triumph");

  delay(2000);
}
```
</details>

## Adding MQTT
1. To add MQTT support we need to include a library called `PubSubClient` to the project. Click `Libraries` under `QUICK ACCESS` in the PlatformIO menu and search for `PubSubClient`. Click on the one created by Nick O'Leary and click `Add to project`. Select your project in the dropdown and click `Add`.