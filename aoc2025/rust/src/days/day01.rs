fn parse(input: &str) -> Vec<(char, i64)> {
    input
        .lines()
        .map(str::trim)
        .filter(|l| !l.is_empty())
        .map(|l| {
            let mut chars = l.chars();
            let dir = chars.next().expect("empty line in input");
            let dist: i64 = chars.as_str().parse().expect("bad distance");
            (dir, dist)
        })
        .collect()
}

pub fn part1(input: &str) -> i64 {
    let ops = parse(input);
    let mut pos: i64 = 50; // Initial position.
    let mut count: i64 = 0;

    for (dir, dist) in ops {
        // Calculate new position.
        pos = match dir {
            'L' | 'l' => pos - dist,
            'R' | 'r' => pos + dist,
            other => panic!("unexpected direction: {}", other),
        };

        // Wrap around if answer is outside 0 - 99.
        pos = pos.rem_euclid(100);

        if pos == 0 {
            count += 1;
        }
    }

    count
}

/// Part 2: count every time *any click* causes the dial to point at 0 (including intermediate clicks).
///
/// Efficient approach per rotation:
/// For a rotation of `dist` steps starting at `s`:
///  - For R (increasing): we want k in [1..=dist] with (s + k) % 100 == 0.
///    Solve k ≡ (100 - s) mod 100. If that residue is 0, the first valid k is 100.
///  - For L (decreasing): we want k in [1..=dist] with (s - k) % 100 == 0.
///    Solve k ≡ s mod 100. If residue 0, first valid k is 100.
/// Number of occurrences = 0 if first_k > dist else 1 + floor((dist - first_k)/100).
pub fn part2(input: &str) -> i64 {
    let ops = parse(input);
    let mut pos: i64 = 50;
    let mut total_count: i64 = 0;

    for (dir, dist) in ops {
        // compute occurrences during this rotation
        let first_k_opt: Option<i64> = match dir {
            'R' | 'r' => {
                // k ≡ (100 - pos) mod 100, but k must be >= 1
                let residue = (100 - pos.rem_euclid(100)) % 100;
                let first_k = if residue == 0 { 100 } else { residue };
                Some(first_k)
            }
            'L' | 'l' => {
                // k ≡ pos mod 100, but k must be >= 1
                let residue = pos.rem_euclid(100);
                let first_k = if residue == 0 { 100 } else { residue };
                Some(first_k)
            }
            other => panic!("unexpected direction: {}", other),
        };

        if let Some(first_k) = first_k_opt {
            if first_k <= dist {
                // occurrences spaced every 100 steps after first_k
                let occ = 1 + (dist - first_k) / 100;
                total_count += occ;
            }
        }

        // update position to the end of the rotation
        pos = match dir {
            'L' | 'l' => pos - dist,
            'R' | 'r' => pos + dist,
            _ => unreachable!(),
        };

        pos = pos.rem_euclid(100);
    }

    total_count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example01.txt");
        assert_eq!(part1(&input), 3);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example01.txt");
        assert_eq!(part2(&input), 6);
    }

    #[test]
    fn single_big_rotation_hits_multiple_times() {
        // start at 50, R1000 -> increases position by 1000 => 10 full laps -> 10 times hitting 0
        let input = "R1000\n";
        assert_eq!(part2(input), 10);
        // For part1, the final position returns to 50 -> does not count
        assert_eq!(part1(input), 0);
    }
}
