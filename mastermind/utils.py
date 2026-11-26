from pathlib import Path

with (Path(__file__).parent / "colours.csv").open("r") as f:
    colours = {colour.strip() for colour in f.read().split(",")}

ntocol_dict = {i + 1:val.lower() for i,val in enumerate(sorted(colours))}
colton_dict = {val.lower():i + 1 for i,val in enumerate(sorted(colours))}