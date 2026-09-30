# ENPOWER website: all visible text

Every string the page shows comes from this file. British spelling, no em-dashes.
Image paths are relative to `index.html`.

---

## Meta

- `<title>`: ENPOWER | Chalcogenide thin films for indoor photovoltaics
- meta description: ENPOWER develops sustainable chalcogenide thin film solar cells (kesterite, antimony chalcogenides, CdTe and selenium) for indoor light and low power IoT devices. CETP Joint Call 2023.

## Navigation (left rail, in this order)

1. Project (`#project`)
2. Experimental results (`#results`)
3. Modelling (`#modelling`)
4. Consortium (`#consortium`)
5. Contact (`#contact`)

Theme toggle labels: "Light" / "Dark" (aria-label: "Switch colour theme").

---

## Hero

- Eyebrow: ENPOWER · CETP Joint Call 2023
- Heading (h1): Sustainable chalcogenide thin films for low power photovoltaics
- Subtext: Wide bandgap thin film solar cells designed for the light of offices, homes and factories, in order to power IoT devices without batteries.
- Link (single CTA): See the experimental results → `#results`
- Image: `assets/img/hero.png`
  - alt: Three-dimensional model of a furnished office showing how much light reaches each surface, with a small indoor solar cell marked in red on a desk in front of the window.
  - caption: Realistic indoor PV modelling of a furnished office. The colour scale gives the light reflected by every surface (logarithmic), with 10 W/m² entering through each window and the ceiling panels on; the cell sits on the desk by the left window.

---

## Project (`#project`)

- Section label: 01 · Project
- Heading (h2): Indoor light is a different resource

Paragraphs:

1. The number of connected devices is expected to reach one trillion by 2035, and most of them will still rely on batteries that need replacing, recharging and recycling. A large part of these devices will however operate indoors, where a small solar cell could power them for their whole lifetime. Indoor lighting (LEDs, fluorescent tubes, daylight through a window) emits mostly in the visible range, which shifts the optimum bandgap of the absorber from about 1.1 eV for sunlight to the 1.5 to 2.0 eV region.

2. ENPOWER aims to demonstrate a new generation of cost-efficient, robust and stable PV devices specially designed for indoor applications, based on wide bandgap chalcogenide thin films: kesterites (CZTS), antimony chalcogenides, CdTe and elemental selenium. All of them are made with low-cost, scalable deposition processes and low environmental impact materials, and none of them suffers from the stability issues that still limit perovskite, organic and dye-sensitised cells.

Three work lines (render as a plain three-row list with hairline separators, NOT cards):

- Materials: kesterites (CZTS), Sb chalcogenides, CdTe and elemental Se, with the bandgap tuned for indoor light.
- Devices: identification of the performance limiting factors and optimised architectures, in particular the selective contacts.
- Indoor specificities and real testing: real indoor situations, a dedicated characterisation platform and long-term monitoring.

Timeline (three rows, year label on the left):

- Year 1: IoT device power requirements, indoor characterisation platform, modelling results and optimal indoor architecture.
- Year 2: optimised absorbers (bandgap) and selective contacts.
- Year 3: complete prototype of a PV-powered IoT system and monitoring results.

Figure: `assets/img/results/wp-structure.png`
- alt: Work package structure of ENPOWER, from requirements and device design to absorbers, selective contacts, prototyping and demonstration, with the advisory board below.
- caption: Work package structure and advisory board (Worldsensing, Solems, Soplugged, Metsolar and CTF Solar).

---

## Experimental results (`#results`)

- Section label: 02 · Experimental results
- Heading (h2): Measured under indoor light
- Intro: All the devices below were measured under controlled indoor illumination, at incident powers down to a few tens of µW/cm² and colour temperatures from 2700 to 6000 K. Efficiencies are given both under the standard AM1.5G spectrum and under indoor light, since the two can differ by a factor of almost two for the same cell.

Key figures strip (four values, large numbers with a small label, static, no count-up):

