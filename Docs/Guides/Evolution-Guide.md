# Evolution Guide

This is the player-facing evolution reference for the **HeartGold Retiled Expansion v6.6.0** build. It is generated from the evolution configuration used to build the patch, rather than from vanilla HeartGold rules.

## What changed

- Pokémon and forms through the configured Generation 9 data set are present in the engine tables.
- The Fairy type is enabled.
- Many later-generation evolution methods and items are supported, including Ice Stone, Linking Cord, Black Augurite, Syrupy Apple, Auspicious Armor, Malicious Armor, and move-based methods.
- The configured table contains no trade-only method. Former trade evolutions use level or item alternatives.
- 7 configured evolutions can use a **Linking Cord**. The same families also have an additional configured path where shown.
- Some location-based evolutions also have a stone alternative. For example, Magneton can use a Thunder Stone.
- Mega Evolution is a temporary battle transformation, not a permanent evolution. See [HG-Engine Features](HG-Engine-Features.md) and [Item Locations](Item-Locations.md).

> [!NOTE]
> Form-change rows are included because they are part of the same compiled table, even when they are not ordinary permanent evolutions. A target labelled “form N” uses the engine's numeric form slot.

## Linking Cord alternatives

| Pokémon | Evolves into | Method |
| --- | --- | --- |
| Kadabra | Alakazam | Use Linking Cord |
| Machoke | Machamp | Use Linking Cord |
| Graveler | Golem | Use Linking Cord |
| Haunter | Gengar | Use Linking Cord |
| Boldore | Gigalith | Use Linking Cord |
| Gurdurr | Conkeldurr | Use Linking Cord |
| Graveler Alolan | Golem (form 1) | Use Linking Cord |

## Complete configured evolution list

Use your browser's find command to search for a Pokémon or evolution item.

