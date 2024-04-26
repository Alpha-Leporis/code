'''
A new Chemistry teacher is very strict and wants the students to do well in class. To aid this, lectures on each chapter Will be repeated periodically through the semester. In each class, the next chapter is presented. When they reach the end of the book, the lectures
start over with chapter 0. More formally, if there are numChapters in the book. then on the ith day. the lecture will be on chapter i%numChapters. The first day of class is class[0], and the first chapter is chapter O. If there are 3 chapters, daily lectures are on chapters
Class = [0,1,2,0,1,2,...]. At class[4], the lecture will be on chapter 4 % 3 = 1.

One of the students is going to be out of class for a wedding. and the teacher is concerned about missed lectures. Given the first and last days the student will be out. determine the number of chapters for which the student Will miss lectures.

For example, there are numChapters = 4 chapters in the book. The student iS out of class beginning on day b^k||t through ending day e = 5. The series Of lectures are on chapters class = [0,1,2,3,0,1,2,3,...]. starting from day 0. For class[3] through class[5], lectures are given on chapters 3, 0 and 1. The student Will miss lectures on 3 chapters.

Function Description
Complete the function missedLectures in the editor below. The function must return an integer.

missedLectures has the following parameters:
int numChapters: an integer
int b : an integer
int e : an integer
'''

# soltution:

'''
we need to calculate the number of unique chapters covered during the student's absence from class. 
We can do this by determining the number of lectures given during the student's absence and counting 
the unique chapters presented in those lectures.

This function missedLectures calculates the number of chapters the student will miss lectures on during 
their absence from class. It takes three parameters: firstDay (the first day the student will be absent), 
lastDay (the last day the student will be absent), and numChapters (the total number of chapters in the book). 
It returns the number of missed chapters.

Time complexity: O(1)
Space complexity: O(1)
'''

def missedLectures(firstDay, lastDay, numChapters):
    totalDays = lastDay - firstDay + 1
    missedChapters = totalDays % numChapters
    return missedChapters

# Example usage:
numChapters = 4 # Number of chapters
firstDay = 3 # start of range
lastDay = 5 # end of range
print(missedLectures(firstDay, lastDay, numChapters))  # Output: 3


# second solution:

def missed_lecture(numChapters, b, e):
    classes = []
    no_of_lectures = numChapters * (e + 1)
    for i in range(no_of_lectures):
        classes.append(i % numChapters)
    distinct_chapters = set(classes[b:e+1])
    return len(distinct_chapters)

numChapters = 4
b=3
e=5
print(missed_lecture(numChapters, b, e))