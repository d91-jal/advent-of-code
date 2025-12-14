const OFFSETS: [(isize, isize); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

fn parse(input: &str) -> Vec<Vec<char>> {
    input
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| l.chars().collect())
        .collect()
}

pub fn part1(input: &str) -> i64 {
    let grid = parse(input);

    if grid.is_empty() {
        return 0;
    }

    let rows = grid.len();
    let cols = grid[0].len();
    let mut accessible: i64 = 0;

    for r in 0..rows {
        for c in 0..cols {
            if grid[r][c] != '@' {
                continue;
            }

            let mut count_adj = 0;

            for (dr, dc) in &OFFSETS {
                let nr = r as isize + dr;
                let nc = c as isize + dc;

                if nr >= 0 && nr < rows as isize && nc >= 0 && nc < cols as isize {
                    if grid[nr as usize][nc as usize] == '@' {
                        count_adj += 1;
                    }
                }
            }

            if count_adj < 4 {
                accessible += 1;
            }
        }
    }

    accessible
}

pub fn part2(input: &str) -> i64 {
    let grid = parse(input);
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = crate::common::utils::read_input("resources/example04.txt");
        assert_eq!(part1(&input), 13);
    }

    #[test]
    fn example_part2() {
        let input = crate::common::utils::read_input("resources/example04.txt");
        assert_eq!(part2(&input), 43);
    }
}
