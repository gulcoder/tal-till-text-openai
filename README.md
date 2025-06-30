# 🎧 Ljudtranskribering med OpenAI Whisper

Detta projekt visar hur man använder OpenAI:s Whisper-modell i Python för att transkribera ljud till text. Du får testa allt från grundläggande transkribering till att skapa egna CLI-verktyg.

## 🎯 Syfte

Utforska hur Whisper-modellen hanterar ljudfiler och genererar textutdata i olika format och språk.

## 🧪 Övningar

### 1️⃣ Övning 1: Grunderna i transkribering med Whisper

**Beskrivning:**  
Lär dig hur man laddar upp en ljudfil och använder OpenAI:s Whisper-modell för att transkribera ljudet till text.

**Mål:**  
Förstå grunderna i `openai.Audio.transcribe`-funktionen.

**Prompt:**  
Transkribera en `.mp3`-fil med tal till text.

**Förväntat utfall:**  
En korrekt textversion av ljudfilens innehåll.

---

### 2️⃣ Övning 2: Transkribera på andra språk

**Beskrivning:**  
Testa hur bra Whisper hanterar icke-engelska språk, t.ex. svenska.

**Mål:**  
Lära sig att specificera språk manuellt vid behov.

**Prompt:**  
Transkribera en svensk talfil.

**Förväntat utfall:**  
Korrekt återgiven svensk text.

---

### 3️⃣ Övning 3: Få texten med timestamps (SRT)

**Beskrivning:**  
Lär dig hur man genererar undertexter i SRT-format från ljud.

**Mål:**  
Förstå hur man använder alternativet `response_format`.

**Prompt:**  
Transkribera till undertextformat.

**Förväntat utfall:**  
En `.srt`-fil med tidskoder och text.

---

### 4️⃣ Övning 4: Jämför olika transkriptionsformat

**Beskrivning:**  
Lär dig hur man hämtar resultat i olika format: `json`, `text`, `verbose_json`.

**Mål:**  
Förstå skillnaden mellan utdataformaten.

**Prompt:**  
Transkribera och visa alla tre formaten.

**Förväntat utfall:**  
Olika utskrifter som visar skillnader i struktur och metadata.

---

### 5️⃣ Övning 5: Bygg ett enkelt CLI för transkribering

**Beskrivning:**  
Skapa ett Python-CLI-verktyg där användaren kan ange ljudfilens namn och välja utdataformat.

**Mål:**  
Praktisera interaktiv Python och transkribering med användarinmatning.

**Prompt:**  
Bygg ett gränssnitt där användaren kan välja fil och format.

**Förväntat utfall:**  
Ett verktyg som låter användaren få transkriptionen enligt valda parametrar.

---
