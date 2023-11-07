/*
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   25.09.2023
@brief  Blind UHF Project
@device Rasp Pi Pico W
@UHF    MetraTec
*/


const String respo = "Response:";
const byte reset[] = {0x52, 0x53, 0x54, 0x0D};
const byte ets[] = {0x53, 0x54, 0x44, 0x20, 0x45, 0x54, 0x53, 0x0D};
const byte sriOn[] = {0x53, 0x52, 0x49, 0x20, 0x4F, 0x4E, 0x0D};
const byte inv[] = {0x49, 0x4E, 0x56, 0x0D};

// SET MSK
const byte setMsk[] = {0x53, 0x45, 0x54, 0x20, 0x4D, 0x53, 0x4B};
const byte tagRead[] = {0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44};
const byte tagRead1[] = {0x52, 0x44, 0x54, 0x20, 0x54, 0x49, 0x44, 0x20, 0x30, 0x20, 0x30};

String words[10];
int wordCount = 0;

// Vibration
bool vibration = false;
int vibPin = 11;
// Ton
int tonPin = 9;

void setup()
{
  // Speed of Serial1 for reading strings
  Serial1.setTimeout(10);
  // Start serial communication on Serial1 (TX1, RX0) at the desired baud rate
  Serial1.begin(115200); // Change the baud rate to match your sensor's specification
  Serial.begin(115200);
  Serial1.write(reset, sizeof(reset));
  Serial.println(respo + "RST=" + Serial1.readString());
  Serial1.write(ets, sizeof(ets));
  Serial.println(respo + "STD ETS=" + Serial1.readString());
  Serial1.write(sriOn, sizeof(sriOn));
  Serial.println(respo + "SRI ON=" + Serial1.readString());
}
void loop()
{
  if (Serial1.available())
  {
    String res = Serial1.readString();
    if (res.indexOf("NSS") != -1)
    {
      Serial.println(respo + "NSS");
      Serial1.write(ets, sizeof(ets));
    }
    else if (res.indexOf("CRT") != -1)
    {
      Serial.println(respo + "CRT");
      Serial1.write(reset, sizeof(reset));
      Serial.println(respo + "RST");
      Serial1.write(ets, sizeof(ets));
      Serial.println(respo + "SRION");
      Serial1.write(sriOn, sizeof(sriOn));
    }
    else if (res.length() > 20)
    {
      res.replace("\n", " ");
      res.replace("IVF", "");
      res.replace("INV ", "");
      res.replace("BOF", "");
      wordCount = 0;
      // Find the first word
      int startIndex = 0;
      int spaceIndex = res.indexOf(' ');
      while (spaceIndex >= 0 && wordCount < 10)
      {
        words[wordCount] = res.substring(startIndex, spaceIndex);
        wordCount++;
        // Update the start and end indices to find the next word
        startIndex = spaceIndex + 1;
        spaceIndex = res.indexOf(' ', startIndex);
      }
      // Handle the last word (if any) after the loop
      if (wordCount < 10)
      {
        words[wordCount] = res.substring(startIndex);
        wordCount++;
      }

      // Print the extracted words
      for (int i = 0; i < wordCount; i++)
      {
        words[i].replace("IVF", "");
        words[i].replace("INV ", "");
        words[i].replace("BOF", "");
        Serial.println(respo + words[i]);
        if (words[i].length() > 20)
          {
            tone(tonPin, 200);
            delay(20);
            noTone(tonPin);
            delay(100);
          }
    }
  }
  else
  {
    Serial.println(respo + "TTC");
    Serial1.write(inv, sizeof(inv));
  }
}}