- 18.1 % · Ge-alloyed CZTS at 3 mW/cm² (~10 000 lux)
- 18 % · Sb₂S₃ with sulphide electron transport layers, indoor
- 15.2 % · Cd-free CZTS (ink route, ALD ZTO), indoor
- > 10 % · Elemental selenium, indoor

### 2.1 Indoor characterisation platform

Text: In order to compare devices under realistic and reproducible conditions, we built a characterisation platform around a 28-LED class AAA solar simulator (G2V Pico). Both the incident power and the colour temperature of the source can be varied, covering 24 to 10 248 lux in agreement with the IEC TS 62607-7-2 standard. We also measured the light available at four real positions in the laboratory, which ranges from 1.9 mW/cm² (~9000 lux) near the window down to 0.07 mW/cm² (~280 lux) in the darkest corner.

Table (caption: "Light measured at four positions in the laboratory"):

| Position | Power (mW/cm²) | Illuminance (lux) |
|---|---|---|
| 1 | 1.9 | ~9000 |
| 2 | 0.09 | ~320 |
| 3 | 1.55 | ~7800 |
| 4 | 0.07 | ~280 |

Figures:
- `platform-lab.jpg` · alt: Laboratory office used for the indoor light measurements. · caption: The laboratory where the four positions were measured.
- `platform-simulator.jpg` · alt: The G2V Pico LED solar simulator. · caption: 28-LED class AAA solar simulator (G2V Pico).
- `platform-spectra.png` · alt: Spectral power density of the simulator at several colour temperatures and at 100, 50, 25 and 10 % intensity. · caption: Source spectra at variable colour temperature and incident power.

### 2.2 Kesterite: Li and Na co-doped CZTS

Text: Our first serious attempt with kesterite used a Cu₂ZnSnS₄ absorber (1.5 eV) co-doped with lithium and sodium. The cell reaches 10.1 % under AM1.5G, however it performs much better indoors, with 15 % at 3 mW/cm² (about 10 000 lux). These results were published in Solar RRL (2025).

Reference line (small, linked): "Attaining 15.1% Efficiency in Cu₂ZnSnS₄ Solar Cells Under Indoor Conditions Through Sodium and Lithium Codoping", Solar RRL 2400756 (2025).

Figures:
- `czts-jv.png` · alt: Current-voltage curve of the Li-Na co-doped CZTS cell under AM1.5G, 10.1 % efficiency. · caption: AM1.5G: Voc 722 mV, Jsc 23.4 mA/cm², FF 59.1 %, PCE 10.1 %.
- `czts-sem.png` · alt: Top view and cross-section electron micrographs of the co-doped CZTS absorber. · caption: Top view and cross-section of the Li-Na co-doped absorber.
- `czts-indoor-maps.png` · alt: Maps of open-circuit voltage, short-circuit current, fill factor and efficiency against incident power and colour temperature. · caption: Indoor performance maps against incident power and colour temperature.

### 2.3 Kesterite: Ge-alloyed CZTS

Text: Alloying 10 % Ge into the kesterite widens the bandgap to 1.6 eV, closer to the indoor optimum. The efficiency under AM1.5G increases to 11.7 %, and indoors it reaches 18.1 % at 3 mW/cm². The maps highlight that the efficiency remains remarkably stable across colour temperatures, and stays above ~13.5 % down to the lowest incident powers measured.

Figures:
- `czts-ge-jv.png` · alt: Current-voltage curve of the Ge-alloyed CZTS cell under AM1.5G, 11.7 % efficiency. · caption: AM1.5G: Voc 813 mV, Jsc 21.3 mA/cm², FF 67.8 %, PCE 11.7 %.
- `czts-ge-pce.png` · alt: Efficiency map of the Ge-alloyed CZTS cell against incident power and colour temperature, up to 18.1 %. · caption: Efficiency under LED light.
- `czts-ge-voc.png` · alt: Open-circuit voltage map of the Ge-alloyed CZTS cell. · caption: Open-circuit voltage.
- `czts-ge-ff.png` · alt: Fill factor map of the Ge-alloyed CZTS cell. · caption: Fill factor.
- `czts-ge-jsc.png` · alt: Short-circuit current map of the Ge-alloyed CZTS cell. · caption: Short-circuit current.

