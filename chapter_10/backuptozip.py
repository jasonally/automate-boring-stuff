#! /usr/bin/env python3
# backuptozip.py – Copies an entire folder and its contents into a ZIP file
# whose filename increments.

import zipfile, os

def backup_to_zip(folder):
	# Back up the entire contents of "folder" into a ZIP file.
	folder = os.path.abspath(folder) # Make sure folder is absolute.

	# Figure out filename code should use based on which files already exist.
	number = 1
	while True:
		zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zip_filename):
			break # Stop when you find filename which doesn't exist.
		number += 1

	# Create the ZIP file.
	print(f'Creating {zip_filename}')
	backupzip = zipfile.ZipFile(zip_filename, 'w') # Open in write mode.

	# Walk the entire folder tree and compress the files in each folder.
	for folder_name, subfolder, filenames in os.walk(folder):
		print(f'Adding files in {folder_name}...')
		# Add the current folder to the ZIP file.
		backupzip.write(folder_name)

		# Add all the files in this folder to the ZIP file.
		for filename in filenames:
			new_base = os.path.basename(folder) + '_'
			if filename.startswith(new_base) and filename.endswith('.zip'):
				continue # Don't back up the backup ZIP files.
			backupzip.write(os.path.join(folder_name, filename))
	backupzip.close()
	print('Done.')

backup_to_zip('<path>')