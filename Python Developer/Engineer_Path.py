#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
EMBEDDED SYSTEM ENGINEER

| Kategoria                         | Junior Embedded Engineer                                                                   | Mid Embedded Engineer                                                                                  |
|----------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Języki programowania (C/C++)     | Podstawy C/C++, struktury, wskaźniki, proste moduły.                                        | Zaawansowane C/C++ (MISRA, optymalizacja pamięci, modularność, code review).                           |
| Architektura MCU/MPU             | Podstawowa znajomość mikrokontrolerów ARM/AVR/ESP.                                          | Dogłębna znajomość architektur (ARM Cortex-M), pipeline, przerwań, low-power modes.                     |
| Obsługa peryferiów               | Konfiguracja GPIO, UART, I2C, SPI na poziomie przykładów.                                   | Samodzielna konfiguracja skomplikowanych peryferiów (DMA, timers, ADC, PWM, CAN).                      |
| RTOS                             | Użycie gotowych przykładów FreeRTOS (task, queue).                                          | Projektowanie systemu z RTOS: priorytetyzacja tasków, synchronizacja, analiza czasu rzeczywistego.     |
| Embedded Linux                   | Podstawy terminala, struktura katalogów.                                                    | Tworzenie driverów, systemd, praca z Yocto/Buildroot, konfiguracja kernel modules.                      |
| Niskopoziomowe debugowanie       | Podstawy debuggera (breakpoint, step).                                                      | SWD/JTAG, trace, analizatory logiczne, debugowanie race condition i problemów czasu rzeczywistego.     |
| Protokoly komunikacyjne          | Wykorzystanie protokołów w przykładach (UART/I2C).                                           | Projektowanie protokołów, optymalizacja komunikacji, praca z CAN, Modbus, BLE, Ethernet.               |
| Elektronika                      | Podstawy elektroniki cyfrowej, czytanie schematów.                                           | Analiza schematów, podstawy projektowania PCB, dobór komponentów, filtrowanie zasilania.               |
| Systemy wersji                   | Podstawy Git (commit, push).                                                                | Zaawansowany Git (branching, rebase, code review, CI flow).                                             |
| Narzędzia i środowisko           | IDE (Keil, STM32CubeIDE), podstawy CMake.                                                   | Zaawansowane build-systemy (CMake, Ninja), automatyzacja, cross-compiling toolchains.                   |
| Testowanie                       | Proste testy funkcjonalne na sprzęcie.                                                      | Testy jednostkowe (Unity/CMock), testy na symulatorach, testy regresyjne, testy hardware-in-the-loop.  |
| Optymalizacja                    | Brak świadomości kosztów czasowych/pamięciowych.                                             | Profilowanie, optymalizacja czasu wykonania i zużycia pamięci, analiza wykorzystania stosu/heap.       |
| Dokumentacja                     | Pisanie prostych opisów funkcji.                                                            | Tworzenie dokumentacji technicznej, specyfikacji, diagramów architektury, API dla firmware.            |
| Bezpieczeństwo                   | Podstawowe pojęcia (watchdog, CRC).                                                         | Projektowanie niezawodnych systemów, zabezpieczenia firmware, bootloadery, aktualizacje OTA.           |
| Umiejętności projektowe          | Realizacja zadań pod nadzorem.                                                              | Samodzielne prowadzenie modułów projektowych, szacowanie zadań, mentoring młodszych inżynierów.         |

TOOLS:
• C, C++, czasem Python
• Keil uVision, IAR, SEGGER Embedded Studio, STM32CubeIDE
• ARM GCC Toolchain, CLang
• STM32CubeMX, ESP-IDF, Atmel Studio
• FreeRTOS, Zephyr
• SWD/JTAG: ST-Link, J-Link
• Oscyloskop, multimetr, analizator logiczny
• Git, GitLab/GitHub
• CMake, Makefile
• protokoły: UART, SPI, I2C, CAN
• narzędzia debug: GDB, Ozone
• narzędzia do pomiarów energii: Power Profiler Kit, Otii Arc
• Docker (dla CI)
• Jira / Confluence

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Iot ENGINEER

