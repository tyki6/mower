# Mower
Simulate Mow.
# Installation
## Requirements
- python >=3.6
- Or docker
- [file with all valid information](#file-structure)
# Usage
## Python
`python main.py [YOUR_FILE]`
## Docker
`docker build -t dev .`
`docker run -v $(pwd):/home/app dev [YOUR_FILE]`
# File Structure
## First line
The first line corresponds to the upper right corner of the lawn. The bottom left corner is implicitly (0, 0).
Attented: number number(Ex: 5 5)
## Second line
The Second line corresponds to list of mower's movement.L: left orientation, R: right orientation, F: forward
Attended: [LRF]*(Ex: LLLLRLRLRFFFFFF)


# Result
At the end of the simulation, the final position and orientation of each mower is output in the order that the mower appeared in the input.
## Example
Result:
```text
1 3 N
5 1 E
```
