import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  else:
    list2 = [list[:3], list[3:6], list[6:]]
    arr = np.array(list2)

    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
    var = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
    stdev = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
    max = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]
    min = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]
    sum = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
  
    calculations = {"mean": mean, "variance": var, "standard deviation": stdev, "max": max, "min": min, "sum": sum}
  
    return calculations