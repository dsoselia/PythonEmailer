PyArchiver
--------

To use (with caution), simply do::

    >>> import pyarchiver
    >>> pyarchiver.get_archivation_methods()
    ['bz2','gzip','lzma']
    >>> file_to_archive = "/Full/Path/To/The/File/We/Plan/To/Archive"
    >>> archive_location = "/Full/Path/To/Archive/Location"
    >>> archive_file_name = "ArchiveFile" #No extension is needed
    >>> archivation_method = 'lzma'
    >>> pyarchiver.archive(file_to_archive,
                           archive_location,
                           archive_file_name,
                           archivation_method)
