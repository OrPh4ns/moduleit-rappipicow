bool vibration = false;
int motorPin = 4;

int ton = 9;

void setup() 
{
}

void loop() {


tone(ton, 400);
delay(200);
noTone(ton);
delay(800);

//tone(ton, 50, 200);

}
