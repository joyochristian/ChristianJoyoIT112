print("Cheater Detector 3000 🔍")
print("--------------------------")

score = 0

q1 = input("Does he look at random girls? (yes/no): ").lower()
if q1 == "yes":
    score += 1

q2 = input("Does he get defensive when you ask simple questions? (yes/no): ").lower()
if q2 == "yes":
    score += 1

q3 = input("Is he suddenly too busy for you but active online? (yes/no): ").lower()
if q3 == "yes":
    score += 1

q4 = input("Has he lied before? (yes/no): ").lower()
if q4 == "yes":
    score += 1

print("\nResult:")
if score == 0:
    print("He seems loyal 😊 (based on your answers)")
elif score <= 2:
    print("Hmm... Some small red flags 🚩")
else:
    print("Warning! Major red flags 🚩🚩🚩")

print("\nRemember: Communication is better than suspicion.")
