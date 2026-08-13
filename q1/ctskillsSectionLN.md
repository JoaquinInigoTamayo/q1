Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"


Section: 9-Pinatubo                             Score:____________
C# / Name: #15 / Joaquin Iñigo L. Tamayo        Date: 8/13/2026

Scenario
The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:
Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem:
  Our identified main problem is the school canteen’s efficiency.
  
Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:
  1. Some students take too long to decide what to order.
  2. The cashier has to manually calculate totals and give change.
  3. There is no system to track which food items are running out.
  4. Hundreds of students usually buy from one station.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:
1. Some students take too long to decide what to order.
  - CT Skill - Abstraction
  - Make the menu visible to students even while waiting in line by posting the foods available on the wall.
2. The cashier has to manually calculate totals and give change.
  - CT Skill - Algorithmic thinking
  - Set up an application where all the food’s prices are listed and have it automatically calculate the change based on the payment the customer made.
3. There is no system to track which food items are running out.
  - CT Skill - Algorithmic thinking
  - Have the application monitor how many servings can be distributed.
4. Hundreds of students usually buy from one station.
  - CT Skill - Pattern recognition
  - Have another station set up with more food variations available.

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem
- 3rd sub-problem:
1. Start
2. Enter the amount of servings of food distributed
3. Enter the amount of servings of food at the start of lunch
4. Subtract the amount of servings distributed from the amount of servings before
5. If the amount of servings left is lower than 10, decrease portion sizes or restock that food item
6. If the amount of servings left is higher than 10, there is no need to lower portion sizes or restock that food item
7. Repeat this process every 5 to 10 minutes
8. End

