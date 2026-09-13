import xml.etree.ElementTree as ET

# Sample XML Data
xml_data = """<students>
    <student id="101">
        <name>Alice</name>
        <department>CS</department>
        <cgpa>3.85</cgpa>
    </student>
    <student id="102">
        <name>Bob</name>
        <department>ECE</department>
        <cgpa>3.70</cgpa>
    </student>
</students>"""

# Parse XML string (Use ET.parse('filename.xml') for a file)
root = ET.fromstring(xml_data)

# Display parsed data
print(f"Root Tag: {root.tag}\n" + "=" * 35)

for student in root.findall("student"):
    student_id = student.attrib.get("id")
    name = student.find("name").text
    dept = student.find("department").text
    cgpa = student.find("cgpa").text

    print(
        f"ID: {student_id} | Name: {name} | Dept: {dept} | CGPA: {cgpa}"
    )