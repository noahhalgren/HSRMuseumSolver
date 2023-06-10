
# HSR Museum Solver

This is some code to find the most optimal placement of each worker in the different museum rooms. I know this code is super innoficient and could be made x1000 faster, but it runs in under 5 seconds with 2 rooms and 12 workers, so for now it's good enough. When I get to the point where more rooms and workers are unlocked and this thing gets slower, maybe I'll return and make it faster.

This code will return the most optimal placement of each worker in your rooms based on stats and requirements. If a perfect S score for each room is not possible, it will give the combination where you gain the highest score possible per room, as well as an orientation that requires the least ammount of upgrades in each room to achieve an S.



## How to Use

Once files are downloaded, make sure to add your data about your museum to the workers.txt and rooms.txt files.

These are read by the .py file to make calculations based on your museum so keep them up to date as you upgrade rooms and unlock new workers.

### workers.txt
![Screenshot1](https://i.imgur.com/2Yo1MCg.png)
This file should contain a list of your workers. Each worker has 4 attributes:
 - Name (MUST BE A ONE WORD NAME. If someone has a multi-word name: give them a nickname)
 - Tour Duration Stat
 - Education Value Stat
 - Visitor Appeal Stat

Keep this file updated as you unlock more workers.

*Make sure there are no extra empty lines at the end of the file after adding new workers*

### rooms.txt
![Screenshot2](https://i.imgur.com/gp0yGNj.png)
This file should contain a list of your open rooms. Each room has 9 attributes:
 - Name (MUST BE A ONE WORD NAME. Give rooms a nickname as needed)
 - Tour Duration Needed
 - Education Value Needed
 - Visitor Appeal Needed
 - Base Tour Duration
 - Base Education Value
 - Base Visitor Appeal

*'Base' values are the ammount of points a room has when no workers are assigned. These are obtained from upgrading rooms*

Keep this file updated as you upgrade and gain rooms. Also update this file after unlocking new artifacts, as they may affect values needed in some way.

*Make sure there are no extra empty lines at the end of the file after adding new rooms*
## Run Locally

Clone the project

```bash
  git clone https://github.com/noahhalgren/HSRMuseumSolver
```

Go to the project directory

```bash
  cd HSRMuseumSolver
```

No dependencies, just run the .py file.
## Yes, I know it's slow

I wrote this in 30 min inbetween work meetings. It checks every possible permutation of workers, which I know is inefficient since order doesnt matter within rooms, it only matters whic h room they're in, but it was the first thought and it runs fast *enough* and most importantly: it works. 

As more rooms and people are unlocked I may revisit to use combination instead. Only issue is that order doesnt matter within each room, but which room they're in does, so I'll have to rewrite a large chunk of this to make that efficency change. For now though, better than doing it manually.