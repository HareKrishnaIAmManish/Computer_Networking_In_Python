import os
from collections import Counter
counts=Counter()
print(type(counts))
for currentdir, dirnames, filenames in os.walk("."):
    print("hello")
    print(currentdir)
    print("bye")
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
for extension, count in counts.items():
    print(f"{extension:8}{count}")  #:means padding left align right align means>
