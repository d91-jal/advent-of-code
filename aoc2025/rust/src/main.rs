// ===== main.rs =====

mod days;
use std::env;

fn main() {
    let mut args = env::args().skip(1);

    let day: u32 = args
        .next()
        .unwrap_or_else(|| {
            eprintln!("Usage: cargo run -- <day> [part]");
            std::process::exit(1);
        })
        .parse()
        .expect("Day must be a number");

    let part = args.next().and_then(|p| p.parse::<u32>().ok());

    let filename = format!("resources/day{:02}.txt", day);
    let input = std::fs::read_to_string(&filename)
        .unwrap_or_else(|_| panic!("Could not read {}", filename));

    match day {
        1 => dispatch(&input, part, days::day01::part1, days::day01::part2),
        // Add more days here:
        // 2 => dispatch(&input, part, days::day02::part1, days::day02::part2),
        _ => panic!("Day {} not implemented", day),
    }
}

fn dispatch(input: &str, part: Option<u32>, p1: fn(&str) -> i64, p2: fn(&str) -> i64) {
    match part {
        Some(1) => println!("Part 1: {}", p1(input)),
        Some(2) => println!("Part 2: {}", p2(input)),
        None => {
            println!("Part 1: {}", p1(input));
            println!("Part 2: {}", p2(input));
        }
        _ => eprintln!("Invalid part: expected 1 or 2"),
    }
}
