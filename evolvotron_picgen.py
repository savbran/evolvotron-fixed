"""EvolvotronPicGen script  (Author: Saverio Brancaccio)

This module script can be used to generate .png or .ppm pictures starting from Evolvotron .xml function files.

**SIMPLE USAGE**
    1. Copy this script in a folder containing xml files saved from Evolvotron.
    2. Launch the script with CLI command: python evolvotron_picgen.py.
    3. Read the informative messages printed on terminal during the script execution (target folder, etc.).
    4. After the script execution ends, check the content of the target folder.
    5. Target folder will contain the rasterized pictures (.png or ppm) generated from Evolvotron .xml files.
"""

import os


class EvolvotronPicGen:
    """A picture generator with which it is possible to create rasterized pictures (png, ppm)
starting from Evolvotron function files (xml).

**USAGE**
    The class can be instantiated without arguments because default ones are defined in __init__ function.
    As an example, see this module main() function to easy understand the use of the class.

**PARAMETERS**
    To change characteristics of the pictures to rasterize, destination folder, etc.
    you can change the __init__ function arguments:

    - input_extension
    - input_path
    - output_picture_resolution
    - output_picture_extension
    - output_path

    TODO: implement handling of input arguments received from terminal command line when the script is executed.
    """

    def __init__(self,
                 input_extension='xml',
                 input_path='.',
                 output_picture_resolution='1920x1080',
                 output_picture_extension='png',
                 output_path='.' + os.path.sep + 'evolvotron_pictures' + os.path.sep):

        # == USER PARAMETERS ==
        self.INPUT_EXTENSION = input_extension
        self.INPUT_PATH = input_path
        self.OUTPUT_PICTURE_RESOLUTION = output_picture_resolution
        self.OUTPUT_PICTURE_EXTENSION = output_picture_extension
        self.OUTPUT_PATH = output_path

        print('')
        print('==================================================')
        print('== PICTURES GENERATOR FROM EVOLVOTRON XML FILES ==')
        print('== (EvolvotronPicGen) by Saverio Brancaccio     ==')
        print('==================================================')
        print('')

    def _get_evolvotron_render_command(self, xml_filename):
        """Returns the evolvotron_render full command.\n
        The method creates a full CLI command like the one reported in the example below.

        Example (argument xml_filename as 'picture.xml'):
            cat picture.xml | evolvotron_renderer -j -m 4 -s 1920x1080 -o ./evolvotron_pictures/picture.png

        :param xml_filename: (string) the name of the xml file saved by Evolvotron
        :return: (string) the full command
        """

        # == BUILD THE FULL COMMAND ==

        # set the picture filename using the source xml filename with changed extension
        final_picture_filename = xml_filename.rsplit('.', 1)[0] + '.' + self.OUTPUT_PICTURE_EXTENSION

        # build the full command with all necessary arguments
        full_command = 'cat' + ' ' + xml_filename + ' | ' \
                       + 'evolvotron_render' + ' -j -m 4 -s ' + self.OUTPUT_PICTURE_RESOLUTION \
                       + ' -o ' + self.OUTPUT_PATH + final_picture_filename

        return full_command

    @staticmethod
    def _get_fileslist_by_extension(extension='xml', folder='.'):
        """Returns a list of files with specific extension contained in the given folder.
        If no files are found, it returns an empty list.

        :param extension: (string) the extension used for file filtering
        :param folder: (string) the folder name containing files to filter
        :return: (list) the filtered list of file names (example name: 'filename.ext')
        or an empty list.
        """
        # initialize the filtered file list to an empty list
        filtered_list = []

        # check if there are computable files into given folder
        file_list = os.listdir(folder)
        # scan all file names obtained from folder
        for element in file_list:
            # current element is a file
            if os.path.isfile(element):
                # current element is a file with wanted extension
                if element.endswith('.' + extension):
                    # add filename to the filtered list
                    filtered_list.append(element)

        return filtered_list

    def generate_pictures(self):
        """Run a command for each file in folder to create related picture.

        """
        # Get the input file list, used to generate rasterized pictures
        file_list = self._get_fileslist_by_extension(self.INPUT_EXTENSION, self.INPUT_PATH)

        # files found
        if len(file_list) > 0:

            # == PRINT STARTUP INFO ==
            # settings
            print('Settings used for picture generation:')
            print('')
            print('    - pictures resolution: ' + self.OUTPUT_PICTURE_RESOLUTION)
            print('    - pictures extension: ' + self.OUTPUT_PICTURE_EXTENSION)
            print('    - input folder: ' + os.path.abspath(self.INPUT_PATH) + os.path.sep)
            print('    - target folder: ' + os.path.abspath(self.OUTPUT_PATH) + os.path.sep)
            print('')

            # input files
            print('Computable files found ' + str(len(file_list)) + ' ' +
                  'into folder ' + os.path.abspath(self.INPUT_PATH) + os.path.sep)
            print('')
            for filename in file_list:
                print('    ' + filename)

            # == GENERATE PICTURES ==
            # create output folder if it does not exist at specific path
            if not (os.path.exists(self.OUTPUT_PATH)):
                os.mkdir(self.OUTPUT_PATH)

            # create the corresponding picture in output folder for each file in file_list
            for filename in file_list:
                # print info message for the current file
                print(' ')
                print('Generating picture for the file: ' + filename)
                print('into folder: ' + os.path.abspath(self.OUTPUT_PATH) + os.path.sep + ' ...')

                # run terminal command to create a picture for the current file
                os.system(self._get_evolvotron_render_command(filename))

            # == PRINT FINAL INFO ==
            print('')
            print('Pictures generation task finished.')
            print('')

        # files not found
        else:
            print('No computable files found, no action performed.')
            print('')


def main():
    picture_generator = EvolvotronPicGen()
    picture_generator.generate_pictures()


if __name__ == '__main__':
    main()
