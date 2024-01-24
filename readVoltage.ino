void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600)
}

void loop() {
  // put your main code here, to run repeatedly:
  float voltageDifference = analogRead(A0);
  Serial.print(voltageDifference);
}

// Simply read the voltageDifference from Wheatstone Bridge + Arduino
