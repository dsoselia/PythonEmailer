# -*- coding: utf-8 -*-
"""PyArchiver core."""
import os
import subprocess


class pyarchiver:
    """.Basic pyarchiver class."""

    def __init__(self, file_to_archive, archivation_path, archiving_method):
        """.The init function"""
        self.file_to_archive = file_to_archive
        self.archivation_path = archivation_path
        self.archiving_method = archiving_method
        self.archiving_methods = ['bzip2', 'gzip', 'lzma']
        self.archiving_methods_dictionary = {"bzip2": 'bz2',
                                             "gzip": 'gz',
                                             "lzma": 'lzma'}

    def __check_if_archivation_methods_exist(self):
        """.Checks if archivation methods are collable\
           and returns True or False."""
        prcs = subprocess.Popen(
            [self.archiving_method, "--help"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        try:
            output, err = prcs.communicate()
            #print("Output: ", output)
            #print("Error Message: ", err)
        except subprocess.CalledProcessError as errr:
            print(errr.output)
            return False
        return True

    def __check_if_input_file_exists(self):
        """.If file/folder exist return True, else False."""
        if os.path.exists(self.file_to_archive):
            return True
        else:
            return False

    def __check_and_make_output_location(self):
        """.Checks if folder exists and creates if not."""
        if os.path.exists(self.archivation_path):
            return True
        else:
            try:
                os.makedirs(self.archivation_path)
                print("%s created" % self.archivation_path)
                return True
            except OSError:
                print("Check if you have permissions to %s" %
                      self.archivation_path)
                return False
        return False

    def __make_archive(self):
        prcs = subprocess.Popen(
            [self.archiving_method,
             self.file_to_archive],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        try:
            output, err = prcs.communicate()
            return_code = prcs.returncode
            if return_code != 0:
                print(err)
                return False
            else:
                return True
        except subprocess.CalledProcessError as errr:
            print(errr.output)
            return False
        return False

    def __source_cleanup(self):
        """.Moving the archived file to the predefined location."""
        output_file_full_path = "%s/%s.%s" % (
            self.archivation_path, self.file_to_archive.split("/")[-1],
            self.archiving_methods_dictionary[self.archiving_method])
        filename_to_move = "%s.%s" % (self.file_to_archive,
                                      self.archiving_methods_dictionary[self.archiving_method])
        prcs = subprocess.Popen(
            ["mv", "%s" % filename_to_move, output_file_full_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        try:
            prcs.communicate()
            return True
        except subprocess.CalledProcessError as errr:
            print(errr.output)
            return False
        return False

    def pyarchiver(self):
        """.The main function doing the archivation."""
        if self.__check_if_archivation_methods_exist():
            pass
        else:
            print("%s is not installed or available" % self.archiving_method)
            return False
        if self.__check_if_input_file_exists():
            pass
        else:
            print("%s file doesn't exist or not available" %
                  self.file_to_archive)
            return False
        if self.__check_and_make_output_location():
            pass
        else:
            print("%s path is not available" % self.archivation_path)
            return False
        if self.__make_archive():
            pass
        else:
            print("Archivation of %s failed" % self.file_to_archive)
            return False
        if self.__source_cleanup():
            return True
        else:
            return False
        print("PyArchiver Failed With Unknown Reason.")
        return False
