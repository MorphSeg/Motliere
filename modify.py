import subprocess


def find_package_location(package_name):
    try:
        # Run pip show command to get package information
        result = subprocess.check_output(['pip', 'show', package_name]).decode('utf-8')
        # Split the output by line and search for 'Location' line
        for line in result.split('\n'):
            if line.startswith('Location:'):
                # Extract the location
                location = line.split(':', 1)[1].strip()
                return location + '/' + package_name
        return None  # Package not found
    except subprocess.CalledProcessError:
        return None  # Package not found or error occurred

def add_column_names():
    print(f'Adding the column names to the data files')
    # Open the file for reading and writing in text mode
    with open(find_package_location('motliere') + '/data/' + 'fra.derivations', 'r+') as file:
        # Read the original content
        original_content = file.read()

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Add the new line at the beginning
        new_line = "source	target	features	derivation\n"
        file.write(new_line)

        # Write the original content back after the new line
        file.write(original_content)

    with open(find_package_location('motliere') + '/data/' + 'fra.segmentations', 'r+') as file:
        # Read the original content
        original_content = file.read()

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Add the new line at the beginning
        new_line = "source	target	features	segmentation\n"
        file.write(new_line)

        # Write the original content back after the new line
        file.write(original_content)

def modify_file():
    print(f'Modifying the files for better results')
    # Open the file for reading and writing in text mode
    # with open(find_package_location('motliere') + '/data/' + 'fra.derivations', 'r+') as file:
    #     # Read the original content
    #     original_content = file.read()


    #     # Write the original content back after the new line
    #     file.write(original_content)

    with open(find_package_location('motliere') + '/data/' + 'fra.segmentations', 'a') as file:
        # appending new data    
        new_data = """avoir	ayant	V|V.PTCP;PRS	avoir|ant
avoir	eu	V|V.PTCP;PST	avoir|eu
avoir	ai	V|IND;PRS;1;SG	avoir|ai
avoir	as	V|IND;PRS;2;SG	avoir|as
avoir	a	V|IND;PRS;3;SG	avoir|a
avoir	avons	V|IND;PRS;1;PL	avoir|ons
avoir	avez	V|IND;PRS;2;PL	avoir|ez
avoir	ont	V|IND;PRS;3;PL	avoir|ont
avoir	avais	V|IND;PST;IPFV;1;SG	avoir|ais
avoir	avais	V|IND;PST;IPFV;2;SG	avoir|ais
avoir	avait	V|IND;PST;IPFV;3;SG	avoir|ait
avoir	avions	V|IND;PST;IPFV;1;PL	avoir|ions
avoir	aviez	V|IND;PST;IPFV;2;PL	avoir|iez
avoir	avaient	V|IND;PST;IPFV;3;PL	avoir|aient
avoir	eus	V|IND;PST;PFV;1;SG	avoir|euses
avoir	eus	V|IND;PST;PFV;2;SG	avoir|eus
avoir	eut	V|IND;PST;PFV;3;SG	avoir|eut
avoir	eûmes	V|IND;PST;PFV;1;PL	avoir|ûmes
avoir	eûtes	V|IND;PST;PFV;2;PL	avoir|ûtes
avoir	eurent	V|IND;PST;PFV;3;PL	avoir|urent
avoir	aurai	V|IND;FUT;1;SG	avoir|rai
avoir	auras	V|IND;FUT;2;SG	avoir|ras
avoir	aura	V|IND;FUT;3;SG	avoir|ra
avoir	aurons	V|IND;FUT;1;PL	avoir|rons
avoir	aurez	V|IND;FUT;2;PL	avoir|rez
avoir	auront	V|IND;FUT;3;PL	avoir|ront
avoir	aurais	V|COND;1;SG	avoir|rais
avoir	aurais	V|COND;2;SG	avoir|rais
avoir	aurait	V|COND;3;SG	avoir|rait
avoir	aurions	V|COND;1;PL	avoir|rions
avoir	auriez	V|COND;2;PL	avoir|riez
avoir	auraient	V|COND;3;PL	avoir|raient
avoir	aie	V|SBJV;PRS;1;SG	avoir|e
avoir	aies	V|SBJV;PRS;2;SG	avoir|es
avoir	ait	V|SBJV;PRS;3;SG	avoir|t
avoir	ayons	V|SBJV;PRS;1;PL	avoir|ons
avoir	ayez	V|SBJV;PRS;2;PL	avoir|ez
avoir	aient	V|SBJV;PRS;3;PL	avoir|ent
avoir	eusse	V|SBJV;PST;IPFV;1;SG	avoir|usse
avoir	eusses	V|SBJV;PST;IPFV;2;SG	avoir|usses
avoir	eût	V|SBJV;PST;IPFV;3;SG	avoir|ût
avoir	eussions	V|SBJV;PST;IPFV;1;PL	avoir|ussions
avoir	eussiez	V|SBJV;PST;IPFV;2;PL	avoir|ussiez
avoir	eussent	V|SBJV;PST;IPFV;3;PL	avoir|ussent"""

        file.write(new_data)

'''
The actual code that will be executed when the file is run start HERE
Applying the function to the data files
and downloading the French model
'''

# Add column names to the data files
add_column_names()


# Download the French model
print(f'Download the French model')
command = ['python', '-m', 'spacy', 'download', 'fr_core_news_md']
try:
        # Execute the command
    # Use subprocess.run to execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output and error (if any)
    print('Output:', result.stdout)
    print(f'French model successfully downloaded')
except subprocess.CalledProcessError as e:
        # Handle errors in case the command fails
        print(f"Failed to download model.")
        print('Error:', e.stderr)
        print('Return Code:', e.returncode)
except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {str(e)}")


# Adding data to files and modifications 
# modify_file() # put this line in comment to keep the file as it originally was