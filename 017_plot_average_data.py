import re
import numpy as np
import matplotlib.pyplot as plt

path = "test.csv"

check_code = re.compile("[0-9]{4}/[0-9]{2}/[0-9]{2}")

data_a = np.arange(0)
data_b = np.arange(0)
data_c = np.arange(0)
counter = 0

with open(path) as f:
    for temp_line in f:
        if re.match(check_code, temp_line) is not None:
            print(temp_line.split(",")[2])
            data_a = np.append(data_a, temp_line.split(",")[2])
            data_b = np.append(data_b, temp_line.split(",")[3])

            counter = counter + 1
            data_c = np.append(data_c, counter)

plt.plot(data_c, data_a)
plt.show()
