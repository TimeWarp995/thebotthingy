from datetime import timedelta

sleptLate = False
wokeLate = False
turnsUp = True
absent = False

studentAmount = int(input("Input the amount of students in the class: "))
students = []
x = 1

while studentAmount >= x:
  theStudent = input(f"Write the name of student {x}: ")
  students.append(theStudent)
  x = x + 1

print("")
print("Aight, making sure. The students are: ")

x = 1

while len(students) >= x:
  print(students[x-1])
  x = x + 1

print("")

x = 1

print("Now, tell me when the students slept. Use the 24-hour clock and write in this format [23:40] where 23 is hours and 40 is minutes.")

studentSleepTimes = {}

while studentAmount >= x:
  sleepTime = input(f"When did {students[x-1]} sleep? ")
  studentSleepTimes[students[x-1]] = sleepTime
  x = x + 1

print("")
print("Now, tell me when the students woke up. Same format as before, remember!")

x = 1

while studentAmount >= x:
  wakeTime = input(f"When did {students[x-1]} wake up? ")
  studentSleepTimes[students[x-1] + "1"] = wakeTime
  x = x + 1

x = 1

while studentAmount >= x:
  timesV1 = studentSleepTimes[students[x-1]].split(":")
  hourV1 = int(timesV1[0])
  minV1 = int(timesV1[1])
  print(timesV1, students[x-1])

  timesV2 = studentSleepTimes[students[x-1] + "1"].split(":")
  hourV2 = int(timesV2[0])
  minV2 = int(timesV2[1])
  print(timesV2, students[x-1] + "1")
  
  val1 = timedelta(2022, 1, 1, hourV1, minV1, 0)
  val2 = timedelta(2022, 1, 3, hourV2, minV2, 0)
  
  finalSleepTotal = val2 - val1

  print(f"{students[x-1]} slept for {finalSleepTotal}.")

  x = x + 1

print(studentSleepTimes)
