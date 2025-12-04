fn parse(input: &str) -> Vec<(i64, i64)> {
    input
        .trim()
        .split(',')
        .map(|range| {
            let (a, b) = range.split_once('-').expect("Malformed range in input");
            (
                a.parse::<i64>().expect("Bad number"),
                b.parse::<i64>().expect("Bad number"),
            )
        })
        .collect()
}

/// For all numbers in the range, sum those that are invalid.
pub fn part1(input: &str) -> i64 {
    let ranges = parse(input);

    let mut sum: i64 = 0;

    for (start, end) in ranges {
        for n in start..=end {
            if is_invalid(n) {
                sum += n;
            }
        }
    }

    sum
}

pub fn part2(input: &str) -> i64 {
    let ranges = parse(input);
    0
}

/// A number is invalid if it is XY where X == Y
fn is_invalid(n: i64) -> bool {
    let s = n.to_string();
    let len = s.len();

    // Must be even length to split evenly
    if len % 2 != 0 {
        return false;
    }

    let mid = len / 2;
    let (left, right) = s.split_at(mid);

    left == right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example02.txt");
        assert_eq!(part1(&input), 1227775554);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example02.txt");
        assert_eq!(part2(&input), 0);
    }
}