| Kategoria                          | Junior IoT Engineer                                                                           | Mid IoT Engineer                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Podstawy IoT                      | Rozumie koncepcję IoT, podstawowe elementy systemu (device–cloud–app).                        | Projektuje architekturę IoT end-to-end, zna typowe wzorce i modele komunikacji.                          |
| Mikrokontrolery / Firmware        | Podstawy C/C++/MicroPython; proste programy na ESP32/STM32.                                  | Samodzielne projektowanie firmware, RTOS, optymalizacja, praca z wieloma peryferiami.                    |
| Protokły komunikacyjne            | MQTT/HTTP – podstawy; podstawy JSON i serializacji.                                           | MQTT QoS, CoAP, BLE, Thread, LoRaWAN, NB-IoT, projektowanie własnych protokołów wymiany danych.          |
| Łączność / moduły radiowe         | Podstawy Wi-Fi/BLE, konfiguracja gotowych modułów.                                            | Dobór technologii komunikacyjnej (LTE-M, NB-IoT, LoRa), optymalizacja energii, analiza RSSI/SNR.         |
| Cloud IoT                         | Podstawy usług IoT w AWS/Azure/GCP (rejestracja urządzeń).                                   | Integracja urządzeń z chmurą, device shadow, telemetry pipelines, OTA updates w chmurze.                |
| Bezpieczeństwo IoT                | Podstawy szyfrowania i kluczy (TLS, certyfikaty).                                             | Projektowanie bezpiecznego fw, provisioning kluczy, hardening, secure boot, OTA z weryfikacją podpisu.   |
| Edge Computing                    | Podstawy przetwarzania danych lokalnie.                                                       | Architektura edge, filtrowanie danych, offload logiki z chmury, optymalizacja ruchu.                     |
| Elektronika i hardware            | Czytanie podstawowych schematów; rezystory, czujniki, moduły.                                | Dobór elementów, analiza zasilania, filtrowanie, współpraca z hardware w procesie projektowym.           |
| Czujniki i aktuatory              | Podłączenie prostych sensorów (I2C/SPI).                                                     | Kalibracja sensorów, analiza błędów pomiarowych, integracja wielu czujników i sensor-fusion.            |
| Systemy operacyjne                | Podstawy FreeRTOS, podstawy Linux (terminal).                                                 | Yocto/Buildroot, tworzenie driverów, analiza logów, optymalizacja kernel/boot time.                      |
| DevOps IoT / CI                   | Podstawy Git; uruchamianie pipeline’ów testowych.                                             | Automatyzacja buildów firmware, testy na urządzeniach fizycznych, CI/CD dla IoT.                         |
| Testowanie IoT                    | Testy manualne urządzeń, pomiar podstawowych parametrów.                                     | Testy integracyjne (device-cloud), testy sieciowe, testy wytrzymałości, testy zużycia energii.           |
| Zarządzanie energią               | Świadomość, że urządzenie musi oszczędzać energię.                                            | Projektowanie firmware low-power, deep sleep, analizy poboru prądu, wybór odpowiednich MCU/modułów.      |
| Analiza danych IoT                | Podstawy logowania danych i wysyłania telemetrii.                                             | Wstępne przetwarzanie edge, analiza danych sensorowych, wykrywanie anomalii.                             |
| Skalowanie IoT                    | Podłączenie pojedynczego urządzenia do chmury.                                                | Obsługa tysięcy urządzeń, device fleet management, monitoring, rollout aktualizacji OTA.                 |
| Umiejętności projektowe           | Praca według zadań, wymaga wsparcia przy integracji systemów.                                | Samodzielne prowadzenie modułów projektowych, dokumentacja, współpraca z zespołami HW/Cloud/Product.    |