| From | Result | Configured method |
| --- | --- | --- |
| Bulbasaur | Ivysaur | Level 16 |
| Ivysaur | Venusaur | Level 32 |
| Charmander | Charmeleon | Level 16 |
| Charmeleon | Charizard | Level 36 |
| Squirtle | Wartortle | Level 16 |
| Wartortle | Blastoise | Level 36 |
| Caterpie | Metapod | Level 7 |
| Metapod | Butterfree | Level 10 |
| Weedle | Kakuna | Level 7 |
| Kakuna | Beedrill | Level 10 |
| Pidgey | Pidgeotto | Level 18 |
| Pidgeotto | Pidgeot | Level 36 |
| Rattata | Raticate | Level 20 |
| Spearow | Fearow | Level 20 |
| Ekans | Arbok | Level 22 |
| Pikachu | Raichu | Use Thunder Stone |
| Sandshrew | Sandslash | Level 22 |
| Nidoran♀ | Nidorina | Level 16 |
| Nidorina | Nidoqueen | Use Moon Stone |
| Nidoran♂ | Nidorino | Level 16 |
| Nidorino | Nidoking | Use Moon Stone |
| Clefairy | Clefable | Use Moon Stone |
| Vulpix | Ninetales | Use Fire Stone |
| Jigglypuff | Wigglytuff | Use Moon Stone |
| Zubat | Golbat | Level 22 |
| Golbat | Crobat | High friendship |
| Oddish | Gloom | Level 21 |
| Gloom | Vileplume | Use Leaf Stone |
| Gloom | Bellossom | Use Sun Stone |
| Paras | Parasect | Level 24 |
| Venonat | Venomoth | Level 31 |
| Diglett | Dugtrio | Level 26 |
| Meowth | Persian | Level 28 |
| Psyduck | Golduck | Level 33 |
| Mankey | Primeape | Level 28 |
| Primeape | Annihilape | Configured form argument 20 |
| Growlithe | Arcanine | Use Fire Stone |
| Poliwag | Poliwhirl | Level 25 |
| Poliwhirl | Poliwrath | Use Water Stone |
| Poliwhirl | Politoed | Level 36 |
| Abra | Kadabra | Level 16 |
| Kadabra | Alakazam | Level 36 |
| Kadabra | Alakazam | Use Linking Cord |
| Machop | Machoke | Level 28 |
| Machoke | Machamp | Level 36 |
| Machoke | Machamp | Use Linking Cord |
| Bellsprout | Weepinbell | Level 21 |
| Weepinbell | Victreebel | Use Leaf Stone |
| Tentacool | Tentacruel | Level 30 |
| Geodude | Graveler | Level 25 |
| Graveler | Golem | Level 36 |
| Graveler | Golem | Use Linking Cord |
| Ponyta | Rapidash | Level 40 |
| Slowpoke | Slowbro | Level 37 |
| Slowpoke | Slowking | Level 36 |
| Magnemite | Magneton | Level 30 |
| Magneton | Magnezone | Level up in a magnetic field |
| Magneton | Magnezone | Use Thunder Stone |
| Doduo | Dodrio | Level 31 |
| Seel | Dewgong | Level 34 |
| Grimer | Muk | Level 38 |
| Shellder | Cloyster | Use Water Stone |
| Gastly | Haunter | Level 25 |
| Haunter | Gengar | Level 36 |
| Haunter | Gengar | Use Linking Cord |
| Onix | Steelix | Level 36 |
| Drowzee | Hypno | Level 26 |
| Krabby | Kingler | Level 28 |
| Voltorb | Electrode | Level 30 |
| Exeggcute | Exeggutor | Use Leaf Stone |
| Cubone | Marowak | Level 28 |
| Lickitung | Lickilicky | Level up knowing Rollout |
| Koffing | Weezing | Level 35 |
| Rhyhorn | Rhydon | Level 42 |
| Rhydon | Rhyperior | Level 36 |
| Chansey | Blissey | High friendship |
| Tangela | Tangrowth | Level up knowing Ancient Power |
| Horsea | Seadra | Level 32 |
| Seadra | Kingdra | Level 36 |
| Goldeen | Seaking | Level 33 |
| Staryu | Starmie | Use Water Stone |
| Scyther | Scizor | Level 36 |
| Scyther | Kleavor | Use Black Augurite |
| Electabuzz | Electivire | Level 36 |
| Magmar | Magmortar | Level 36 |
| Magikarp | Gyarados | Level 20 |
| Eevee | Leafeon | Use Leaf Stone |
| Eevee | Glaceon | Use Ice Stone |
| Eevee | Jolteon | Use Thunder Stone |
| Eevee | Vaporeon | Use Water Stone |
| Eevee | Flareon | Use Fire Stone |
| Eevee | Sylveon | Level up knowing a Fairy-type move |
| Eevee | Espeon | High friendship during the day |
| Eevee | Umbreon | High friendship at night |
| Porygon | Porygon2 | Level 36 |
| Omanyte | Omastar | Level 40 |
| Kabuto | Kabutops | Level 40 |
| Dratini | Dragonair | Level 30 |
| Dragonair | Dragonite | Level 55 |
| Chikorita | Bayleef | Level 16 |
| Bayleef | Meganium | Level 32 |
| Cyndaquil | Quilava | Level 14 |
| Quilava | Typhlosion | Level 36 |
| Totodile | Croconaw | Level 18 |
| Croconaw | Feraligatr | Level 30 |
| Sentret | Furret | Level 15 |
| Hoothoot | Noctowl | Level 20 |
| Ledyba | Ledian | Level 18 |
| Spinarak | Ariados | Level 22 |
| Chinchou | Lanturn | Level 27 |
| Pichu | Pikachu | High friendship |
| Cleffa | Clefairy | High friendship |
| Igglybuff | Jigglypuff | High friendship |
| Togepi | Togetic | High friendship |
| Togetic | Togekiss | Use Shiny Stone |
| Natu | Xatu | Level 25 |
| Mareep | Flaaffy | Level 15 |
| Flaaffy | Ampharos | Level 30 |
| Marill | Azumarill | Level 18 |
| Hoppip | Skiploom | Level 18 |
| Skiploom | Jumpluff | Level 27 |
| Aipom | Ambipom | Level up knowing Double Hit |
| Sunkern | Sunflora | Use Sun Stone |
| Yanma | Yanmega | Level up knowing Ancient Power |
| Wooper | Quagsire | Level 20 |
| Murkrow | Honchkrow | Use Dusk Stone |
| Misdreavus | Mismagius | Use Dusk Stone |
| Girafarig | Farigiraf | Level up knowing Twin Beam |
| Pineco | Forretress | Level 31 |
| Dunsparce | Dudunspars | Level up knowing Hyper Drill |
| Gligar | Gliscor | Use Razor Fang at night |
| Snubbull | Granbull | Level 23 |
| Sneasel | Weavile | Use Razor Claw at night |
| Teddiursa | Ursaring | Level 30 |
| Ursaring | Ursaluna | Use Peat Block at night |
| Slugma | Magcargo | Level 38 |
| Swinub | Piloswine | Level 33 |
| Piloswine | Mamoswine | Level up knowing Ancient Power |
| Remoraid | Octillery | Level 25 |
| Houndour | Houndoom | Level 24 |
| Phanpy | Donphan | Level 25 |
| Porygon2 | Porygon-Z | Level 36 |
| Stantler | Wyrdeer | Configured form argument 20 |
| Tyrogue | Hitmonchan | Level 20 with Attack < Defense |
| Tyrogue | Hitmonlee | Level 20 with Attack > Defense |
| Tyrogue | Hitmontop | Level 20 with Attack = Defense |
| Smoochum | Jynx | Level 30 |
| Elekid | Electabuzz | Level 30 |
| Magby | Magmar | Level 30 |
| Larvitar | Pupitar | Level 30 |
| Pupitar | Tyranitar | Level 55 |
| Treecko | Grovyle | Level 16 |
| Grovyle | Sceptile | Level 36 |
| Torchic | Combusken | Level 16 |
| Combusken | Blaziken | Level 36 |
| Mudkip | Marshtomp | Level 16 |
| Marshtomp | Swampert | Level 36 |
| Poochyena | Mightyena | Level 18 |
| Zigzagoon | Linoone | Level 20 |
| Wurmple | Silcoon | Level 7 (personality branch B) |
| Wurmple | Cascoon | Level 7 (personality branch A) |
| Silcoon | Beautifly | Level 10 |
| Cascoon | Dustox | Level 10 |
| Lotad | Lombre | Level 14 |
| Lombre | Ludicolo | Use Water Stone |
| Seedot | Nuzleaf | Level 14 |
| Nuzleaf | Shiftry | Use Leaf Stone |
| Taillow | Swellow | Level 22 |
| Wingull | Pelipper | Level 25 |
| Ralts | Kirlia | Level 20 |
| Kirlia | Gardevoir | Level 30 |
| Kirlia | Gallade | Use 109 (male) |
| Surskit | Masquerain | Level 22 |
| Shroomish | Breloom | Level 23 |
| Slakoth | Vigoroth | Level 18 |
| Vigoroth | Slaking | Level 36 |
| Nincada | Ninjask | Level 20 (Ninjask branch) |
| Nincada | Shedinja | Level 20 with an empty party slot and spare Poké Ball |
| Whismur | Loudred | Level 20 |
| Loudred | Exploud | Level 40 |
| Makuhita | Hariyama | Level 24 |
| Azurill | Marill | High friendship |
| Nosepass | Probopass | Level up in a magnetic field |
| Nosepass | Probopass | Use Thunder Stone |
| Skitty | Delcatty | Use Moon Stone |
| Aron | Lairon | Level 32 |
| Lairon | Aggron | Level 42 |
| Meditite | Medicham | Level 37 |
| Electrike | Manectric | Level 26 |
| Roselia | Roserade | Use Shiny Stone |
| Gulpin | Swalot | Level 26 |
| Carvanha | Sharpedo | Level 30 |
| Wailmer | Wailord | Level 40 |
| Numel | Camerupt | Level 33 |
| Spoink | Grumpig | Level 32 |
| Trapinch | Vibrava | Level 35 |
| Vibrava | Flygon | Level 45 |
| Cacnea | Cacturne | Level 32 |
| Swablu | Altaria | Level 35 |
| Barboach | Whiscash | Level 30 |
| Corphish | Crawdaunt | Level 30 |
| Baltoy | Claydol | Level 36 |
| Lileep | Cradily | Level 40 |
| Anorith | Armaldo | Level 40 |
| Feebas | Milotic | Beauty 170 |
| Feebas | Milotic | Level 36 |
| Shuppet | Banette | Level 37 |
| Duskull | Dusclops | Level 37 |
| Dusclops | Dusknoir | Level 36 |
| Wynaut | Wobbuffet | Level 15 |
| Snorunt | Glalie | Level 42 |
| Snorunt | Froslass | Use 109 (female) |
| Spheal | Sealeo | Level 32 |
| Sealeo | Walrein | Level 44 |
| Clamperl | Huntail | Level 36 |
| Clamperl | Gorebyss | Level 36 |
| Bagon | Shelgon | Level 30 |
| Shelgon | Salamence | Level 50 |
| Beldum | Metang | Level 20 |
| Metang | Metagross | Level 45 |
| Turtwig | Grotle | Level 18 |
| Grotle | Torterra | Level 32 |
| Chimchar | Monferno | Level 14 |
| Monferno | Infernape | Level 36 |
| Piplup | Prinplup | Level 16 |
| Prinplup | Empoleon | Level 36 |
| Starly | Staravia | Level 14 |
| Staravia | Staraptor | Level 34 |
| Bidoof | Bibarel | Level 15 |
| Kricketot | Kricketune | Level 10 |
| Shinx | Luxio | Level 15 |
| Luxio | Luxray | Level 30 |
| Budew | Roselia | High friendship during the day |
| Cranidos | Rampardos | Level 30 |
| Shieldon | Bastiodon | Level 30 |
| Burmy | Wormadam | Level 20 (female) |
| Burmy | Mothim | Level 20 (male) |
| Combee | Vespiquen | Level 21 (female) |
| Buizel | Floatzel | Level 26 |
| Cherubi | Cherrim | Level 25 |
| Shellos | Gastrodon | Level 30 |
| Drifloon | Drifblim | Level 28 |
| Buneary | Lopunny | High friendship |
| Glameow | Purugly | Level 38 |
| Chingling | Chimecho | High friendship at night |
| Stunky | Skuntank | Level 34 |
| Bronzor | Bronzong | Level 33 |
| Bonsly | Sudowoodo | Level up knowing Mimic |
| Mime Jr. | Mr. Mime | Level up knowing Mimic |
| Happiny | Chansey | Use Oval Stone during the day |
| Gible | Gabite | Level 24 |
| Gabite | Garchomp | Level 48 |
| Munchlax | Snorlax | High friendship |
| Riolu | Lucario | High friendship during the day |
| Hippopotas | Hippowdon | Level 34 |
| Skorupi | Drapion | Level 40 |
| Croagunk | Toxicroak | Level 37 |
| Finneon | Lumineon | Level 31 |
| Mantyke | Mantine | Level up with Remoraid in the party |
| Snover | Abomasnow | Level 40 |
| Snivy | Servine | Level 17 |
| Servine | Serperior | Level 36 |
| Tepig | Pignite | Level 17 |
| Pignite | Emboar | Level 36 |
| Oshawott | Dewott | Level 17 |
| Dewott | Samurott | Level 36 |
| Patrat | Watchog | Level 20 |
| Lillipup | Herdier | Level 16 |
| Herdier | Stoutland | Level 32 |
| Purrloin | Liepard | Level 20 |
| Pansage | Simisage | Use Leaf Stone |
| Pansear | Simisear | Use Fire Stone |
| Panpour | Simipour | Use Water Stone |
| Munna | Musharna | Use Moon Stone |
| Pidove | Tranquill | Level 21 |
| Tranquill | Unfezant | Level 32 (male) |
| Tranquill | Unfezant (form 1) | Level 32 (female) |
| Blitzle | Zebstrika | Level 27 |
| Roggenrola | Boldore | Level 25 |
| Boldore | Gigalith | Level 36 |
| Boldore | Gigalith | Use Linking Cord |
| Woobat | Swoobat | High friendship |
| Drilbur | Excadrill | Level 31 |
| Timburr | Gurdurr | Level 25 |
| Gurdurr | Conkeldurr | Level 36 |
| Gurdurr | Conkeldurr | Use Linking Cord |
| Tympole | Palpitoad | Level 25 |
| Palpitoad | Seismitoad | Level 36 |
| Sewaddle | Swadloon | Level 20 |
| Swadloon | Leavanny | High friendship |
| Venipede | Whirlipede | Level 22 |
| Whirlipede | Scolipede | Level 30 |
| Cottonee | Whimsicott | Use Sun Stone |
| Petilil | Lilligant | Use Sun Stone |
| Sandile | Krokorok | Level 29 |
| Krokorok | Krookodile | Level 40 |
| Darumaka | Darmanitan | Level 35 |
| Dwebble | Crustle | Level 34 |
| Scraggy | Scrafty | Level 39 |
| Yamask | Cofagrigus | Level 34 |
| Tirtouga | Carracosta | Level 37 |
| Archen | Archeops | Level 37 |
| Trubbish | Garbodor | Level 36 |
| Zorua | Zoroark | Level 30 |
| Minccino | Cinccino | Use Shiny Stone |
| Gothita | Gothorita | Level 32 |
| Gothorita | Gothitelle | Level 41 |
| Solosis | Duosion | Level 32 |
| Duosion | Reuniclus | Level 41 |
| Ducklett | Swanna | Level 35 |
| Vanillite | Vanillish | Level 35 |
| Vanillish | Vanilluxe | Level 47 |
| Deerling | Sawsbuck | Level 34 |
| Karrablast | Escavalier | Level 36 |
| Karrablast | Escavalier | Level up with Shelmet in the party |
| Foongus | Amoonguss | Level 39 |
| Frillish | Jellicent | Level 40 (male) |
| Joltik | Galvantula | Level 36 |
| Ferroseed | Ferrothorn | Level 40 |
| Klink | Klang | Level 38 |
| Klang | Klinklang | Level 49 |
| Tynamo | Eelektrik | Level 39 |
| Eelektrik | Eelektross | Use Thunder Stone |
| Elgyem | Beheeyem | Level 42 |
| Litwick | Lampent | Level 41 |
| Lampent | Chandelure | Use Dusk Stone |
| Axew | Fraxure | Level 38 |
| Fraxure | Haxorus | Level 48 |
| Cubchoo | Beartic | Level 37 |
| Shelmet | Accelgor | Level 36 |
| Shelmet | Accelgor | Level up with Karrablast in the party |
| Mienfoo | Mienshao | Level 50 |
| Golett | Golurk | Level 43 |
| Pawniard | Bisharp | Level 52 |
| Bisharp | Kingambit | Configured form argument 3 |
| Rufflet | Braviary | Level 54 |
| Vullaby | Mandibuzz | Level 54 |
| Deino | Zweilous | Level 50 |
| Zweilous | Hydreigon | Level 64 |
| Larvesta | Volcarona | Level 59 |
| Chespin | Quilladin | Level 16 |
| Quilladin | Chesnaught | Level 36 |
| Fennekin | Braixen | Level 16 |
| Braixen | Delphox | Level 36 |
| Froakie | Frogadier | Level 16 |
| Frogadier | Greninja | Level 36 |
| Bunnelby | Diggersby | Level 20 |
| Fletchling | Flechinder | Level 17 |
| Flechinder | Talonflame | Level 35 |
| Scatterbug | Spewpa | Level 9 |
| Spewpa | Vivillon | Level 12 |
| Litleo | Pyroar | Level 35 (male) |
| Litleo | Pyroar (form 1) | Level 35 (female) |
| Flabébé | Floette | Level 19 |
| Floette | Florges | Use Shiny Stone |
| Skiddo | Gogoat | Level 32 |
| Pancham | Pangoro | Level Nidoran♂ with a Dark-type Pokémon in the party |
| Espurr | Meowstic | Level 25 (male) |
| Espurr | Meowstic (form 1) | Level 25 (female) |
| Honedge | Doublade | Level 35 |
| Doublade | Aegislash | Use Dusk Stone |
| Spritzee | Aromatisse | Level 36 |
| Swirlix | Slurpuff | Level 36 |
| Inkay | Malamar | Level 30 |
| Binacle | Barbaracle | Level 39 |
| Skrelp | Dragalge | Level 48 |
| Clauncher | Clawitzer | Level 37 |
| Helioptile | Heliolisk | Use Sun Stone |
| Tyrunt | Tyrantrum | Level 39 during the day |
| Amaura | Aurorus | Level 39 |
| Goomy | Sliggoo | Level 40 |
| Sliggoo | Goodra | Level 50 while it is raining |
| Phantump | Trevenant | Level 36 |
| Pumpkaboo | Gourgeist | Level 36 |
| Bergmite | Avalugg | Level 37 |
| Noibat | Noivern | Level 48 |
| Rowlet | Dartrix | Level 17 |
| Dartrix | Decidueye | Level 34 |
| Litten | Torracat | Level 17 |
| Torracat | Incineroar | Level 34 |
| Popplio | Brionne | Level 17 |
| Brionne | Primarina | Level 34 |
| Pikipek | Trumbeak | Level 14 |
| Trumbeak | Toucannon | Level 28 |
| Yungoos | Gumshoos | Level 20 during the day |
| Grubbin | Charjabug | Level 20 |
| Charjabug | Vikavolt | Level up in a magnetic field |
| Charjabug | Vikavolt | Use Thunder Stone |
| Crabrawler | Crabomnabl | Use Ice Stone |
| Cutiefly | Ribombee | Level 25 |
| Rockruff | Lycanroc | Level 25 during the day |
| Rockruff | Lycanroc (form 1) | Level 25 at night |
| Mareanie | Toxapex | Level 38 |
| Mudbray | Mudsdale | Level 30 |
| Dewpider | Araquanid | Level 22 |
| Fomantis | Lurantis | Level 34 during the day |
| Morelull | Shiinotic | Level 24 |
| Salandit | Salazzle | Level 33 (female) |
| Stufful | Bewear | Level 27 |
| Bounsweet | Steenee | Level 18 |
| Steenee | Tsareena | Level up knowing Stomp |
| Wimpod | Golisopod | Level 30 |
| Sandygast | Palossand | Level 42 |
| Type: Null | Silvally | High friendship |
| Jangmo-o | Hakamo-o | Level 35 |
| Hakamo-o | Kommo-o | Level 45 |
| Cosmog | Cosmoem | Level 43 |
| Cosmoem | Solgaleo | Level 53 during the day |
| Cosmoem | Lunala | Level 53 at night |
| Poipole | Naganadel | Level up knowing Dragon Pulse |
| Grookey | Thwackey | Level 16 |
| Thwackey | Rillaboom | Level 35 |
| Scorbunny | Raboot | Level 16 |
| Raboot | Cinderace | Level 35 |
| Sobble | Drizzile | Level 16 |
| Drizzile | Inteleon | Level 35 |
| Skwovet | Greedent | Level 24 |
| Rookidee | Corvsquire | Level 18 |
| Corvsquire | Corviknite | Level 38 |
| Blipbug | Dottler | Level 10 |
| Dottler | Orbeetle | Level 30 |
| Nickit | Thievul | Level 18 |
| Gossifleur | Eldegoss | Level 20 |
| Wooloo | Dubwool | Level 24 |
| Chewtle | Drednaw | Level 22 |
| Yamper | Boltund | Level 25 |
| Rolycoly | Carkol | Level 18 |
| Carkol | Coalossal | Level 34 |
| Applin | Flapple | Use Tart Apple |
| Applin | Appletun | Use Sweet Apple |
| Applin | Dipplin | Use Syrupy Apple |
| Silicobra | Sandaconda | Level 36 |
| Arrokuda | Baraskewda | Level 26 |
| Toxel | Toxtricity | Level 30 with an Amped-form nature |
| Toxel | Toxtricity (form 1) | Level 30 with a Low Key-form nature |
| Sizzlipede | Centskorch | Level 28 |
| Clobbopus | Grapploct | Level up knowing Taunt |
| Sinistea | Poltegeist | Use Cracked Pot |
| Hatenna | Hattrem | Level 32 |
| Hattrem | Hatterene | Level 42 |
| Impidimp | Morgrem | Level 32 |
| Morgrem | Grimmsnarl | Level 42 |
| Milcery | Alcremie | Spin clockwise for under 5 seconds during the day |
| Milcery | Alcremie (form 1) | Spin counterclockwise for under 5 seconds during the day |
| Milcery | Alcremie (form 2) | Spin clockwise for under 5 seconds at night |
| Milcery | Alcremie (form 3) | Spin counterclockwise for over 5 seconds at night |
| Milcery | Alcremie (form 4) | Spin clockwise for over 5 seconds at night |
| Milcery | Alcremie (form 5) | Spin counterclockwise for under 5 seconds at night |
| Milcery | Alcremie (form 6) | Spin counterclockwise for over 5 seconds during the day |
| Milcery | Alcremie (form 7) | Spin clockwise for over 5 seconds during the day |
| Milcery | Alcremie (form 8) | Spin for over 10 seconds in the evening |
| Snom | Frosmoth | High friendship at night |
| Cufant | Copperajah | Level 34 |
| Duraludon | Archaludon | Use Metal Alloy |
| Dreepy | Drakloak | Level 50 |
| Drakloak | Dragapult | Level 60 |
| Kubfu | Urshifu | Use Scroll of Darkness |
| Kubfu | Urshifu (form 1) | Use Scroll of Waters |
| Sprigatito | Floragato | Level 16 |
| Floragato | Mewscarada | Level 36 |
| Fuecoco | Crocalor | Level 16 |
| Crocalor | Skeledirge | Level 36 |
| Quaxly | Quaxwell | Level 16 |
| Quaxwell | Quaquaval | Level 36 |
| Lechonk | Oinkologne | Level 18 (male) |
| Lechonk | Oinkologne (form 1) | Level 18 (female) |
| Tarountula | Spidops | Level 15 |
| Nymble | Lokix | Level 24 |
| Pawmi | Pawmo | Level 18 |
| Pawmo | Pawmot | Walk 0 steps using the following mechanic, then level up |
| Tandemaus | Maushold | Level 25 |
| Fidough | Dachsbun | Level 26 |
| Smoliv | Dolliv | Level 25 |
| Dolliv | Arboliva | Level 35 |
| Nacli | Naclstack | Level 24 |
| Naclstack | Garganacl | Level 38 |
| Charcadet | Armarouge | Use Auspicious Armor |
| Charcadet | Ceruledge | Use Malicious Armor |
| Tadbulb | Bellibolt | Use Thunder Stone |
| Wattrel | Kilowatrel | Level 25 |
| Maschiff | Mabosstiff | Level 30 |
| Shroodle | Grafaiai | Level 28 |
| Bramblin | Bramblgast | Walk 0 steps using the following mechanic, then level up |
| Toedscool | Toedscruel | Level 30 |
| Capsakid | Scovillain | Use Fire Stone |
| Rellor | Rabsca | Walk 0 steps using the following mechanic, then level up |
| Flittle | Espathra | Level 35 |
| Tinkatink | Tinkatuff | Level 24 |
| Tinkatuff | Tinkaton | Level 38 |
| Wiglett | Wugtrio | Level 26 |
| Finizen | Palafin | Level 38 |
| Varoom | Revavroom | Level 40 |
| Glimmet | Glimmora | Level 35 |
| Greavard | Houndstone | Level 30 at night |
| Cetoddle | Cetitan | Use Ice Stone |
| Frigibax | Arctibax | Level 35 |
| Arctibax | Baxcalibur | Level 54 |
| Gimmighoul | Gholdengo | Configured form argument 999 |
| Dipplin | Hydrapple | Level up knowing Dragon Cheer |
| Polchgeist | Sinistcha | Use Cracked Pot |
| Rattata Alolan | Raticate (form 1) | Level 20 at night |
| Sandshrew Alolan | Sandslash (form 1) | Use Ice Stone |
| Vulpix Alolan | Ninetales (form 1) | Use Ice Stone |
| Diglett Alolan | Dugtrio (form 1) | Level 26 |
| Meowth Alolan | Persian (form 1) | High friendship |
| Geodude Alolan | Graveler (form 1) | Level 25 |
| Graveler Alolan | Golem (form 1) | Level 36 |
| Graveler Alolan | Golem (form 1) | Use Linking Cord |
| Grimer Alolan | Muk (form 1) | Level 38 |
| Meowth Galarian | Perrserker | Level 28 |
| Ponyta Galarian | Rapidash (form 1) | Level 40 |
| Slowpoke Galarian | Slowbro (form 2) | Use Galarica Cuff |
| Slowpoke Galarian | Slowking (form 1) | Use Galarica Wreath |
| Farfetch'd Galarian | Sirfetch’d | Land 3 critical hits in one battle, then level up |
| Mr. Mime Galarian | Mr. Rime | Level 42 |
| Corsola Galarian | Cursola | Level 38 |
| Zigzagoon Galarian | Linoone (form 1) | Level 20 |
| Linoone Galarian | Obstagoon | Level 35 |
| Darumaka Galarian | Darmanitan (form 1) | Use Ice Stone |
| Yamask Galarian | Runerigus | Level up after taking 49 damage without fainting |
| Shellos East Sea | Gastrodon | Level 30 |
| Basculin White Striped | Basclegion | Level 0 (male) |
| Basculin White Striped | Basclegion (form 1) | Level 0 (female) |
| Deerling Summer | Sawsbuck | Level 34 |
| Deerling Autumn | Sawsbuck | Level 34 |
| Deerling Winter | Sawsbuck | Level 34 |
| Flabébé Yellow Flower | Floette | Level 19 |
| Flabébé Orange Flower | Floette | Level 19 |
| Flabébé Blue Flower | Floette | Level 19 |
| Flabébé White Flower | Floette | Level 19 |
| Floette Yellow Flower | Florges | Use Shiny Stone |
| Floette Orange Flower | Florges | Use Shiny Stone |
| Floette Blue Flower | Florges | Use Shiny Stone |
| Floette White Flower | Florges | Use Shiny Stone |
| Pumpkaboo Small | Gourgeist | Level 36 |
| Pumpkaboo Large | Gourgeist | Level 36 |
| Pumpkaboo Super | Gourgeist | Level 36 |
| Rockruff Own Tempo | Lycanroc (form 2) | Level 25 at dusk |
| Sinistea Antique | Poltegeist | Use Chipped Pot |
| Growlithe Hisuian | Arcanine (form 1) | Use Fire Stone |
| Voltorb Hisuian | Electrode (form 1) | Use Leaf Stone |
| Qwilfish Hisuian | Overqwil | Level up knowing Barb Barrage |
| Sneasel Hisuian | Sneasler | Use Razor Claw during the day |
| Zorua Hisuian | Zoroark (form 1) | Level 30 |
| Sliggoo Hisuian | Goodra (form 1) | Level 50 while it is raining |
| Frillish Female | Jellicent (form 1) | Level 40 (female) |
| Wooper Paldean | Clodsire | Level 20 |
| Poltchageist Masterpiece | Sinistcha | Use Chipped Pot |

