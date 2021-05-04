# Snake med AI


## AI-Backgrund:

### Reinforcment Learning
Förstärkningslärning eller RL är ett område inom maskininlärning som behandlar hur en mjukvaruagent bör agera för att maximera någon typ av sammanräknad belöning.

#### Q-Learning
Q-Learning är en RL-algorithm som lär sig värdet (value) av datorns agerande (action) i ett visst tillstånd (state). Datorn behöver därför inte en färdigframställd miljö och blir då "model-free". Genom att träna modellen med belöning (reward) då den gör något bra och straff då den gör något dåligt, samt att den lägger agerandet på minne, kommer modellen automatiskt träna sig. 

##### Deep Q-Learning
Det här tillvägagångssättet utvidgar RL genom att använda ett "deep neural network" för att förutspå hur den ska agera. 

I mitt fall använder jag mig av ett "feedforward nural network" 

##### Q-Tables

##### Learning Rate

##### Discount Factor


## FILER

### Agent
Sätter ihop game och model samt tränar AI:n genom att köra algoritmen

### Game
Ett standard snake-spel, det är endast lite modifierat för att kunna ta emot vad agent:s val, istället för en användare.

### Model
Motsvarar "deep Q-Learning" och är den delen som förutspår nästa steg med ett feedforward nural network.
Med 11 perceptroner i input-lagret, ett värde från varje boolen i state och 3 output-lager som ger en lista där i form av [0,0,0], vilket ger riktningen ormen ska röra sig i. 
(Mer information under VIKTIGA VARIABLER, ACTION)

### Helper
Skriver ut AI:ns framsteg i en graf.


## Viktiga variabler

### Reward (det den kan få)
- äta mat:      +10
- game over:    -10
- annars:         0
  

### Action (det den kan göra)
- rakt          ->      [1,0,0]
- höger sväng   ->      [0,1,0]
- vänster sväng ->      [0,0,1]
- Vi tillåter den inte att svänga bakåt då den dör automatiskt, för att röra sig bakåt måste den kombinera de olika valen.
  
### State (informationen om miljön, Sant eller Falskt)

- Vilket håll faran (väggen/ dens egna kropp är åt).
- Det nuvarande riktningen den rör sig åt.
- Hållet maten är åt.

## EX (11 värden):
[danger straight, danger right, danger left,

direction left, direction right,
direction up, direction down,

food left, food right,
food up, food down
]







