# Install Kafka on macOS

## Prerequisites
1. **Java Installation**
   - Ensure that Java is installed on your machine. If not, follow the steps below:
     - Visit [Oracle Java Downloads](https://www.oracle.com/java/technologies/downloads/).
     - Download the `.dmg` file for your operating system.

## Kafka Installation
1. **Download Kafka**
   - Go to the [Apache Kafka Downloads](https://kafka.apache.org/downloads) page.
   - Use the Binary downloads section or, if you know your required Kafka version, use the following commands:
     ```bash
     wget https://www.apache.org/dyn/closer.cgi?path=/kafka/3.7.0/kafka_2.13-3.7.0.tgz
     # Create a directory for Kafka e.g., streaming
     mkdir streaming
     mv kafka_2.13-3.7.0.tgz streaming
     cd streaming
     tar xzvf kafka_2.13-3.7.0.tgz
     ```

2. **Set Up the Environment Path**
   - Add Kafka binaries to your PATH environment variable by editing one of your shell configuration files. Choose the appropriate file based on the shell you use:
     ```bash
     cd ~
     open -e .bash_profile  # For Bash users
     open -e .zshrc         # For Zsh users
     open -e .zshenv        # Alternatively for Zsh users
     ```
   - Add the following line to your shell configuration file:
     ```bash
     export PATH="$PATH:/Users/jurisildam/servers/kafka_2.13-3.7.0/bin"
     ```
   - Alternatively, you can specify the Kafka path in a configuration file:
     ```yaml
     # In the conf/config_variables.yml
     kafka_path: '/Users/jurisildam/servers/kafka_2.13-3.7.0'
     ```

## Virtual Environment and Dependencies
1. **Set Up Python Virtual Environment**
   - Create and activate a Python virtual environment:
     ```bash
     python3 -m venv streaming
     source streaming/bin/activate
     ```
   
2. **Install Python Packages**
   - Install necessary Python packages:
     ```bash
     pip install kafka-python zookeeper river pyyaml path
     ```
	- Alternatevely:
     ```bash
     pip install requirements
     ```