### 2.4 Cd-free contacts and selective layers

Text: The CdS buffer absorbs an important part of the blue light, which is precisely where LEDs emit. We therefore replaced it by ZnSnO (ZTO) grown by atomic layer deposition, applied both to the PVD and to the molecular ink routes of CZTS. The PVD route gives a record active area efficiency of 10.11 % under AM1.5G and up to 11 % indoors after optimising the post-deposition treatment, while the ink route gives 9.57 % under AM1.5G and up to 15.2 % indoors. For Sb₂S₃ and Se devices we developed a set of selective layers (TiO₂, ZnS, ZnO, Zn(O,S), Zn(Mg,O) and CdS as electron transport layers; Spiro-OMeTAD and MoOx as hole transport layers). Sulphide based electron transport layers allow the successful growth of Sb₂S₃ absorbers in superstrate configuration, and the best devices reach indoor efficiencies of up to 18 %.

Figures:
- `czts-ink-route.png` · alt: Schematic of the molecular ink route used to prepare CZTS absorbers. · caption: Molecular ink route.
- `contacts-pce.png` · alt: Efficiency map of a Cd-free CZTS device against incident power density and colour temperature, up to 15.2 %. · caption: Efficiency of the Cd-free CZTS (ink route) against incident power and colour temperature.
- `contacts-voc.png` · alt: Open-circuit voltage map of the Cd-free device. · caption: Open-circuit voltage.
- `contacts-ff.png` · alt: Fill factor map of the Cd-free device. · caption: Fill factor.

### 2.5 Elemental selenium

Text: Selenium (about 1.9 eV) is a single element absorber, which makes it one of the simplest materials to process. By thermal evaporation, we optimised the hole transport layer among MoOx, WOx and V₂Ox, and with 20 nm of MoOx the device reaches 5.6 % under AM1.5G. Indoors, both 20 nm of MoOx and 10 nm of V₂O₅ allow to exceed 10 %. With vapour transport deposition, the highest efficiencies are obtained around 120 °C, where the film grows with a (003) orientation; this orientation also gives an improved and stable performance under indoor light, above 10 %.

Figures:
- `se-stack.png` · alt: Layer stack of the selenium cell: glass, FTO, TiO₂, selenium, MoOx and a gold contact. · caption: Superstrate device: SLG / FTO / TiO₂ / Se / MoOx / Au.
- `se-evap-jv.png` · alt: Current-voltage curve of the evaporated selenium cell with 20 nm MoOx under AM1.5G. · caption: AM1.5G with 20 nm MoOx: Voc 760 mV, Jsc 12.8 mA/cm², FF 57.3 %, PCE 5.6 %.
- `se-evap-maps-b.png` · alt: Indoor performance maps of an evaporated selenium device. · caption: Indoor performance maps of an evaporated device (hole transport layer study).
- `se-samples.jpg` · alt: Selenium films deposited by vapour transport deposition along a temperature gradient. · caption: VTD films across the substrate temperature range.
- `se-vtd-temperature-maps.png` · alt: Grid of indoor performance maps for selenium devices grown between 100 and 125 °C. · caption: Indoor maps of VTD devices grown between 125 and 100 °C.

### 2.6 Benchmarking chalcogenide technologies

Text: We measured CdTe, Sb₂S₃, CZTS, Se, nano-Si and a commercial a-Si module on the same platform. Many devices perform surprisingly well indoors, which corroborates their potential for high efficiencies. However, the performance is compromised at very low irradiance when the shunt resistance is too low: Rsh should be at least 1 MΩ·cm², and Rs should not be detrimental.

