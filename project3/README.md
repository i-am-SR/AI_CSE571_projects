# AI_CSE571_projects
CSE 571 Artificial Intelligence Projects

**Result of running the project**


<pre>
srnew@srnew-VirtualBox:~/Desktop/CSE579AI/PJ3-logic/wumpus$ python wumpus.py -k
HybridWumpusAgent.register_environment()
HybridWumpusAgent.reset()
HWA.create_wumpus_KB(): adding initial wumpus axioms
    total number of axioms=38
    total number of clauses=425
          >>> time elapsed: 0.07105
Scores: <HybridWumpusAgent>=0
  0   1   2   3   4   5    time_step=0
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | G | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # | ^ |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 0
   HWA.make_percept_sentence(): ~Stench0 & ~Breeze0 & ~Glitter0 & ~Bump0 & ~Scream0
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench0 & ~Breeze0 & ~Glitter0 & ~Bump0 & ~Scream0
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (1, 1)
          >>> time elapsed while making current location queries: 0.501918
     HWA.infer_and_set_belief_heading()
        Current inferred heading: north
          >>> time elapsed while making belief heading queries:0.032153
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 430
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 770
         Total clauses added to KB: 340
[0] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): ?

Available Commands:
   The following are valid Hunt The Wumpus actions:
     'TurnRight', 'TurnLeft', 'Forward', 'Grab', 'Climb', 'Shoot', 'Wait'
   Enter '?' or 'help' to get this command info
   Enter 'quit' or 'stop' or 'exit' to stop playing
   Enter 'env' to display current wumpus environment
   Enter 'kbsat' to check if the agent's KB is satisfiable
      If the KB is NOT satisfiable, then there's a contradiction that needs fixing.
      NOTE: A satisfiable KB does not mean there aren't other problems.
   Enter 'save-axioms' to save all of the KB axioms to 'kb-axioms.txt'
      This will overwrite any existing 'kb-axioms.txt'
   Enter 'save-clauses' to save all of the KB clauses to text file 'kb-clauses.txt'
      This will overwrite any existing 'kb-clauses.txt'
   Enter 'props' to list all of the proposition bases
   Queries:
      qp : Query a single proposition;
           E.g. 'qp B1_1' or 'qp OK1_1_3', 'qp HeadingWest4'
      qpl : Query a-temporal location-based proposition at all x,y locations;
           E.g., 'qpl P' runs all queries of P<x>_<y>
      qplt : Query temporal and location-based propositions at all x,y locations;
           E.g., 'qplt OK 4' runs all queries of the OK<x>_<y>_4
      q! : Run ALL queries for optionally specified time (default is current time);
           (can be time consuming!)

[0] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-1
  0   1   2   3   4   5    time_step=1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | G | P |   | # | 3
|---|---|---|---|---|---|
| # | ^ |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 1
   HWA.make_percept_sentence(): Stench1 & ~Breeze1 & ~Glitter1 & ~Bump1 & ~Scream1
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench1 & ~Breeze1 & ~Glitter1 & ~Bump1 & ~Scream1
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (1, 2)
          >>> time elapsed while making current location queries: 1.022123
     HWA.infer_and_set_belief_heading()
        Current inferred heading: north
          >>> time elapsed while making belief heading queries:0.07155
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 776
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 1153
         Total clauses added to KB: 377
[1] You perceive: ['Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): TurnRight
<HybridWumpusAgent> perceives ['Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does TurnRight

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-2
  0   1   2   3   4   5    time_step=2
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | G | P |   | # | 3
|---|---|---|---|---|---|
| # | > |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 2
   HWA.make_percept_sentence(): Stench2 & ~Breeze2 & ~Glitter2 & ~Bump2 & ~Scream2
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench2 & ~Breeze2 & ~Glitter2 & ~Bump2 & ~Scream2
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (1, 2)
          >>> time elapsed while making current location queries: 1.579263
     HWA.infer_and_set_belief_heading()
        Current inferred heading: east
          >>> time elapsed while making belief heading queries:0.393723
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 1159
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 1645
         Total clauses added to KB: 486
[2] You perceive: ['Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-3
  0   1   2   3   4   5    time_step=3
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | G | P |   | # | 3
|---|---|---|---|---|---|
| # |   | > |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 3
   HWA.make_percept_sentence(): ~Stench3 & ~Breeze3 & ~Glitter3 & ~Bump3 & ~Scream3
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench3 & ~Breeze3 & ~Glitter3 & ~Bump3 & ~Scream3
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 2)
          >>> time elapsed while making current location queries: 2.373358
     HWA.infer_and_set_belief_heading()
        Current inferred heading: east
          >>> time elapsed while making belief heading queries:0.600201
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 1651
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 2246
         Total clauses added to KB: 595
[3] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): TurnLeft
<HybridWumpusAgent> perceives ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does TurnLeft

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-4
  0   1   2   3   4   5    time_step=4
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | G | P |   | # | 3
|---|---|---|---|---|---|
| # |   | ^ |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 4
   HWA.make_percept_sentence(): ~Stench4 & ~Breeze4 & ~Glitter4 & ~Bump4 & ~Scream4
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench4 & ~Breeze4 & ~Glitter4 & ~Bump4 & ~Scream4
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 2)
          >>> time elapsed while making current location queries: 3.470819
     HWA.infer_and_set_belief_heading()
        Current inferred heading: north
          >>> time elapsed while making belief heading queries:0.221471
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 2252
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 2847
         Total clauses added to KB: 595
