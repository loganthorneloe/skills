# Coverage questions — GPS (frozen before generation)
Score each 0/1/2 from the report alone. 2 = a novice reading only this report could answer correctly; 1 = partial, implicit, or needs inference the report does not support; 0 = missing or wrong.
Q1. What do GPS satellites broadcast? Key: signals carrying precise transmit time and the satellite's position (orbit data/ephemeris).
Q2. How does the receiver turn a signal into a distance? Key: distance = signal travel time × speed of light; travel time = receive time − transmit time.
Q3. How do several distances give a position? Key: each distance puts you on a sphere around a satellite; intersecting spheres from several satellites (trilateration) narrows to one point.
Q4. Why are at least four satellites needed? Key: the phone's cheap clock has an unknown offset, a fourth unknown besides x, y, z; four measurements solve all four (clock error is solved, not assumed).
Q5. Why must clocks be so precise? Key: light travels about 30 cm per nanosecond; a microsecond error is ~300 m; satellites carry atomic clocks.
Q6. Why does relativity matter? Key: satellite clocks tick faster by about 38 microseconds/day net (gravity faster ~45, speed slower ~7); uncorrected, errors would grow kilometers per day; clocks are adjusted.
Q7. What limits everyday accuracy? Key: atmospheric delays (ionosphere/troposphere), multipath reflections, satellite geometry, orbit/clock errors; typical few-meter accuracy; corrections (dual frequency, augmentation) improve it.
Q8 (transfer). In a city between tall buildings your phone's position jumps 50 m. Explain likely causes using the mechanism. Key: blocked satellites worsen geometry and reflected signals travel longer paths, overestimating distances (multipath), which shifts the solution.
