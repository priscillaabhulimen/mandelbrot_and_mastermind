with open("colours.csv", "r") as f:
    colours = {colour.strip() for colour in f.read().split(",")}

ntocol_dict = {i + 1:val for i,val in enumerate(sorted(colours))}
colton_dict = {val:i + 1 for i,val in enumerate(sorted(colours))}