[4] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-5
  0    1    2    3    4    5     time_step=5
|----|----|----|----|----|----|
| #  | #  | #  | #  | #  | #  | 5
|----|----|----|----|----|----|
| #  |    |    |    |    | #  | 4
|----|----|----|----|----|----|
| #  | W  | ^G | P  |    | #  | 3
|----|----|----|----|----|----|
| #  |    |    |    |    | #  | 2
|----|----|----|----|----|----|
| #  |    |    | P  |    | #  | 1
|----|----|----|----|----|----|
| #  | #  | #  | #  | #  | #  | 0
|----|----|----|----|----|----|

------------------------------------------------------------------
At time 5
   HWA.make_percept_sentence(): Stench5 & Breeze5 & Glitter5 & ~Bump5 & ~Scream5
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench5 & Breeze5 & Glitter5 & ~Bump5 & ~Scream5
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 3)
          >>> time elapsed while making current location queries: 4.515866
     HWA.infer_and_set_belief_heading()
        Current inferred heading: north
          >>> time elapsed while making belief heading queries:0.298688
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 2853
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 3339
         Total clauses added to KB: 486
[5] You perceive: ['Stench', 'Breeze', 'Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Grab
<HybridWumpusAgent> perceives ['Stench', 'Breeze', 'Glitter', '~Bump', '~Scream'] and does Grab

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-6
  0   1   2   3   4   5    time_step=6
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | ^ | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 6
   HWA.make_percept_sentence(): Stench6 & Breeze6 & ~Glitter6 & ~Bump6 & ~Scream6
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench6 & Breeze6 & ~Glitter6 & ~Bump6 & ~Scream6
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 3)
          >>> time elapsed while making current location queries: 5.320266
     HWA.infer_and_set_belief_heading()
        Current inferred heading: north
          >>> time elapsed while making belief heading queries:0.334465
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 3345
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 3831
         Total clauses added to KB: 486
[6] You perceive: ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): TurnLeft
<HybridWumpusAgent> perceives ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream'] and does TurnLeft

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-7
  0   1   2   3   4   5    time_step=7
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | < | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 7
   HWA.make_percept_sentence(): Stench7 & Breeze7 & ~Glitter7 & ~Bump7 & ~Scream7
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench7 & Breeze7 & ~Glitter7 & ~Bump7 & ~Scream7
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 3)
          >>> time elapsed while making current location queries: 6.111667
     HWA.infer_and_set_belief_heading()
        Current inferred heading: west
          >>> time elapsed while making belief heading queries:0.769238
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 3837
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 4323
         Total clauses added to KB: 486
[7] You perceive: ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): TurnLeft
<HybridWumpusAgent> perceives ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream'] and does TurnLeft

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-8
  0   1   2   3   4   5    time_step=8
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W | v | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 8
   HWA.make_percept_sentence(): Stench8 & Breeze8 & ~Glitter8 & ~Bump8 & ~Scream8
     HWA.agent_program(): kb.tell(percept_sentence):
         Stench8 & Breeze8 & ~Glitter8 & ~Bump8 & ~Scream8
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 3)
          >>> time elapsed while making current location queries: 6.940798
     HWA.infer_and_set_belief_heading()
        Current inferred heading: south
          >>> time elapsed while making belief heading queries:1.357949
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 4329
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 4924
         Total clauses added to KB: 595
[8] You perceive: ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['Stench', 'Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-9
  0   1   2   3   4   5    time_step=9
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W |   | P |   | # | 3
|---|---|---|---|---|---|
| # |   | v |   |   | # | 2
|---|---|---|---|---|---|
| # |   |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 9
   HWA.make_percept_sentence(): ~Stench9 & ~Breeze9 & ~Glitter9 & ~Bump9 & ~Scream9
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench9 & ~Breeze9 & ~Glitter9 & ~Bump9 & ~Scream9
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 2)
          >>> time elapsed while making current location queries: 8.16696
     HWA.infer_and_set_belief_heading()
        Current inferred heading: south
          >>> time elapsed while making belief heading queries:1.513859
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 4930
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 5416
         Total clauses added to KB: 486