TOOLS:
• Mikrokontrolery: ESP32, STM32, nRF52
• Firmware: C, C++, MicroPython
• ESP-IDF, STM32CubeIDE, Zephyr
• protokoły IoT: MQTT, CoAP, BLE, LoRaWAN, NB-IoT
• narzędzia RF: analizator widma, testery antenowe
• IoT Cloud:
    - AWS IoT Core
    - Azure IoT Hub
    - GCP IoT Core (wycofywany, ale spotykany)
• Docker, docker-compose
• Linux, bash
• Git
• systemy monitoringu: Grafana, Prometheus, Datadog
• narzędzia do testów urządzeń:
    - logic analyzers
    - oscyloskopy
    - JTAG/SWD tools
• OTA update platforms
• JSON, CBOR, Protocol Buffers
• narzędzia sieciowe: Wireshark, MQTT Explorer

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
FIRMWARE ENGINEER

| Kategoria                          | Junior Firmware Engineer                                                                      | Mid Firmware Engineer                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Języki programowania              | Podstawy C/C++, podstawowe wskaźniki, proste moduły.                                          | Zaawansowany C/C++, optymalizacja pamięci, MISRA, architektura firmware.                                     |
| Mikrokontrolery                   | Proste projekty na STM32/ESP32/AVR.                                                           | Znajomość architektury ARM Cortex-M, pipeline, przerwania, low-power modes.                                  |
| Peripherals / HAL                 | Konfiguracja GPIO, UART, I2C, SPI na poziomie przykładów.                                     | Zaawansowana konfiguracja DMA, ADC, PWM, timers, CAN, watchdog, low-level drivers.                           |
| RTOS                              | Podstawy FreeRTOS: tworzenie tasków, kolejki, semafory z tutoriali.                          | Projektowanie systemów RTOS: priorytetyzacja tasków, synchronizacja, unikanie deadlocków, analiza timingów. |
| Debugowanie                       | Breakpointy, step-by-step, podstawy JTAG/SWD.                                                 | Trace, analizatory logiczne, debugowanie race conditions, analiza stosu/heap.                               |
| Komunikacja                       | Proste użycie protokołów: UART, podstawy MQTT/HTTP.                                           | Projektowanie protokołów, obsługa BLE/LoRa/CAN, optymalizacja komunikacji, bezpieczeństwo danych.           |
| Zużycie energii                   | Świadomość deep sleep, ale bez projektowania.                                                 | Optymalizacja low-power, planowanie cykli pracy, analiza poboru energii, dobór trybów uśpienia.             |
| OTA / bootloaders                 | Korzystanie z gotowych rozwiązań OTA.                                                         | Projektowanie bootloaderów, aktualizacje OTA z weryfikacją podpisów, fallback firmware.                     |
| Embedded Linux                    | Podstawy terminala, uruchamianie skryptów.                                                    | Kernel drivers, Yocto/Buildroot, systemd, konfiguracja modułów jądra.                                        |
| Testowanie firmware               | Podstawowe testy funkcjonalne na urządzeniu.                                                  | Testy jednostkowe (Unity), testy HIL, regresja, testy wydajności i stabilności.                             |
| Dokumentacja                      | Opisy funkcji i modułów.                                                                      | Architektura firmware, dokumentacja API, UML, specyfikacja wymagań technicznych.                           |
| Umiejętności projektowe           | Realizacja zadań pod nadzorem.                                                                | Samodzielne prowadzenie modułów, mentoring, estymacja czasu, wsparcie w code review.                         |

TOOLS:
• C, C++, Python (opcjonalnie)
• FreeRTOS, Zephyr, ThreadX
• ARM GCC Toolchain, Clang
• Make, CMake, Ninja
• IDE: Keil uVision, IAR Embedded Workbench, STM32CubeIDE
• debuggery: ST-Link, J-Link, Ozone, GDB
• oscyloskop, analizator logiczny
• narzędzia low-level: OpenOCD
• Git, GitHub/GitLab, Gerrit
• Yocto/Buildroot (jeśli pracuje na Embedded Linux)
• protokoły: UART, I2C, SPI, CAN, USB
• narzędzia do analizy energii: Otii, PPK2
• narzędzia CI: Jenkins, GitLab CI
• narzędzia dokumentacyjne: Doxygen, Confluence

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
HARDWARE ENGINEER

