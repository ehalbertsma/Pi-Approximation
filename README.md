# Pi-Approximation
_Uses nothing but a uniform random number generator to approximate pi_

## Theory:
Consider a circular dartboard of radius 1 centred at the origin on a cardboard square of area 4. If we throw darts at the board, then there should be a roughly equal density <img src="https://render.githubusercontent.com/render/math?math=\rho"> of darts on the dartboard, and of darts on the cardboard around the outside of the dartboard. Note that we are assuming a uniform distribution and considering only darts that are at least inside the square.

So the number of darts in the circle is approximately:
<img src="https://render.githubusercontent.com/render/math?math=n_{circle} = \rho A_{circle} = \rho \times 1\pi">

And the number of darts outside the circle (and thus in the square) is approximately:
<img src="https://render.githubusercontent.com/render/math?math=n_{circle} = \rho A_{square} = \rho \times 4">

If we divide the darts inside and outside the square:
<img src="https://render.githubusercontent.com/render/math?math=\frac{n_{circle}}{n_square}} = \pi/4">

## Execution:
In my program, we only consider numbers in the first quadrant to simplify calculations. Thus, we generate two floating point numbers in the interval <img src="https://render.githubusercontent.com/render/math?math=[0,1)">. Since the ratio of areas remains the same, the formula does not change.
We consider the first number an x-coordinate and the second number a y-coordinate. This lets us check whether the point is on the circle by evaluating: 
<img src="https://render.githubusercontent.com/render/math?math=x^2+y^2<1">
If it is in the circle, we count it, and otherwise it is in the square. After the desired number of iterations, the formula above calculates pi.

## Performance
Upon running the program 10 times with 1,000,000 "darts", the value of pi was accurate to decimals.
