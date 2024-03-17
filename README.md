
# AirBnB Clone - The Console

<a href="https://imgur.com/3oxzjru"><img src="https://imgur.com/3oxzjru" title="source: imgur.com" /></a>

This project is a command-line interface (CLI) implementation for managing AirBnB objects. It serves as the first step towards building a full web application, the AirBnB clone. The CLI allows users to create, retrieve, update, and delete various objects such as users, states, cities, and places.

## Installation

To run the AirBnB clone console, ensure you have Python 3.8.5 or later installed on your system. Follow these steps:


1. Clone the repository:

```bash
git clone <https://github.com/Luamix550/holbertonschool-AirBnB_clone.git>
```

2. Navigate to the project directory:

```bash
cd AirBnB_clone
```

3. Execute the console:

```bash
./console.py
```

## Usage

Once the console is running, you can interact with it using various commands. Here's how you can get started:

### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
```

### Non-Interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

### Available Commands

- `help`: Display information about available commands.
- `quit`: Exit the console.

## Tests

To run the unit tests, execute the following command:

```bash
python3 -m unittest discover tests
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request



## Authors

- [@Luamix550](https://github.com/Luamix550)
- [@JuanRestrepoV](https://github.com/JuanRestrepoV)
