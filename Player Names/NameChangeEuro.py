def name_change(df): # A bit of manual effort - need to all for other teams as well :(
    name_replacements = \
    {'Kobbie Mainoo':'Kobbie Mainoo',
    'Virgil van Dijk':'Virgil van Dijk',
    'Jordan Pickford':'Jordan Pickford',
    'John Stones':'John Stones',
    'Nathan Aké':'Nathan Aké',
    'Stefan de Vrij':'Stefan de Vrij',
    'Jerdy Schouten':'Jerdy Schouten',
    'Denzel Dumfries':'Denzel Dumfries',
    'Marc Guehi':'Marc Guehi',
    'Declan Rice':'Declan Rice',
    'Jude Bellingham':'Jude Bellingham',
    'Kieran Trippier':'Kieran Trippier',
    'Phil Foden':'Phil Foden',
    'Kyle Walker':'Kyle Walker',
    'Bukayo Saka':'Bukayo Saka',
    'Harry Kane':'Harry Kane',
    'Bart Verbruggen':'Bart Verbruggen',
    'Memphis Depay':'Memphis Depay',
    'Xavi Simons':'Xavi Simons',
    'Tijjani Reijnders':'Tijjani Reijnders',
    'Donyell Malen':'Donyell Malen',
    'Cody Mathès Gakpo':'Cody Gakpo',
    'Joey Veerman':'Joey Veerman',
    'Luke Shaw':'Luke Shaw',
    'Wout Weghorst':'Wout Weghorst',
    'Cole Palmer':'Cole Palmer',
    'Ollie Watkins':'Ollie Watkins',
    'Joshua Zirkzee':'Joshua Zirkzee',
    'Conor Gallagher':'Conor Gallagher',
    'Brian Brobbey':'Brian Brobbey',
    'Unai Simón Mendibil':'Unai Simón',
    'Robin Aime Robert Le Normand':'Robin Le Normand',
    'Daniel Carvajal Ramos':'Daniel Carvajal',
    'Álvaro Borja Morata Martín':'Álvaro Morata',
    'Daniel Olmo Carvajal':'Daniel Olmo',
    'Rodrigo Hernández Cascante':'Rodrigo Hernández',
    'Aymeric Laporte':'Aymeric Laporte',
    'Lamine Yamal Nasraoui Ebana':'Lamine Yamal',
    'Marc Cucurella Saseta':'Marc Cucurella',
    'Nicholas Williams Arthuer':'Nicholas Williams',
    'Fabián Ruiz Peña':'Fabián Ruiz',
    'Martín Zubimendi Ibáñez':'Martín Zubimendi',
    'Mikel Oyarzabal Ugarte':'Mikel Oyarzabal',
    'José Ignacio Fernández Iglesias':'Nacho',
    'Ivan Toney':'Ivan Toney',
    'Mikel Merino Zazón':'Mikel Merino',
    'Adrien Rabiot':'Adrien Rabiot',
    'N\'Golo Kanté':'N\'Golo Kanté',
    'Jules Koundé':'Jules Koundé',
    'Dayotchanculle Upamecano':'Dayot Upamecano',
    'Randal Kolo Muani':'Randal Kolo',
    'Aurélien Djani Tchouaméni':'Aurélien Tchouaméni',
    'William Saliba':'William Saliba',
    'Mike Maignan':'Mike Maignan',
    'Jesús Navas González':'Jesús Navas',
    'Theo Bernard François Hernández':'Theo Hernández',
    'Kylian Mbappé Lottin':'Kylian Mbappé',
    'Ousmane Dembélé':'Ousmane Dembélé',
    'Daniel Vivian Moreno':'Daniel Vivian',
    'Antoine Griezmann':'Antoine Griezmann',
    'Eduardo Camavinga':'Eduardo Camavinga',
    'Bradley Barcola':'Bradley Barcola',
    'Ferrán Torres García':'Ferrán Torres',
    'Olivier Giroud':'Olivier Giroud',
    'Hakan Çalhanoğlu':'Hakan Çalhanoğlu',
    'Kaan Ayhan':'Kaan Ayhan',
    'Fehmi Mert Günok':'Fehmi Mert',
    'Salih Özcan':'Salih Özcan',
    'Samet Akaydin':'Samet Akaydin',
    'Abdülkerim Bardakcı':'Abdülkerim Bardakcı',
    'Steven Bergwijn':'Steven Bergwijn',
    'Mert Müldür':'Mert Müldür',
    'Arda Güler':'Arda Güler',
    'Ferdi Erenay Kadıoğlu':'Ferdi Kadıoğlu',
    'Kenan Yildiz':'Kenan Yildiz',
    'Barış Alper Yılmaz':'Barış Yılmaz',
    'Micky van de Ven':'Micky van de Ven',
    'Okay Yokuşlu':'Okay Yokuşlu',
    'Mehmet Zeki Çelik':'Mehmet Zeki',
    'Muhammed Kerem Aktürkoğlu':'Kerem Aktürkoğlu',
    'Jeremie Frimpong':'Jeremie Frimpong',
    'Semih Kılıçsoy':'Semih Kılıçsoy',
    'Cenk Tosun':'Cenk Tosun',
    'Bertuğ Özgür Yıldırım':'Bertuğ Yıldırım',
    'João Maria Lobo Alves Palhinha Gonçalves':'João Palhinha',
    'Bruno Miguel Borges Fernandes':'Bruno Fernandes',
    'Kléper Laveran Lima Ferreira':'Pepe',
    'Diogo Meireles Costa':'Diogo Costa',
    'Rúben Santos Gato Alves Dias':'Rúben Dias',
    'João Pedro Cavaco Cancelo':'João Cancelo',
    'Nuno Mendes':'Nuno Mendes',
    'Rafael Alexandre Conceição Leão':'Rafael Leão',
    'Cristiano Ronaldo dos Santos Aveiro':'Cristiano Ronaldo',
    'Bernardo Mota Veiga de Carvalho e Silva':'Bernardo Silva',
    'Vitor Machado Ferreira':'Vitor Ferreira',
    'Nélson Cabral Semedo':'Nélson Semedo',
    'Francisco Fernandes Conceição':'Francisco Conceição',
    'Rúben Diogo Da Silva Neves':'Rúben Neves',
    'Marcus Thuram':'Marcus Thuram',
    'Youssouf Fofana':'Youssouf Fofana',
    'João Félix Sequeira':'João Félix',
    'Matheus Luiz Nunes':'Matheus Nunes',
    'Marcel Sabitzer':'Marcel Sabitzer',
    'Nicolas Seiwald':'Nicolas Seiwald',
    'Patrick Wimmer':'Patrick Wimmer',
    'Alexander Prass':'Alexander Prass',
    'Florian Grillitsch':'Florian Grillitsch',
    'Philipp Lienhart':'Philipp Lienhart',
    'Stefan Posch':'Stefan Posch',
    'Maximilian Wöber':'Maximilian Wöber',
    'Patrick Pentz':'Patrick Pentz',
    'Romano Schmid':'Romano Schmid',
    'Lutsharel Geertruida':'Lutsharel Geertruida',
    'Marko Arnautović':'Marko Arnautović',
    'Leopold Querfeld':'Leopold Querfeld',
    'Georginio Wijnaldum':'Georginio Wijnaldum',
    'Konrad Laimer':'Konrad Laimer',
    'Christoph Baumgartner':'Christoph Baumgartner',
    'Michael Gregoritsch':'Michael Gregoritsch',
    'Andreas Weimann':'Andreas Weimann',
    'Jannik Vestergaard':'Jannik Vestergaard',
    'Christian Dannemann Eriksen':'Christian Eriksen',
    'Rasmus Winther Højlund':'Rasmus Højlund',
    'Pierre-Emile Højbjerg':'Pierre Højbjerg',
    'Trent Alexander-Arnold':'Trent Alexander-Arnold',
    'Victor Bernth Kristansen':'Victor Kristansen',
    'Joakim Mæhle':'Joakim Mæhle',
    'Morten Hjulmand':'Morten Hjulmand',
    'Andreas Christensen':'Andreas Christensen',
    'Joachim Andersen':'Joachim Andersen',
    'Jonas Older Wind':'Jonas Wind',
    'Kasper Schmeichel':'Kasper Schmeichel',
    'Alexander Hartmann Bah':'Alexander Hartmann',
    'Mikkel Damsgaard':'Mikkel Damsgaard',
    'Jarrod Bowen':'Jarrod Bowen',
    'Eberechi Eze':'Eberechi Eze',
    'Yussuf Yurary Poulsen':'Yussuf Poulsen',
    'Andreas Skov Olsen':'Andreas Skov Olsen',
    'Christian Nørgaard':'Christian Nørgaard',
    'Ricardo Iván Rodríguez Araya':'Ricardo Rodríguez',
    'Yann Sommer':'Yann Sommer',
    'Ezri Konsa Ngoyo':'Ezri Konsa',
    'Granit Xhaka':'Granit Xhaka',
    'Fabian Lukas Schär':'Fabian Schär',
    'Manuel Obafemi Akanji':'Manuel Akanji',
    'Breel-Donald Embolo':'Breel Embolo',
    'Fabian Rieder':'Fabian Rieder',
    'Michel Aebischer':'Michel Aebischer',
    'Dan Ndoye':'Dan Ndoye',
    'Remo Freuler':'Remo Freuler',
    'Ruben Vargas':'Ruben Vargas',
    'Silvan Widmer':'Silvan Widmer',
    'Steven Zuber':'Steven Zuber',
    'Denis Lemi Zakaria Lako Lado':'Denis Zakaria',
    'Xherdan Shaqiri':'Xherdan Shaqiri',
    'Vincent Sierro':'Vincent Sierro',
    'Mohamed Zeki Amdouni':'Mohamed Amdouni',
    'Kai Havertz':'Kai Havertz',
    'Toni Kroos':'Toni Kroos',
    'Jamal Musiala':'Jamal Musiala',
    'David Raum':'David Raum',
    'Jonathan Tah':'Jonathan Tah',
    'Emre Can':'Emre Can',
    'Antonio Rüdiger':'Antonio Rüdiger',
    'Joshua Kimmich':'Joshua Kimmich',
    'Manuel Neuer':'Manuel Neuer',
    'İlkay Gündoğan':'İlkay Gündoğan',
    'Leroy Sané':'Leroy Sané',
    'Robert Andrich':'Robert Andrich',
    'Florian Wirtz':'Florian Wirtz',
    'Maximilian Mittelstädt':'Maximilian Mittelstädt',
    'Niclas Füllkrug':'Niclas Füllkrug',
    'Thomas Müller':'Thomas Müller',
    'Waldemar Anton':'Waldemar Anton',
    'José Luis Sanmartín Mato':'José Sanmartín',
    'Pedro González López':'Pedri',
    'Nico Schlotterbeck':'Nico Schlotterbeck',
    'Deniz Undav':'Deniz Undav',
    'Kevin De Bruyne':'Kevin De Bruyne',
    'Youri Tielemans':'Youri Tielemans',
    'Jan Vertonghen':'Jan Vertonghen',
    'Koen Casteels':'Koen Casteels',
    'Wout Faes':'Wout Faes',
    'Oleksandr Svatok':'Oleksandr Svatok',
    'Artem Dovbyk':'Artem Dovbyk',
    'Roman Yaremchuk':'Roman Yaremchuk',
    'Georgiy Sudakov':'Georgiy Sudakov',
    'Mykola Shaparenko':'Mykola Shaparenko',
    'Vitalii Mykolenko':'Vitalii Mykolenko',
    'Amadou Onana':'Amadou Onana',
    'Leandro Trossard':'Leandro Trossard',
    'Timothy Castagne':'Timothy Castagne',
    'Arthur Theate':'Arthur Theate',
    'Anatolii Trubin':'Anatolii Trubin',
    'Oleksandr Tymchyk':'Oleksandr Tymchyk',
    'Illia Zabarnyi':'Illia Zabarnyi',
    'Jeremy Doku':'Jeremy Doku',
    'Romelu Lukaku Menama':'Romelu Lukaku',
    'Mykola Matvienko':'Mykola Matvienko',
    'Volodymyr Brazhko':'Volodymyr Brazhko',
    'Oleksandr Zinchenko':'Oleksandr Zinchenko',
    'Orel Mangala':'Orel Mangala',
    'Yannick Ferreira Carrasco':'Yannick Carrasco',
    'Taras Stepanenko':'Taras Stepanenko',
    'Ruslan Malinovskiy':'Ruslan Malinovskiy',
    'Johan Bakayoko':'Johan Bakayoko',
    'Vladyslav Vanat':'Vladyslav Vanat',
    'Andriy Yarmolenko':'Andriy Yarmolenko',
    'Ikoma Loïs Openda':'Ikoma Openda',
    'Antonín Barák':'Antonín Barák',
    'Ladislav Krejčí':'Ladislav Krejčí',
    'Tomáš Holeš':'Tomáš Holeš',
    'Merih Demiral':'Merih Demiral',
    'Lukáš Provod':'Lukáš Provod',
    'Vladimír Coufal':'Vladimír Coufal',
    'Jindřich Staněk':'Jindřich Staněk',
    'Adam Hložek':'Adam Hložek',
    'David Jurásek':'David Jurásek',
    'Robin Hranáč':'Robin Hranáč',
    'İsmail Yüksek':'İsmail Yüksek',
    'Tomáš Souček':'Tomáš Souček',
    'Mojmír Chytil':'Mojmír Chytil',
    'Matěj Kovář':'Matěj Kovář',
    'Tomáš Chorý':'Tomáš Chorý',
    'Ondřej Lingr':'Ondřej Lingr',
    'Jan Kuchta':'Jan Kuchta',
    'Matěj Jurásek':'Matěj Jurásek',
    'Orkun Kökçü':'Orkun Kökçü',
    'Patrik Schick':'Patrik Schick',
    'Uğurcan Çakır':'Uğurcan Çakır',
    'Vitezslav Jaros':'Vitezslav Jaros',
    'Lukáš Červ':'Lukáš Červ',
    'Philipp Mwene':'Philipp Mwene',
    'Kevin Danso':'Kevin Danso',
    'İrfan Can Kahveci':'İrfan Can Kahveci',
    'Florin Constantin Niţă':'Florin Constantin Niţă',
    'Marius Mihai Marin':'Marius Mihai Marin',
    'Denis Mihai Drăguş':'Denis Mihai Drăguş',
    'Radu Drăgușin':'Radu Drăgușin',
    'Răzvan Gabriel Marin':'Răzvan Gabriel Marin',
    'Andrei Florin Ratiu':'Andrei Florin Ratiu',
    'Vasile Mogoș':'Vasile Mogoș',
    'Ianis Hagi':'Ianis Hagi',
    'Nicolae Claudiu Stanciu':'Nicolae Claudiu Stanciu',
    'Dennis Man':'Dennis Man',
    'Andrei Burcă Andonie':'Andrei Burcă Andonie',
    'Bogdan Racovițan':'Bogdan Racovițan',
    'Alexandru Cicâldău':'Alexandru Cicâldău',
    'Valentin Mihai Mihăilă':'Valentin Mihai Mihăilă',
    'Darius Dumitru Olaru':'Darius Dumitru Olaru',
    'Denis Alibec':'Denis Alibec',
    'Jan Oblak':'Jan Oblak',
    'Jure Balkovec':'Jure Balkovec',
    'Jaka Bijol':'Jaka Bijol',
    'Timi Elšnik':'Timi Elšnik',
    'Jan Mlakar':'Jan Mlakar',
    'Benjamin Šeško':'Benjamin Šeško',
    'Adam Gnezda Čerin':'Adam Gnezda Čerin',
    'Andraž Šporar':'Andraž Šporar',
    'Petar Stojanović':'Petar Stojanović',
    'Vanja Drkušić':'Vanja Drkušić',
    'Žan Karničnik':'Žan Karničnik',
    'Diogo José Teixeira da Silva':'Diogo José Teixeira da Silva',
    'Žan Celar':'Žan Celar',
    'Jon Gorenc Stankovič':'Jon Gorenc Stankovič',
    'Benjamin Verbič':'Benjamin Verbič',
    'Josip Iličić':'Josip Iličić',
    'Dodi Lukebakio':'Dodi Lukebakio',
    'Charles De Ketelaere':'Charles De Ketelaere',
    'Otar Kiteishvili':'Otar Kiteishvili',
    'Luka Lochoshvili':'Luka Lochoshvili',
    'Guram Kashia':'Guram Kashia',
    'Giorgi Mamardashvili':'Giorgi Mamardashvili',
    'Giorgi Chakvetadze':'Giorgi Chakvetadze',
    'Lasha Dvali':'Lasha Dvali',
    'Khvicha Kvaratskhelia':'Khvicha Kvaratskhelia',
    'Giorgi Kochorashvili':'Giorgi Kochorashvili',
    'Georges Mikautadze':'Georges Mikautadze',
    'Giorgi Gvelesiani':'Giorgi Gvelesiani',
    'Otar Kakabadze':'Otar Kakabadze',
    'Sandro Altunashvili':'Sandro Altunashvili',
    'Zuriko Davitashvili':'Zuriko Davitashvili',
    'Alejandro Grimaldo García':'Alejandro Grimaldo García',
    'Heorhii Tsitaishvili':'Heorhii Tsitaishvili',
    'Nika Kvekveskiri':'Nika Kvekveskiri',
    'Budu Zivzivadze':'Budu Zivzivadze',
    'David Strelec':'David Strelec',
    'Milan Škriniar':'Milan Škriniar',
    'Denis Vavro':'Denis Vavro',
    'Martin Dúbravka':'Martin Dúbravka',
    'Ondrej Duda':'Ondrej Duda',
    'Stanislav Lobotka':'Stanislav Lobotka',
    'Peter Pekarík':'Peter Pekarík',
    'Dávid Hancko':'Dávid Hancko',
    'Lukáš Haraslín':'Lukáš Haraslín',
    'Juraj Kucka':'Juraj Kucka',
    'Ivan Schranz':'Ivan Schranz',
    'Róbert Boženík':'Róbert Boženík',
    'Tomáš Suslov':'Tomáš Suslov',
    'Matúš Bero':'Matúš Bero',
    'László Bénes':'László Bénes',
    'Norbert Gyömbér':'Norbert Gyömbér',
    'Ľubomír Tupta':'Ľubomír Tupta',
    'Strahinja Pavlović':'Strahinja Pavlović',
    'Srđan Mijailović':'Srđan Mijailović',
    'Nikola Milenković':'Nikola Milenković',
    'Milos Veljkovic':'Milos Veljkovic',
    'Predrag Rajković':'Predrag Rajković',
    'Andrija Živković':'Andrija Živković',
    'Lazar Samardžić':'Lazar Samardžić',
    'Aleksandar Mitrović':'Aleksandar Mitrović',
    'Ivan Ilić':'Ivan Ilić',
    'Saša Lukić':'Saša Lukić',
    'Nemanja Gudelj':'Nemanja Gudelj',
    'Luka Jović':'Luka Jović',
    'Dušan Tadić':'Dušan Tadić',
    'Dušan Vlahović':'Dušan Vlahović',
    'Kasper Dolberg':'Kasper Dolberg',
    'Filip Mladenović':'Filip Mladenović',
    'Thomas Delaney':'Thomas Delaney',
    'Sergej Milinković-Savić':'Sergej Milinković-Savić',
    'Qazim Laçi':'Qazim Laçi',
    'Ylber Ramadani':'Ylber Ramadani',
    'Rey Manaj':'Rey Manaj',
    'David Raya Martin':'David Raya Martin',
    'Nedim Bajrami':'Nedim Bajrami',
    'Mario Mitaj':'Mario Mitaj',
    'Berat Djimsiti':'Berat Djimsiti',
    'Thomas Strakosha':'Thomas Strakosha',
    'Kristjan Asllani':'Kristjan Asllani',
    'Iván Balliu Campeny':'Iván Balliu Campeny',
    'Jasir Asani':'Jasir Asani',
    'Arlind Afrim Ajeti':'Arlind Afrim Ajeti',
    'Armando Broja':'Armando Broja',
    'Fermin Lopez Marin':'Fermin Lopez Marin',
    'Medon Berisha':'Medon Berisha',
    'Arbër Hoxha':'Arbër Hoxha',
    'Ernest Muçi':'Ernest Muçi',
    'Alejandro Baena Rodríguez':'Alejandro Baena Rodríguez',
    'Benjamin Henrichs':'Benjamin Henrichs',
    'Jacob Bruun Larsen':'Jacob Bruun Larsen',
    'Gianluca Mancini':'Gianluca Mancini',
    'Nicolò Barella':'Nicolò Barella',
    'Federico Chiesa':'Federico Chiesa',
    'Gianluigi Donnarumma':'Gianluigi Donnarumma',
    'Giovanni Di Lorenzo':'Giovanni Di Lorenzo',
    'Bryan Cristante':'Bryan Cristante',
    'Matteo Darmian':'Matteo Darmian',
    'Alessandro Bastoni':'Alessandro Bastoni',
    'Nicolò Fagioli':'Nicolò Fagioli',
    'Stephan El Shaarawy':'Stephan El Shaarawy',
    'Gianluca Scamacca':'Gianluca Scamacca',
    'Mattia Zaccagni':'Mattia Zaccagni',
    'Lorenzo Pellegrini':'Lorenzo Pellegrini',
    'Kwadwo Duah':'Kwadwo Duah',
    'Leonidas Stergiou':'Leonidas Stergiou',
    'Andrea Cambiaso':'Andrea Cambiaso',
    'Mateo Retegui':'Mateo Retegui',
    'Davide Frattesi':'Davide Frattesi',
    'Renato Steffen':'Renato Steffen',
    'András Schäfer':'András Schäfer',
    'Willi Orban':'Willi Orban',
    'Jack Hendry':'Jack Hendry',
    'Grant Campbell Hanley':'Grant Campbell Hanley',
    'Billy Gilmour':'Billy Gilmour',
    'Scott McKenna':'Scott McKenna',
    'Andrew Robertson':'Andrew Robertson',
    'Callum Styles':'Callum Styles',
    'John McGinn':'John McGinn',
    'Che Adams':'Che Adams',
    'Péter Gulácsi':'Péter Gulácsi',
    'Endre Botka':'Endre Botka',
    'Barnabás Varga':'Barnabás Varga',
    'Dominik Szoboszlai':'Dominik Szoboszlai',
    'Roland Sallai':'Roland Sallai',
    'Scott McTominay':'Scott McTominay',
    'Callum McGregor':'Callum McGregor',
    'Anthony Ralston':'Anthony Ralston',
    'Angus Gunn':'Angus Gunn',
    'Márton Dárdai':'Márton Dárdai',
    'Milos Kerkez':'Milos Kerkez',
    'Bendegúz Bolla':'Bendegúz Bolla',
    'Ádám Nagy':'Ádám Nagy',
    'Martin Ádám':'Martin Ádám',
    'Attila Szalai':'Attila Szalai',
    'Stuart Armstrong':'Stuart Armstrong',
    'Lawrence Shankland':'Lawrence Shankland',
    'Ryan Christie':'Ryan Christie',
    'Kenneth McLean':'Kenneth McLean',
    'Kevin Csoboth':'Kevin Csoboth',
    'Zsolt Nagy':'Zsolt Nagy',
    'Lewis Morgan':'Lewis Morgan',
    'László Kleinheisler':'László Kleinheisler',
    'Kingsley Coman':'Kingsley Coman',
    'Jorge Luiz Frello Filho':'Jorge Luiz Frello Filho',
    'Riccardo Calafiori':'Riccardo Calafiori',
    'Federico Dimarco':'Federico Dimarco',
    'Giacomo Raspadori':'Giacomo Raspadori',
    'Ayoze Pérez Gutiérrez':'Ayoze Pérez Gutiérrez',
    'Josip Šutalo':'Josip Šutalo',
    'Marcelo Brozović':'Marcelo Brozović',
    'Dominik Livaković':'Dominik Livaković',
    'Joško Gvardiol':'Joško Gvardiol',
    'Josip Juranović':'Josip Juranović',
    'Elseid Hysaj':'Elseid Hysaj',
    'Luka Modrić':'Luka Modrić',
    'Ivan Perišić':'Ivan Perišić',
    'Mateo Kovačić':'Mateo Kovačić',
    'Andrej Kramarić':'Andrej Kramarić',
    'Lovro Majer':'Lovro Majer',
    'Bruno Petković':'Bruno Petković',
    'Luka Sučić':'Luka Sučić',
    'Mario Pašalić':'Mario Pašalić',
    'Taulant Sulejmanov':'Taulant Sulejmanov',
    'Ante Budimir':'Ante Budimir',
    'Klaus Gjasula':'Klaus Gjasula',
    'Mirlind Daku':'Mirlind Daku',
    'Martin Baturina':'Martin Baturina',
    'Borna Sosa':'Borna Sosa',
    'Ivica Ivušić':'Ivica Ivušić',
    'Attila Fiola':'Attila Fiola',
    'Chris Führich':'Chris Führich',
    'Dániel Gazdag':'Dániel Gazdag',
    'Gernot Trauner':'Gernot Trauner',
    'Zeno Debast':'Zeno Debast',
    'Adam Obert':'Adam Obert',
    'Dávid Ďuriš':'Dávid Ďuriš',
    'Michael Ijemuan Folorunsho':'Michael Ijemuan Folorunsho',
    'Piotr Zieliński':'Piotr Zieliński',
    'Sebastian Szymański':'Sebastian Szymański',
    'Nicola Zalewski':'Nicola Zalewski',
    'Bartosz Salamon':'Bartosz Salamon',
    'Jakub Piotr Kiwior':'Jakub Piotr Kiwior',
    'Przemysław Frankowski':'Przemysław Frankowski',
    'Wojciech Szczęsny':'Wojciech Szczęsny',
    'Jan Bednarek':'Jan Bednarek',
    'Kacper Urbanski':'Kacper Urbanski',
    'Taras Wiktorowicz Romanczuk':'Taras Wiktorowicz Romanczuk',
    'Adam Buksa':'Adam Buksa',
    'Jakub Moder':'Jakub Moder',
    'Karol Świderski':'Karol Świderski',
    'Bartosz Slisz':'Bartosz Slisz',
    'Jakub Piotrowski':'Jakub Piotrowski',
    'Bartosz Bereszyński':'Bartosz Bereszyński',
    'Mykhailo Mudryk':'Mykhailo Mudryk',
    'Oleksandr Zubkov':'Oleksandr Zubkov',
    'Maksym Talovierov':'Maksym Talovierov',
    'Serhii Sydorchuk':'Serhii Sydorchuk',
    'Leo Sauer':'Leo Sauer',
    'Anzor Mekvabishvili':'Anzor Mekvabishvili',
    'Václav Černý':'Václav Černý',
    'Solomon Kverkvelia':'Solomon Kverkvelia',
    'Petr Ševčík':'Petr Ševčík',
    'Saba Lobzhanidze':'Saba Lobzhanidze',
    'Giorgi Kvilitaia':'Giorgi Kvilitaia',
    'Yusuf Yazıcı':'Yusuf Yazıcı',
    'Paweł Dawidowicz':'Paweł Dawidowicz',
    'Krzysztof Piątek':'Krzysztof Piątek',
    'Robert Lewandowski':'Robert Lewandowski',
    'Kamil Grosicki':'Kamil Grosicki',
    'João Neves':'João Neves',
    'Gonçalo Bernardo Inácio':'Gonçalo Inácio',
    'Pedro Lomba Neto':'Pedro Neto',
    'Danilo Luís Hélio Pereira':'Danilo Pereira',
    'António João Pereira Albuquerque Tavares Silva':'António João Silva',
    'José Diogo Dalot Teixeira':'José Dalot',
    'Gonçalo Matias Ramos':'Gonçalo Ramos',
    'Łukasz Skorupski':'Łukasz Skorupski',
    'Michał Skóraś':'Michał Skóraś',
    'Andriy Lunin':'Andriy Lunin',
    'Viktor Tsygankov':'Viktor Tsygankov',
    'Yukhym Konoplya':'Yukhym Konoplya',
    'Florinel Teodor Coman':'Florinel Coman',
    'Nicușor Silviu Bancu':'Nicușor Bancu',
    'Adrián Rus':'Adrián Rus',
    'George Alexandru Puşcaş':'George Puşcaş',
    'Deian Cristian Sorescu':'Deian Sorescu',
    'Erik Janža':'Erik Janža',
    'Anthony Gordon':'Anthony Gordon',
    'Josip Stanišić':'Josip Stanišić',
    'Marin Pongracic':'Marin Pongracic',
    'Luka Ivanušec':'Luka Ivanušec',
    'Maximilian Beier':'Maximilian Beier',
    'Altay Bayındır':'Altay Bayındır',
    'Yunus Akgün':'Yunus Akgün',
    'Mijat Gaćinović':'Mijat Gaćinović',
    'Žan Vipotnik':'Žan Vipotnik',
    'Veljko Birmančević':'Veljko Birmančević',
    'David Brekalo':'David Brekalo',
    'Kieran Tierney':'Kieran Tierney',
    'Pavel Šulc':'Pavel Šulc',
    'David Doudera':'David Doudera',
    'Filip Kostić':'Filip Kostić',
    'Ádám Lang':'Ádám Lang',
    'Ryan Porteous':'Ryan Porteous',
    'Pascal Groß':'Pascal Groß'}

    df['player'] = df['player'].replace(name_replacements)
    df['pass_recipient'] = df['pass_recipient'].replace(name_replacements)
    return df


# In[ ]:




