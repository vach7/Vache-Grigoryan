class CircuitParser:
    def __init__(self):
        self.circuit = []

    def parse_netlist(self, file_path):

        #HSPICE netlist to Python

        with open(file_path, 'r') as file:
            lines = file.readlines()

        sub_circuit = {
            "transistor": [],
            "dummy_transistor": [],
            "resistor": []
        }

        for line in lines:
            line = line.strip()

            # Skip comments and empty lines
            if line.startswith("*") or not line:
                continue

            if line.startswith("xr"):
                parts = line.split()
                name = parts[0]
                parameters = " ".join(parts[1:])
                sub_circuit["resistor"].append({
                    "parameter": name,
                    "value": parameters
                })

            elif line.startswith("M") or line.startswith("X"):
                if line.startswith("M_dm") or line.startswith("X_dm"):
                    parts = line.split()
                    name = parts[0]
                    parameters = " ".join(parts[1:])

                    sub_circuit["dummy_transistor"].append({
                    "parameter": name,
                    "value": parameters
                    })
                else:
                    parts = line.split()
                    name = parts[0]
                    parameters = " ".join(parts[1:])
                    sub_circuit["transistor"].append({
                    "parameter": name,
                    "value": parameters})


        self.circuit.append({"sub_circuit": sub_circuit})

    def write_netlist(self, file_path):

        #Python object to netlis.

        with open(file_path, 'w') as file:
            for sub in self.circuit:
                sub_circuit = sub["sub_circuit"]
                file.write("***************************************************************************" + "\n")
                file.write("Resistors" + "\n")
                file.write("***************************************************************************" + "\n")
                for resistor in sub_circuit["resistor"]:
                    line = f"{resistor['parameter']} {resistor['value']}\n"
                    file.write(line)
                file.write("***************************************************************************" + "\n")
                file.write("Transistors" + "\n")
                file.write("***************************************************************************" + "\n")
                for transistor in sub_circuit["transistor"]:
                    line = f"{transistor['parameter']} {transistor['value']}\n"
                    file.write(line)
                file.write("***************************************************************************" + "\n")
                file.write("Dummy Transistors" + "\n")
                file.write("***************************************************************************" + "\n")
                for dummy_transistor in sub_circuit["dummy_transistor"]:
                    line = f"{dummy_transistor['parameter']} {dummy_transistor['value']}\n"
                    file.write(line)



parser = CircuitParser()
parser.parse_netlist("opamp_netlist.txt")
print("Parsed Circuit Structure:", parser.circuit)
parser.write_netlist("parameters.txt")