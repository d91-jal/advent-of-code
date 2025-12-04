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

/// Part 1: simulate the dial and count how many times it points at 0 after a rotation.
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

/// Part 2: count every time the dial points at 0 during the rotations.
///
/// For each rotation spec in the input:
///  - Find the distance to the next occurrence of 0 from the starting position s.
///  - Then calculate how many full rotations the remaining distance will cover.
///  - Update the position to the end of the rotation.
pub fn part2(input: &str) -> i64 {
    let ops = parse(input);
    let mut pos: i64 = 50;
    let mut total_count: i64 = 0;

    for (dir, dist) in ops {
        // Find the initial distance to 0 in this rotation.
        let first_k_opt: Option<i64> = match dir {
            'R' | 'r' => {
                let residue = (100 - pos.rem_euclid(100)) % 100;
                let first_k = if residue == 0 { 100 } else { residue };
                Some(first_k)
            }
            'L' | 'l' => {
                let residue = pos.rem_euclid(100);
                let first_k = if residue == 0 { 100 } else { residue };
                Some(first_k)
            }
            other => panic!("unexpected direction: {}", other),
        };

        // We are now pointing at 0. Calculate how many full rotations fit in the remaining distance.
        if let Some(first_k) = first_k_opt {
            if first_k <= dist {
                let occ = 1 + (dist - first_k) / 100;
                total_count += occ;
            }
        }

        // Calculate new position.
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