| Kategoria                          | Junior Hardware Engineer                                                                      | Mid Hardware Engineer                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Elektronika analogowa             | Podstawy: rezystory, kondensatory, diody, tranzystory.                                        | Projektowanie układów analogowych: filtry, wzmacniacze, układy pomiarowe, kondycjonowanie sygnałów.         |
| Elektronika cyfrowa               | Podstawowe bramki logiczne, podstawy mikrokontrolerów.                                        | Projektowanie złożonych układów cyfrowych, magistrale (I2C, SPI, UART, CAN), analiza czasowa.               |
| Schematy elektryczne              | Otwieranie i czytanie prostych schematów.                                                      | Samodzielne projektowanie schematów, dobór komponentów, analiza kompatybilności i zaleceń producentów.       |
| PCB Design                        | Podstawy PCB (1–2 warstwy), praca w KiCad/Altium na templatach.                               | Projektowanie wielowarstwowych PCB, separacja sygnałów, impedancja, EMC/EMI, stack-up projektów.           |
| Zasilanie                         | Podstawy stabilizatorów, zasilaczy liniowych.                                                 | Projektowanie sekcji zasilania, buck/boost, filtrowanie, analiza tętnień, zabezpieczenia nadprądowe.        |
| Czujniki i moduły                 | Podłączanie gotowych modułów (np. I2C → sensor temperatury).                                  | Integracja sensorów analogowych/cyfrowych, interpretacja datasheetów, kalibracja torów pomiarowych.         |
| EMC/EMI                           | Świadomość zakłóceń i prostych zasad prowadzenia ścieżek.                                     | Projektowanie układów zgodnych z normami EMC, analiza zakłóceń, redukcja szumów, testy pre-compliance.     |
| Prototypowanie                    | Lutowanie, montaż płytek, uruchamianie gotowych zestawów.                                     | Tworzenie prototypów, debugowanie hardware, analiza sygnałów oscyloskopem, analizatorami, generatory.       |
| Dokumentacja techniczna           | Podstawowe rysunki, opisy komponentów.                                                        | Tworzenie BOM, specyfikacji technicznych, analiza kosztów, dokumentacja produkcyjna.                       |
| Produkcja                         | Świadomość procesu produkcji PCB.                                                             | Współpraca z fabrykami (DFM, DFA), dobór technologii montażu, testy fabryczne.                              |
| Normy i certyfikacja              | Podstawowa znajomość CE/FCC na poziomie pojęć.                                                 | Przygotowanie urządzeń do certyfikacji, testy ESD, HIPOT, bezpieczeństwo urządzeń, dokumentacja zgodności.  |
| Systemy złożone                   | Realizacja prostych modułów.                                                                  | Integracja hardware+firmware, analiza wadliwych układów, projektowanie modułów w złożonych systemach.      |

TOOLS:
• CAD PCB:
    - Altium Designer
    - KiCad
    - Eagle (często legacy)
• Symulatory obwodów:
    - LTSpice
    - PSpice
• Analizatory sygnałów:
    - Oscyloskop
    - Analizator logiczny
    - Multimetr
• JTAG/SWD programatory
• narzędzia EMC:
    - generatory impulsów
    - testery ESD
• narzędzia RF (jeśli IoT / radio):
    - analizator sieci
    - VNA
• Dokumentacja:
    - datasheety sensorów
    - IPC-2221, IPC-7351 (normy PCB)
• Systemy do BOM i produkcji:
    - Altium Concord Pro / Vault
    - Octopart, Digi-Key tools
• Git (opcjonalnie, jeśli współpraca z firmware)
• Python do automatyzacji testów hardware (mile widziane)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PYTHON DEVELOPER

