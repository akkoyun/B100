# B100<sup>AA</sup> Design Review

B100 is an open source (open hardware) GSM IoT module. B100 use Telit GE910 GSM modem in communication layer. All hardware is reviewed by manufacturer such as Telit. In this folder all review version files and design review reports are published.

## Review Time Line

**Telit**

| Review Date | Review Version | Review Link      |
|-------------|----------------|------------------|
| 11.01.2021  | Schematic R1   | Telit DR33285 R1 |
| 18.01.2021  | Schematic R2   | Telit DR33285 R2 |
| 21.01.2021  | Schematic R3   | Telit DR33285 R3 |
| 28.01.2021  | Schematic R4   | Telit DR33285 R4 |
| 01.02.2021  | PCB R1         | Telit DR33285 R5 |
| 11.02.2021  | PCB R2         | Telit DR33285 R6 |
|             | PCB R3         | Telit DR33285 R7 |

### Telit DR33285 R1

| Power Supply | Missing Information   |
|--------------|-----------------------|
| SIM Pins     | Improvements possible |
| Digital Pins | Fail                  |
| Audio        | Not Applicable        |
| RF           | Improvements possible |

#### Power supply

* Missing information on the 1V8 supply used for powering level shifter sides connected to the Telit modem.

#### SIM pins

* C34 capacitor on SIMVCC shall be sized up to 1uF or 100nF.

#### Digital pins

* In order to avoid back powering, it is strongly recommended to avoid having any HIGH logic level signal applied to the digital pins of the GE910 QUAD when the module is powered off or during an ON/OFF transition. The +1V8 power circuitry is not necessary. Use VAUX instead. If the external circuitry is used anyway, select one provided of enable pin, then use modem’s VAUX to control its EN. VAUX output pad is a 1V8@100mA power output specific for external use. In this power configurations, level shifter protect modem against latch-up, since they follow modem power status. When more than 60mA current is absorbed from VAUX, its heating generation contribution to the overall modem heating becomes not neglected.

* The use of open collector buffers or bidirectional voltage level translators with unidirectional signals is in principle correct but they are less immune to RF and dependent on Pull-Up/Down that could be present at any side of the voltage translator; some have different power range for both Vcca and Vccb, in some cases you must guarantee Vcca < Vccb, and their OE should be powered only from Vcca signal. We prefer unidirectional level shifters; if you anyway decide for bidirectional buffers, then those designed for PU/PD like TXS, NXS, FXLA and NVT200x are preferable, they work better if strong PU/PD are internally present like in some of our modems. We strongly suggest using a dual supply buffer component for unidirectional signals like UART. Example of this are SN74AVC2T245, SN74AVC4T774 or SN74LVC2T45, for 5V signals. They are more immune to RF and are independent on Pull-Up or Pull-Down that could be present at any side of the voltage translator. Place 33pF on both power supplies. The Power bank side connected to the modem should be directly powered by modem’s VAUX/PWRMON to prevent latch-up from happening.

#### RF aspects

* We suggest making provision, of 33pF filtering capacitors to GND also on power Sources and signals on input-output connectors (J2, J3,..).