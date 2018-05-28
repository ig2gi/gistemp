
blues = ["8,69,148","33,113,181","66,146,198","107,174,214","158,202,225", "198,219,239","222,235,247", "247,251,255"]
blue_vals = [-1.5,-1.25,-1.0,-0.75,-0.5,-0.25,-0.1,-0.0]

reds = ["255,245,235","254,230,206", "253,208,162", "253,174,107", "253,141,60", "241,105,19", "217,72,1", "140,45,4"]
red_vals = [0.1,0.25,0.5,0.75,1.0,1.25,1.5,20]

def evaluate(d):
    # cold values
    for i,v in enumerate(blue_vals):
        if d <= v:
            return blues[i]
    # hot values
    for i,v in enumerate(red_vals):
        if d <= v:
            return reds[i]
    # d > 1.5
    return reds[7]

def scale(name):
    s = blues if name == "blue" else reds
    sv = blue_vals if name == "blue" else red_vals
    return [(str(sv[i]) + ":"+ v) for i,v in enumerate(s)]

print scale("red")