| Kategoria                     | Junior                                                                 | Mid                                                                                     |
|------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Składnia i struktury danych  | Podstawowe struktury danych (listy, słowniki, krotki, zbiory).         | Zaawansowane idiomy: list/dict comprehension, f-strings, moduł `collections`.            |
| OOP                          | Klasy, obiekty, proste dziedziczenie.                                  | SOLID, polimorfizm, wzorce projektowe.                                                   |
| Zaawansowane mechanizmy      | Podstawy wyjątków (`try/except`).                                      | Dekoratory, generatory, context managers, świadomość GIL.                                |
| Algorytmy / Złożoność        | Rozwiązywanie prostych problemów bez analizy złożoności.               | Analiza O(n), optymalizacja wyboru struktur danych.                                      |
| Czysty kod                   |• Zgodność z PEP8, krótkie funkcje.                                      | Refaktoryzacja, modularność, projektowanie architektury.                                |
| Testy                        |• Proste testy jednostkowe, uruchamianie istniejących testów.            | Testy integracyjne, mocking, `pytest` (fixture’y, parametryzacja).                       |
| Git                          | clone, commit, push, pull                                               | rebase, rozwiązywanie konfliktów, strategie branchowania.                                |
| Środowisko pracy             |• `venv`, `pipenv`                                                        | Docker, docker-compose.                                                                  |
| Bazy danych                  |• CRUD, podstawy SQL, proste ORM                                          | Zaawansowany SQL, indeksy, migracje (Alembic), optymalizacja zapytań.                    |
| API                          |• Proste endpointy w Flask/Django.                                       | REST, GraphQL, middleware, serializacja, walidacja.                                      |
| Bezpieczeństwo               |• Podstawy uwierzytelniania.                                              | Zrozumienie XSS, CSRF, SQL Injection, stosowanie dobrych praktyk bezpieczeństwa.         |
| Wydajność / skalowanie       | Brak wiedzy o optymalizacji.                                            | Cache (Redis), async/await, FastAPI, podstawy profilowania i optymalizacji aplikacji.    |

TOOLS:
• Python 3.x
• PyCharm / VS Code
• pip, venv, pipenv, poetry
• Git, GitHub/GitLab/Bitbucket
• pytest, unittest, coverage
• black, flake8, pylint, mypy
• Docker, docker-compose
• Virtualenv / pyenv
• Jupyter Notebook
• FastAPI / Django / Flask
• SQLAlchemy, Alembic
• Requests, httpx
• Celery, Redis
• PostgreSQL / MySQL / SQLite
• REST API tools: Postman, Insomnia
• Logging (logging, structlog)
• CI/CD: GitHub Actions / GitLab CI

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
AUTOMATION TEST ENGINEER

