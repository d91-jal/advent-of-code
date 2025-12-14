fn parse(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| l.chars().collect())
        .collect()
}

fn part1(input: &str) -> i64 {
    let grid = parse(input);
    0
}

fn part2(input: &str) -> i64 {
    let grid = parse(input);
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example05.txt");
        assert_eq!(part1(&input), 0);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example05.txt");
        assert_eq!(part2(&input), 0);
    }
}
