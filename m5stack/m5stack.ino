/*
@author Abdulrahman Othman
@email  abdulrahman.othman@web.de
@date   1.10.2023
@brief  Blind UHF Project
*/

// 52 53 54 0D
const byte hardware_version[] = {0xBB,0x00,0x03,0x00,0x01,0x00,0x04,0x7E};


void setup()
{
  Serial1.setTimeout(10);
  // Start serial communication on Serial1 (TX1, RX0) at the desired baud rate
  Serial1.begin(115200); // Change the baud rate to match your sensor's specification
  Serial.begin(115200);

  // int d_counter = 0;
  // Serial.print("Started  ");
  // while(d_counter!=10)
  // {
  //   Serial.print(" .");
  //   d_counter++;
  // }
  // Serial.println();
 // Serial1.write(reset, sizeof(reset));
  //Serial.println("Restting Reader ][ "+Serial1.readString());
  // delay(2000); 
}

void loop()
{
  Serial.println(hardware_version);
  Serial1.write(hardware_version, sizeof(hardware_version));
  Serial.println(Serial1.readString());
  if (Serial1.available())
  {
    //Serial.println(Serial.readString());
  }
  else
  {
    //Serial1.print("oooo"); //reset, sizeof(reset)
  }
  delay(300);
}