| Kategoria                          | Junior Automation Test Engineer                                                             | Mid Automation Test Engineer                                                                                   |
|-----------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Podstawy testowania               | Znajomość podstaw ISTQB, rodzaje testów, cykl życia oprogramowania.                         | Głębokie zrozumienie strategii testowania, analiz ryzyka, projektowania scenariuszy testowych.                |
| Testy manualne                    | Pisanie prostych przypadków testowych i wykonywanie testów.                                 | Projektowanie kompletnych scenariuszy, tworzenie planów testów, analiza defektów i ich priorytów.             |
| Języki programowania              | Podstawy jednego języka (Python/Java/JavaScript).                                           | Biegłość w języku automatyzacji + dobre praktyki OOP, refaktoryzacja kodu frameworków.                         |
| Automatyzacja testów              | Tworzenie prostych skryptów automatyzacji.                                                  | Projektowanie frameworków automatyzacji, utrzymywanie i rozwijanie istniejących rozwiązań.                     |
| Testy UI                          | Selenium, Playwright – podstawy (lokatory, proste testy).                                   | Zaawansowane lokatory, page object pattern, obsługa danych testowych, stabilizacja testów UI.                 |
| Testy API                         |• Podstawy Postmana, proste testy API (GET/POST).                                             | Automatyzacja API w narzędziach (REST Assured, pytest + requests), mockowanie, testy kontraktowe.              |
| Testy integracyjne / E2E          |• Uruchamianie gotowych testów E2E.                                                           | Projektowanie i optymalizacja pełnych testów E2E, orkiestracja testów, testy w pipeline’ach CI.               |
| CI/CD                             |• Znajomość podstaw działania pipeline’ów.                                                    | Tworzenie i konfiguracja pipeline’ów (GitHub Actions, GitLab CI, Jenkins).                                      |
| Narzędzia testowe                 | Podstawy Jiry, TestRail; podstawy Git.                                                      | Zaawansowane użycie systemów zarządzania testami i Git (branching, code review).                               |
| Bazy danych                       |• Proste zapytania SQL (SELECT).                                                              | Złożone zapytania, JOINy, testowanie warstw danych, walidacja danych w automatyzacji.                          |
| Architektura systemu              |• Ogólny zarys działania aplikacji webowych i API.                                            | Analiza architektury systemu, identyfikacja punktów krytycznych, współpraca z developmentem przy projektowaniu.|
| Testy wydajności                  |• Podstawy JMeter / k6 (uruchamianie scenariuszy).                                            | Tworzenie scenariuszy obciążeniowych, analiza metryk, raportowanie wyników.                                    |
| Debugowanie                       | Identyfikacja podstawowych defektów i analiza logów.                                        | Dogłębne debugowanie problemów, analiza logów aplikacji/serwera, korelacja błędów między warstwami.           |
| Praktyki jakości                  | Trzymanie się checklist, poprawność wykonania testów.                                       | Usprawnianie procesów jakości, proponowanie ulepszeń, optymalizacja zakresu testów.                            |
| Komunikacja i współpraca          | Raportowanie błędów, praca w zespole.                                                       | Współpraca z developerami, product ownerami, prowadzenie przeglądów testów, mentoring juniorów.                |

TOOLS:
• Język automatyzacji: Python / Java / JavaScript
• Selenium / Playwright / Cypress
• pytest / JUnit / TestNG
• Allure / ReportPortal
• Git + systemy CI (GitHub Actions, GitLab CI, Jenkins)
• Postman, Newman•
• REST Assured, requests•
• SQL (PostgreSQL, MySQL)•
• JMeter / Gatling / k6 (testy wydajności)•
• Docker do uruchamiania środowisk testowych•
• TestRail / Zephyr / Xray•
• Jira, Confluence
• Browser DevTools
• narzędzia mocking: WireMock, MockServer•
• Kubernetes – **mile widziane**

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Narzędzia i Technologie Wpólne dla powyższych stanowisk:

