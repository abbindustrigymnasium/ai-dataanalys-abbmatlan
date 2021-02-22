# DATAANALYS

### Jag, Carl  och Linus:
Vi har börjat på ett projekt där vi ska analysera rörelsen av en muspekare, tanken är att vi sedan ska kunna använda oss av datat för att hitta samband mellan rörelser som användaren gjort. Vårat nästa steg var att skirva logaritmer som kunde avgöra om användaren exempel gjort rörelsen; cirkel, horisontellt-streck, diagonalt-streck, halvcirkel eller vertikalt-streck. Vi hann aldrig dit, men det var tanken.

## FILER
Just nu har vi flera filer med kod som måste köras när man använder programmet. Först kör man mouse-tracker.py för att skriva in data i en val csv-fil.
Csv-filen (exempel cikel.csv eller streck.csv) kan sedan visas visuellt med graph.py och graph2.py. Skillnaden mellan dem är att en genererar en graf som består av acceleration/tid medans den andra endast visar en graf med muspekarens x/y-värden. 
