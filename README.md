<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AirBnB Clone - The Console</title>
</head>
<body>
    <h1>AirBnB Clone - The Console</h1>

    <p>This project is a command-line interface (CLI) implementation for managing AirBnB objects. It serves as the first step towards building a full web application, the AirBnB clone. The CLI allows users to create, retrieve, update, and delete various objects such as users, states, cities, and places.</p>

    <h2>Installation</h2>

    <p>To run the AirBnB clone console, ensure you have Python 3.8.5 or later installed on your system. Follow these steps:</p>

    <ol>
        <li>Clone the repository:</li>
    </ol>

    <pre><code>git clone &lt;repository_url&gt;
    </code></pre>

    <ol start="2">
        <li>Navigate to the project directory:</li>
    </ol>

    <pre><code>cd AirBnB_clone
    </code></pre>

    <ol start="3">
        <li>Execute the console:</li>
    </ol>

    <pre><code>./console.py
    </code></pre>

    <h2>Usage</h2>

    <p>Once the console is running, you can interact with it using various commands. Here's how you can get started:</p>

    <h3>Interactive Mode</h3>

    <pre><code>$ ./console.py
    (hbnb) help

    Documented commands (type help &lt;topic&gt;):
    ========================================
    EOF  help  quit

    (hbnb) 
    </code></pre>

    <h3>Non-Interactive Mode</h3>

    <pre><code>$ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help &lt;topic&gt;):
    ========================================
    EOF  help  quit
    (hbnb) 
    </code></pre>

    <h3>Available Commands</h3>

    <ul>
        <li><code>help</code>: Display information about available commands.</li>
        <li><code>quit</code>: Exit the console.</li>
    </ul>

    <h2>Tests</h2>

    <p>To run the unit tests, execute the following command:</p>

    <pre><code>python3 -m unittest discover tests
    </code></pre>

    <h2>Contributing</h2>

    <ol>
        <li>Fork the repository</li>
        <li>Create your feature branch (<code>git checkout -b feature/YourFeature</code>)</li>
        <li>Commit your changes (<code>git commit -am 'Add some feature'</code>)</li>
        <li>Push to the branch (<code>git push origin feature/YourFeature</code>)</li>
        <li>Create a new Pull Request</li>
    </ol>

    <h2>Authors</h2>

    <ul>
        <li>Guillaume</li>
        <li>Juan Pablo Restrepo</li>
        <li>Luis Alfonso Diaz</li>
    </ul>
</body>
</html>