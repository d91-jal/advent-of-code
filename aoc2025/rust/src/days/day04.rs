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
    0
}

pub fn part2(input: &str) -> i64 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example04.txt");
        assert_eq!(part1(&input), 0);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example04.txt");
        assert_eq!(part2(&input), 0);
    }
}
