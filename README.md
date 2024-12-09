# DDoS Attack Tool

**Disclaimer:**

* This tool is for educational purposes only. 
* Using this tool for any unauthorized activity, including but not limited to denial-of-service attacks, is illegal and unethical. 
* The developer is not responsible for any misuse of this tool.

**Features:**

* Performs a basic UDP flood attack on a target IP address.
* Optionally targets a specific port or randomly selects ports.

**Usage:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gaurav909565/ddos_tool.git
   ```

2. **Navigate to the repository:**
   ```bash
   cd ddos_tool/
   ```

3. **Run the script:**
   ```bash
   python ddos_tool.py 
   ```

4. **Enter the target IP address.**

5. **Optionally, enter the target port. If no port is specified, the script will randomly select ports.**

**Example:**

* **To attack on port 80:**
   ```bash
   python ddos_tool.py 
   Target IP >> 192.168.1.100
   Port      >> 80
   ```

* **To attack on random ports:**
   ```bash
   python ddos_tool.py 
   Target IP >> 192.168.1.100
   Port      >> 
   ```

**Note:**

* This is a basic implementation and may not be very effective against modern defenses.
* This script should only be used against systems that you have explicit permission to test.
* **Never use this script for malicious purposes.**

**Disclaimer:**

This tool is for educational and ethical purposes only. The developer is not responsible for any misuse of this tool, and never target systems without proper authorization.. Using this tool for illegal activities is strictly prohibited.
