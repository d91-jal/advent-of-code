fn parse(input: &str) -> Vec<Vec<i8>> {
    input
        .lines()
        .map(str::trim)
        .filter(|l| !l.is_empty())
        .map(|s| {
            s.chars()
                .map(|c| c.to_digit(10).expect("non-digit in input") as i8)
                .collect()
        })
        .collect()
}

pub fn part1(input: &str) -> i64 {
    let banks = parse(input);
    let mut sum: i64 = 0;

    for bank in banks {
        sum += max_joltage(&bank, 2) as i64;
    }

    sum
}

pub fn part2(input: &str) -> i64 {
    let banks = parse(input);
    let mut sum: i64 = 0;

    for bank in banks {
        sum += max_joltage(&bank, 12) as i64;
    }

    sum
}

/// General idea: find the first instance of the largest digit in the current window,
/// leaving enough space for the remaining digits to be selected afterwards.
/// Then repeat for the next digit, starting just after the selected digit.
fn max_joltage(bank: &Vec<i8>, size: usize) -> i64 {
    if bank.len() < size {
        panic!("bank must have at least {} elements", size);
    }

    let n = bank.len();
    let mut result: Vec<i8> = Vec::with_capacity(size);
    let mut start = 0;

    for remaining in (0..size).rev() {
        let end = n - remaining;
        let mut max_val = 0;
        let mut max_idx = start;

        for idx in start..end {
            let val = bank[idx];

            if val > max_val {
                max_val = val;
                max_idx = idx;

                if max_val == 9 {
                    // Early exit if we found the maximum possible digit.
                    break;
                }
            }
        }

        result.push(max_val);
        start = max_idx + 1;
    }

    // Convert the selected digits into a number
    result.iter().fold(0i64, |acc, d| acc * 10 + (*d as i64))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example03.txt");
        assert_eq!(part1(&input), 357);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example03.txt");
        assert_eq!(part2(&input), 3121910778619);
    }
}