Figures:
- `benchmark-jv.jpg` · alt: Current-voltage curves of CdTe, Sb₂S₃, CZTS, Se, nano-Si and a-Si devices. · caption: Current-voltage curves of the six technologies.
- `benchmark-maps-2.jpg` · alt: Efficiency maps of the six technologies against incident power and colour temperature. · caption: Indoor efficiency maps of the six technologies.

### 2.7 Advanced characterisation

Text: We developed Raman scattering and reflectance based methodologies in order to assess the thickness and composition of the functional layers directly in the device: (Sb,Bi)₂S₃ alloys, MoOx, ZnSnO, Zn(O,S), i-ZnO and Al:ZnO. The Raman spectra follow the composition of the (Sb,Bi)₂S₃ solid solution, and the reflectance allows to map the apparent thickness of nanometric MoOx layers across a whole sample.

Figures:
- `raman-sbbis.png` · alt: Raman spectra of (Sb,Bi)₂S₃ with increasing bismuth content. · caption: Raman spectra across the (Sb,Bi)₂S₃ solid solution.
- `raman-thickness-maps.png` · alt: Maps of apparent MoOx thickness and roughness over a sample. · caption: In-device apparent thickness of MoOx from reflectance.
- `raman-combinatorial.png` · alt: Combinatorial sample with a thickness gradient and discrete sample set. · caption: Combinatorial and discrete sample designs.

### 2.8 Real-time monitoring

Text: A custom software tracks the maximum power point of the cells and performs periodic current-voltage measurements, in order to follow the devices over long periods under changing light. The example below shows the same cell under three illumination regimes: the efficiency varies by a factor of about 3 and returns cleanly to its baseline.

Figures:
- `monitoring-setup.png` · alt: Monitoring setup with LEDs, power meter and cells, and example traces. · caption: Monitoring setup and example traces.
- `monitoring-pce.png` · alt: Efficiency of one cell over time under three light regimes. · caption: Same cell, three light regimes.

### 2.9 Next steps

Text: The last year focuses on the prototype: electrical interconnection and encapsulation of the cells into mini-modules, and the demonstration of a PV-powered IoT device.

Figure (small inset): `prototype.png` · alt: First prototype of a PV-powered IoT sensor with an antenna. · caption: First PV-powered IoT prototype.

---

## Modelling (`#modelling`)

- Section label: 03 · Modelling
- Heading (h2): Why indoor cells need a different design

Intro: The modelling was used to identify the main performance limiting factors before optimising the devices, and to predict how a cell behaves once placed in a real room.

### 3.1 Optimum bandgap

Text: Under AM1.5G, the thermalisation and transmission losses place the optimum bandgap close to 1.1 to 1.4 eV. Under an LED spectrum, the narrow emission in the visible range moves the optimum to about 1.8 to 1.9 eV, whatever the colour temperature, with detailed balance efficiencies above 50 %.

Figures:
- `theory-sq-am15.png` · alt: Energy losses and converted energy against bandgap under the AM1.5 solar spectrum. · caption: Energy balance against bandgap, AM1.5 solar spectrum.
- `theory-sq-led.png` · alt: Energy losses and converted energy against bandgap under a 5000 K LED. · caption: Energy balance against bandgap, 5000 K indoor LED.
- `theory-pce-eg-cct.png` · alt: Efficiency map against bandgap and colour temperature with the optimum bandgap marked. · caption: Detailed balance efficiency against bandgap and LED colour temperature.

### 3.2 Contacts and resistances

Text: The contact layers are more critical indoors than outdoors: a CdS buffer absorbs a large part of the LED emission, while ZnS is almost transparent in that range. On the electrical side, series resistances up to ~100 Ω·cm² remain acceptable due to the low currents, whereas at low injection a shunt resistance above 10⁵ Ω·cm² is almost mandatory.

