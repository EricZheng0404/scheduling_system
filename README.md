# scheduling_system

## Context
In my company, we have teaching assistants (TA) to monitor students on students' vocabulary memorization by audio call. But most of TAs are part-time, so they have different working time on different days of a week. Also for students, their available time is different on different days. It would be laborious to match TAs and students manually. To make people's life eaiser, I started this sheduling system.

## Models
There are two models in the models.py: 1. Students, which contains name (student's name), time (the time of a day at which they can have a vocabulary test), day (day of week); 2. Teachers, which contains name (TA's name), start_time (the time they start work), end_time (the time they end their work), day (day of week). 

For day in both Students and Teachers, some choices are give: 
```
DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)
```

For example, some instances of Teachers would be:  
A, 10:00, 10:30, 4 (for TA A, he starts work at 10:00 and ends work at 10:30 on Friday)  
B, 10:00, 10:45, 4  
 
some instances of Students would be like:  
C, 10:00, 4 (for student C, he is available at 10:00 on Friday)  
D, 10:00, 4  
E, 19:00, 4  
F, 10:45, 4  

## Logic
In the result page, first the system time will be requested in the backend, so only students and TAs who are available on the day of the week would be accessed. For TA' start_time to end_time, it's a period. This period is then divided into many 15-minute slots. The goal of this system is to match students into these slots. It does not matter which student matched into which TA's time slot as long as it is a match. All the students who do not have a TA will also be shown on the page. 

For example, TA A has a start_time of 10:00 and an end_time of 10:30 on Friday, so he has 3 slots: 10:00, 10:15, 10:30; TA B has a start_time of 10:00 and an end_time of 10:45 on Friday, so he has 4 slots: 10:00, 10:15, 10:30, 10:45. Student C is available at 10:00 on 4 (Friday), so on Friday, he is matched into the 10:00 slot of TA A. Student D is available on 10:00, but TA A's 10:00 slot is not available already, so he is matched into the TA B's 10:00 slot. For student F, he is available on 10:45, only TA B has that slot, so student F is matched into the 10:45 slot of TA B. At last, student E is available only at 19:00, but none of the TA has that opening, so he is not covered.

## End Result
The output will be:
<img width="129" alt="image" src="https://user-images.githubusercontent.com/32259752/207383039-49d4c0a7-a09e-4ce5-9525-d7205413d402.png">
