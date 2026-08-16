Annex A Computational Thinking Exercise: "Smart School Canteen Queue"

| Section: 9-Pinatubo | Score:____________ | C# / Name: #15 / Joaquin Iñigo L. Tamayo | Date: 8/13/2026 |
Groupmates: #13 Knoah Kenji D. Padilla, #14 Rafael Akiles Micael D. Rodriguez |

The problem: Finding the highest (Maximum) number from a given list of numbers.

- Pseudocode 1:
Algorithm FindMax1(numbers)

   max ← numbers[0]
   
   For i from 1 to length(numbers)-1
   
   If numbers[i] > max Then
      
   max ← numbers[i]
         
   End If
      
   EndFor
   
   Return max
   
   EndAlgorithm

- Pseudocode 2:
Algorithm FindMax2(numbers)

   For i from 0 to length(numbers)-1bigger ← true
   
   For j from 0 to length(numbers)-1
      
   If numbers[j] > numbers[i] Then
         
   bigger ← false
            
   EndIf
         
   EndFor
      
   If bigger = true Then
      
   Return numbers[i]
         
   EndIf
      
   EndFor

   EndAlgorithm

1. Efficiency:
Which algorithm is faster when the list of numbers is very large? Why?
- Pseudocode 1 is faster if the list of numbers is large because it  has only one nested loop causing the program to end with fewer actions. It also does not repeat work unnecessarily unlike Pseudocode 2 which compares each number to each other even if that number was already shown to be less than another number in previous comparisons, leading to potentially redundant and repeated steps.

2. Readability:
Which algorithm is easier to understand at first glance? What makes it clearer?
- Pseudocode 1 is easier to understand because 'max' as a variable name is more accurate than 'bigger' as we are looking for the number with the highest value, and since it has one nested loop instead of 2 it is simpler to read and has fewer lines of code.

3. Maintainability:
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?
-  I would have an easier time modifying pseudocode one. This is due to the fact that the second pseudocode has two loops, which makes it more tedious to construct new code for the min.

 4. Testability:
Which algorithm is easier to test with different inputs? Why?
-  Pseudocode 1, since it is faster and more efficient in calculating the largest number compared to pseudocode 2. This makes testing multiple numbers easier for the user.

5. Security:
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?
- Both Pseudocodes have to first, validate that the list is not empty/null to ensure that it is safe from index-out-of-bounds crashes, as well as checking if the list contains any non-numerical values to produce clear output. Pseudocode 2 also needs a limit on the size of the list to prevent program freezes due to its loops and large number of steps.  

6. Final Answer
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer
- Based on our answers from 1 to 5, the better algorithm is the first pseudocode. It is easier to understand, faster and more efficient to use, and overall better for clarification and upgrading. Pseudocode 2 is noticeably harder and less efficient than the first, since it goes through tons of unnecessary steps.







