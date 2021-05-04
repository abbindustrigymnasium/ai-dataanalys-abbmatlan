# Snake med AI


## AI-Backgrund:

### Reinforcment Learning
Förstärkningslärning eller RL är ett område inom maskininlärning som behandlar hur en mjukvaruagent bör agera för att maximera någon typ av sammanräknad belöning.

#### Q-Learning
Q-Learning är en RL-algorithm som lär sig värdet (value) av datorns agerande (action) i ett visst tillstånd (state). Datorn behöver därför inte en färdigframställd miljö och blir då "model-free". Genom att träna modellen med belöning (reward) då den gör något bra och straff då den gör något dåligt, samt att den lägger agerandet på minne, kommer modellen automatiskt träna sig. 

##### Deep Q-Learning
Det här tillvägagångssättet utvidgar RL genom att använda ett "deep neural network" för att förutspå hur den ska agera.

##### Q-Tables

##### Learning Rate

##### Discount Factor


## FIlER

### Agent
Sätter ihop game och model samt tränar AI:n genom att köra algoritmen

### Game
Ett standard snake-spel, det är endast lite modifierat för att kunna ta emot vad agent:s val, istället för en användare.

### Model
Motsvarar "deep Q-Learning" och är den delen som förutspår nästa steg.

### Helper
Skriver ut AI:ns framsteg i en graf.






