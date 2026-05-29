/*
 * SolarGuard — Estação Receptora IoT
 * Computer Organization and Architecture | Global Solution 2026.1
 * FIAP 1CCPY — Grupo 5
 *
 * Simulação no TinkerCAD: Arduino Uno + TMP36 + LDR + Botão + LCD 16x2
 *
 * Pinagem:
 *   TMP36        → A1
 *   Botão vib.   → pino 3
 *   LED alerta   → pino 4
 *   LCD RS       → pino 12
 *   LCD EN       → pino 11
 *   LCD D4–D7   → pinos 10, 9, 8, 7
 *   LDR          → A0 (divisor com resistor 10kΩ para GND)
 */

#include <LiquidCrystal.h>

// ── Definição de pinos ──────────────────────────────────────────────────────
#define TEMP_PIN     A1
#define VIB_PIN      3
#define LED_PIN      4
#define LDR_PIN      A0

// ── Objetos ─────────────────────────────────────────────────────────────────
// LiquidCrystal(RS, EN, D4, D5, D6, D7)
LiquidCrystal lcd(12, 11, 10, 9, 8, 7);

// ── Limiares SolarGuard (alinhados com o sistema Python) ────────────────────
const float TEMP_ATENCAO  = 30.0;   // °C — atenção
const float TEMP_CRITICO  = 35.0;   // °C — crítico
const int   LUZ_ATENCAO   = 400;    // W/m² equivalente — geração comprometida
const int   LUZ_CRITICA   = 200;    // W/m² equivalente — geração insuficiente

// ── Controle de tela ─────────────────────────────────────────────────────────
uint8_t  tela       = 0;
uint8_t  NUM_TELAS  = 4;
unsigned long trocaTela = 0;
const unsigned long INTERVALO = 3000UL;   // 3 s por tela

// ── Controle de leitura ──────────────────────────────────────────────────────
unsigned long ultimaLeitura = 0;
const unsigned long LEITURA = 1000UL;     // 1 s entre leituras

// ── Estado global dos sensores ───────────────────────────────────────────────
float temperatura  = 0.0;
int   irradiancia  = 0;
bool  vibracao     = false;
bool  alertaAtivo  = false;

// ── Protótipos ───────────────────────────────────────────────────────────────
void lerSensores();
void avaliarAlertas();
void atualizarLCD();
void exibirSerial();
void telaStatus();
void telaTemperatura();
void telaIrradiancia();
void telaVibracao();


// ════════════════════════════════════════════════════════════════════════════
//  SETUP
// ════════════════════════════════════════════════════════════════════════════
void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(VIB_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  lcd.setCursor(0, 0);
  lcd.print("  * SOLARGUARD *");
  lcd.setCursor(0, 1);
  lcd.print(" Inicializando..");
  delay(2000);
  lcd.clear();

  Serial.println(F("========================================="));
  Serial.println(F("   SOLARGUARD - Estacao Receptora IoT"));
  Serial.println(F("   Global Solution 2026.1 | FIAP 1CCPY"));
  Serial.println(F("========================================="));
  Serial.println();
}


// ════════════════════════════════════════════════════════════════════════════
//  LOOP PRINCIPAL
// ════════════════════════════════════════════════════════════════════════════
void loop() {
  unsigned long agora = millis();

  if (agora - ultimaLeitura >= LEITURA) {
    ultimaLeitura = agora;
    lerSensores();
    avaliarAlertas();
    exibirSerial();
  }

  if (agora - trocaTela >= INTERVALO) {
    trocaTela = agora;
    lcd.clear();
    tela = (tela + 1) % NUM_TELAS;
  }

  atualizarLCD();

  if (alertaAtivo) {
    digitalWrite(LED_PIN, (millis() / 400) % 2);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
}


// ════════════════════════════════════════════════════════════════════════════
//  LEITURA DE SENSORES
// ════════════════════════════════════════════════════════════════════════════
void lerSensores() {
  // TMP36 — converte leitura analógica para temperatura em °C
  int rawTemp     = analogRead(TEMP_PIN);
  float tensao    = rawTemp * (5.0 / 1023.0);
  temperatura     = (tensao - 0.5) * 100.0;

  // LDR — mapeia 0–1023 para 0–1000 W/m² (irradiância simulada)
  int ldrBruto = analogRead(LDR_PIN);
  irradiancia  = map(ldrBruto, 0, 1023, 0, 1000);

  // Botão — HIGH = vibração/instabilidade detectada
  vibracao = (digitalRead(VIB_PIN) == HIGH);
}


// ════════════════════════════════════════════════════════════════════════════
//  AVALIAÇÃO DE ALERTAS
// ════════════════════════════════════════════════════════════════════════════
void avaliarAlertas() {
  alertaAtivo = (temperatura > TEMP_ATENCAO)
             || (irradiancia  < LUZ_ATENCAO)
             || vibracao;
}


// ════════════════════════════════════════════════════════════════════════════
//  SAÍDA SERIAL
// ════════════════════════════════════════════════════════════════════════════
void exibirSerial() {
  Serial.print(F("Temp: "));
  Serial.print(temperatura, 1);
  Serial.print(F(" C  |  Irrad: "));
  Serial.print(irradiancia);
  Serial.print(F(" W/m2  |  Vib: "));
  Serial.print(vibracao ? F("DETECTADA") : F("Estavel  "));
  Serial.print(F("  |  Alerta: "));
  Serial.println(alertaAtivo ? F("[!] ATIVO") : F("[ ] OK   "));
}


// ════════════════════════════════════════════════════════════════════════════
//  CONTROLE DO LCD
// ════════════════════════════════════════════════════════════════════════════
void atualizarLCD() {
  switch (tela) {
    case 0: telaStatus();       break;
    case 1: telaTemperatura();  break;
    case 2: telaIrradiancia();  break;
    case 3: telaVibracao();     break;
  }
}

void telaStatus() {
  lcd.setCursor(0, 0);
  lcd.print("  * SOLARGUARD *");
  lcd.setCursor(0, 1);
  if (alertaAtivo) {
    lcd.print("! ALERTA ATIVO !");
  } else {
    lcd.print(" Status:    OK  ");
  }
}

void telaTemperatura() {
  lcd.setCursor(0, 0);
  lcd.print("Temp:  ");
  lcd.print(temperatura, 1);
  lcd.print(" C   ");
  lcd.setCursor(0, 1);
  if (temperatura > TEMP_CRITICO) {
    lcd.print("Status: CRITICO ");
  } else if (temperatura > TEMP_ATENCAO) {
    lcd.print("Status: ATENCAO ");
  } else {
    lcd.print("Status: NORMAL  ");
  }
}

void telaIrradiancia() {
  lcd.setCursor(0, 0);
  lcd.print("Irrad: ");
  lcd.print(irradiancia);
  lcd.print(" W/m2  ");
  lcd.setCursor(0, 1);
  if (irradiancia < LUZ_CRITICA) {
    lcd.print("Geracao: CRITICA");
  } else if (irradiancia < LUZ_ATENCAO) {
    lcd.print("Geracao: BAIXA  ");
  } else {
    lcd.print("Geracao: OK     ");
  }
}

void telaVibracao() {
  lcd.setCursor(0, 0);
  lcd.print("Estabilidade:   ");
  lcd.setCursor(0, 1);
  if (vibracao) {
    lcd.print("! INSTABILIDADE!");
  } else {
    lcd.print(" Modulo estavel ");
  }
}