[9] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-10
  0   1   2   3   4   5    time_step=10
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W |   | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   | v | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 10
   HWA.make_percept_sentence(): ~Stench10 & Breeze10 & ~Glitter10 & ~Bump10 & ~Scream10
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench10 & Breeze10 & ~Glitter10 & ~Bump10 & ~Scream10
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 1)
          >>> time elapsed while making current location queries: 8.829716
     HWA.infer_and_set_belief_heading()
        Current inferred heading: south
          >>> time elapsed while making belief heading queries:1.654616
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 5422
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     1
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  60
         Number of clauses in KB after: 5740
         Total clauses added to KB: 318
[10] You perceive: ['~Stench', 'Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): TurnRight
<HybridWumpusAgent> perceives ['~Stench', 'Breeze', '~Glitter', '~Bump', '~Scream'] and does TurnRight

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-11
  0   1   2   3   4   5    time_step=11
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W |   | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # |   | < | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 11
   HWA.make_percept_sentence(): ~Stench11 & Breeze11 & ~Glitter11 & ~Bump11 & ~Scream11
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench11 & Breeze11 & ~Glitter11 & ~Bump11 & ~Scream11
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (2, 1)
          >>> time elapsed while making current location queries: 9.254907
     HWA.infer_and_set_belief_heading()
        Current inferred heading: west
          >>> time elapsed while making belief heading queries:1.165653
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 5746
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     2
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  61
         Number of clauses in KB after: 6086
         Total clauses added to KB: 340
[11] You perceive: ['~Stench', 'Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Forward
<HybridWumpusAgent> perceives ['~Stench', 'Breeze', '~Glitter', '~Bump', '~Scream'] and does Forward

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=-12
  0   1   2   3   4   5    time_step=12
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W |   | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # | < |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

------------------------------------------------------------------
At time 12
   HWA.make_percept_sentence(): ~Stench12 & ~Breeze12 & ~Glitter12 & ~Bump12 & ~Scream12
     HWA.agent_program(): kb.tell(percept_sentence):
         ~Stench12 & ~Breeze12 & ~Glitter12 & ~Bump12 & ~Scream12
     HWA.infer_and_set_belief_location()
        Current believed location (inferred): (1, 1)
          >>> time elapsed while making current location queries: 9.852415
     HWA.infer_and_set_belief_heading()
        Current inferred heading: west
          >>> time elapsed while making belief heading queries:1.235905
     HWA.agent_program(): Prepare to add temporal axioms
         Number of clauses in KB before: 6092
       HWA.add_temporal_axioms()
           number of location_OK axioms:         16
           number of percept_to_loc axioms:      32
           number of at_location ssa axioms:     1
           number of non-location ssa axioms:    6
           number of mutually_exclusive axioms:  5
       Total number of axioms being added:  60
         Number of clauses in KB after: 6373
         Total clauses added to KB: 281
[12] You perceive: ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream']
Enter Action ('?' for list of commands): Climb
<HybridWumpusAgent> perceives ['~Stench', '~Breeze', '~Glitter', '~Bump', '~Scream'] and does Climb

Current Wumpus Environment:
Scores: <HybridWumpusAgent>=987
  0   1   2   3   4   5    time_step=13
|---|---|---|---|---|---|
| # | # | # | # | # | # | 5
|---|---|---|---|---|---|
| # |   |   |   |   | # | 4
|---|---|---|---|---|---|
| # | W |   | P |   | # | 3
|---|---|---|---|---|---|
| # |   |   |   |   | # | 2
|---|---|---|---|---|---|
| # | < |   | P |   | # | 1
|---|---|---|---|---|---|
| # | # | # | # | # | # | 0
|---|---|---|---|---|---|

DONE.
number_of_clauses_over_epochs: [770, 1153, 1645, 2246, 2847, 3339, 3831, 4323, 4924, 5416, 5740, 6086, 6373]
belief_loc_query_times: [0.5019180000000001, 1.0221230000000001, 1.579263, 2.3733580000000005, 3.4708190000000005, 4.515865999999999, 5.320265999999998, 6.111667000000001, 6.940798000000001, 8.166959999999996, 8.829716000000005, 9.25490700000001, 9.852415000000008]
Final Scores: <HybridWumpusAgent>=987
</pre>
