# Evolution guide — Pokémon Heartfelt Gold

These tables are generated from the current hg-engine authoring source supplied for Heartfelt Gold. The patch binary has not been independently decoded against these tables. Encounter availability still depends on game progress.

Search for either Pokémon or an item. “Form N” is the engine's numeric form slot. Some special methods depend on engine handlers and still need in-game verification; the final column exposes the exact method constant for source checking.

Sources: [evolution table](../../HG-Engine/data/Evolutions.c), local `Data/Pokemon/Evolution-Methods.csv`, local `Data/Pokemon/Evolution-Policy-Changes.csv`.

| From | Result | Configured requirement | Engine method |
| --- | --- | --- | --- |
| Abra | Kadabra | Lv 16 | EVO_LEVEL |
| Aipom | Ambipom | Lv 34 | EVO_LEVEL |
| Amaura | Aurorus | Lv 39 | EVO_LEVEL |
| Anorith | Armaldo | Lv 40 | EVO_LEVEL |
| Applin | Appletun | Sweet Apple | EVO_STONE |
| Applin | Dipplin | Syrupy Apple | EVO_STONE |
| Applin | Flapple | Tart Apple | EVO_STONE |
| Archen | Archeops | Lv 37 | EVO_LEVEL |
| Arctibax | Baxcalibur | Lv 54 | EVO_LEVEL |
| Aron | Lairon | Lv 32 | EVO_LEVEL |
| Arrokuda | Baraskewda | Lv 26 | EVO_LEVEL |
| Axew | Fraxure | Lv 30 | EVO_LEVEL |
| Azurill | Marill | Friendship | EVO_FRIENDSHIP |
| Bagon | Shelgon | Lv 30 | EVO_LEVEL |
| Baltoy | Claydol | Lv 36 | EVO_LEVEL |
| Barboach | Whiscash | Lv 30 | EVO_LEVEL |
| Basculin White Striped | Basclegion | Lv 30 · Male | EVO_LEVEL_MALE |
| Basculin White Striped | Basclegion (form 1) | Lv 30 · Female | EVO_LEVEL_FEMALE |
| Bayleef | Meganium | Lv 32 | EVO_LEVEL |
| Beldum | Metang | Lv 20 | EVO_LEVEL |
| Bellsprout | Weepinbell | Lv 21 | EVO_LEVEL |
| Bergmite | Avalugg | Lv 37 | EVO_LEVEL |
| Bergmite | Avalugg (form 1) | Dawn Stone | EVO_STONE |
| Bidoof | Bibarel | Lv 15 | EVO_LEVEL |
| Binacle | Barbaracle | Lv 39 | EVO_LEVEL |
| Bisharp | Kingambit | Lv 45 | EVO_LEVEL |
| Blipbug | Dottler | Lv 10 | EVO_LEVEL |
| Blitzle | Zebstrika | Lv 27 | EVO_LEVEL |
| Boldore | Gigalith | Lv 40 | EVO_LEVEL |
| Bonsly | Sudowoodo | Knows Mimic | EVO_HAS_MOVE |
| Bounsweet | Steenee | Lv 18 | EVO_LEVEL |
| Braixen | Delphox | Lv 36 | EVO_LEVEL |
| Bramblin | Bramblgast | Lv 30 | EVO_LEVEL |
| Brionne | Primarina | Lv 34 | EVO_LEVEL |
| Bronzor | Bronzong | Lv 33 | EVO_LEVEL |
| Budew | Roselia | Lv 15 | EVO_LEVEL |
| Buizel | Floatzel | Lv 26 | EVO_LEVEL |
| Bulbasaur | Ivysaur | Lv 16 | EVO_LEVEL |
| Buneary | Lopunny | Friendship | EVO_FRIENDSHIP |
| Bunnelby | Diggersby | Lv 20 | EVO_LEVEL |
| Burmy | Mothim | Lv 20 · Male | EVO_LEVEL_MALE |
| Burmy | Wormadam | Lv 20 · Female | EVO_LEVEL_FEMALE |
| Cacnea | Cacturne | Lv 32 | EVO_LEVEL |
| Capsakid | Scovillain | Fire Stone | EVO_STONE |
| Carkol | Coalossal | Lv 34 | EVO_LEVEL |
| Carvanha | Sharpedo | Lv 30 | EVO_LEVEL |
| Cascoon | Dustox | Lv 10 | EVO_LEVEL |
| Caterpie | Metapod | Lv 7 | EVO_LEVEL |
| Cetoddle | Cetitan | Ice Stone | EVO_STONE |
| Chansey | Blissey | Lv 34 | EVO_LEVEL |
| Charcadet | Armarouge | Auspicious Armor | EVO_STONE |
| Charcadet | Ceruledge | Malicious Armor | EVO_STONE |
| Charjabug | Vikavolt | Thunder Stone | EVO_STONE |
| Charmander | Charmeleon | Lv 16 | EVO_LEVEL |
| Charmeleon | Charizard | Lv 36 | EVO_LEVEL |
| Cherubi | Cherrim | Lv 25 | EVO_LEVEL |
| Chespin | Quilladin | Lv 16 | EVO_LEVEL |
| Chewtle | Drednaw | Lv 22 | EVO_LEVEL |
| Chikorita | Bayleef | Lv 16 | EVO_LEVEL |
| Chimchar | Monferno | Lv 14 | EVO_LEVEL |
| Chinchou | Lanturn | Lv 27 | EVO_LEVEL |
| Chingling | Chimecho | Lv 28 | EVO_LEVEL |
| Clamperl | Gorebyss | Lv 36 · Female | EVO_LEVEL_FEMALE |
| Clamperl | Huntail | Lv 36 · Male | EVO_LEVEL_MALE |
| Clauncher | Clawitzer | Lv 37 | EVO_LEVEL |
| Clefairy | Clefable | Moon Stone | EVO_STONE |
| Cleffa | Clefairy | Lv 15 | EVO_LEVEL |
| Clobbopus | Grapploct | Knows Taunt | EVO_HAS_MOVE |
| Combee | Vespiquen | Lv 21 · Female | EVO_LEVEL_FEMALE |
| Combusken | Blaziken | Lv 36 | EVO_LEVEL |
| Corphish | Crawdaunt | Lv 30 | EVO_LEVEL |
| Corsola | Cursola | Lv 38 | EVO_LEVEL |
| Corvsquire | Corviknite | Lv 38 | EVO_LEVEL |
| Cosmoem | Lunala | Lv 55 · Night | EVO_LEVEL_NIGHT |
| Cosmoem | Solgaleo | Lv 55 · Day | EVO_LEVEL_DAY |
| Cosmog | Cosmoem | Lv 43 | EVO_LEVEL |
| Cottonee | Whimsicott | Sun Stone | EVO_STONE |
| Crabrawler | Crabomnabl | Ice Stone | EVO_STONE |
| Cranidos | Rampardos | Lv 30 | EVO_LEVEL |
| Croagunk | Toxicroak | Lv 37 | EVO_LEVEL |
| Crocalor | Skeledirge | Lv 36 | EVO_LEVEL |
| Croconaw | Feraligatr | Lv 30 | EVO_LEVEL |
| Cubchoo | Beartic | Lv 37 | EVO_LEVEL |
| Cubone | Marowak | Lv 28 | EVO_LEVEL |
| Cubone | Marowak (form 1) | Dusk Stone | EVO_STONE |
| Cufant | Copperajah | Lv 34 | EVO_LEVEL |
| Cutiefly | Ribombee | Lv 25 | EVO_LEVEL |
| Cyndaquil | Quilava | Lv 14 | EVO_LEVEL |
| Dartrix | Decidueye | Lv 34 · Night | EVO_LEVEL_NIGHT |
| Dartrix | Decidueye (form 1) | Lv 34 · Day | EVO_LEVEL_DAY |
| Darumaka | Darmanitan | Lv 35 | EVO_LEVEL |
| Darumaka | Darmanitan (form 1) | Ice Stone | EVO_STONE |
| Deerling | Sawsbuck | Lv 34 | EVO_LEVEL |
| Deerling Autumn | Sawsbuck | Lv 34 | EVO_LEVEL |
| Deerling Summer | Sawsbuck Summer | Lv 34 | EVO_LEVEL |
| Deerling Winter | Sawsbuck | Lv 34 | EVO_LEVEL |
| Deino | Zweilous | Lv 30 | EVO_LEVEL |
| Dewott | Samurott | Lv 36 · Day | EVO_LEVEL_DAY |
| Dewott | Samurott (form 1) | Lv 36 · Night | EVO_LEVEL_NIGHT |
| Dewpider | Araquanid | Lv 22 | EVO_LEVEL |
| Diglett | Dugtrio | Lv 26 | EVO_LEVEL |
| Diglett | Dugtrio (form 1) | Lv 26 | EVO_LEVEL |
| Dipplin | Hydrapple | Knows Dragon Pulse | EVO_HAS_MOVE |
| Doduo | Dodrio | Lv 31 | EVO_LEVEL |
| Dolliv | Arboliva | Lv 35 | EVO_LEVEL |
| Dottler | Orbeetle | Lv 30 | EVO_LEVEL |
| Doublade | Aegislash | Dusk Stone | EVO_STONE |
| Dragonair | Dragonite | Lv 55 | EVO_LEVEL |
| Drakloak | Dragapult | Lv 50 | EVO_LEVEL |
| Dratini | Dragonair | Lv 30 | EVO_LEVEL |
| Dreepy | Drakloak | Lv 30 | EVO_LEVEL |
| Drifloon | Drifblim | Lv 28 | EVO_LEVEL |
| Drilbur | Excadrill | Lv 31 | EVO_LEVEL |
| Drizzile | Inteleon | Lv 35 | EVO_LEVEL |
| Drowzee | Hypno | Lv 26 | EVO_LEVEL |
| Ducklett | Swanna | Lv 35 | EVO_LEVEL |
| Dunsparce | Dudunspars | Knows Hyper Drill | EVO_HAS_MOVE |
| Duosion | Reuniclus | Lv 41 | EVO_LEVEL |
| Duraludon | Archaludon | Metal Alloy | EVO_STONE |
| Dusclops | Dusknoir | Lv 42 | EVO_LEVEL |
| Duskull | Dusclops | Lv 28 | EVO_LEVEL |
| Dwebble | Crustle | Lv 34 | EVO_LEVEL |
| Eelektrik | Eelektross | Thunder Stone | EVO_STONE |
| Eevee | Espeon | Dawn Stone | EVO_STONE |
| Eevee | Flareon | Fire Stone | EVO_STONE |
| Eevee | Glaceon | Ice Stone | EVO_STONE |
| Eevee | Jolteon | Thunder Stone | EVO_STONE |
| Eevee | Leafeon | Leaf Stone | EVO_STONE |
| Eevee | Sylveon | Shiny Stone | EVO_STONE |
| Eevee | Umbreon | Dusk Stone | EVO_STONE |
| Eevee | Vaporeon | Water Stone | EVO_STONE |
| Ekans | Arbok | Lv 22 | EVO_LEVEL |
| Electabuzz | Electivire | Lv 45 | EVO_LEVEL |
| Electrike | Manectric | Lv 26 | EVO_LEVEL |
| Elekid | Electabuzz | Lv 30 | EVO_LEVEL |
| Elgyem | Beheeyem | Lv 42 | EVO_LEVEL |
| Espurr | Meowstic | Lv 25 · Male | EVO_LEVEL_MALE |
| Espurr | Meowstic (form 1) | Lv 25 · Female | EVO_LEVEL_FEMALE |
| Exeggcute | Exeggutor | Leaf Stone | EVO_STONE |
| Exeggcute | Exeggutor (form 1) | Sun Stone | EVO_STONE |
| Farfetch’d | Sirfetch’d | 3 critical hits | EVO_AMOUNT_OF_CRITICAL_HITS |
| Feebas | Milotic | Lv 34 | EVO_LEVEL |
| Fennekin | Braixen | Lv 16 | EVO_LEVEL |
| Ferroseed | Ferrothorn | Lv 40 | EVO_LEVEL |
| Fidough | Dachsbun | Lv 26 | EVO_LEVEL |
| Finizen | Palafin | Lv 38 | EVO_LEVEL |
| Finneon | Lumineon | Lv 31 | EVO_LEVEL |
| Flaaffy | Ampharos | Lv 30 | EVO_LEVEL |
| Flabébé | Floette | Lv 19 | EVO_LEVEL |
| Flabebe Blue Flower | Floette | Lv 19 | EVO_LEVEL |
| Flabebe Orange Flower | Floette | Lv 19 | EVO_LEVEL |
| Flabebe White Flower | Floette | Lv 19 | EVO_LEVEL |
| Flabebe Yellow Flower | Floette | Lv 19 | EVO_LEVEL |
| Flechinder | Talonflame | Lv 35 | EVO_LEVEL |
| Fletchling | Flechinder | Lv 17 | EVO_LEVEL |
| Flittle | Espathra | Lv 35 | EVO_LEVEL |
| Floette | Florges | Shiny Stone | EVO_STONE |
| Floette Blue Flower | Florges | Shiny Stone | EVO_STONE |
| Floette Orange Flower | Florges | Shiny Stone | EVO_STONE |
| Floette White Flower | Florges | Shiny Stone | EVO_STONE |
| Floette Yellow Flower | Florges | Shiny Stone | EVO_STONE |
| Floragato | Mewscarada | Lv 36 | EVO_LEVEL |
| Fomantis | Lurantis | Lv 34 | EVO_LEVEL |
| Foongus | Amoonguss | Lv 39 | EVO_LEVEL |
| Fraxure | Haxorus | Lv 45 | EVO_LEVEL |
| Frigibax | Arctibax | Lv 35 | EVO_LEVEL |
| Frillish | Jellicent | Lv 40 · Male | EVO_LEVEL_MALE |
| Frillish Female | Jellicent (form 1) | Lv 40 · Female | EVO_LEVEL_FEMALE |
| Froakie | Frogadier | Lv 16 | EVO_LEVEL |
| Frogadier | Greninja | Lv 36 | EVO_LEVEL |
| Fuecoco | Crocalor | Lv 16 | EVO_LEVEL |
| Gabite | Garchomp | Lv 48 | EVO_LEVEL |
| Gastly | Haunter | Lv 25 | EVO_LEVEL |
| Geodude | Graveler | Lv 25 | EVO_LEVEL |
| Geodude | Graveler (form 1) | Lv 25 | EVO_LEVEL |
| Gible | Gabite | Lv 24 | EVO_LEVEL |
| Gimmighoul | Gholdengo | Form Argument · 999 | EVO_FORM_ARGUMENT |
| Girafarig | Farigiraf | Knows Twin Beam | EVO_HAS_MOVE |
| Glameow | Purugly | Lv 38 | EVO_LEVEL |
| Gligar | Gliscor | Razor Fang | EVO_STONE |
| Glimmet | Glimmora | Lv 35 | EVO_LEVEL |
| Gloom | Bellossom | Sun Stone | EVO_STONE |
| Gloom | Vileplume | Leaf Stone | EVO_STONE |
| Golbat | Crobat | Lv 38 | EVO_LEVEL |
| Goldeen | Seaking | Lv 33 | EVO_LEVEL |
| Golett | Golurk | Lv 43 | EVO_LEVEL |
| Goomy | Sliggoo | Lv 30 | EVO_LEVEL |
| Goomy | Sliggoo (form 1) | Metal Alloy | EVO_STONE |
| Gossifleur | Eldegoss | Lv 20 | EVO_LEVEL |
| Gothita | Gothorita | Lv 32 | EVO_LEVEL |
| Gothorita | Gothitelle | Lv 41 | EVO_LEVEL |
| Graveler | Golem | Lv 40 | EVO_LEVEL |
| Graveler | Golem (form 1) | Lv 42 | EVO_LEVEL |
| Greavard | Houndstone | Lv 30 | EVO_LEVEL |
| Grimer | Muk | Lv 38 | EVO_LEVEL |
| Grimer | Muk (form 1) | Lv 38 | EVO_LEVEL |
| Grookey | Thwackey | Lv 16 | EVO_LEVEL |
| Grotle | Torterra | Lv 32 | EVO_LEVEL |
| Grovyle | Sceptile | Lv 36 | EVO_LEVEL |
| Growlithe | Arcanine | Fire Stone | EVO_STONE |
| Growlithe | Arcanine (form 1) | Fire Stone | EVO_STONE |
| Grubbin | Charjabug | Lv 20 | EVO_LEVEL |
| Gulpin | Swalot | Lv 26 | EVO_LEVEL |
| Gurdurr | Conkeldurr | Lv 40 | EVO_LEVEL |
| Hakamo-o | Kommo-o | Lv 45 | EVO_LEVEL |
| Happiny | Chansey | Oval Stone | EVO_STONE |
| Hatenna | Hattrem | Lv 32 | EVO_LEVEL |
| Hattrem | Hatterene | Lv 42 | EVO_LEVEL |
| Haunter | Gengar | Lv 40 | EVO_LEVEL |
| Helioptile | Heliolisk | Sun Stone | EVO_STONE |
| Herdier | Stoutland | Lv 32 | EVO_LEVEL |
| Hippopotas | Hippowdon | Lv 34 | EVO_LEVEL |
| Honedge | Doublade | Lv 35 | EVO_LEVEL |
| Hoothoot | Noctowl | Lv 20 | EVO_LEVEL |
| Hoppip | Skiploom | Lv 18 | EVO_LEVEL |
| Horsea | Seadra | Lv 25 | EVO_LEVEL |
| Houndour | Houndoom | Lv 24 | EVO_LEVEL |
| Igglybuff | Jigglypuff | Lv 15 | EVO_LEVEL |
| Impidimp | Morgrem | Lv 32 | EVO_LEVEL |
| Inkay | Malamar | Lv 30 | EVO_LEVEL |
| Ivysaur | Venusaur | Lv 32 | EVO_LEVEL |
| Jangmo-o | Hakamo-o | Lv 35 | EVO_LEVEL |
| Jigglypuff | Wigglytuff | Moon Stone | EVO_STONE |
| Joltik | Galvantula | Lv 36 | EVO_LEVEL |
| Kabuto | Kabutops | Lv 40 | EVO_LEVEL |
| Kadabra | Alakazam | Lv 40 | EVO_LEVEL |
| Kakuna | Beedrill | Lv 10 | EVO_LEVEL |
| Karrablast | Escavalier | Lv 30 | EVO_LEVEL |
| Kirlia | Gallade | Stone #109 · Male | EVO_STONE_MALE |
| Kirlia | Gardevoir | Lv 30 | EVO_LEVEL |
| Klang | Klinklang | Lv 39 | EVO_LEVEL |
| Klink | Klang | Lv 28 | EVO_LEVEL |
| Koffing | Weezing | Lv 35 · Night | EVO_LEVEL_NIGHT |
| Koffing | Weezing (form 1) | Lv 35 · Day | EVO_LEVEL_DAY |
| Krabby | Kingler | Lv 28 | EVO_LEVEL |
| Kricketot | Kricketune | Lv 10 | EVO_LEVEL |
| Krokorok | Krookodile | Lv 40 | EVO_LEVEL |
| Kubfu | Urshifu | Scroll Of Darkness | EVO_STONE |
| Kubfu | Urshifu (form 1) | Scroll Of Waters | EVO_STONE |
| Lairon | Aggron | Lv 42 | EVO_LEVEL |
| Lampent | Chandelure | Dusk Stone | EVO_STONE |
| Larvesta | Volcarona | Lv 45 | EVO_LEVEL |
| Larvitar | Pupitar | Lv 30 | EVO_LEVEL |
| Lechonk | Oinkologne | Lv 18 · Male | EVO_LEVEL_MALE |
| Lechonk | Oinkologne (form 1) | Lv 18 · Female | EVO_LEVEL_FEMALE |
| Ledyba | Ledian | Lv 18 | EVO_LEVEL |
| Lickitung | Lickilicky | Lv 34 | EVO_LEVEL |
| Lileep | Cradily | Lv 40 | EVO_LEVEL |
| Lillipup | Herdier | Lv 16 | EVO_LEVEL |
| Linoone | Obstagoon | Lv 40 | EVO_LEVEL |
| Litleo | Pyroar | Lv 35 · Male | EVO_LEVEL_MALE |
| Litleo | Pyroar (form 1) | Lv 35 · Female | EVO_LEVEL_FEMALE |
| Litten | Torracat | Lv 17 | EVO_LEVEL |
| Litwick | Lampent | Lv 31 | EVO_LEVEL |
| Lombre | Ludicolo | Water Stone | EVO_STONE |
| Lotad | Lombre | Lv 14 | EVO_LEVEL |
| Loudred | Exploud | Lv 40 | EVO_LEVEL |
| Luxio | Luxray | Lv 30 | EVO_LEVEL |
| Machoke | Machamp | Lv 40 | EVO_LEVEL |
| Machop | Machoke | Lv 28 | EVO_LEVEL |
| Magby | Magmar | Lv 30 | EVO_LEVEL |
| Magikarp | Gyarados | Lv 20 | EVO_LEVEL |
| Magmar | Magmortar | Lv 45 | EVO_LEVEL |
| Magnemite | Magneton | Lv 30 | EVO_LEVEL |
| Magneton | Magnezone | Thunder Stone | EVO_STONE |
| Makuhita | Hariyama | Lv 24 | EVO_LEVEL |
| Mankey | Primeape | Lv 28 | EVO_LEVEL |
| Mantyke | Mantine | Lv 32 | EVO_LEVEL |
| Mareanie | Toxapex | Lv 38 | EVO_LEVEL |
| Mareep | Flaaffy | Lv 15 | EVO_LEVEL |
| Marill | Azumarill | Lv 18 | EVO_LEVEL |
| Marshtomp | Swampert | Lv 36 | EVO_LEVEL |
| Maschiff | Mabosstiff | Lv 30 | EVO_LEVEL |
| Meditite | Medicham | Lv 37 | EVO_LEVEL |
| Meltan | Melmetal | Lv 38 | EVO_LEVEL |
| Meowth | Perrserker | Lv 28 | EVO_LEVEL |
| Meowth | Persian | Lv 28 | EVO_LEVEL |
| Meowth | Persian (form 1) | Friendship | EVO_FRIENDSHIP |
| Metang | Metagross | Lv 45 | EVO_LEVEL |
| Metapod | Butterfree | Lv 10 | EVO_LEVEL |
| Mienfoo | Mienshao | Lv 38 | EVO_LEVEL |
| Milcery | Alcremie | Strawberry Sweet | EVO_STONE |
| Milcery | Alcremie (form 1) | Berry Sweet | EVO_STONE |
| Milcery | Alcremie (form 2) | Love Sweet | EVO_STONE |
| Milcery | Alcremie (form 3) | Star Sweet | EVO_STONE |
| Milcery | Alcremie (form 4) | Clover Sweet | EVO_STONE |
| Milcery | Alcremie (form 5) | Flower Sweet | EVO_STONE |
| Milcery | Alcremie (form 6) | Ribbon Sweet | EVO_STONE |
| Mime Jr. | Mr. Mime | Knows Mimic | EVO_HAS_MOVE |
| Mime Jr. | Mr. Mime (form 1) | Ice Stone | EVO_STONE |
| Minccino | Cinccino | Shiny Stone | EVO_STONE |
| Misdreavus | Mismagius | Lv 34 | EVO_LEVEL |
| Monferno | Infernape | Lv 36 | EVO_LEVEL |
| Morelull | Shiinotic | Lv 24 | EVO_LEVEL |
| Morgrem | Grimmsnarl | Lv 42 | EVO_LEVEL |
| Mr. Mime | Mr. Rime | Lv 42 | EVO_LEVEL |
| Mudbray | Mudsdale | Lv 30 | EVO_LEVEL |
| Mudkip | Marshtomp | Lv 16 | EVO_LEVEL |
| Munchlax | Snorlax | Friendship | EVO_FRIENDSHIP |
| Munna | Musharna | Moon Stone | EVO_STONE |
| Murkrow | Honchkrow | Lv 34 | EVO_LEVEL |
| Nacli | Naclstack | Lv 24 | EVO_LEVEL |
| Naclstack | Garganacl | Lv 38 | EVO_LEVEL |
| Natu | Xatu | Lv 25 | EVO_LEVEL |
| Nickit | Thievul | Lv 18 | EVO_LEVEL |
| Nidoran♀ | Nidorina | Lv 16 | EVO_LEVEL |
| Nidoran♂ | Nidorino | Lv 16 | EVO_LEVEL |
| Nidorina | Nidoqueen | Lv 36 | EVO_LEVEL |
| Nidorino | Nidoking | Lv 36 | EVO_LEVEL |
| Nincada | Ninjask | Lv 20 · Ninjask | EVO_LEVEL_NINJASK |
| Nincada | Shedinja | Lv 20 · Shedinja | EVO_LEVEL_SHEDINJA |
| Noibat | Noivern | Lv 38 | EVO_LEVEL |
| Nosepass | Probopass | Lv 34 | EVO_LEVEL |
| Numel | Camerupt | Lv 33 | EVO_LEVEL |
| Nuzleaf | Shiftry | Leaf Stone | EVO_STONE |
| Nymble | Lokix | Lv 24 | EVO_LEVEL |
| Oddish | Gloom | Lv 21 | EVO_LEVEL |
| Omanyte | Omastar | Lv 40 | EVO_LEVEL |
| Onix | Steelix | Lv 30 | EVO_LEVEL |
| Oshawott | Dewott | Lv 17 | EVO_LEVEL |
| Palpitoad | Seismitoad | Lv 36 | EVO_LEVEL |
| Pancham | Pangoro | Lv 32 | EVO_LEVEL |
| Panpour | Simipour | Water Stone | EVO_STONE |
| Pansage | Simisage | Leaf Stone | EVO_STONE |
| Pansear | Simisear | Fire Stone | EVO_STONE |
| Paras | Parasect | Lv 24 | EVO_LEVEL |
| Patrat | Watchog | Lv 20 | EVO_LEVEL |
| Pawmi | Pawmo | Lv 18 | EVO_LEVEL |
| Pawmo | Pawmot | Lv 36 | EVO_LEVEL |
| Pawniard | Bisharp | Lv 30 | EVO_LEVEL |
| Petilil | Lilligant | Sun Stone | EVO_STONE |
| Petilil | Lilligant (form 1) | Dawn Stone | EVO_STONE |
| Phanpy | Donphan | Lv 25 | EVO_LEVEL |
| Phantump | Trevenant | Lv 30 | EVO_LEVEL |
| Pichu | Pikachu | Lv 15 | EVO_LEVEL |
| Pidgeotto | Pidgeot | Lv 36 | EVO_LEVEL |
| Pidgey | Pidgeotto | Lv 18 | EVO_LEVEL |
| Pidove | Tranquill | Lv 21 | EVO_LEVEL |
| Pignite | Emboar | Lv 36 | EVO_LEVEL |
| Pikachu | Raichu | Thunder Stone | EVO_STONE |
| Pikachu | Raichu (form 1) | Dawn Stone | EVO_STONE |
| Pikipek | Trumbeak | Lv 14 | EVO_LEVEL |
| Piloswine | Mamoswine | Lv 42 | EVO_LEVEL |
| Pineco | Forretress | Lv 31 | EVO_LEVEL |
| Piplup | Prinplup | Lv 16 | EVO_LEVEL |
| Poipole | Naganadel | Lv 38 | EVO_LEVEL |
| Polchgeist | Sinistcha | Cracked Pot | EVO_STONE |
| Poliwag | Poliwhirl | Lv 25 | EVO_LEVEL |
| Poliwhirl | Politoed | Kings Rock | EVO_STONE |
| Poliwhirl | Poliwrath | Water Stone | EVO_STONE |
| Poltchageist Masterpiece | Sinistcha | Chipped Pot | EVO_STONE |
| Ponyta | Rapidash | Lv 40 | EVO_LEVEL |
| Ponyta | Rapidash (form 1) | Lv 40 | EVO_LEVEL |
| Poochyena | Mightyena | Lv 18 | EVO_LEVEL |
| Popplio | Brionne | Lv 17 | EVO_LEVEL |
| Porygon | Porygon2 | Lv 30 | EVO_LEVEL |
| Porygon2 | Porygon-Z | Lv 40 | EVO_LEVEL |
| Primeape | Annihilape | Form Argument · 20 | EVO_FORM_ARGUMENT |
| Prinplup | Empoleon | Lv 36 | EVO_LEVEL |
| Psyduck | Golduck | Lv 33 | EVO_LEVEL |
| Pumpkaboo | Gourgeist | Lv 30 | EVO_LEVEL |
| Pumpkaboo Large | Gourgeist | Lv 30 | EVO_LEVEL |
| Pumpkaboo Small | Gourgeist | Lv 30 | EVO_LEVEL |
| Pumpkaboo Super | Gourgeist | Lv 30 | EVO_LEVEL |
| Pupitar | Tyranitar | Lv 55 | EVO_LEVEL |
| Purrloin | Liepard | Lv 20 | EVO_LEVEL |
| Quaxly | Quaxwell | Lv 16 | EVO_LEVEL |
| Quaxwell | Quaquaval | Lv 36 | EVO_LEVEL |
| Quilava | Typhlosion | Lv 36 · Day | EVO_LEVEL_DAY |
| Quilava | Typhlosion (form 1) | Lv 36 · Night | EVO_LEVEL_NIGHT |
| Quilladin | Chesnaught | Lv 36 | EVO_LEVEL |
| Qwilfish | Overqwil | Knows Barb Barrage | EVO_HAS_MOVE |
| Raboot | Cinderace | Lv 35 | EVO_LEVEL |
| Ralts | Kirlia | Lv 20 | EVO_LEVEL |
| Rattata | Raticate | Lv 20 | EVO_LEVEL |
| Rattata | Raticate (form 1) | Lv 20 | EVO_LEVEL |
| Rellor | Rabsca | Lv 30 | EVO_LEVEL |
| Remoraid | Octillery | Lv 25 | EVO_LEVEL |
| Rhydon | Rhyperior | Lv 45 | EVO_LEVEL |
| Rhyhorn | Rhydon | Lv 30 | EVO_LEVEL |
| Riolu | Lucario | Friendship | EVO_FRIENDSHIP |
| Rockruff | Lycanroc | Lv 25 · Day | EVO_LEVEL_DAY |
| Rockruff | Lycanroc (form 1) | Lv 25 · Night | EVO_LEVEL_NIGHT |
| Rockruff | Lycanroc (form 2) | Dusk Stone | EVO_STONE |
| Rockruff Own Tempo | Lycanroc (form 2) | Dusk Stone | EVO_STONE |
| Roggenrola | Boldore | Lv 25 | EVO_LEVEL |
| Rolycoly | Carkol | Lv 18 | EVO_LEVEL |
| Rookidee | Corvsquire | Lv 18 | EVO_LEVEL |
| Roselia | Roserade | Shiny Stone | EVO_STONE |
| Rowlet | Dartrix | Lv 17 | EVO_LEVEL |
| Rufflet | Braviary | Lv 38 · Day | EVO_LEVEL_DAY |
| Rufflet | Braviary | Lv 38 · Night | EVO_LEVEL_NIGHT |
| Salandit | Salazzle | Lv 33 · Female | EVO_LEVEL_FEMALE |
| Sandile | Krokorok | Lv 29 | EVO_LEVEL |
| Sandshrew | Sandslash | Lv 22 | EVO_LEVEL |
| Sandshrew | Sandslash (form 1) | Ice Stone | EVO_STONE |
| Sandygast | Palossand | Lv 42 | EVO_LEVEL |
| Scatterbug | Spewpa | Lv 9 | EVO_LEVEL |
| Scorbunny | Raboot | Lv 16 | EVO_LEVEL |
| Scraggy | Scrafty | Lv 39 | EVO_LEVEL |
| Scyther | Kleavor | Black Augurite | EVO_STONE |
| Scyther | Scizor | Metal Coat | EVO_STONE |
| Seadra | Kingdra | Lv 45 | EVO_LEVEL |
| Sealeo | Walrein | Lv 44 | EVO_LEVEL |
| Seedot | Nuzleaf | Lv 14 | EVO_LEVEL |
| Seel | Dewgong | Lv 34 | EVO_LEVEL |
| Sentret | Furret | Lv 15 | EVO_LEVEL |
| Servine | Serperior | Lv 36 | EVO_LEVEL |
| Sewaddle | Swadloon | Lv 20 | EVO_LEVEL |
| Shelgon | Salamence | Lv 50 | EVO_LEVEL |
| Shellder | Cloyster | Water Stone | EVO_STONE |
| Shellos | Gastrodon | Lv 30 | EVO_LEVEL |
| Shellos East Sea | Gastrodon | Lv 30 | EVO_LEVEL |
| Shelmet | Accelgor | Lv 30 | EVO_LEVEL |
| Shieldon | Bastiodon | Lv 30 | EVO_LEVEL |
| Shinx | Luxio | Lv 15 | EVO_LEVEL |
| Shroodle | Grafaiai | Lv 28 | EVO_LEVEL |
| Shroomish | Breloom | Lv 23 | EVO_LEVEL |
| Shuppet | Banette | Lv 37 | EVO_LEVEL |
| Silcoon | Beautifly | Lv 10 | EVO_LEVEL |
| Silicobra | Sandaconda | Lv 36 | EVO_LEVEL |
| Sinistea | Poltegeist | Cracked Pot | EVO_STONE |
| Sinistea Antique | Poltegeist | Chipped Pot | EVO_STONE |
| Sizzlipede | Centskorch | Lv 28 | EVO_LEVEL |
| Skiddo | Gogoat | Lv 32 | EVO_LEVEL |
| Skiploom | Jumpluff | Lv 27 | EVO_LEVEL |
| Skitty | Delcatty | Moon Stone | EVO_STONE |
| Skorupi | Drapion | Lv 40 | EVO_LEVEL |
| Skrelp | Dragalge | Lv 38 | EVO_LEVEL |
| Skwovet | Greedent | Lv 24 | EVO_LEVEL |
| Slakoth | Vigoroth | Lv 18 | EVO_LEVEL |
| Sliggoo | Goodra | Lv 50 · Rain | EVO_LEVEL_RAIN |
| Sliggoo | Goodra (form 1) | Lv 50 · Rain | EVO_LEVEL_RAIN |
| Slowpoke | Slowbro | Lv 37 | EVO_LEVEL |
| Slowpoke | Slowbro (form 2) | Galarica Cuff | EVO_STONE |
| Slowpoke | Slowking | Kings Rock | EVO_STONE |
| Slowpoke | Slowking (form 1) | Galarica Wreath | EVO_STONE |
| Slugma | Magcargo | Lv 32 | EVO_LEVEL |
| Smoliv | Dolliv | Lv 25 | EVO_LEVEL |
| Smoochum | Jynx | Lv 24 | EVO_LEVEL |
| Sneasel | Sneasler | Lv 30 | EVO_LEVEL |
| Sneasel | Weavile | Lv 34 | EVO_LEVEL |
| Snivy | Servine | Lv 17 | EVO_LEVEL |
| Snom | Frosmoth | Friendship | EVO_FRIENDSHIP |
| Snorunt | Froslass | Stone #109 · Female | EVO_STONE_FEMALE |
| Snorunt | Glalie | Lv 42 | EVO_LEVEL |
| Snover | Abomasnow | Lv 40 | EVO_LEVEL |
| Snubbull | Granbull | Lv 23 | EVO_LEVEL |
| Sobble | Drizzile | Lv 16 | EVO_LEVEL |
| Solosis | Duosion | Lv 32 | EVO_LEVEL |
| Spearow | Fearow | Lv 20 | EVO_LEVEL |
| Spewpa | Vivillon | Lv 12 | EVO_LEVEL |
| Spheal | Sealeo | Lv 32 | EVO_LEVEL |
| Spinarak | Ariados | Lv 22 | EVO_LEVEL |
| Spoink | Grumpig | Lv 32 | EVO_LEVEL |
| Sprigatito | Floragato | Lv 16 | EVO_LEVEL |
| Spritzee | Aromatisse | Lv 30 | EVO_LEVEL |
| Squirtle | Wartortle | Lv 16 | EVO_LEVEL |
| Stantler | Wyrdeer | Lv 38 | EVO_LEVEL |
| Staravia | Staraptor | Lv 34 | EVO_LEVEL |
| Starly | Staravia | Lv 14 | EVO_LEVEL |
| Staryu | Starmie | Water Stone | EVO_STONE |
| Steenee | Tsareena | Knows Stomp | EVO_HAS_MOVE |
| Stufful | Bewear | Lv 27 | EVO_LEVEL |
| Stunky | Skuntank | Lv 34 | EVO_LEVEL |
| Sunkern | Sunflora | Sun Stone | EVO_STONE |
| Surskit | Masquerain | Lv 22 | EVO_LEVEL |
| Swablu | Altaria | Lv 35 | EVO_LEVEL |
| Swadloon | Leavanny | Friendship | EVO_FRIENDSHIP |
| Swinub | Piloswine | Lv 25 | EVO_LEVEL |
| Swirlix | Slurpuff | Lv 30 | EVO_LEVEL |
| Tadbulb | Bellibolt | Thunder Stone | EVO_STONE |
| Taillow | Swellow | Lv 22 | EVO_LEVEL |
| Tandemaus | Maushold | Lv 25 | EVO_LEVEL |
| Tangela | Tangrowth | Lv 34 | EVO_LEVEL |
| Tarountula | Spidops | Lv 15 | EVO_LEVEL |
| Teddiursa | Ursaring | Lv 30 | EVO_LEVEL |
| Tentacool | Tentacruel | Lv 30 | EVO_LEVEL |
| Tepig | Pignite | Lv 17 | EVO_LEVEL |
| Thwackey | Rillaboom | Lv 35 | EVO_LEVEL |
| Timburr | Gurdurr | Lv 25 | EVO_LEVEL |
| Tinkatink | Tinkatuff | Lv 24 | EVO_LEVEL |
| Tinkatuff | Tinkaton | Lv 38 | EVO_LEVEL |
| Tirtouga | Carracosta | Lv 37 | EVO_LEVEL |
| Toedscool | Toedscruel | Lv 30 | EVO_LEVEL |
| Togepi | Togetic | Lv 21 | EVO_LEVEL |
| Togetic | Togekiss | Shiny Stone | EVO_STONE |
| Torchic | Combusken | Lv 16 | EVO_LEVEL |
| Torracat | Incineroar | Lv 34 | EVO_LEVEL |
| Totodile | Croconaw | Lv 18 | EVO_LEVEL |
| Toxel | Toxtricity | Lv 30 · Amped nature | EVO_LEVEL_NATURE_AMPED |
| Toxel | Toxtricity (form 1) | Lv 30 · Nature Low Key | EVO_LEVEL_NATURE_LOW_KEY |
| Tranquill | Unfezant | Lv 32 · Male | EVO_LEVEL_MALE |
| Tranquill | Unfezant (form 1) | Lv 32 · Female | EVO_LEVEL_FEMALE |
| Trapinch | Vibrava | Lv 30 | EVO_LEVEL |
| Treecko | Grovyle | Lv 16 | EVO_LEVEL |
| Trubbish | Garbodor | Lv 36 | EVO_LEVEL |
| Trumbeak | Toucannon | Lv 28 | EVO_LEVEL |
| Turtwig | Grotle | Lv 18 | EVO_LEVEL |
| Tympole | Palpitoad | Lv 25 | EVO_LEVEL |
| Tynamo | Eelektrik | Lv 29 | EVO_LEVEL |
| Type: Null | Silvally | Friendship | EVO_FRIENDSHIP |
| Tyrogue | Hitmonchan | Lv 20 · Atk < Def | EVO_LEVEL_ATK_LT_DEF |
| Tyrogue | Hitmonlee | Lv 20 · Atk > Def | EVO_LEVEL_ATK_GT_DEF |
| Tyrogue | Hitmontop | Lv 20 · Atk = Def | EVO_LEVEL_ATK_EQ_DEF |
| Tyrunt | Tyrantrum | Lv 39 | EVO_LEVEL |
| Ursaring | Ursaluna | Lv 45 | EVO_LEVEL |
| Vanillish | Vanilluxe | Lv 40 | EVO_LEVEL |
| Vanillite | Vanillish | Lv 28 | EVO_LEVEL |
| Varoom | Revavroom | Lv 40 | EVO_LEVEL |
| Venipede | Whirlipede | Lv 22 | EVO_LEVEL |
| Venonat | Venomoth | Lv 31 | EVO_LEVEL |
| Vibrava | Flygon | Lv 45 | EVO_LEVEL |
| Vigoroth | Slaking | Lv 36 | EVO_LEVEL |
| Voltorb | Electrode | Lv 30 | EVO_LEVEL |
| Voltorb | Electrode (form 1) | Leaf Stone | EVO_STONE |
| Vullaby | Mandibuzz | Lv 38 | EVO_LEVEL |
| Vulpix | Ninetales | Fire Stone | EVO_STONE |
| Vulpix | Ninetales (form 1) | Ice Stone | EVO_STONE |
| Wailmer | Wailord | Lv 40 | EVO_LEVEL |
| Wartortle | Blastoise | Lv 36 | EVO_LEVEL |
| Wattrel | Kilowatrel | Lv 25 | EVO_LEVEL |
| Weedle | Kakuna | Lv 7 | EVO_LEVEL |
| Weepinbell | Victreebel | Lv 34 | EVO_LEVEL |
| Whirlipede | Scolipede | Lv 30 | EVO_LEVEL |
| Whismur | Loudred | Lv 20 | EVO_LEVEL |
| Wiglett | Wugtrio | Lv 26 | EVO_LEVEL |
| Wimpod | Golisopod | Lv 30 | EVO_LEVEL |
| Wingull | Pelipper | Lv 25 | EVO_LEVEL |
| Woobat | Swoobat | Friendship | EVO_FRIENDSHIP |
| Wooloo | Dubwool | Lv 24 | EVO_LEVEL |
| Wooper | Clodsire | Lv 20 | EVO_LEVEL |
| Wooper | Quagsire | Lv 20 | EVO_LEVEL |
| Wurmple | Cascoon | Lv 7 · personality high | EVO_LEVEL_PID_HI |
| Wurmple | Silcoon | Lv 7 · personality low | EVO_LEVEL_PID_LO |
| Wynaut | Wobbuffet | Lv 15 | EVO_LEVEL |
| Yamask | Cofagrigus | Lv 34 | EVO_LEVEL |
| Yamask | Runerigus | Take 49 damage | EVO_HURT_IN_BATTLE_AMOUNT |
| Yamper | Boltund | Lv 25 | EVO_LEVEL |
| Yanma | Yanmega | Lv 34 | EVO_LEVEL |
| Yungoos | Gumshoos | Lv 20 | EVO_LEVEL |
| Zigzagoon | Linoone | Lv 20 | EVO_LEVEL |
| Zigzagoon | Linoone (form 1) | Lv 20 | EVO_LEVEL |
| Zorua | Zoroark | Lv 30 | EVO_LEVEL |
| Zorua | Zoroark (form 1) | Lv 30 | EVO_LEVEL |
| Zubat | Golbat | Lv 22 | EVO_LEVEL |
| Zweilous | Hydreigon | Lv 50 | EVO_LEVEL |
