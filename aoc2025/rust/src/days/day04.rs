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
    analyze_accessible_positions(&grid).0
}

pub fn part2(input: &str) -> i64 {
    let mut grid = parse(input);
    let mut result: i64 = 0;

    while analyze_accessible_positions(&grid).0 > 0 {
        let (accessible_count, accessible_positions) = analyze_accessible_positions(&grid);
        result += accessible_count;

        for (r, c) in accessible_positions {
            grid[r][c] = '#';
        }
    }

    result
}


fn analyze_accessible_positions(grid: &Vec<Vec<char>>) -> (i64, Vec<(usize, usize)>) {
    let mut accessible: i64 = 0;
    let mut accessible_positions: Vec<(usize, usize)> = Vec::new();

    if grid.is_empty() {
        return (accessible, accessible_positions);
    }

    let rows = grid.len();
    let cols = grid[0].len();

    // Go through each cell in the grid
    for r in 0..rows {
        for c in 0..cols {
            if grid[r][c] != '@' {
                continue;
            }

            let mut count_adj = 0;

            // If the cell is occupied, check adjacent cells and count how many are occupied.
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
                accessible_positions.push((r, c));
            }
        }
    }

    (accessible, accessible_positions)
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
