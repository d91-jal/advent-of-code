use std::collections::HashSet;

/// Merge overlapping/adjacent ranges and sort them
fn merge_ranges(mut ranges: Vec<(i128, i128)>) -> Vec<(i128, i128)> {
    if ranges.is_empty() {
        return vec![];
    }

    ranges.sort_unstable_by_key(|r| r.0);
    let mut merged: Vec<(i128, i128)> = Vec::with_capacity(ranges.len());
    let mut cur = ranges[0];

    for r in ranges.into_iter().skip(1) {
        if r.0 <= cur.1 + 1 {
            // overlap or adjacent
            cur.1 = cur.1.max(r.1);
        } else {
            merged.push(cur);
            cur = r;
        }
    }

    merged.push(cur);
    merged
}

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

/// parse into i128 Vec
fn parse_i128(s: &str) -> Vec<(i128, i128)> {
    parse(s)
        .into_iter()
        .map(|(a, b)| (a as i128, b as i128))
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

/// Generate all possible invalid numbers and check them against the ranges.
/// This is quicker than checking every number for large ranges.
pub fn part2(input: &str) -> i64 {
    let ranges_i128 = parse_i128(input);
    let merged = merge_ranges(ranges_i128);

    let max_end = merged.iter().map(|(_, end)| *end).max().unwrap_or(0);

    // Compute number of digits in the biggest number of the input.
    let max_digits = num_digits_i128(max_end);

    // Generate all repeated-pattern numbers up to max_digits
    let mut seen = HashSet::<i128>::new();

    // pattern length p from 1..=max_digits/2 (must repeat at least twice)
    for p in 1..=(max_digits / 2) {
        // pattern ranges: for p == 1 => 1..=9, otherwise 10^(p-1) .. 10^p - 1
        let start_pat = if p == 1 { 1 } else { pow10_i128(p - 1) };
        let end_pat = pow10_i128(p) - 1;

        for pat in start_pat..=end_pat {
            // number of repeats t from 2 up to floor(max_digits / p)
            let max_t = max_digits / p;
            let base = pow10_i128(p);

            let mut num: i128 = 0;
            for t in 1..=max_t {
                // append one more pattern
                num = num * base + pat;
                if t >= 2 {
                    // now num is pattern repeated t times
                    // Only collect numbers with digit length <= max_digits (it will be)
                    seen.insert(num);
                }
            }
        }
    }

    // Sum numbers that fall into any merged range
    let mut total: i128 = 0;
    for &n in &seen {
        if in_any_range(n, &merged) {
            total += n;
        }
    }

    // result fits in i64 for AoC inputs; but keep i128 arithmetic then cast
    total as i64
}

/// Check if n is in any (sorted/merged) range
fn in_any_range(n: i128, ranges: &[(i128, i128)]) -> bool {
    // linear scan is fine for AoC-sized lists; binary search possible if bigger
    for &(a, b) in ranges {
        if n < a {
            return false; // ranges sorted; early exit
        }
        if a <= n && n <= b {
            return true;
        }
    }
    false
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

/// Divide by ten until non-zero remainder.
fn num_digits_i128(mut n: i128) -> usize {
    if n == 0 {
        return 1;
    }

    let mut c = 0;

    if n < 0 {
        n = -n;
    }

    while n > 0 {
        n /= 10;
        c += 1;
    }

    c
}

fn pow10_i128(exp: usize) -> i128 {
    let mut v: i128 = 1;

    for _ in 0..exp {
        v *= 10;
    }

    v
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
        assert_eq!(part2(&input), 4174379265);
    }
}
