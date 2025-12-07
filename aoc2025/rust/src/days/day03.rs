fn parse(input: &str) -> Vec<Vec<i32>> {
    input
        .lines()
        .map(str::trim)
        .filter(|l| !l.is_empty())
        .map(|s| {
            s.chars()
                .map(|c| c.to_digit(10).expect("non-digit in input") as i32)
                .collect()
        })
        .collect()
}

pub fn part1(input: &str) -> i64 {
    let ops = parse(input);
    0
}

pub fn part2(input: &str) -> i64 {
    let ops = parse(input);
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example03.txt");
        assert_eq!(part1(&input), 0);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example03.txt");
        assert_eq!(part2(&input), 0);
    }
}
