# Claims
- C1: GPS has at least 24 (currently ~31) satellites in medium Earth orbit at ~20,200 km, two orbits a day, six planes, arranged so at least four are visible from virtually anywhere.
- C2: Each satellite broadcasts a repeating PRN code plus a 50 bps navigation message carrying its orbit (ephemeris), clock-correction data, and system time.
- C3: A receiver measures signal travel time by aligning a local replica of the code; pseudorange = c (t_rx - t_tx); one range puts the receiver on a sphere around the satellite.
- C4: The receiver clock offset is a fourth unknown, so at least four satellites are needed; with more, least squares is used, solved iteratively.
- C5: Timing precision drives accuracy: 1 ns of timing error is ~30 cm of range; satellites carry atomic clocks; receivers use quartz.
- C6: Relativity makes satellite clocks run fast by ~4.465e-10 (~38 us/day); the clock is set to 10.2299999954326 MHz before launch; uncorrected, errors would exceed 11 km in a day.
- C7: Remaining error sources (ionosphere, troposphere, multipath, blockage, geometry) and typical smartphone accuracy (~4.9 m open sky; URE commitment <=2.0 m).
- C8: Phones use assisted GNSS (ephemeris, clock correction, time, approx position over network) to cut time to first fix; the broadcast message itself is slow (50 bps).
