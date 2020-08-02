To install the compiler on Linux:
cargo build --release
sudo cp ./target/release/jinglec /usr/local/bin/jinglec

To install stdlib:
sudo mkdir /usr/local/lib/jinglec/
sudo cp std /usr/local/lib/jinglec/
