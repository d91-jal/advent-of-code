pub fn read_input(filename: &str) -> String {
    let input = std::fs::read_to_string(&filename)
        .unwrap_or_else(|_| panic!("Could not read {}", filename));

    input
}