## Mega Evolution entries

Mega Evolution requires the Mega Ring activation and usually the matching held Mega Stone. Rayquaza instead requires Dragon Ascent.

| Pokémon | Mega form | Requirement |
| --- | --- | --- |
| Venusaur | Mega Venusaur | Mega Stone |
| Charizard | Mega Charizard X | Mega Stone |
| Charizard | Mega Charizard Y | Mega Stone |
| Blastoise | Mega Blastoise | Mega Stone |
| Beedrill | Mega Beedrill | Mega Stone |
| Pidgeot | Mega Pidgeot | Mega Stone |
| Alakazam | Mega Alakazam | Mega Stone |
| Slowbro | Mega Slowbro | Mega Stone |
| Gengar | Mega Gengar | Mega Stone |
| Kangaskhan | Mega Kangaskhan | Mega Stone |
| Pinsir | Mega Pinsir | Mega Stone |
| Gyarados | Mega Gyarados | Mega Stone |
| Aerodactyl | Mega Aerodactyl | Mega Stone |
| Mewtwo | Mega Mewtwo X | Mega Stone |
| Mewtwo | Mega Mewtwo Y | Mega Stone |
| Meganium | Meganium | Form |
| Ampharos | Mega Ampharos | Mega Stone |
| Steelix | Mega Steelix | Mega Stone |
| Scizor | Mega Scizor | Mega Stone |
| Heracross | Mega Heracross | Mega Stone |
| Houndoom | Mega Houndoom | Mega Stone |
| Tyranitar | Mega Tyranitar | Mega Stone |
| Sceptile | Mega Sceptile | Mega Stone |
| Blaziken | Mega Blaziken | Mega Stone |
| Swampert | Mega Swampert | Mega Stone |
| Gardevoir | Mega Gardevoir | Mega Stone |
| Sableye | Mega Sableye | Mega Stone |
| Mawile | Mega Mawile | Mega Stone |
| Aggron | Mega Aggron | Mega Stone |
| Medicham | Mega Medicham | Mega Stone |
| Manectric | Mega Manectric | Mega Stone |
| Sharpedo | Mega Sharpedo | Mega Stone |
| Camerupt | Mega Camerupt | Mega Stone |
| Altaria | Mega Altaria | Mega Stone |
| Castform | Castform Sunny | Form |
| Castform | Castform Rainy | Form |
| Banette | Mega Banette | Mega Stone |
| Absol | Mega Absol | Mega Stone |
| Glalie | Mega Glalie | Mega Stone |
| Salamence | Mega Salamence | Mega Stone |
| Metagross | Mega Metagross | Mega Stone |
| Latias | Mega Latias | Mega Stone |
| Latios | Mega Latios | Mega Stone |
| Kyogre | Primal Kyogre | Primal |
| Groudon | Primal Groudon | Primal |
| Rayquaza | Mega Rayquaza | Mega Stone |
| Cherrim | Cherrim Sunshine | Form |
| Lopunny | Mega Lopunny | Mega Stone |
| Garchomp | Mega Garchomp | Mega Stone |
| Lucario | Mega Lucario | Mega Stone |
| Abomasnow | Mega Abomasnow | Mega Stone |
| Gallade | Mega Gallade | Mega Stone |
| Audino | Mega Audino | Mega Stone |
| Darmanitan | Darmanitan Zen Mode | Form |
| Darmanitan | Darmanitan Zen Mode Galarian | Form |
| Meloetta | Meloetta Pirouette | Form |
| Greninja | Greninja Ash | Form |
| Aegislash | Aegislash Blade | Form |
| Xerneas | Xerneas Active | Form |
| Zygarde | Zygarde 10 Complete | Form |
| Zygarde | Zygarde 50 Complete | Form |
| Diancie | Mega Diancie | Mega Stone |
| Wishiwashi | Wishiwashi School | Form |
| Minior | Minior Core Red | Form |
| Minior | Minior Core Orange | Form |
| Mimikyu | Mimikyu Busted | Form |
| Mimikyu | Mimikyu Busted Large | Form |
| Necrozma | Necrozma Ultra Dusk Mane | Form |
| Necrozma | Necrozma Ultra Dawn Wings | Form |
| Cramorant | Cramorant Gulping | Form |
| Cramorant | Cramorant Gorging | Form |
| Eiscue | Eiscue Noice Face | Form |
| Morpeko | Morpeko Hangry | Form |
| Zacian | Zacian Crowned | Form |
| Zamazenta | Zamazenta Crowned | Form |
| Eternatus | Eternatus Eternamax | Form |
| Palafin | Palafin Hero | Form |
| Ogerpon | Ogerpon Teal Mask Terastal | Form |
| Ogerpon | Ogerpon Wellspring Mask Terastal | Form |
| Terapagos | Terapagos Terastal | Form |
| Terapagos | Terapagos Stellar | Form |
| Mega Venusaur | Mega Venusaur | Mega Stone |
| Mega Charizard X | Mega Charizard X | Mega Stone |
| Mega Charizard Y | Mega Charizard Y | Mega Stone |
| Mega Blastoise | Mega Blastoise | Mega Stone |
| Mega Beedrill | Mega Beedrill | Mega Stone |
| Mega Pidgeot | Mega Pidgeot | Mega Stone |
| Mega Alakazam | Mega Alakazam | Mega Stone |
| Mega Slowbro | Mega Slowbro | Mega Stone |
| Mega Gengar | Mega Gengar | Mega Stone |
| Mega Kangaskhan | Mega Kangaskhan | Mega Stone |
| Mega Pinsir | Mega Pinsir | Mega Stone |
| Mega Gyarados | Mega Gyarados | Mega Stone |
| Mega Aerodactyl | Mega Aerodactyl | Mega Stone |
| Mega Mewtwo X | Mega Mewtwo X | Mega Stone |
| Mega Mewtwo Y | Mega Mewtwo Y | Mega Stone |
| Mega Ampharos | Mega Ampharos | Mega Stone |
| Mega Steelix | Mega Steelix | Mega Stone |
| Mega Scizor | Mega Scizor | Mega Stone |
| Mega Heracross | Mega Heracross | Mega Stone |
| Mega Houndoom | Mega Houndoom | Mega Stone |
| Mega Tyranitar | Mega Tyranitar | Mega Stone |
| Mega Sceptile | Mega Sceptile | Mega Stone |
| Mega Blaziken | Mega Blaziken | Mega Stone |
| Mega Swampert | Mega Swampert | Mega Stone |
| Mega Gardevoir | Mega Gardevoir | Mega Stone |
| Mega Sableye | Mega Sableye | Mega Stone |
| Mega Mawile | Mega Mawile | Mega Stone |
| Mega Aggron | Mega Aggron | Mega Stone |
| Mega Medicham | Mega Medicham | Mega Stone |
| Mega Manectric | Mega Manectric | Mega Stone |
| Mega Sharpedo | Mega Sharpedo | Mega Stone |
| Mega Camerupt | Mega Camerupt | Mega Stone |
| Mega Altaria | Mega Altaria | Mega Stone |
| Mega Banette | Mega Banette | Mega Stone |
| Mega Absol | Mega Absol | Mega Stone |
| Mega Glalie | Mega Glalie | Mega Stone |
| Mega Salamence | Mega Salamence | Mega Stone |
| Mega Metagross | Mega Metagross | Mega Stone |
| Mega Latias | Mega Latias | Mega Stone |
| Mega Latios | Mega Latios | Mega Stone |
| Mega Rayquaza | Mega Rayquaza | Mega Stone |
| Mega Lopunny | Mega Lopunny | Mega Stone |
| Mega Garchomp | Mega Garchomp | Mega Stone |
| Mega Lucario | Mega Lucario | Mega Stone |
| Mega Abomasnow | Mega Abomasnow | Mega Stone |
| Mega Gallade | Mega Gallade | Mega Stone |
| Mega Audino | Mega Audino | Mega Stone |
| Mega Diancie | Mega Diancie | Mega Stone |
| Primal Kyogre | Primal Kyogre | Primal |
| Primal Groudon | Primal Groudon | Primal |
| Rattata Alolan | Rattata Alolan | Form |
| Raticate Alolan | Raticate Alolan | Form |
| Raichu Alolan | Raichu Alolan | Form |
| Sandshrew Alolan | Sandshrew Alolan | Form |
| Sandslash Alolan | Sandslash Alolan | Form |
| Vulpix Alolan | Vulpix Alolan | Form |
| Ninetales Alolan | Ninetales Alolan | Form |
| Diglett Alolan | Diglett Alolan | Form |
| Dugtrio Alolan | Dugtrio Alolan | Form |
| Meowth Alolan | Meowth Alolan | Form |
| Persian Alolan | Persian Alolan | Form |
| Geodude Alolan | Geodude Alolan | Form |
| Graveler Alolan | Graveler Alolan | Form |
| Golem Alolan | Golem Alolan | Form |
| Grimer Alolan | Grimer Alolan | Form |
| Muk Alolan | Muk Alolan | Form |
| Exeggutor Alolan | Exeggutor Alolan | Form |
| Marowak Alolan | Marowak Alolan | Form |
| Raticate Alolan Large | Raticate Alolan Large | Form |
| Marowak Alolan Large | Marowak Alolan Large | Form |
| Gumshoos Large | Gumshoos Large | Form |
| Vikavolt Large | Vikavolt Large | Form |
| Ribombee Large | Ribombee Large | Form |
| Araquanid Large | Araquanid Large | Form |
| Lurantis Large | Lurantis Large | Form |
| Salazzle Large | Salazzle Large | Form |
| Togedemaru Large | Togedemaru Large | Form |
| Mimikyu Large | Mimikyu Large | Form |
| Mimikyu Busted Large | Mimikyu Busted Large | Form |
| Kommo O Large | Kommo O Large | Form |
| Meowth Galarian | Meowth Galarian | Form |
| Ponyta Galarian | Ponyta Galarian | Form |
| Rapidash Galarian | Rapidash Galarian | Form |
| Slowpoke Galarian | Slowpoke Galarian | Form |
| Slowbro Galarian | Slowbro Galarian | Form |
| Farfetchd Galarian | Farfetchd Galarian | Form |
| Weezing Galarian | Weezing Galarian | Form |
| Mr Mime Galarian | Mr Mime Galarian | Form |
| Articuno Galarian | Articuno Galarian | Form |
| Zapdos Galarian | Zapdos Galarian | Form |
| Moltres Galarian | Moltres Galarian | Form |
| Slowking Galarian | Slowking Galarian | Form |
| Corsola Galarian | Corsola Galarian | Form |
| Zigzagoon Galarian | Zigzagoon Galarian | Form |
| Linoone Galarian | Linoone Galarian | Form |
| Darumaka Galarian | Darumaka Galarian | Form |
| Darmanitan Galarian | Darmanitan Galarian | Form |
| Yamask Galarian | Yamask Galarian | Form |
| Stunfisk Galarian | Stunfisk Galarian | Form |
| Pikachu Cosplay | Pikachu Cosplay | Form |
| Pikachu Rock Star | Pikachu Rock Star | Form |
| Pikachu Belle | Pikachu Belle | Form |
| Pikachu Pop Star | Pikachu Pop Star | Form |
| Pikachu Ph D | Pikachu Ph D | Form |
| Pikachu Libre | Pikachu Libre | Form |
| Pikachu Original Cap | Pikachu Original Cap | Form |
| Pikachu Hoenn Cap | Pikachu Hoenn Cap | Form |
| Pikachu Sinnoh Cap | Pikachu Sinnoh Cap | Form |
| Pikachu Unova Cap | Pikachu Unova Cap | Form |
| Pikachu Kalos Cap | Pikachu Kalos Cap | Form |
| Pikachu Alola Cap | Pikachu Alola Cap | Form |
| Pikachu Partner Cap | Pikachu Partner Cap | Form |
| Pikachu World Cap | Pikachu World Cap | Form |
| Castform Sunny | Castform Sunny | Form |
| Castform Rainy | Castform Rainy | Form |
| Castform Snowy | Castform Snowy | Form |
| Cherrim Sunshine | Cherrim Sunshine | Form |
| Shellos East Sea | Shellos East Sea | Form |
| Gastrodon East Sea | Gastrodon East Sea | Form |
| Dialga Origin | Dialga Origin | Form |
| Palkia Origin | Palkia Origin | Form |
| Basculin Blue Striped | Basculin Blue Striped | Form |
| Basculin White Striped | Basculin White Striped | Form |
| Darmanitan Zen Mode | Darmanitan Zen Mode | Form |
| Darmanitan Zen Mode Galarian | Darmanitan Zen Mode Galarian | Form |
| Deerling Summer | Deerling Summer | Form |
| Deerling Autumn | Deerling Autumn | Form |
| Deerling Winter | Deerling Winter | Form |
| Sawsbuck Summer | Sawsbuck Summer | Form |
| Sawsbuck Autumn | Sawsbuck Autumn | Form |
| Sawsbuck Winter | Sawsbuck Winter | Form |
| Tornadus Therian | Tornadus Therian | Form |
| Thundurus Therian | Thundurus Therian | Form |
| Landorus Therian | Landorus Therian | Form |
| Kyurem White | Kyurem White | Form |
| Kyurem Black | Kyurem Black | Form |
| Keldeo Resolute | Keldeo Resolute | Form |
| Meloetta Pirouette | Meloetta Pirouette | Form |
| Genesect Douse Drive | Genesect Douse Drive | Form |
| Genesect Shock Drive | Genesect Shock Drive | Form |
| Genesect Burn Drive | Genesect Burn Drive | Form |
| Genesect Chill Drive | Genesect Chill Drive | Form |
| Greninja Battle Bond | Greninja Battle Bond | Form |
| Greninja Ash | Greninja Ash | Form |
| Vivillon Polar | Vivillon Polar | Form |
| Vivillon Tundra | Vivillon Tundra | Form |
| Vivillon Continental | Vivillon Continental | Form |
| Vivillon Garden | Vivillon Garden | Form |
| Vivillon Elegant | Vivillon Elegant | Form |
| Vivillon Meadow | Vivillon Meadow | Form |
| Vivillon Modern | Vivillon Modern | Form |
| Vivillon Marine | Vivillon Marine | Form |
| Vivillon Archipelago | Vivillon Archipelago | Form |
| Vivillon High Plains | Vivillon High Plains | Form |
| Vivillon Sandstorm | Vivillon Sandstorm | Form |
| Vivillon River | Vivillon River | Form |
| Vivillon Monsoon | Vivillon Monsoon | Form |
| Vivillon Savanna | Vivillon Savanna | Form |
| Vivillon Sun | Vivillon Sun | Form |
| Vivillon Ocean | Vivillon Ocean | Form |
| Vivillon Jungle | Vivillon Jungle | Form |
| Vivillon Fancy | Vivillon Fancy | Form |
| Vivillon Poke Ball | Vivillon Poke Ball | Form |
| Flabebe Yellow Flower | Flabebe Yellow Flower | Form |
| Flabebe Orange Flower | Flabebe Orange Flower | Form |
| Flabebe Blue Flower | Flabebe Blue Flower | Form |
| Flabebe White Flower | Flabebe White Flower | Form |
| Floette Yellow Flower | Floette Yellow Flower | Form |
| Floette Orange Flower | Floette Orange Flower | Form |
| Floette Blue Flower | Floette Blue Flower | Form |
| Floette White Flower | Floette White Flower | Form |
| Floette Eternal Flower | Floette Eternal Flower | Form |
| Florges Yellow Flower | Florges Yellow Flower | Form |
| Florges Orange Flower | Florges Orange Flower | Form |
| Florges Blue Flower | Florges Blue Flower | Form |
| Florges White Flower | Florges White Flower | Form |
| Furfrou Heart | Furfrou Heart | Form |
| Furfrou Star | Furfrou Star | Form |
| Furfrou Diamond | Furfrou Diamond | Form |
| Furfrou Debutante | Furfrou Debutante | Form |
| Furfrou Matron | Furfrou Matron | Form |
| Furfrou Dandy | Furfrou Dandy | Form |
| Furfrou La Reine | Furfrou La Reine | Form |
| Furfrou Kabuki | Furfrou Kabuki | Form |
| Furfrou Pharaoh | Furfrou Pharaoh | Form |
| Aegislash Blade | Aegislash Blade | Form |
| Pumpkaboo Small | Pumpkaboo Small | Form |
| Pumpkaboo Large | Pumpkaboo Large | Form |
| Pumpkaboo Super | Pumpkaboo Super | Form |
| Gourgeist Small | Gourgeist Small | Form |
| Gourgeist Large | Gourgeist Large | Form |
| Gourgeist Super | Gourgeist Super | Form |
| Xerneas Active | Xerneas Active | Form |
| Zygarde 10 | Zygarde 10 | Form |
| Zygarde 10 Power Construct | Zygarde 10 Power Construct | Form |
| Zygarde 50 Power Construct | Zygarde 50 Power Construct | Form |
| Zygarde 10 Complete | Zygarde 10 Complete | Form |
| Zygarde 50 Complete | Zygarde 50 Complete | Form |
| Hoopa Unbound | Hoopa Unbound | Form |
| Oricorio Pom Pom | Oricorio Pom Pom | Form |
| Oricorio Pau | Oricorio Pau | Form |
| Oricorio Sensu | Oricorio Sensu | Form |
| Rockruff Own Tempo | Rockruff Own Tempo | Form |
| Lycanroc Midnight | Lycanroc Midnight | Form |
| Lycanroc Dusk | Lycanroc Dusk | Form |
| Wishiwashi School | Wishiwashi School | Form |
| Minior Meteor Orange | Minior Meteor Orange | Form |
| Minior Meteor Yellow | Minior Meteor Yellow | Form |
| Minior Meteor Green | Minior Meteor Green | Form |
| Minior Meteor Blue | Minior Meteor Blue | Form |
| Minior Meteor Indigo | Minior Meteor Indigo | Form |
| Minior Meteor Violet | Minior Meteor Violet | Form |
| Minior Core Red | Minior Core Red | Form |
| Minior Core Orange | Minior Core Orange | Form |
| Minior Core Yellow | Minior Core Yellow | Form |
| Minior Core Green | Minior Core Green | Form |
| Minior Core Blue | Minior Core Blue | Form |
| Minior Core Indigo | Minior Core Indigo | Form |
| Minior Core Violet | Minior Core Violet | Form |
| Mimikyu Busted | Mimikyu Busted | Form |
| Necrozma Dusk Mane | Necrozma Dusk Mane | Form |
| Necrozma Dawn Wings | Necrozma Dawn Wings | Form |
| Necrozma Ultra Dusk Mane | Necrozma Ultra Dusk Mane | Form |
| Necrozma Ultra Dawn Wings | Necrozma Ultra Dawn Wings | Form |
| Magearna Original | Magearna Original | Form |
| Pikachu Partner | Pikachu Partner | Form |
| Eevee Partner | Eevee Partner | Form |
| Cramorant Gulping | Cramorant Gulping | Form |
| Cramorant Gorging | Cramorant Gorging | Form |
| Toxtricity Low Key | Toxtricity Low Key | Form |
| Sinistea Antique | Sinistea Antique | Form |
| Polteageist Antique | Polteageist Antique | Form |
| Alcremie Berry Sweet | Alcremie Berry Sweet | Form |
| Alcremie Love Sweet | Alcremie Love Sweet | Form |
| Alcremie Star Sweet | Alcremie Star Sweet | Form |
| Alcremie Clover Sweet | Alcremie Clover Sweet | Form |
| Alcremie Flower Sweet | Alcremie Flower Sweet | Form |
| Alcremie Ribbon Sweet | Alcremie Ribbon Sweet | Form |
| Eiscue Noice Face | Eiscue Noice Face | Form |
| Morpeko Hangry | Morpeko Hangry | Form |
| Zacian Crowned | Zacian Crowned | Form |
| Zamazenta Crowned | Zamazenta Crowned | Form |
| Eternatus Eternamax | Eternatus Eternamax | Form |
| Urshifu Rapid Strike | Urshifu Rapid Strike | Form |
| Zarude Dada | Zarude Dada | Form |
| Calyrex Ice Rider | Calyrex Ice Rider | Form |
| Calyrex Shadow Rider | Calyrex Shadow Rider | Form |
| Enamorus Therian | Enamorus Therian | Form |
| Growlithe Hisuian | Growlithe Hisuian | Form |
| Arcanine Hisuian | Arcanine Hisuian | Form |
| Voltorb Hisuian | Voltorb Hisuian | Form |
| Electrode Hisuian | Electrode Hisuian | Form |
| Typhlosion Hisuian | Typhlosion Hisuian | Form |
| Qwilfish Hisuian | Qwilfish Hisuian | Form |
| Sneasel Hisuian | Sneasel Hisuian | Form |
| Samurott Hisuian | Samurott Hisuian | Form |
| Lilligant Hisuian | Lilligant Hisuian | Form |
| Zorua Hisuian | Zorua Hisuian | Form |
| Zoroark Hisuian | Zoroark Hisuian | Form |
| Braviary Hisuian | Braviary Hisuian | Form |
| Sliggoo Hisuian | Sliggoo Hisuian | Form |
| Goodra Hisuian | Goodra Hisuian | Form |
| Avalugg Hisuian | Avalugg Hisuian | Form |
| Decidueye Hisuian | Decidueye Hisuian | Form |
| Kleavor Lord | Kleavor Lord | Form |
| Lilligant Lady | Lilligant Lady | Form |
| Arcanine Lord | Arcanine Lord | Form |
| Electrode Lord | Electrode Lord | Form |
| Avalugg Lord | Avalugg Lord | Form |
| Unfezant Female | Unfezant Female | Form |
| Frillish Female | Frillish Female | Form |
| Jellicent Female | Jellicent Female | Form |
| Pyroar Female | Pyroar Female | Form |
| Meowstic Female | Meowstic Female | Form |
| Indeedee Female | Indeedee Female | Form |
| Basculegion Female | Basculegion Female | Form |
| Maushold Family Of Three | Maushold Family Of Three | Form |
| Squawkabilly Blue Plumage | Squawkabilly Blue Plumage | Form |
| Squawkabilly Yellow Plumage | Squawkabilly Yellow Plumage | Form |
| Squawkabilly White Plumage | Squawkabilly White Plumage | Form |
| Palafin Hero | Palafin Hero | Form |
| Tatsugiri Droopy | Tatsugiri Droopy | Form |
| Tatsugiri Stretchy | Tatsugiri Stretchy | Form |
| Dudunsparce Three Segment | Dudunsparce Three Segment | Form |
| Gimmighoul Roaming | Gimmighoul Roaming | Form |
| Wooper Paldean | Wooper Paldean | Form |
| Tauros Combat | Tauros Combat | Form |
| Tauros Blaze | Tauros Blaze | Form |
| Tauros Aqua | Tauros Aqua | Form |
| Oinkologne Female | Oinkologne Female | Form |
| Revavroom Segin | Revavroom Segin | Form |
| Revavroom Schedar | Revavroom Schedar | Form |
| Revavroom Navi | Revavroom Navi | Form |
| Revavroom Ruchbah | Revavroom Ruchbah | Form |
| Koraidon Limited Build | Koraidon Limited Build | Form |
| Koraidon Sprinting Build | Koraidon Sprinting Build | Form |
| Koraidon Swimming Build | Koraidon Swimming Build | Form |
| Koraidon Gliding Build | Koraidon Gliding Build | Form |
| Miraidon Low Power Mode | Miraidon Low Power Mode | Form |
| Miraidon Drive Mode | Miraidon Drive Mode | Form |
| Miraidon Aquatic Mode | Miraidon Aquatic Mode | Form |
| Miraidon Glide Mode | Miraidon Glide Mode | Form |
| Poltchageist Masterpiece | Poltchageist Masterpiece | Form |
| Sinistcha Masterpiece | Sinistcha Masterpiece | Form |
| Ogerpon Wellspring Mask | Ogerpon Wellspring Mask | Form |
| Ogerpon Hearthflame Mask | Ogerpon Hearthflame Mask | Form |
| Ogerpon Cornerstone Mask | Ogerpon Cornerstone Mask | Form |
| Ogerpon Teal Mask Terastal | Ogerpon Teal Mask Terastal | Form |
| Ogerpon Wellspring Mask Terastal | Ogerpon Wellspring Mask Terastal | Form |
| Ogerpon Hearthflame Mask Terastal | Ogerpon Hearthflame Mask Terastal | Form |
| Ogerpon Cornerstone Mask Terastal | Ogerpon Cornerstone Mask Terastal | Form |
| Ursaluna Bloodmoon | Ursaluna Bloodmoon | Form |
| Terapagos Terastal | Terapagos Terastal | Form |
| Terapagos Stellar | Terapagos Stellar | Form |