Figures:
- `theory-parasitic-absorption.png` · alt: Absorptivity of CdS and ZnS buffers compared with two LED spectra. · caption: Parasitic absorption of the buffer layer against LED spectra (2649 K and 6415 K).
- `theory-pce-rs.png` · alt: Efficiency against series resistance and incident power. · caption: Efficiency against series resistance.
- `theory-pce-rsh.png` · alt: Efficiency against shunt resistance and incident power. · caption: Efficiency against shunt resistance.

### 3.3 Realistic indoor PV modelling

Text: The light reaching a cell depends on where it is placed: the windows, the luminaires, the reflectance of the walls and the furniture all matter. We therefore model the room in three dimensions, solving the inter-reflections on every surface, furniture included, and couple the spectrum reaching the cell to the device model. This gives the power produced over time, the voltage stability (essential for IoT), the energy that can be stored and the efficiency under changing illumination.

Figure: `assets/img/hero.png` (reused, cropped differently) · alt: Three-dimensional model of a furnished office with the light on every surface and the position of the indoor solar cell. · caption: Furnished office, 10 W/m² at each window and ceiling panels on. The cell (red) lies on the desk in front of the left window.

---

## Consortium (`#consortium`)

- Section label: 04 · Consortium
- Heading (h2): Four groups, complementary expertise

Rows (logo, institution, lead):

- UPC · Universitat Politècnica de Catalunya, Barcelona (coordinator) · Marcel Placidi · logo `assets/img/logos/upc-wide.png`
- IREC · Catalonia Institute for Energy Research, Sant Adrià de Besòs · Alejandro Pérez-Rodríguez · logo `assets/img/logos/irec.png`
- TalTech · Tallinn University of Technology · Nicolae Spalatu · logo `assets/img/logos/taltech.png`
- UNIVR · Università degli Studi di Verona · Alessandro Romeo · logo `assets/img/logos/univr.png`

---

## Contact (`#contact`)

- Section label: 05 · Contact
- Heading (h2): Contact
- Text: For any question on the project, collaboration or access to the results, please contact the coordinator.
- Name: Marcel Placidi
- Role: Associate Professor, Universitat Politècnica de Catalunya (UPC) and IREC
- Email: marcel.placidi@upc.edu (mailto link)

---

## Funding strip (MANDATORY, first screen)

AEI rule (Guía de publicidad AEI, v09, 2026): on a project website the funding mention and
logos must appear on every page, and on the home page in the upper part, visible WITHOUT
scrolling. So this strip sits at the top of the page (above or inside the hero), on desktop
and on mobile, and is repeated in the footer.

- Lockup image: `assets/img/logos/miciu-cofinanciado-aei.png` (official MICIU + Cofinanciado por la Unión Europea + AEI lockup, 1800 x 349; keep its own coloured panels, do not recolour or put on a mat; show it at least ~300 px wide on desktop and full width on mobile). alt: Ministerio de Ciencia, Innovación y Universidades, cofinanciado por la Unión Europea, Agencia Estatal de Investigación.
- Statement (Spanish, as required, names must stay in Spanish): Proyecto ENPOWER financiado por MICIU/AEI/10.13039/501100011033 y cofinanciado por la Unión Europea.
- Statement (English, smaller, below): ENPOWER is funded by MICIU/AEI/10.13039/501100011033 and co-funded by the European Union, within the Clean Energy Transition Partnership (CETP) Joint Call 2023 (proposal Cetp-2023-00435).
- Put an HTML comment right before the Spanish statement: `<!-- TODO: insert the AEI grant reference (e.g. PCI2024-xxxxxx) after "Proyecto ENPOWER" once known -->`

## Footer

- ENPOWER logo (`assets/img/logos/enpower.png`, dark theme `enpower-dark.png`, which already carries its own paper tile)
- Funding lockup again + both statements.
- Secondary logos row (smaller than the lockup, never larger): CETP (`cetp.png`), EU "Co-funded by the European Union" (`eu-cofunded-positive.png` light theme, `eu-cofunded-negative.png` dark theme).
- Small line: © 2026 ENPOWER consortium
