import os


class EvolvotronPicGen:

    def __init__(self,
                 input_extension='xml',
                 input_path='.',
                 output_image_resolution='1920x1080',
                 output_image_extension='png',
                 output_path='.' + os.path.sep + 'evolvotron_pictures' + os.path.sep):

        # == USER PARAMETERS ==
        self.INPUT_EXTENSION = input_extension
        self.INPUT_PATH = input_path

        self.OUTPUT_IMAGE_RESOLUTION = output_image_resolution
        self.OUTPUT_IMAGE_EXTENSION = output_image_extension
        self.OUTPUT_PATH = output_path

        print('==================================================')
        print('== PICTURES GENERATOR FROM EVOLVOTRON XML FILES ==')
        print('== by Saverio Brancaccio                        ==')
        print('==================================================')

    def _get_full_renderer_cmd(self, xml_filename):
        """Returns the evolvotron_renderer full command.\n
        The method creates a full CLI command like the one reported in the example below.

        Example (argument xml_filename as 'image.xml'):
            cat image.xml | evolvotron_renderer -j -m 4 -s 1920x1080 -o ./evolvotron_pictures/image.png

        :param xml_filename: (string) the name of the xml file saved by Evolvotron
        :return: (string) the full command
        """

        # == BUILD THE FULL COMMAND ==
        # set the name of the picture to create
        final_picture_filename = xml_filename.rsplit('.', 1)[0] + '.' + self.OUTPUT_IMAGE_EXTENSION
        # build the full command with all necessary arguments
        full_command = 'cat' + ' ' + xml_filename + ' | ' \
                       + 'evolvotron_render' + ' -j -m 4 -s ' + self.OUTPUT_IMAGE_RESOLUTION \
                       + ' -o ' + self.OUTPUT_PATH + final_picture_filename

        return full_command

    def _get_file_list_filtered_by_extension(self, extension='xml', folder='.'):
        """Returns a list of files with specific extension contained in the given folder.
        If no files are found, it returns an empty list.

        :param extension: (string) the extension used for filtering files into the given folder
        :param folder: (string) the folder name containing the files to filter and put then into filtered list
        :return: (list) the list of filtered file names, with the format 'filename.ext'.
        """
        # initialize the filtered file list to an empty list
        filtered_list = []

        # check if there are computable files into given folder
        file_list = os.listdir(folder)
        files_counter = 0
        # one or more files with wanted extension are found, so build the file list
        for element in file_list:
            # current element is a file
            if os.path.isfile(element):
                # current element is a file with wanted extension
                if element.endswith('.' + extension):
                    # increment counter of found files
                    files_counter += 1
                    # add filename to the filtered list
                    filtered_list.append(element)
        print('Computable files found: ' + str(files_counter))
        print('in folder: ' + os.path.abspath(self.INPUT_PATH) + os.path.sep)

        # if no file with wanted extension is found return an empty list
        if files_counter <= 0:
            print('No computable files found: no action performed.')
            # return empty list
            return []

        return filtered_list

    def generate_pictures(self):
        """Run a command for each file in folder to create related picture.

        """
        # Get the input file list, used to generate rasterized pictures
        file_list = self._get_file_list_filtered_by_extension(self.INPUT_EXTENSION, self.INPUT_PATH)

        if len(file_list) > 0:
            # create folder 'evolvotron_pictures' if it does not exist
            # at specific path
            if not (os.path.exists(self.OUTPUT_PATH)):
                os.mkdir(self.OUTPUT_PATH)

            for filename in file_list:
                # print info message for the current file
                print(' ')
                print('Generating picture for the file: ' + filename + ' ...')

                # run CLI command to create a picture for the current file
                #full_command = self._get_full_renderer_cmd(filename)

                os.system(self._get_full_renderer_cmd(filename))


def main():
    generatior = EvolvotronPicGen()
    generatior.generate_pictures()


if __name__ == '__main__':
    main()
