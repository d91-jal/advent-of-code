/// Parse the input into (ranges, ids)
fn parse(input: &str) -> (Vec<(i64, i64)>, Vec<i64>) {
    let input = input.replace("\r\n", "\n");
    let mut sections = input.split("\n\n");
    let ranges_section = sections.next().expect("Missing ranges section.");
    let ids_section = sections.next().expect("Missing IDs section.");

    let ranges = ranges_section
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|line| {
            let (a, b) = line.split_once('-').expect("Bad range");
            (
                a.trim().parse::<i64>().expect("Bad number."),
                b.trim().parse::<i64>().expect("Bad number."),
            )
        })
        .collect::<Vec<_>>();

    let ids = ids_section
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|line| line.trim().parse::<i64>().expect("Bad ID."))
        .collect::<Vec<_>>();

    (ranges, ids)
}

pub fn part1(input: &str) -> i64 {
    let (ranges, ids) = parse(input);
    let merged = merge_ranges(ranges);
    // Count number of IDs which are in any of the merged ranges.
    ids.into_iter().filter(|&id| is_fresh(id, &merged)).count() as i64
}

pub fn part2(input: &str) -> i64 {
    let (ranges, _ids) = parse(input);
    let merged = merge_ranges(ranges);
    // Just count total number of fresh IDs which is easy from the merged ranges.
    let fresh: i64 = merged.iter().map(|&(start, end)| end - start + 1).sum();

    fresh
}

/// Merge overlapping or adjacent ranges
fn merge_ranges(mut ranges: Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    if ranges.is_empty() {
        return ranges;
    }

    ranges.sort_unstable_by_key(|r| r.0);
    let mut merged = Vec::new();
    let mut current = ranges[0];

    for (start, end) in ranges.into_iter().skip(1) {
        if start <= current.1 + 1 {
            // Overlap or touching.
            current.1 = current.1.max(end);
        } else {
            merged.push(current);
            current = (start, end);
        }
    }

    merged.push(current);
    merged
}

/// Check if an id is within any range
fn is_fresh(id: i64, ranges: &[(i64, i64)]) -> bool {
    // ranges are sorted and merged
    for &(start, end) in ranges {
        if id < start {
            return false; // early exit
        }

        if id <= end {
            return true;
        }
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example05.txt");
        assert_eq!(part1(&input), 3);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example05.txt");
        assert_eq!(part2(&input), 14);
    }
}
