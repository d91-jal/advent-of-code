fn parse(input: &str) -> Vec<(Vec<i64>, char)> {
    let mut lines = input.lines();

    // Read the four numeric rows
    let nums: Vec<Vec<i64>> = (0..4)
        .map(|_| {
            lines
                .next()
                .expect("Missing numeric line")
                .split_whitespace()
                .map(|s| s.parse::<i64>().expect("Bad number"))
                .collect()
        })
        .collect();

    // Read the character row
    let chars: Vec<char> = lines
        .next()
        .expect("Missing operation line")
        .split_whitespace()
        .map(|s| s.chars().next().expect("Empty char"))
        .collect();

    let cols = chars.len();

    // Transpose rows -> columns
    (0..cols)
        .map(|i| {
            let column = nums.iter().map(|row| row[i]).collect();
            (column, chars[i])
        })
        .collect()
}

pub fn part1(input: &str) -> i64 {
    let problems = parse(input);
    0
}

pub fn part2(input: &str) -> i64 {
    let problems = parse(input);
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example06.txt");
        assert_eq!(part1(&input), 0);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example06.txt");
        assert_eq!(part2(&input), 0);
    }
}