| Narzędzie                                             | Gdzie                                   | Status                                                                                                                                                                                                 |
| ----------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Git (oraz GitHub / GitLab)                            | Wszystkie role                          | Niezbędny standard wersjonowania pracy                                                                                                                                                                 |
| Jira / Confluence                                     | Wszystkie role                          | Standard korporacyjny do zarządzania zadaniami i dokumentacją                                                                                                                                          |
| Python                                                | Wszystkie role                          | Oprócz roli Python Developera, Python pojawia się jako: język testów (QA), narzędzie do skryptowania (Embedded/Firmware), język backendu IoT oraz narzędzie do automatyzacji testów sprzętu (Hardware) |
| Docker                                                | Python Dev, QA, IoT, Embedded           | Konteneryzacja środowisk budowania                                                                                                                                                                     |
| CI/CD (GitHub Actions / GitLab CI)                    | Python Dev, QA, Embedded, Firmware, IoT | Automatyzacja testów i budowania kodu (firmware'u lub aplikacji)                                                                                                                                       |
| Języki C / C++                                        | Embedded, Firmware, IoT                 | Hardware musi je rozumieć, by czytać kod                                                                                                                                                               |
| Protokoły Komunikacyjne (UART, SPI, I2C)              | Embedded, Firmware, IoT, Hardware       | Kluczowa wiedza dziedzinowa                                                                                                                                                                            |
| Narzędzia Pomiarowe (Oscyloskop, Analizator Logiczny) | Embedded, Firmware, IoT, Hardware       | Niezbędne do debugowania fizycznego sprzętu                                                                                                                                                            |

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Jakie kompetencje są potrzebne dla Junior & Mid Automation Engineer

| **Kategoria**                     | **Junior Automation Engineer (Entry Level)**                                                                            | **Mid Automation Engineer (Market Standard)**                                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Języki programowania**          | Solidne podstawy jednego języka (Python/Java/JS/TS). Rozumienie pętli, warunków, podstaw OOP.                           | Biegłość w pisaniu czystego kodu (Clean Code), wzorce projektowe (Page Object, Factory), asynchroniczność, obsługa wyjątków.                |
| **Frameworki UI**                 | Podstawy Selenium lub Playwright (uruchamianie testów, proste asercje, lokalizowanie elementów po ID/CSS/XPath).        | Budowa frameworka od zera (Playwright/Cypress), obsługa Shadow DOM, iframes, multiple tabs. Stabilizacja testów (flaky tests).              |
| **Testy API**                     | Rozumienie metod HTTP (GET/POST). Manualne testy w Postman. Proste skrypty w requests (Python) lub REST Assured (Java). | Pełna automatyzacja API w kodzie. Testy kontraktowe, mockowanie serwisów, weryfikacja złożonych JSON-ów, autoryzacja (OAuth2).              |
| **CI / CD & DevOps**              | Wiedza teoretyczna: czym jest pipeline, commit, push. Uruchamianie testów lokalnie.                                     | Konfiguracja pipeline’ów (GitHub Actions / GitLab CI), konteneryzacja testów (Docker), równoległe uruchamianie testów (parallel execution). |
| **Bazy Danych (SQL)**             | Proste zapytania SELECT, WHERE, ORDER BY. Weryfikacja czy rekord powstał.                                               | Złożone JOIN, procedury składowane. Seedowanie bazy — przygotowywanie i czyszczenie danych testowych przed testami.                         |
| **Narzędzia i AI**                | Korzystanie z gotowych promptów do generowania prostych przypadków testowych (ChatGPT/Copilot).                         | Świadome wykorzystanie AI do generowania danych testowych, refaktoryzacji kodu i analizy logów błędów.                                      |
| **Raportowanie i Analiza**        | Zgłaszanie bugów w Jira. Generowanie prostych raportów HTML (np. Allure — podstawy).                                    | Integracja raportowania (Allure/ReportPortal) z CI/CD. Analiza “flaky tests” i Root Cause Analysis nieudanych buildów.                      |
| **Systemy Kontroli Wersji (Git)** | Podstawowe komendy: `git clone`, `add`, `commit`, `push`.                                                               | Praca na branchach (feature branches), rozwiązywanie konfliktów (merge/rebase), udział w Code Review (zatwierdzanie PR-ów).                 |
| **Testy Wydajnościowe**           | Uruchamianie gotowych skryptów (np. w JMeter) przygotowanych przez seniorów.                                            | Pisanie scenariuszy obciążeniowych w kodzie (np. k6 w JS/TS lub Gatling), analiza metryk (RPS, latency).                                    |

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Zaobserwowane narzędzia i technologie:

Python Developer:
-> Zgodność z PEP 8, pisanie czytelnych funkcji.
-> Podstawy Git (clone, commit, push, pull).
-> OOP. Wzorce Projektowe, Polimorfizm, Enkapsulacja, Zasady SOLID.
-> Implementacja prostych widoków/endpointów (np. Flask, Django).

Automatyzacja Testów:
-> Uruchamianie i pisanie prostych testów jednostkowych (unittest, pytest, mocking).
-> Użycie środowisk wirtualnych (Docker).
-> Podstawowe zapytania SQL.
-> REST, API, Postaman.
-> Selenium, Playwright.

