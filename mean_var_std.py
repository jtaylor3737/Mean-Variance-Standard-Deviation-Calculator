import numpy as np

def calculate(list):
    x = np.asarray(list)
    try:
        x = x.reshape(3,3) 
    except:
        raise ValueError ('List must contain nine numbers.',list)
    calculations = {'mean': [np.mean(x, axis = 0).tolist(), np.mean(x, axis = 1).tolist(), np.mean(x)],
                    'variance': [np.var(x, axis = 0).tolist(), np.var(x, axis = 1).tolist(), np.var(x)],
                    'standard deviation': [np.std(x,axis = 0).tolist(), np.std(x, axis = 1).tolist(), np.std(x)],
                    'max': [np.max(x,axis = 0).tolist(), np.max(x,axis = 1).tolist(), np.max(x)],
                    'min': [np.min(x,axis = 0).tolist(), np.min(x,axis = 1).tolist(), np.min(x)],
                    'sum': [np.sum(x,axis=0).tolist(), np.sum(x,axis=1).tolist(), np.sum(x)]}
    return calculations